# mailroom-dev-graph

Interactive knowledge graph of [mailroom-dev](https://github.com/Exios66/mailroom-dev), rebuilt 2026-08-31 from commit [`69f572a2`](https://github.com/Exios66/mailroom-dev/commit/69f572a2eec37b69de0b7bdb55f849c06ecf0905).

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

- **Symbols** — all 4,881 code symbols; double-click any node to isolate it + its neighbors.
- **Modules** — 508 source files aggregated; node size = symbol count; double-click a module to open its symbols.
- **Layers** — the 9 workspace packages; double-click a layer to focus it.
- **Edge semantics** — solid = AST-extracted, **dashed amber = rule-inferred** (graphify's confidence_score < 1.0 pool, 587 edges, avg confidence 0.89; hover any edge for its relation + confidence).
- **⚡ insights** — data-driven navigation: top **hidden connections** (inferred and cross-package edges, ranked, click to jump), **bridge nodes** spanning the most packages (click to isolate), a **spotlight** that shows only inferred edges, and a **cross-package edges only** lens.
- **⛓ edges** — filter the relation types (`calls`, `imports`, `contains`, …) and the inferred edges on/off.
- **★ god nodes** — spotlight the 12 most-connected hubs from the report.
- **Labels** — culled by zoom level: far out only hubs are labeled, zoom in for everything.

## Corpus

- **Included:** All 9 workspace packages' production code — `llm-mailroom`, `llm-entity-extraction`, `agent-mailroom`, `The-Mailroom`, `llm-dojo-scoring`, `local-mailroom-sandbox`, `claims-data-eda`, `Enron-Evaluation-Environment`
- **Excluded:** `tests/`, `notebooks/`, `.opencode/skills`, `docs/`, `deploy/`, frontend assets
- **Extractor:** graphify 0.9.53, `--code-only` AST, 0 LLM tokens

## Stats

- **4,881 code symbols** · **16,305 edges** · **252 communities** · **508 files**

## Rebuild

```bash
git clone https://github.com/Exios66/mailroom-dev.git /tmp/mailroom-dev
# copy the .graphifyignore shown in the last rebuild notes
uv tool install graphifyy
graphify extract /tmp/mailroom-dev --code-only --force
graphify cluster-only /tmp/mailroom-dev --no-label --no-viz
graphify tree --graph /tmp/mailroom-dev/graphify-out/graph.json --output tree.html --label mailroom-dev
graphify export html --graph /tmp/mailroom-dev/graphify-out/graph.json
```

Then regenerate the data bundle (the page shell `index.html` is static — it loads `data.js`):

```bash
python3 scripts/regenerate_data_js.py \
  /tmp/mailroom-dev/graphify-out/graph.json \
  data.js \
  data.js   # previous bundle, to preserve layer definitions
```

`report.html`'s stat tiles are updated by hand from the `graphify extract` summary.

Note: `data.js` ends with `graphEdgeConf` — the per-edge confidence map for the inferred edges, joined from `graph.json` links (`source`, `target`, `relation` → `confidence_score` where `confidence_score < 1.0`). Re-append it after any regeneration, or the ⚡ insights panel loses its confidence readout.