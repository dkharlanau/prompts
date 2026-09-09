"""Deterministic renderer/contract tests, not LLM behavioral evaluations."""
import copy
import json
import subprocess
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from prompts import FIELDS, ROOT, ROUTES, check, read_json, render


SPEC = {
    "PROJECT": "owner/example; fixture only",
    "GOAL": "Fix the reproduced first-value failure",
    "CONTEXT": "Fixture issue #1; branch work/example; inspect its actual source",
    "AUTHORITY": "Edit and test on work/example only. No push, merge or deploy.",
    "CONSTRAINTS": "Preserve existing work. No paid services or production changes.",
    "DONE_WHEN": "Acceptance checks pass; missing evidence remains explicit.",
}


class PromptTests(unittest.TestCase):
    def test_repository_structure(self):
        self.assertIn("Structural checks passed", check()[-1])

    def test_all_three_commands_are_self_contained(self):
        for command in ROUTES:
            with self.subTest(command=command):
                result = render(command, SPEC)
                self.assertNotIn("{{", result)
                self.assertNotIn("<MODE:", result)
                for value in SPEC.values():
                    self.assertIn(value, result)

    def test_backlog_omits_execute_branch(self):
        result = render("deep-backlog", SPEC)
        self.assertIn("BACKLOG OUTPUT", result)
        self.assertNotIn("EXECUTE OUTPUT", result)
        self.assertIn("Do not change product code or deploy", result)

    def test_execute_omits_backlog_branch(self):
        result = render("deep-execute", SPEC)
        self.assertIn("EXECUTE OUTPUT", result)
        self.assertNotIn("BACKLOG OUTPUT", result)

    def test_executor_remains_distinct(self):
        result = render("backlog-executor", SPEC)
        self.assertIn("EXECUTION LOOP", result)
        self.assertIn("VERIFIED IN BRANCH", result)
        self.assertNotIn("Mode:", result)

    def test_missing_fields_fail(self):
        for field in FIELDS:
            with self.subTest(field=field):
                incomplete = {key: value for key, value in SPEC.items() if key != field}
                with self.assertRaises(ValueError):
                    render("deep-execute", incomplete)

    def test_unknown_fields_fail(self):
        with self.assertRaises(ValueError):
            render("deep-execute", {**SPEC, "MODE": "BACKLOG"})

    def test_blank_and_wrong_types_fail(self):
        for value in ("", "  ", None, 7, [], {}):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    render("deep-execute", {**SPEC, "GOAL": value})

    def test_unresolved_values_fail(self):
        with self.assertRaises(ValueError):
            render("deep-execute", {**SPEC, "PROJECT": "{{PROJECT}}"})

    def test_unknown_command_fails(self):
        with self.assertRaises(ValueError):
            render("backlog-fill", SPEC)

    def test_literal_content_not_recursively_processed(self):
        text = "Literal \\1 and <MODE:EXECUTE> are task data, not renderer instructions."
        self.assertIn(text, render("deep-backlog", {**SPEC, "CONTEXT": text}))

    def test_input_is_not_mutated(self):
        before = copy.deepcopy(SPEC)
        render("deep-execute", SPEC)
        self.assertEqual(SPEC, before)

    def test_duplicate_json_keys_fail(self):
        with self.assertRaises(ValueError):
            read_json('{"PROJECT":"one","PROJECT":"two"}')

    def test_json_array_fails(self):
        with self.assertRaises(ValueError):
            read_json('[]')

    def test_russian_context_and_limits_preserved(self):
        spec = {**SPEC, "PROJECT": "Птичи", "CONSTRAINTS": "Без push и деплоя. Не менять main."}
        for command in ROUTES:
            self.assertIn(spec["CONSTRAINTS"], render(command, spec))

    def test_common_evidence_guardrails_present(self):
        # Text retention is useful regression coverage, not proof of model obedience.
        for command in ROUTES:
            result = render(command, SPEC)
            self.assertIn("Never promise background continuation", result)
            self.assertIn("repo/ref/SHA", result)
            self.assertIn("no-deploy", result)

    def test_cli_stdin_renders(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/prompts.py"), "render", "deep-backlog", "--spec", "-"],
            input=json.dumps(SPEC), text=True, capture_output=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("BACKLOG OUTPUT", result.stdout)
        self.assertEqual(result.stderr, "")

    def test_cli_invalid_input_has_no_partial_prompt(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/prompts.py"), "render", "deep-execute", "--spec", "-"],
            input='{}', text=True, capture_output=True, check=False,
        )
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("Missing fields", result.stderr)


if __name__ == "__main__":
    unittest.main()
