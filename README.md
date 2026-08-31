# mailroom-dev-graph

Interactive knowledge graph of [mailroom-dev](https://github.com/Exios66/mailroom-dev), rebuilt 2026-08-30 from commit [`998922f`](https://github.com/Exios66/mailroom-dev/commit/998922f0dd12107949a20a08489b88c3771e9030).

Live site: https://exios66.github.io/mailroom-dev-graph/

## How to read it

The knowledge map spans the entire mailroom-dev monorepo — 9 workspace packages covering the LLM-Mailroom constellation. It's scoped to **production Python code only** and is meant to be walked, not stared at.

| Page | What it is |
|---|---|
| [Architecture map](./index.html) | Default view. Three zoom levels: **layers → modules → symbols** (toolbar or double-click drill-down). Conveyor strip jumps to the 13 LangGraph nodes. ⛓ edge-type filter. **⚡ LLM edge scan**: hidden connections, bridge nodes, inferred-edge spotlight with per-edge confidence. ★ god-node spotlight. Double-click isolates a neighborhood. `/` searches · `i` opens insights. |
| [Module tree](./tree.html) | Filesystem collapsible tree of the same graph. |
| [Report](./report.html) | God nodes, communities, bridges, suggested questions. |
| [Classic vis](./graph.html) | Graphify's stock force-directed canvas, if you want the hairball. |

## Reading the architecture map

- **Symbols** — all 4,870 code symbols; double-click any node to isolate it + its neighbors.
- **Modules** — 463 source files aggregated; node size = symbol count; double-click a module to open its symbols.
- **Layers** — the 9 workspace packages; double-click a layer to focus it.
- **Edge semantics** — solid = AST-extracted, **dashed amber = LLM-inferred** (graphify's edge scan, 571 edges, avg confidence 0.89; hover any edge for its relation + confidence).
- **⚡ insights** — data-driven navigation: top **hidden connections** (LLM-inferred and cross-package edges, ranked, click to jump), **bridge nodes** spanning the most packages (click to isolate), a **spotlight** that shows only inferred edges, and a **cross-package edges only** lens.
- **⛓ edges** — filter the 12 relation types (`calls`, `imports`, `contains`, …) and the inferred edges on/off.
- **★ god nodes** — spotlight the 12 most-connected hubs from the report.
- **Labels** — culled by zoom level: far out only hubs are labeled, zoom in for everything.

## Corpus

- **Included:** All 9 workspace packages' production code — `llm-mailroom`, `llm-entity-extraction`, `agent-mailroom`, `The-Mailroom`, `llm-dojo-scoring`, `local-mailroom-sandbox`, `claims-data-eda`, `Enron-Evaluation-Environment`
- **Excluded:** `tests/`, `notebooks/`, `.opencode/skills`, `docs/`, `deploy/`, frontend assets
- **Extractor:** graphify 0.9.48, `--code-only` AST, 0 LLM tokens

## Stats

- **4,870 code symbols** · **16,161 edges** · **325 communities** · **463 files**

## Rebuild

```bash
git clone https://github.com/Exios66/mailroom-dev.git /tmp/mailroom-dev
# copy the .graphifyignore from this repo's last rebuild notes
uv tool install graphifyy
graphify extract /tmp/mailroom-dev --code-only --force --resolution 0.4 --exclude-hubs 99
graphify cluster-only /tmp/mailroom-dev --no-label --no-viz --resolution 0.4 --exclude-hubs 99
graphify tree --graph /tmp/mailroom-dev/graphify-out/graph.json --output tree.html --label mailroom-dev
```

Then regenerate `index.html` / `report.html` / `graph.html` from `graph.json` using the generator scripts.

Note: `data.js` ends with `graphEdgeConf` — the per-edge confidence map for the LLM-inferred edges, joined from `graph.json` links (`source`, `target`, `relation` → `confidence_score`). Re-append it after any regeneration, or the ⚡ insights panel loses its confidence readout.
