# Website stack adapter

Use only for website work, after the target's trusted entry point. This is supporting guidance for the existing commands, not another prompt, framework migration or deployment authorization. In ChatGPT, read the selector and relevant sections; do not prepend this entire guide to every run. Repository preparation stays in [REPOSITORY_SETUP.md](REPOSITORY_SETUP.md); publication rules stay in [GITHUB_WORKFLOW.md](GITHUB_WORKFLOW.md).

## 1. Detect the contract, not the brand

GitHub Pages is a static host; Next.js is a framework that can produce static output or require a runtime. They are not mutually exclusive. Select from inspected code/configuration, not the repository name or a remembered deployment. [Sources 1–2](#sources)

| Observed target | Read next | Do not assume |
|---|---|---|
| Plain HTML or another static generator, published to Pages | Static host | That every Pages site uses Jekyll, React or Node |
| Next.js with static export, on Pages or another static host | Next.js common + static export; static host where applicable | That Server Components require a production server |
| Next.js with a supported server/runtime deployment | Next.js common + runtime | That Vercel is required or that all routes render on request |
| Conflicting evidence, another stack, or multiple workspace apps | Resolve the affected app and relevant contract first | That the closest profile authorizes conversion |

Build a small session record using existing maps and targeted source reads:

```text
Target workspace / branch / observed revision:
Framework and resolved version / router or generator:
Rendering and output mode / host and production URL prefix:
Canonical data, routes, templates and generated-output policy:
Working directory / runtime / package manager / lockfile:
Actual check/build commands / safe environment names / side effects:
Production and preview triggers / authority / unresolved evidence:
```

Inspect the affected app's package manifest, lockfile, framework/generator config, entry routes and build workflow. A manifest range is not an installed version. No package manifest is required for plain HTML. In a monorepo, do not confuse root tooling with the application's dependencies or deployment directory. Mark unknowns; resolve consequential contradictions before the affected edit, while continuing independent safe work.

Keep this in the existing session evidence map or repository task map, not a new mandatory manifest. Put resolved facts in CONTEXT, restrictions in AUTHORITY/CONSTRAINTS and actual evidence required in DONE_WHEN. No new user fields or command flags.

## 2. Read and change one vertical slice

Start from the behavior being changed: URL -> route/template -> data/schema -> shared components/styles -> relevant check. Read coupled files at one observed revision, then expand only when an import, contract or failure requires it. Large datasets and generated directories are not default context dumps.

| Change | Minimum coupled surface to inspect |
|---|---|
| Content/data | Canonical record, schema, consuming template, links/IDs and affected route generation |
| UI/interaction | Route, component, existing design tokens/styles, state and relevant behavior checks |
| Routing/discovery | Route source, host prefix, metadata, sitemap/link generation and missing-page behavior |

For data-driven sites, edit canonical records or generators, not thousands of emitted pages. Preserve IDs, slugs, references, locale coverage and URL contracts. When outputs are intentionally committed, regenerate them with the documented tool and include required outputs; do not silently change the repository's policy. Check route-count changes against the intended data change, not a goal of producing more pages.

Reuse existing components, styles, dependencies and tests. A small interaction does not automatically justify a new UI library, client-wide state system or framework migration. Avoid unrelated formatting and lockfile churn in connector replacements.

## 3. Static host, including GitHub Pages

Confirm whether publication consumes a branch/folder or a build artifact, which generator actually runs, and the expected output directory. Preserve CNAME/custom-domain and Jekyll bypass behavior where applicable; do not add or remove `.nojekyll` blindly. Pages can publish custom-built static output. [Sources 1, 3](#sources)

Resolve whether the site lives at the domain root or a project subpath. Test assets, internal links, deep-link reloads, canonical URLs and the generated sitemap against that prefix. Inspect the framework's existing URL helper rather than globally replacing `/` paths. A custom domain can change the correct prefix. [Sources 1, 6](#sources)

Do not add server-dependent endpoints, sessions or server filesystem writes to a static artifact. An external service is a separate architecture, privacy and cost decision, not an invisible substitute for missing hosting features. Do not introduce one without authority.

Validate the generator and its output with existing tools. Serve the built artifact with matching path semantics when a runtime exists; check representative nested routes and a missing route. A development server's SPA fallback can conceal a broken production deep link. Local serving is not proof that Pages deployed that artifact.

## 4. Next.js common: version and boundaries

Determine App Router, Pages Router or coexistence for the affected route. Use version-matched official documentation for APIs you change; do not mix router conventions or apply an upgrade guide as permission to upgrade. Current Next.js guidance describes bundled docs under `node_modules/next/dist/docs/` when available. A GitHub-only reader may not have installed dependencies or those files: use accessible version-matched official docs and state gaps, rather than committing node_modules or inventing a local read. Fetch the relevant documentation/error page, not a whole documentation dump. Preserve framework-managed instruction blocks and the project rules outside them. [Source 4](#sources)

For App Router, keep interactive Client Components narrowly scoped; do not move a whole layout or dataset into the client bundle just to fix a hook/import error. Check serialization and server-only imports across the boundary. Client Components can still be prerendered: browser APIs need browser-safe access. Server Components are not synonymous with request-time rendering. [Sources 2, 5](#sources)

Read the actual scripts and lockfile before installing or verifying. Do not hard-code `npm`, `next export` or `next lint` as universal commands. Current versions use `output: 'export'` with the build; Next.js 16 removed `next lint`, and its build does not run linting. Respect the installed version and configured standalone lint/type/test checks. Do not upgrade dependencies or disable checks to make a task appear green. [Sources 2, 7](#sources)

Keep secrets out of client props, static JSON and logs. `NEXT_PUBLIC_` values are public and can be inlined at build time; changing a runtime setting does not necessarily change an already-built client artifact. Document names, not values. [Source 8](#sources)

### Static export

Preserve the export constraint. Check affected dynamic-route coverage, build-time data availability, output files and a supported image strategy. App Router dynamic routes need their intended build-time parameters; Pages Router uses its own static-generation contracts. Build-time Server Components and eligible static GET Route Handlers can be valid; do not ban them merely for containing server code. [Sources 2, 10](#sources)

Do not introduce request-dependent Route Handlers, Server Actions, ISR or default server image optimization into a static-only deployment. Framework redirects/rewrites needing a server are not supplied by a static host. Do not remove export mode or add a hosted backend as a "fix" without explicit architectural authority. Verify the existing base-path/trailing-slash/image configuration rather than copying a generic Pages config. [Sources 2, 6](#sources)

### Runtime deployment

Inspect the supported deployment runtime, route behavior, caching/revalidation configuration, environment needs and integration boundaries. Do not assume caching defaults across versions or make every route dynamic to suppress a build error. Changes to data freshness need an observable stale/fresh acceptance check, not a speculative performance claim.

For server mutations or authenticated data, retain server-side authorization, input validation and secret boundaries; client visibility is not authorization. Exercise changed loading/error/empty states and failure paths with safe fixtures where feasible. Identify database migrations, paid API calls and production writes before running tests or build hooks. Do not create production side effects as verification.

## 5. Verification without accidental publication

Choose evidence for the changed surface, not an enormous new test suite. Reuse actual checks; distinguish data/schema, lint/types/tests, production build, built-route smoke checks, and browser/visual inspection. A build is not proof of every other category. Shared generators, layouts and config need broader representative coverage than an isolated text edit.

For route/discovery work inspect emitted/served content, status, title/canonical, crawl directives and sitemap inclusion as relevant. No single score, metadata file or successful build proves indexing, rankings or AI recommendations. For UI work inspect the actual revision at useful viewport sizes when tools permit; an old live site is not a preview of an unpublished patch. Record the exact browser gap when unavailable.

Read install/build/test hooks before executing them. A command named `build` is not proof of no network or publication effects. Under no-deploy restrictions, use safe local verification or existing validation-only CI only through an authorized path. Branch pushes can trigger provider previews; absence of a deploy workflow does not prove absence of Vercel or another provider's integration. Do not alter deployment gates to bypass the restriction. [Source 9](#sources)

Report revision, selected profile, changed behavior, commands/results, route/environment tested, browser gaps and publication state. CI evidence must match the checked revision; a production URL may still serve older code. With no runtime or browser, continue source-level work within its risk boundary and label build/render verification as not run. Do not install new infrastructure merely to avoid acknowledging a gap.

## Sources

Checked 2026-09-09. Recheck the relevant version-specific source when changing an API. The profiles and narrow-read strategy are library design choices, not measured speedups or platform guarantees.

1. [GitHub: what Pages hosts and site types](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)
2. [Next.js: App Router static exports](https://nextjs.org/docs/app/guides/static-exports)
3. [GitHub: creating a Pages site and custom generators](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)
4. [Next.js: AI coding agents and version-matched docs](https://nextjs.org/docs/app/guides/ai-agents)
5. [Next.js: Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components)
6. [Next.js: basePath](https://nextjs.org/docs/app/api-reference/config/next-config-js/basePath)
7. [Next.js: version 16 migration reference](https://nextjs.org/docs/app/guides/upgrading/version-16)
8. [Next.js: environment variables](https://nextjs.org/docs/app/guides/environment-variables)
9. [Vercel: deployment environments](https://vercel.com/docs/deployments/environments)
10. [Next.js: Pages Router static exports](https://nextjs.org/docs/pages/guides/static-exports)
