#!/usr/bin/env python3
"""Validate and render the three commands; no network, model calls or writes."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = {"PROJECT", "GOAL", "CONTEXT", "AUTHORITY", "CONSTRAINTS", "DONE_WHEN"}
ROUTES = {
    "deep-backlog": {"workflow": "deep-run", "mode": "BACKLOG"},
    "deep-execute": {"workflow": "deep-run", "mode": "EXECUTE"},
    "backlog-executor": {"workflow": "backlog-executor", "mode": None},
}
TOKEN = re.compile(r"\{\{([A-Z_]+)\}\}")
MODE_BLOCK = re.compile(r"<MODE:(BACKLOG|EXECUTE)>\n(.*?)</MODE:\1>", re.S)


def unique_object(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(text: str) -> dict:
    value = json.loads(text, object_pairs_hook=unique_object)
    if not isinstance(value, dict):
        raise ValueError("Expected a JSON object")
    return value


def catalog(root: Path = ROOT) -> dict:
    data = read_json((root / "catalog.yaml").read_text(encoding="utf-8"))
    if data.get("commands") != ROUTES:
        raise ValueError("Catalog must retain the three supported command routes")
    if set(data.get("fields", [])) != FIELDS or len(data["fields"]) != len(FIELDS):
        raise ValueError("Catalog input fields do not match the six-field contract")
    entries = data.get("prompts", [])
    if len(entries) != 2 or {x["id"] for x in entries} != {"deep-run", "backlog-executor"}:
        raise ValueError("Exactly two canonical workflows are required")
    if data.get("canonical_workflows") != ["deep-run", "backlog-executor"]:
        raise ValueError("Canonical workflow list is inconsistent")
    return data


def load_template(entry: dict, root: Path = ROOT) -> str:
    expected_path = f"loops/{entry['id']}.md"
    if entry["path"] != expected_path:
        raise ValueError(f"Unexpected template path: {entry['path']}")
    path = (root / entry["path"]).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError("Template path escapes the repository")
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        raise ValueError(f"Missing front matter: {entry['path']}")
    for field in ("id", "version", "status"):
        match = re.search(rf"^{field}:\s*(\S+)\s*$", parts[1], re.M)
        if not match or match.group(1) != entry[field]:
            raise ValueError(f"Catalog/front-matter drift: {entry['path']} {field}")
    blocks = re.findall(r"^```text\n(.*?)^```\s*$", parts[2], re.M | re.S)
    if len(blocks) != 1:
        raise ValueError(f"Expected one canonical text block: {entry['path']}")
    template = blocks[0].strip()
    expected_fields = FIELDS | ({"MODE"} if entry["id"] == "deep-run" else set())
    if set(TOKEN.findall(template)) != expected_fields:
        raise ValueError(f"Template placeholders do not match inputs: {entry['path']}")
    residual = TOKEN.sub("", template)
    if "{{" in residual or "}}" in residual:
        raise ValueError(f"Malformed placeholder: {entry['path']}")
    modes = [match.group(1) for match in MODE_BLOCK.finditer(template)]
    expected_modes = ["BACKLOG", "EXECUTE"] if entry["id"] == "deep-run" else []
    if modes != expected_modes or "MODE:" in MODE_BLOCK.sub("", template):
        raise ValueError(f"Invalid mode blocks: {entry['path']}")
    words = len(template.split())
    if words > entry["max_template_words"]:
        raise ValueError(f"Template word budget exceeded: {entry['path']} ({words})")
    return template


def render(command: str, spec: dict, root: Path = ROOT) -> str:
    data = catalog(root)
    if command not in data["commands"]:
        raise ValueError(f"Unknown command: {command}")
    if not isinstance(spec, dict):
        raise ValueError("Run specification must be a JSON object")
    missing, unknown = FIELDS - spec.keys(), spec.keys() - FIELDS
    if missing or unknown:
        raise ValueError(f"Missing fields: {sorted(missing)}; unknown fields: {sorted(unknown)}")
    for key, value in spec.items():
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{key} must be a non-empty string")
        if "{{" in value or "}}" in value:
            raise ValueError(f"Unresolved/template-like placeholder in {key}; reference source paths instead")
    route = data["commands"][command]
    entry = next(item for item in data["prompts"] if item["id"] == route["workflow"])
    template = load_template(entry, root)
    template = MODE_BLOCK.sub(lambda m: m.group(2).strip() if m.group(1) == route["mode"] else "", template)
    values = {**spec, "MODE": route["mode"] or ""}
    result = TOKEN.sub(lambda m: values[m.group(1)], template)
    # User values are substituted once; no evaluation or recursive interpolation.
    return f"PROMPTS {command} | {entry['id']} v{entry['version']}\n\n{result.strip()}\n"


def check(root: Path = ROOT) -> list[str]:
    data = catalog(root)
    expected = {entry["path"] for entry in data["prompts"]}
    actual = {str(path.relative_to(root)) for path in (root / "loops").glob("*.md")}
    if actual != expected:
        raise ValueError(f"Unexpected/missing canonical files: {sorted(actual ^ expected)}")
    report = []
    for entry in data["prompts"]:
        template = load_template(entry, root)
        report.append(f"{entry['id']} v{entry['version']}: {len(template.split())} template words")
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", path.read_text(encoding="utf-8")):
            if ":" in target or target.startswith("#"):
                continue
            target = target.split("#", 1)[0]
            if target and not (path.parent / target).exists():
                raise ValueError(f"Broken local link in {path.relative_to(root)}: {target}")
    sample = {field: f"Verified {field.lower()}" for field in FIELDS}
    for command in data["commands"]:
        result = render(command, sample, root)
        if "{{" in result or "<MODE:" in result:
            raise ValueError(f"Unresolved rendering: {command}")
        report.append(f"{command}: {len(result.split())} rendered words with synthetic inputs")
    report.append("Structural checks passed; agent behavior and outcome benchmarks were NOT run.")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    sub.add_parser("check", help="Check structure, local links, versions and rendering")
    build = sub.add_parser("render", help="Render one command to standard output")
    build.add_argument("command", choices=sorted(ROUTES))
    build.add_argument("--spec", required=True, help="UTF-8 JSON file; '-' for standard input")
    args = parser.parse_args()
    try:
        if args.action == "check":
            print("\n".join(check()))
        else:
            text = sys.stdin.read() if args.spec == "-" else Path(args.spec).read_text(encoding="utf-8")
            print(render(args.command, read_json(text)), end="")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
