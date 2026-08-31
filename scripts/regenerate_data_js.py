#!/usr/bin/env python3
"""Regenerate mailroom-dev-graph data.js from a freshly built graph.json.

Reproduces the data bundle for the custom index.html shell: graphNodes,
graphEdges, graphLayers (counts refreshed), graphPipeline (static 13-node
conveyor), graphGods (top callable hubs), graphRels (edge-type counts).

graphEdgeConf: the previous build carried an LLM edge-scan confidence map.
graphify 0.9.53 has no `scan` subcommand, so this rebuild is AST-only and
emits an empty graphEdgeConf (the insights panel simply has no inferred
edges to show). See README.

Usage: python3 scripts/regenerate_data_js.py <graph.json> <output data.js>
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

NEW_GRAPH = Path(sys.argv[1])
OUT = Path(sys.argv[2])

new = json.loads(NEW_GRAPH.read_text())

BUILT = datetime.now(timezone.utc).strftime("%Y-%m-%d")
COMMIT = new.get("built_at_commit", "?").split("-")[0][:7] if new.get("built_at_commit") else "?.???????"

def esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\r", "")

def js_quote(s: str) -> str:
    return '"' + esc(s) + '"'

# degree
degree = Counter()
for e in new["links"]:
    degree[e["source"]] += 1
    degree[e["target"]] += 1

# preserve old layers definitions (id/title/blurb/color) with new counts
old_js = ""
try:
    old_js = Path(sys.argv[3]).read_text(encoding="utf-8", errors="replace")
except (IndexError, OSError):
    pass
old_layers = []
if old_js:
    m = re.search(r"var graphLayers = (\[.*?\]);", old_js, re.S)
    if m:
        old_layers = json.loads(m.group(1))

layer_of = {}
for n in new["nodes"]:
    sf = n.get("source_file") or ""
    parts = sf.split("/")
    ly = parts[0] if parts else "other"
    layer_of.setdefault(ly, set()).add(n["id"])

# mailroom-dev uses package names as layer ids, not "src"
def layer_id(n: dict) -> str:
    sf = n.get("source_file") or ""
    parts = sf.split("/")
    if len(parts) >= 2 and parts[0] == "packages":
        return parts[1]
    return "other"

layer_ids = {}
for n in new["nodes"]:
    lid = layer_id(n)
    layer_ids.setdefault(lid, 0)
layer_counts = Counter()
for n in new["nodes"]:
    layer_counts[layer_id(n)] += 1

# build layer list: known 9 layers preserved, counts refreshed
KNOWN_LAYER_TITLES = {
    "llm-mailroom": ("Mailroom Pipeline", "Core document conveyor: ingest to classify to extract to judge to archive; FastAPI intake, watcher, bins, agents."),
    "llm-entity-extraction": ("Entity Extraction", "Sorter, specialist agents, eval loops, classification scoring, Hub inventories."),
    "agent-mailroom": ("Agent Mailroom", "Queue-based processing, operator desk, pipeline runner, API + websocket."),
    "The-Mailroom": ("Mailroom UI (Telemetry)", "Dashboard visualizer: Langfuse/trace viewer, multi-source metrics, hosted telemetry UI."),
    "llm-dojo-scoring": ("Dojo Scoring", "Scoring engine: classification, field scoring, bootstrap, consistency checks."),
    "local-mailroom-sandbox": ("Sandbox", "Local experiment env: CLI interface, agent skills, prompts."),
    "claims-data-eda": ("Claims EDA", "Insurance claims EDA: CMS DE-SynPUF exploration, pipeline-ready candidate corpora."),
    "Enron-Evaluation-Environment": ("Enron EDA", "Enron correspondence EDA: message index to pipeline-ready correspondence datasets."),
    "other": ("Other", "Files outside the workspace package layout (root-level artifacts)."),
}
COLORS = ["#34d399", "#38bdf8", "#818cf8", "#fbbf24", "#fb7185", "#a78bfa", "#2dd4bf", "#f472b6", "#64748b"]

layers = []
for lid, cnt in layer_counts.most_common():
    title, blurb = KNOWN_LAYER_TITLES.get(lid, (lid, ""))
    color = "#64748b"
    for ol in old_layers:
        if ol.get("id") == lid:
            color = ol.get("color", color)
            title = ol.get("title", title)
            blurb = ol.get("blurb", blurb)
            break
    layers.append({"id": lid, "title": title, "blurb": blurb, "color": color, "count": cnt})

# pipeline: static 13-node conveyor
PIPELINE = [
    {"id": "ingest", "label": "Ingest", "symbol": "ingest_node"},
    {"id": "classify", "label": "Classify", "symbol": "classify_node"},
    {"id": "retry_classify", "label": "Retry classify", "symbol": "retry_classify_node"},
    {"id": "review_classify", "label": "Lane A review", "symbol": "review_classify_node"},
    {"id": "extract", "label": "Extract", "symbol": "extract_node"},
    {"id": "retry_extract", "label": "Retry extract", "symbol": "retry_extract_node"},
    {"id": "judge_verify", "label": "Lane B judge", "symbol": "judge_verify_node"},
    {"id": "arbiter", "label": "Arbiter", "symbol": "arbiter_node"},
    {"id": "boss_escalation", "label": "Boss", "symbol": "boss_escalation_node"},
    {"id": "human_review", "label": "Human review", "symbol": "human_review_node"},
    {"id": "compile_report", "label": "Report", "symbol": "compile_report_node"},
    {"id": "catalog_write", "label": "Catalog", "symbol": "catalog_write_node"},
    {"id": "archive", "label": "Archive", "symbol": "archive_node"},
]

# gods: top-12 callable hubs
gods = []
for nid, d in degree.most_common():
    node = next(n for n in new["nodes"] if n["id"] == nid)
    if node.get("_callable") is not True:
        continue
    gods.append({"label": node.get("label", node["id"]), "degree": d, "id": node["id"], "file": node.get("source_file", "")})
    if len(gods) >= 12:
        break

# rels
rels = dict(Counter(e.get("relation", "imports") for e in new["links"]).most_common())

# nodes: id, l, t, sf, ly, c, cn, d, loc
# (match the previous bundle: rationale/concept nodes are dropped — they are
#  comment-sidecar nodes, not architecture; edges reference the kept ids only)
DROPPED_TYPES = {"rationale", "concept"}
kept_ids = {n["id"] for n in new["nodes"] if n.get("file_type") not in DROPPED_TYPES}

nodes_out = []
for n in new["nodes"]:
    if n.get("file_type") in DROPPED_TYPES:
        continue
    sf = n.get("source_file") or ""
    nodes_out.append({
        "id": n["id"],
        "l": n.get("label", n["id"]),
        "t": n.get("file_type", "code"),
        "sf": sf,
        "ly": layer_id(n),
        "c": n.get("community", 0),
        "cn": n.get("community_name") or ("Community %s" % n.get("community", 0)),
        "d": degree.get(n["id"], 0),
        "loc": n.get("source_location", ""),
    })

edges_out = []
for e in new["links"]:
    edges_out.append({"f": e["source"], "t": e["target"], "r": e.get("relation", "imports")})

# LLM/rule edge-scan confidence: graphify 0.9.53 marks sub-confidence links
# (confidence_score < 1.0) as the INFERRED pool — the insights panel keys on
# "f\0t\0r" -> confidence, so rebuild graphEdgeConf from exactly those.
edge_conf = {}
for e in new["links"]:
    cs = e.get("confidence_score", 1.0)
    if cs < 1.0:
        edge_conf[f'{e["source"]}\u0000{e["target"]}\u0000{e.get("relation", "imports")}'] = cs

out = []
out.append("// mailroom-dev knowledge graph data")
out.append(f"// Generated {BUILT} @ {COMMIT}")
out.append("")
out.append("var graphNodes = " + json.dumps(nodes_out) + ";")
out.append("var graphEdges = " + json.dumps(edges_out) + ";")
out.append("var graphLayers = " + json.dumps(layers, indent=1) + ";")
out.append("var graphPipeline = " + json.dumps(PIPELINE) + ";")
out.append("var graphGods = " + json.dumps(gods) + ";")
out.append("var graphRels = " + json.dumps(rels) + ";")
out.append("")
out.append("// Rule-inferred edge confidence for sub-confidence edges (graphify confidence_score < 1.0), keyed \"f\\u0000t\\u0000r\"")
out.append("var graphEdgeConf = " + json.dumps(edge_conf) + ";")

OUT.write_text("\n".join(out) + "\n", encoding="utf-8")
print(f"data.js: {len(nodes_out)} nodes, {len(edges_out)} edges, {len(layers)} layers, {len(gods)} gods")
print(f"stats: {len(nodes_out)} symbols / {len(edges_out)} edges / {len(set(n.get('community') for n in new['nodes']))} communities / {len(set(n.get('source_file') for n in new['nodes'] if n.get('source_file')))} files")