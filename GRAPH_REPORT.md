# Graph Report - mailroom-dev  (2026-08-31)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 6661 nodes · 16305 edges · 252 communities (208 shown, 26 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 587 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `69f572a2`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Community 0
- Community 1
- Community 2
- Community 3
- Community 4
- Community 5
- Community 6
- Community 7
- Community 8
- Community 9
- Community 10
- Community 11
- Community 12
- Community 13
- Community 14
- Community 15
- Community 16
- Community 17
- Community 18
- Community 19
- Community 20
- Community 21
- Community 22
- Community 23
- Community 24
- Community 25
- Community 26
- Community 27
- Community 28
- Community 29
- Community 30
- Community 31
- Community 32
- Community 33
- Community 34
- Community 35
- Community 36
- Community 37
- Community 38
- Community 39
- Community 40
- Community 41
- Community 42
- Community 43
- Community 44
- Community 45
- Community 46
- Community 47
- Community 48
- Community 49
- Community 50
- Community 51
- Community 52
- Community 53
- Community 54
- Community 55
- Community 56
- Community 57
- Community 58
- Community 59
- Community 60
- Community 61
- Community 62
- Community 63
- Community 64
- Community 65
- Community 66
- Community 67
- Community 68
- Community 69
- Community 70
- Community 71
- Community 72
- Community 73
- Community 74
- Community 75
- Community 76
- Community 77
- Community 78
- Community 79
- Community 80
- Community 81
- Community 82
- Community 83
- Community 84
- Community 85
- Community 86
- Community 87
- Community 88
- Community 89
- Community 90
- Community 91
- Community 92
- Community 93
- Community 94
- Community 95
- Community 96
- Community 97
- Community 98
- Community 99
- Community 100
- Community 101
- Community 102
- Community 103
- Community 104
- Community 105
- Community 106
- Community 107
- Community 108
- Community 109
- Community 110
- Community 111
- Community 112
- Community 113
- Community 114
- Community 115
- Community 116
- Community 117
- Community 118
- Community 119
- Community 120
- Community 121
- Community 122
- Community 123
- Community 124
- Community 125
- Community 126
- Community 127
- Community 128
- Community 129
- Community 130
- Community 131
- Community 132
- Community 133
- Community 134
- Community 135
- Community 136
- Community 137
- Community 138
- Community 139
- Community 140
- Community 141
- Community 142
- Community 143
- Community 144
- Community 145
- Community 146
- Community 147
- Community 148
- Community 149
- Community 150
- Community 151
- Community 152
- Community 153
- Community 154
- Community 155
- Community 156
- Community 157
- Community 158
- Community 159
- Community 160
- Community 161
- Community 162
- Community 163
- Community 164
- Community 165
- Community 166
- Community 167
- Community 168
- Community 169
- Community 170
- Community 171
- Community 172
- Community 173
- Community 174
- Community 175
- Community 176
- Community 177
- Community 178
- Community 179
- Community 180
- Community 181
- Community 182
- Community 183
- Community 184
- Community 185
- Community 186
- Community 187
- Community 188
- Community 189
- Community 190
- Community 191
- Community 192
- Community 193
- Community 194
- Community 195
- Community 196
- Community 197
- Community 198
- Community 199
- Community 200
- Community 201
- Community 202
- Community 203
- Community 204
- Community 205
- Community 206
- Community 207
- Community 208
- Community 209
- Community 210
- Community 211
- Community 212
- Community 213
- Community 214
- Community 215
- Community 216
- Community 218
- Community 219
- Community 222
- Community 223
- Community 224
- Community 225
- Community 226
- Community 227
- Community 228
- Community 230
- Community 231
- Community 232
- Community 247
- Community 248
- Community 249
- Community 250
- Community 251

## God Nodes (most connected - your core abstractions)
1. `require_env()` - 50 edges
2. `load_braintrust_config()` - 45 edges
3. `interpret_trace()` - 43 edges
4. `create_app()` - 43 edges
5. `LangfuseSource` - 41 edges
6. `load_config()` - 41 edges
7. `PipelineRun` - 39 edges
8. `default_jsonl_path()` - 39 edges
9. `get_prompt()` - 39 edges
10. `SorterAgent` - 38 edges

## Surprising Connections (you probably didn't know these)
- `_source_names()` --uses--> `MultiSource`  [INFERRED]
  packages/The-Mailroom/server/main.py → packages/The-Mailroom/mailroom_ui/multi_source.py
- `fetch_terminal_documents()` --uses--> `DocumentRecord`  [INFERRED]
  packages/llm-mailroom/src/storage/warehouse.py → packages/llm-mailroom/src/storage/catalog.py
- `ImageExtractor` --uses--> `BaseAgent`  [INFERRED]
  packages/llm-mailroom/src/agents/image_extractor.py → packages/llm-mailroom/src/agents/base.py
- `_live_image()` --uses--> `ImageExtractor`  [INFERRED]
  packages/local-mailroom-sandbox/src/mailroom_sandbox/eval/agents.py → packages/llm-mailroom/src/agents/image_extractor.py
- `PDFTranscriber` --uses--> `BaseAgent`  [INFERRED]
  packages/llm-mailroom/src/agents/pdf_transcriber.py → packages/llm-mailroom/src/agents/base.py

## Import Cycles
- None detected.

## Communities (252 total, 26 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.03
Nodes (159): save_manifest(), apply_intake(), Deterministic intake clerk — whitespace / hyphen / NBSP normalize. Procedural…, Normalize ``text`` and emit the ``normalize-intake`` span. Returns…, compile_matter_record(), _fmt_value(), Any, Procedural matter-record assembler (reporter LLM retired). Compiles… (+151 more)

### Community 1 - "Community 1"
Cohesion: 0.03
Nodes (145): active_api_tokens(), analyze_audit_database(), assert_bind_allowed(), _check_database(), _csv_tokens(), _document_payload_from_manifest(), document_source(), _embed_watcher_running() (+137 more)

### Community 2 - "Community 2"
Cohesion: 0.04
Nodes (104): BaseAgent, Classifies legal documents into mailroom document types. Two classification…, Classify a document and return (doc_type, confidence, reasoning). Args:…, Re-evaluate a document after low-confidence classification. Args: doc_text: The…, SorterAgent, main(), print_binary_results(), EvalResultShim (+96 more)

### Community 3 - "Community 3"
Cohesion: 0.04
Nodes (95): get_settings(), The process-wide settings object (lru-cached)., _as_list(), audit_list_field(), audit_scalar_field(), _containment_tokens(), _date_expected_is_null(), _date_grounded_in_doc() (+87 more)

### Community 4 - "Community 4"
Cohesion: 0.03
Nodes (61): BaseAgent, build_structured_schema(), ABC, ChatOpenAI, Base agent class — LangChain-powered LLM helpers with structured output. Every…, Return the FULL document text, capping only past the hard budget. The sorter is…, Plain text completion via the LangChain chain. Args: user_message: The user-…, Structured JSON extraction via ``with_structured_output``. Args: user_message:… (+53 more)

### Community 5 - "Community 5"
Cohesion: 0.04
Nodes (96): accuracy(), binary_metrics(), class_distribution(), confusion_accuracy(), confusion_matrix(), fbeta(), macro_accuracy(), macro_prf() (+88 more)

### Community 6 - "Community 6"
Cohesion: 0.04
Nodes (86): Aggregate per-row usage dicts into one tokens/cost summary. Each usage record…, tokens_summary(), append_experiment(), Append one JSON record to the experiment log (one line per run). The record is…, ContractsSpecialist, InsuranceClaimsSpecialist, log_experiment_to_repo(), main() (+78 more)

### Community 7 - "Community 7"
Cohesion: 0.04
Nodes (89): _experiment_id(), main(), print_comparison(), Resolve an experiment name to its id (creating nothing)., Fetch an experiment and return scored task rows., _summarize(), _task_results(), binary_dataset() (+81 more)

### Community 8 - "Community 8"
Cohesion: 0.09
Nodes (94): build_deck(), _cost(), _date(), _extraction_records(), _extraction_row(), _get(), _lb_group(), _lb_records() (+86 more)

### Community 9 - "Community 9"
Cohesion: 0.04
Nodes (83): equivalent_doc_subclasses(), normalize_doc_subclass(), normalize_sentiment_label(), normalize_sentiment_score(), SorterAgent — Legal Document Classification Agent (LangChain). Classifies…, Coerce a raw sorter subclass output to a canonical doc_subclass key.…, Return True when two doc_subclass keys are the same family or members of the…, Coerce a raw sentiment label to negative/neutral/positive, or None. (+75 more)

### Community 10 - "Community 10"
Cohesion: 0.06
Nodes (77): AsyncSession, DeclarativeBase, archive_document(), _file_sha256(), AuditLogEntry, Path, Best-effort sha256 of the archived file (audit A-7)., get_audit_trail() (+69 more)

### Community 11 - "Community 11"
Cohesion: 0.05
Nodes (61): IntEnum, Bundle, bundle_metric_names(), get_bundle(), Pre-built metric bundles — named groupings of registry metrics per task type,…, Return the named bundle, optionally validating against the registry., Every bundle metric must exist in the registry (fail-fast on typos). Returns…, Resolve a bundle (plus agent extras) to concrete metric names. ``max_tier``… (+53 more)

### Community 12 - "Community 12"
Cohesion: 0.06
Nodes (77): Map specialist agent → live classes it scores (merger listed separately)., specialists_with_suites(), active_corpus(), adapt_hub_row(), example_for_class(), example_rows(), examples_by_class(), hub_sample() (+69 more)

### Community 13 - "Community 13"
Cohesion: 0.08
Nodes (73): _bin_name(), document_view(), floor_bins(), floor_run(), Any, Path, Parked mail sits on a floor tray. In-flight work stays at a desk., read_source_text() (+65 more)

### Community 14 - "Community 14"
Cohesion: 0.08
Nodes (68): compute_metrics(), _p95(), datetime, Aggregations over interpreted runs — every number from Langfuse data., Generation, Metrics, NodeSpan, Phase (+60 more)

### Community 15 - "Community 15"
Cohesion: 0.08
Nodes (66): resolve(), _spawn(), specialist_for(), archive_dir(), claim_inbox(), classified_dir(), copy_classified(), enqueue_inbox() (+58 more)

### Community 16 - "Community 16"
Cohesion: 0.07
Nodes (67): estimate_cost(), estimate_for_record(), price_for(), Any, Per-model token pricing, cost estimation, and usage aggregation. Ported from…, Resolve a model string to its per-1M-token prices (exact, then prefix-matched…, USD cost for one run's token counts, or None when the model's price is unknown…, Cost estimate for an experiment-log record (stage-aware). Returns… (+59 more)

### Community 17 - "Community 17"
Cohesion: 0.05
Nodes (62): OpenAI, get_llm(), get_llm_client(), get_llm_model(), instrument_client(), Wrap the OpenAI client with the active tracing backend. Both Langfuse…, _build_providers(), get_provider() (+54 more)

### Community 18 - "Community 18"
Cohesion: 0.05
Nodes (59): exact_match(), failure(), Score 1.0 if the prediction matches the expected class, else 0.0., Score 1.0 for rows the model failed to classify (error sentinel)., _answer_task(), default_experiment_name(), load_dataset_for_mode(), load_local_documents() (+51 more)

### Community 19 - "Community 19"
Cohesion: 0.06
Nodes (51): ArbiterAgent, BossAgent, PdfTranscriberAgent, BaseAgent, Pipeline role agents — thin runnable wrappers over the vendored prompts. The…, run(user_message, schema) -> parsed dict via _call_structured., Blind second-opinion classifier (sorter_reviewer docclass lineage)., ReporterAgent (+43 more)

### Community 20 - "Community 20"
Cohesion: 0.06
Nodes (51): align_class(), align_subclass(), archive_document_name(), archive_name_from_run(), classification_card(), classification_from_run(), _compact(), _date_token() (+43 more)

### Community 21 - "Community 21"
Cohesion: 0.10
Nodes (54): Lock, main(), get_field_types(), get_type_bands(), _infer_field_types(), list_scores(), metrics_summary(), persist_scores() (+46 more)

### Community 22 - "Community 22"
Cohesion: 0.07
Nodes (50): One Langfuse session (matter in live runs, run-scoped in pilots)., SessionSummary, cache_dir(), cache_status(), _json_default(), load_metrics(), load_run(), load_traces() (+42 more)

### Community 23 - "Community 23"
Cohesion: 0.06
Nodes (56): Image, _attachment(), build_records(), category_of(), _clause_labels_from_data(), clause_labels_from_local(), list_pdf_paths(), load_clause_labels() (+48 more)

### Community 24 - "Community 24"
Cohesion: 0.09
Nodes (52): _mock_get_llm(), Return a fake OpenAI client for BaseAgent construction. Not used by the…, dataset_fingerprint(), parse_expected_fields(), new_record(), _classify_mock(), _expect_from_row(), hf_rows_as_manifest() (+44 more)

### Community 25 - "Community 25"
Cohesion: 0.05
Nodes (48): _LangChainContractsSpecialist, _LangChainSorterAgent, ContractsSpecialist, Contracts specialist — LangChain version vendored from llm-entity-extraction.…, Mailroom-configured contracts specialist. - Model/budget defaults come from…, Sorter agent — LangChain version vendored from llm-entity-extraction. Re-…, Mailroom-configured sorter. - Model/budget defaults come from ``taxonomy.yaml``…, Classify a document, optionally with page images attached. Returns ``(doc_type,… (+40 more)

### Community 26 - "Community 26"
Cohesion: 0.09
Nodes (54): _as_int(), fetch_pipeline_ops(), _get_json(), pipeline_api_prefix(), pipeline_base_url(), producer_url(), Any, Read-only bridge to the llm-mailroom API (watcher + inbox). Document display… (+46 more)

### Community 27 - "Community 27"
Cohesion: 0.05
Nodes (39): _aggregate(), Emitter, get_emitter(), LangfuseSink, LocalManifestSink, Any, Path, Protocol (+31 more)

### Community 28 - "Community 28"
Cohesion: 0.08
Nodes (49): is_enabled(), load_components(), prompt_for_agent(), Any, Sandbox component gates (eval skip + taxonomy routing overlay)., routing_overlay(), is_eval_enabled(), cell_name() (+41 more)

### Community 29 - "Community 29"
Cohesion: 0.07
Nodes (36): run_pipeline(), Warm the score-config schema OFF the document path (O-1).…, warmup_score_configs(), claim_file(), is_ingestion_paused(), list_stale_processing_files(), mark_processing_dead(), Move a stale processing file to the failed bin (finalize path). Used by startup… (+28 more)

### Community 30 - "Community 30"
Cohesion: 0.07
Nodes (34): BaseAgent, _is_retryable_error(), ABC, ChatOpenAI, Exception, Return the agent's system prompt string., System prompt + agent's skill files + tool descriptions + recent outcome…, Lazily build the LangChain ``ChatOpenAI`` client. Uses the OpenRouter base URL… (+26 more)

### Community 31 - "Community 31"
Cohesion: 0.09
Nodes (51): agent_fixture_path(), cache_dir(), fixture_file(), intake_dir(), load_agent_fixtures(), load_hf_fixtures(), load_jsonl(), load_legalbench_fixtures() (+43 more)

### Community 32 - "Community 32"
Cohesion: 0.08
Nodes (45): appendLog(), bindInspectCards(), consoleLog, counts, DOC_CLASSES, escapeHtml(), floor, hiveList (+37 more)

### Community 33 - "Community 33"
Cohesion: 0.08
Nodes (22): Avatar, DEFAULT_HIVE_ACTS, deskNearBin(), DESKS, drawAvatar(), drawBubble(), drawDeskLabel(), drawDeskSet() (+14 more)

### Community 34 - "Community 34"
Cohesion: 0.07
Nodes (30): AnnotationQueueClient, build_parser(), build_queue(), _iso(), LangfuseApiError, main(), main_with_args(), print_summary() (+22 more)

### Community 35 - "Community 35"
Cohesion: 0.10
Nodes (43): _auth_headers(), corpus_id(), corpus_revision(), fetch_rows(), gt_config(), load_ground_truth(), Any, Hugging Face corpus pin for The-Mailroom eval / Langfuse dataset sync.… (+35 more)

### Community 36 - "Community 36"
Cohesion: 0.10
Nodes (27): enriched_recent_runs(), _iso(), langfuse_host(), LangfuseSource, LangfuseUnavailable, list_recent_runs(), _page_data(), Any (+19 more)

### Community 37 - "Community 37"
Cohesion: 0.09
Nodes (40): Any, run_agent(), confidence(), extractable_types(), Return confidence / Lane B budgets, optionally merged with per-class severity.…, conflict_detail(), detect_conflict(), _entities() (+32 more)

### Community 38 - "Community 38"
Cohesion: 0.08
Nodes (40): _add_citation(), analyze(), _budget_shares(), _category_from_question(), _filing_type(), _load_cuad(), _load_full_texts(), main() (+32 more)

### Community 39 - "Community 39"
Cohesion: 0.07
Nodes (29): Arbiter agent — Lane B judgment arbitration (KANBAN-063). Architecture…, build_structured_schema(), BossAgent, BaseAgent, ComplianceSpecialist, BaseAgent, CorporateRecordsSpecialist, BaseAgent (+21 more)

### Community 40 - "Community 40"
Cohesion: 0.06
Nodes (30): get_prompt(), list_prompts(), PROMPT_TEMPLATES(), Get a prompt by version name. Args: version: Prompt version key (e.g.,…, List all available prompt versions., Return all prompt templates as a dict. Single source of truth for…, ComplianceFilingSpecialist, ContractsSpecialist (+22 more)

### Community 41 - "Community 41"
Cohesion: 0.09
Nodes (44): analyze_main(), _cli_export(), _dispatch(), export_main(), Command-line interface. - ``dojo-analyze`` — analyze a results workbook / JSONL…, Route ``python -m llm_dojo_scoring.cli <command> [args...]``. A leading…, sync_main(), _avg_rate() (+36 more)

### Community 42 - "Community 42"
Cohesion: 0.09
Nodes (42): get_extraction_schema(), Return the extraction JSON schema for a doc type (None if unknown)., _date_pair_days(), extraction_diagnostics(), _mean(), _median(), parse_duration_days(), _r2() (+34 more)

### Community 43 - "Community 43"
Cohesion: 0.09
Nodes (41): bene_snapshot(), build_beneficiaries(), carrier_claim_event(), claim_event(), collect_codes(), compact(), iso_date(), jopen() (+33 more)

### Community 44 - "Community 44"
Cohesion: 0.07
Nodes (35): AgentHandle, _annotation_attributes(), _init_opentelemetry(), init_phoenix_tracing(), _instrument_openai(), phoenix_enabled(), phoenix_endpoint_reachable(), phoenix_project_name() (+27 more)

### Community 45 - "Community 45"
Cohesion: 0.09
Nodes (40): compose_argv(), compose_file(), _docker(), CompletedProcess, Path, Docker Compose helpers for the sandbox stack., run_compose(), Local LLM mailroom sandbox. (+32 more)

### Community 46 - "Community 46"
Cohesion: 0.10
Nodes (40): Langfuse, build_prompt(), build_records(), fetch_hf_split(), list_task_dirs(), load_task(), main(), normalize_hf_rows() (+32 more)

### Community 47 - "Community 47"
Cohesion: 0.12
Nodes (23): _attr(), _error_from_events(), _iso(), _parse_io(), PhoenixSource, PhoenixUnavailable, Any, datetime (+15 more)

### Community 48 - "Community 48"
Cohesion: 0.09
Nodes (32): BaseHTTPMiddleware, Listener, create_app(), lifespan(), FastAPI, cors_origins(), Request, Browser-testing hardened headers. Office pages also get a strict CSP. (+24 more)

### Community 49 - "Community 49"
Cohesion: 0.08
Nodes (33): _cli_analyze(), _cli_sync(), _discover_env_file(), fetch_run_records(), group_rows_by_session(), _intake_fields_from_trace(), LangfuseClient, LangfuseConfig (+25 more)

### Community 50 - "Community 50"
Cohesion: 0.06
Nodes (35): The doc_type keys of the agent's (possibly extended) class list., Parse the tag-based vision output into the standard contract. Handles the…, Classify a document PAGE IMAGE with a vision model (qwen). Uses the versioned…, Classify a FULL PDF document in ONE vision call. Every rendered page of the PDF…, classify_image(), clean_prediction(), extract_confidence(), extract_reasoning() (+27 more)

### Community 51 - "Community 51"
Cohesion: 0.09
Nodes (39): ensure_field_score_configs(), Wire deterministic field scoring into Langfuse (GitHub issue #5). The scoring…, Idempotent: register the field-scoring configs in the Langfuse project. The…, Score one extraction deterministically and push every score to Langfuse,…, score_and_log_extraction(), _client(), create_trace_score(), deterministic_verdict_label() (+31 more)

### Community 52 - "Community 52"
Cohesion: 0.08
Nodes (27): get_suite(), _kind_for(), list_suites(), Any, Dedicated per-agent scoring suites. Task bundles (``bundles``) group metrics by…, Return the mailroom class if *name* is a doc-type alias (incl. ``doc:``)., Keep the specialist profile but bind this document class's catalogs.…, Return the dedicated suite for an agent or document type. Accepts profile names… (+19 more)

### Community 53 - "Community 53"
Cohesion: 0.11
Nodes (39): _as_list(), _documents(), _fold(), _fold_key(), is_valid_maud_answer(), _label_content_score(), _macro_f1(), _maybe_json() (+31 more)

### Community 54 - "Community 54"
Cohesion: 0.09
Nodes (38): mean(), Arithmetic mean over a list of numbers (0.0 for an empty list)., load_records(), main(), main_with_args(), Path, Read every experiment record from the JSONL log (append-only source)., _audit_summary_lines() (+30 more)

### Community 55 - "Community 55"
Cohesion: 0.10
Nodes (37): deque, Group, _console(), main(), Path, save(), banner(), debug_panel() (+29 more)

### Community 56 - "Community 56"
Cohesion: 0.12
Nodes (37): best_run(), confusion_drivers(), failure_mode_summary(), metric_trend(), model_summary(), _num(), per_group_summary(), per_subtype_summary() (+29 more)

### Community 57 - "Community 57"
Cohesion: 0.10
Nodes (37): display_name(), load_records(), main(), main_with_args(), select_records(), applicable_categories(), build_category_output(), _clean_span() (+29 more)

### Community 58 - "Community 58"
Cohesion: 0.11
Nodes (35): Sorter Reviewer agent — Lane A second-opinion classification (KANBAN-062).…, Independently classify the document. Returns ``{doc_type, contract_subtype,…, skip_conflict_field(), _compact(), enrich_extraction(), format_sorter_subclass_catalogs(), _normalize(), normalize_claim_type() (+27 more)

### Community 59 - "Community 59"
Cohesion: 0.14
Nodes (38): _agent_models(), build_parser(), _clone(), _cmd_agents_list(), _cmd_agents_show(), _cmd_api(), _cmd_cutover(), _cmd_datasets_help() (+30 more)

### Community 60 - "Community 60"
Cohesion: 0.10
Nodes (38): add_node(), _as_dict(), assert_run(), attach_scores(), attach_scores_via_sdk(), build_run(), cleanup_stale_traces(), DemoRun (+30 more)

### Community 61 - "Community 61"
Cohesion: 0.13
Nodes (33): ndarray, build_stats(), fig_chronic(), fig_comorbidity(), fig_corpus_overview(), fig_costs(), fig_demographics(), fig_monthly_volume() (+25 more)

### Community 62 - "Community 62"
Cohesion: 0.09
Nodes (36): _attach_field_scoring(), _check_cost_watchdog(), diff_report(), _fetch_openrouter_prices(), filter_real_samples(), _ground_truth_scores(), _ingest_scores(), main() (+28 more)

### Community 63 - "Community 63"
Cohesion: 0.14
Nodes (31): hive(), _agent_dir(), deliver(), list_inbox(), Any, Path, roster_status(), seed_hive() (+23 more)

### Community 64 - "Community 64"
Cohesion: 0.12
Nodes (28): chat_json(), _http_json(), LLMError, _mock_route(), Any, RuntimeError, parse_json_object(), Any (+20 more)

### Community 65 - "Community 65"
Cohesion: 0.08
Nodes (29): _apply_dict(), clear_settings_cache(), configure(), FieldScoringSettings, _load_from_path(), load_settings(), Any, Path (+21 more)

### Community 66 - "Community 66"
Cohesion: 0.09
Nodes (31): build_exhibit_records(), detect_record_type(), discover_and_extract(), fetch_filing_index(), fetch_fts_exhibit_hits(), get_with_retry(), index_url(), main() (+23 more)

### Community 67 - "Community 67"
Cohesion: 0.11
Nodes (31): ArbiterAgent, BaseAgent, Judgment arbitration on failed judge verdicts., Decide the outcome for a judge-rejected extraction. Returns ``{decision,…, BaseAgent, Independent second-opinion classifier (blind re-classification)., SorterReviewerAgent, cases_for_agent() (+23 more)

### Community 68 - "Community 68"
Cohesion: 0.12
Nodes (33): as_clause_lines(), clause_handoff(), enrich_contract_extraction(), flatten_cuad_clause_labels(), flatten_maud_clause_labels(), infer_merger_consideration(), normalize_consideration(), parse_json_obj() (+25 more)

### Community 69 - "Community 69"
Cohesion: 0.09
Nodes (17): FakeLangChainLLM, _FakeStructuredRunner, is_classify_call(), MAILROOM-LOCAL (not from upstream): deterministic fake LangChain LLM. The…, Runnable returned by ``with_structured_output``: invoke() yields the…, Extract the human text from a LangChain message list, handling multimodal list…, Replacement for the ChatOpenAI instance the vendored agents construct. -…, user_text_from_messages() (+9 more)

### Community 70 - "Community 70"
Cohesion: 0.10
Nodes (31): apply_intake(), _as_text_and_payload(), deterministic_normalize(), _flag_match(), _gold_from(), _int_match(), intake_prep_completeness(), intake_span_output() (+23 more)

### Community 71 - "Community 71"
Cohesion: 0.11
Nodes (27): amount_exactness(), determination_consistency(), _is_empty(), _norm(), Any, Insurance determination-consistency and amount-exactness scorers. These are…, Score a single predicted extraction for determination/reason coherence. Ground…, 1.0 if the money field matches after normalize; 0.0 if both parseable and… (+19 more)

### Community 72 - "Community 72"
Cohesion: 0.12
Nodes (28): assign_split(), build_merged(), load_cuad_rows(), load_cuad_rows_local(), load_dump_rows(), main(), main_with_args(), Path (+20 more)

### Community 73 - "Community 73"
Cohesion: 0.09
Nodes (30): flush_braintrust(), flush_langfuse(), get_trace_id(), install_on_dropped(), observation(), Open a child observation under the currently active span/trace. Named with…, Warn when the SDK drops events (O-3). Langfuse Python v4 has no ``on_dropped``…, shutdown_langfuse() (+22 more)

### Community 74 - "Community 74"
Cohesion: 0.09
Nodes (29): compute_run_metrics(), Core per-run metrics, computed for EVERY finished run regardless of the tracing…, classify_run_failure(), failure_audit_detail(), Any, BaseException, Classify pipeline crashes so aborted runs are distinguishable. ``run_pipeline``…, Return ``failure_class``, ``reason``, and ``detail`` for an abort. (+21 more)

### Community 75 - "Community 75"
Cohesion: 0.11
Nodes (27): ensure_dirs(), default_environment(), load_env(), Path, Load environment variables from a .env file. The app reads its configuration…, Assign `OBSERVABILITY_ENVIRONMENT` when nothing is set yet. Every entrypoint…, setup_logging(), _aggregate() (+19 more)

### Community 76 - "Community 76"
Cohesion: 0.15
Nodes (28): auth_required(), _b64url(), _b64url_decode(), create_access_token(), decode_token(), get_current_user(), jwt_expiry_hours(), jwt_secret() (+20 more)

### Community 77 - "Community 77"
Cohesion: 0.11
Nodes (29): accuracy_at_k(), build_confidence(), escalation_curve(), load_observations(), main(), main_with_args(), make_figures(), Path (+21 more)

### Community 78 - "Community 78"
Cohesion: 0.11
Nodes (26): all_specialist_field_keys(), Reject Complete payloads whose keys belong to another specialist. Mirrors llm-…, validate_operator_extraction(), _import_contract(), installed_mailroom_version(), _materialize_git_pin(), _origin_for(), _pin_cache_src() (+18 more)

### Community 79 - "Community 79"
Cohesion: 0.14
Nodes (28): _anonymous(), auth_required(), _b64url(), _b64url_decode(), create_access_token(), decode_token(), get_current_user(), get_current_user_or_ingest() (+20 more)

### Community 80 - "Community 80"
Cohesion: 0.15
Nodes (21): Observability: local spans, optional Langfuse/Phoenix, field scoring, trace…, flush_langfuse(), get_client(), _keys_present(), _NoopSpan, observation(), pipeline_trace(), Any (+13 more)

### Community 81 - "Community 81"
Cohesion: 0.09
Nodes (26): _load_rows(), main(), main_with_args(), Path, extraction_ab_v18_50 -> v18; extraction_ab_v22_max_50 -> v22max., Re-score every completed row; return per-field means + overall., rescore_manifest(), _version_from_stem() (+18 more)

### Community 82 - "Community 82"
Cohesion: 0.13
Nodes (21): build_parser(), main(), ArgumentParser, LegalBench suite CLI. Run a LegalBench task, trace it to Langfuse, and log the…, LegalBench evaluation suite — a second lens on model quality. The suite runs…, log_run(), _model_name(), print_summary() (+13 more)

### Community 83 - "Community 83"
Cohesion: 0.19
Nodes (27): date, audit_to_row(), daily_audit_path(), daily_documents_path(), document_to_row(), export_document_to_warehouse(), export_to_warehouse(), fetch_terminal_documents() (+19 more)

### Community 84 - "Community 84"
Cohesion: 0.10
Nodes (23): { app, BrowserWindow, ipcMain, session, shell }, attachSessionGuards(), bindIpc(), boot(), createWindow(), DEFAULT_PORT, http, parseArgs() (+15 more)

### Community 85 - "Community 85"
Cohesion: 0.12
Nodes (24): main(), as_percent(), display_model(), _infer_kind(), load_log(), normalize_results_frame(), parse_experiment_name(), Any (+16 more)

### Community 86 - "Community 86"
Cohesion: 0.12
Nodes (27): _acquire_zenodo_zip(), build_classification_records(), build_contract_records(), _download_zip(), _fetch_hf_csv(), load_contract_texts(), load_maud_rows(), main() (+19 more)

### Community 87 - "Community 87"
Cohesion: 0.14
Nodes (27): Ordered extraction-schema field names used as scoring labels., schema_fields(), align_class(), _as_float(), class_misses_ground_truth(), collect_review_causes(), coverage_below_floor(), expected_class() (+19 more)

### Community 88 - "Community 88"
Cohesion: 0.15
Nodes (25): ArchiveEntry, download_archive(), _entry_row(), list_archive(), preview_archive(), BaseModel, get, Path (+17 more)

### Community 89 - "Community 89"
Cohesion: 0.15
Nodes (23): db_path(), ensure_bins(), migrate(), Create operator tables and seed the default admin when the store is empty., Operator desk — auth, archive, ops, and bin observer. Not a document-display…, ``python -m operator_desk`` — migrate the operator store and print status., mount_operator(), operator_status() (+15 more)

### Community 90 - "Community 90"
Cohesion: 0.13
Nodes (19): apply_event(), main(), _now(), _patch_poller(), Stage changes must not sit behind the 60s detail cache., run_director(), serve(), set_stage() (+11 more)

### Community 91 - "Community 91"
Cohesion: 0.12
Nodes (24): _score_extract(), Compare local (Ollama/vLLM/…) vs API-key (OpenRouter) serving metrics.…, run_local_vs_api_eval(), attach_serving_identity(), compare_from_records(), compare_local_vs_api(), emit(), emit_local_vs_api_scorecard() (+16 more)

### Community 92 - "Community 92"
Cohesion: 0.12
Nodes (23): classify_many(), evidence_for(), _has_any(), _head(), _is_attorney(), label_correspondence(), _own_head(), Attorney/law-firm sender detection from the index row. (+15 more)

### Community 93 - "Community 93"
Cohesion: 0.12
Nodes (24): default_jsonl_path(), dotted_get(), git_snapshot(), load_records(), Any, Path, Experiment-log record helpers: JSONL append/load, dotted access, snapshots.…, Resolve the JSONL log path from env (or the repo default). (+16 more)

### Community 94 - "Community 94"
Cohesion: 0.15
Nodes (25): normalize_contract_subclass(), Canonicalize a docclass expected_subclass through the family map (case- and…, attach_clause_gt(), build_v5(), census(), load_claims(), load_cuad_clause_gt(), load_maud_clause_gt() (+17 more)

### Community 95 - "Community 95"
Cohesion: 0.18
Nodes (22): meta(), accepted_extensions(), agent_config(), agent_roster(), live_doc_types(), llm_provider_name(), Any, stamp_color() (+14 more)

### Community 96 - "Community 96"
Cohesion: 0.12
Nodes (19): bootstrap_ci(), _clean(), delta_significance(), Any, Random, Bootstrap confidence intervals and small-sample delta testing. Ported from…, Wilson score interval for an aggregate proportion. Used when only the aggregate…, Coerce a per-document score list to floats, dropping None/non-numeric. (+11 more)

### Community 97 - "Community 97"
Cohesion: 0.15
Nodes (23): _build_gt_fields(), _coerce_gt_value(), export_jsonl(), main(), Path, Parse list-like GT strings from the Hub into Python values., _load_contracts(), load_dataset() (+15 more)

### Community 98 - "Community 98"
Cohesion: 0.11
Nodes (21): classify_image(), clean_prediction(), extract_confidence(), extract_reasoning(), extract_runner_up(), Path, Extract the model's self-reported confidence (0-1) from a response., Classify a document image using a vision model through OpenRouter API. Args:… (+13 more)

### Community 99 - "Community 99"
Cohesion: 0.10
Nodes (18): applyTiledLayout(), cloneBins(), cloneDesks(), DOOR_SET, DOORS, inRoomInterior(), isWalkable(), layout (+10 more)

### Community 100 - "Community 100"
Cohesion: 0.13
Nodes (14): ImageExtractor, BaseAgent, Path, PDFTranscriber, BaseAgent, Path, PDF transcription agent — converts PDF documents to markdown for downstream…, Heuristic: if a PDF yields a dense, clean text extraction, the LLM reformat… (+6 more)

### Community 101 - "Community 101"
Cohesion: 0.14
Nodes (20): _memory_dir(), _memory_path(), Path, Per-agent OUTCOME MEMORY for the vendored LangChain agents. Every designated…, Count outcomes by source and by feedback keyword (for observability)., Render the last ``k`` outcomes for this agent+doc_type as a prompt appendix —…, recent_context(), stats() (+12 more)

### Community 102 - "Community 102"
Cohesion: 0.15
Nodes (22): Figure, build_all_plots(), plot_confidence_scatter(), plot_cost_efficiency(), plot_failure_modes(), plot_metric_ci(), plot_model_comparison(), plot_per_subtype_heatmap() (+14 more)

### Community 103 - "Community 103"
Cohesion: 0.17
Nodes (19): all_specialist_schema_keys(), coerce_extracted_data(), Any, Human-review resolve helpers (llm-mailroom v0.6.0 / The-Mailroom contract). -…, Normalize operator ``extracted_data``. Empty / missing → ``None``., Pick operator ``extracted_data``, else the parked manifest payload., Reject Complete payloads that do not match the parked document class., resolve_complete_extracted() (+11 more)

### Community 104 - "Community 104"
Cohesion: 0.13
Nodes (17): build_suite(), _cut_points(), expectations_for(), load_rows(), main(), Machine-checkable expectations per agent family × transform., agent_key -> rows carrying {filename, doc_text, gt_fields}., t_dup_content() (+9 more)

### Community 105 - "Community 105"
Cohesion: 0.13
Nodes (10): BaseAgent, ABC, True when this agent's model accepts image input and (optionally) page images…, Build the user-message content for a document input. Vision-capable models get…, Extract a long document in overlapping windows and merge the passes. Documents…, Domain skill files appended below the managed prompt (Langfuse prompt linking…, Truncate document text to the agent's configured input budget, marking the…, load_skills() (+2 more)

### Community 106 - "Community 106"
Cohesion: 0.16
Nodes (21): Message, _clean(), _decode_part(), _hdr(), iter_messages(), main(), main_with_args(), _parse_date() (+13 more)

### Community 107 - "Community 107"
Cohesion: 0.16
Nodes (21): _build_evaluator_request(), _build_output_definition(), _build_rule_request(), _client(), _current_evaluator_prompt(), _ensure_llm_connection(), _existing_rule_ids(), main() (+13 more)

### Community 108 - "Community 108"
Cohesion: 0.21
Nodes (20): clean_agent_rows(), clean_hf_rows(), clean_legalbench_rows(), clean_manifest_rows(), CleanReport, _display_path(), ensure_dotenv_from_example(), normalize_text() (+12 more)

### Community 109 - "Community 109"
Cohesion: 0.19
Nodes (21): _as_dict(), compute_ops_status(), current_runs(), get_distribution(), get_ops_status(), get_throughput(), ingest_event(), ops_health() (+13 more)

### Community 110 - "Community 110"
Cohesion: 0.19
Nodes (20): character_accuracy(), character_error_rate(), _chars(), _error_rate(), _levenshtein(), _mean(), _normalize_text(), Any (+12 more)

### Community 111 - "Community 111"
Cohesion: 0.17
Nodes (20): contract_key(), enrich_row(), flex_pattern(), load_cuad_contracts(), main(), norm(), parse_tsv(), Pattern (+12 more)

### Community 112 - "Community 112"
Cohesion: 0.10
Nodes (14): AgentHandle, deterministic_trace_id(), Any, Per-agent observation handle yielded by…, Attach the agent's composite result to its observation., Log one deterministic logic score against the AGENT's observation., Lazily construct the Langfuse client (singleton). Imported AFTER the…, Open ONE Langfuse trace for a document; yields its :class:`TraceHandle`.… (+6 more)

### Community 113 - "Community 113"
Cohesion: 0.19
Nodes (20): append_record(), build_record(), default_log_path(), default_sibling_root(), git_snapshot(), _inside(), Any, CompletedProcess (+12 more)

### Community 114 - "Community 114"
Cohesion: 0.15
Nodes (19): prompt_templates(), agent_name -> local prompt template (with `{{var}}` placeholders). Single…, client_kwargs(), get_langfuse_client(), instrument_openai_client(), _optional_float(), _optional_int(), pipeline_trace() (+11 more)

### Community 115 - "Community 115"
Cohesion: 0.16
Nodes (20): _denial_reasons(), determination_consistency_is_quality(), honesty_trace_metadata(), insurance_determination_consistent(), insurance_determination_issues(), insurance_expected_set_is_homogeneous(), insurance_gt_is_homogeneous(), _norm_determination() (+12 more)

### Community 116 - "Community 116"
Cohesion: 0.19
Nodes (20): _contracts_from_annotations(), _contracts_from_txt(), _download(), download_all(), _list_hf_files(), _load_subtype_taxonomy(), main(), _normalize_category() (+12 more)

### Community 117 - "Community 117"
Cohesion: 0.15
Nodes (14): LangfuseConfig, LangfuseConfig, _load_dotenv(), load_langfuse_config(), Path, Shared Langfuse environment configuration loader. Reads the Langfuse…, Resolved Langfuse configuration for the current environment., Load and resolve the Langfuse configuration (separate experiment env). Reads… (+6 more)

### Community 118 - "Community 118"
Cohesion: 0.16
Nodes (19): extrapolate(), fit_pipeline_probs(), main(), main_with_args(), make_figures(), _poisson_sf(), Path, Random (+11 more)

### Community 119 - "Community 119"
Cohesion: 0.15
Nodes (19): aggregate_accuracy(), champion_contender(), effectiveness(), main(), main_with_args(), pairwise_matrix(), Mean exact-match over the prompt's own documents (support = n docs)., Select the Monte Carlo champion contender from the pairwise matrix. A version… (+11 more)

### Community 120 - "Community 120"
Cohesion: 0.18
Nodes (19): agent_uses_vision(), _any_specialist_uses_vision(), is_vision_capable(), max_pages(), pipeline_uses_vision(), Path, Vision-capable model helpers for the mailroom pipeline. Some input agents (e.g.…, Render pages of a PDF to a list of PNG image data-URIs. `cap` is the page… (+11 more)

### Community 121 - "Community 121"
Cohesion: 0.20
Nodes (5): MultiSource, Any, datetime, Multi-source aggregator: serve several trace sources through one facade.…, Duck-types TraceSource over an ordered list of concrete sources.

### Community 122 - "Community 122"
Cohesion: 0.17
Nodes (11): archiveApi, documentsApi, runToDocument(), stageToBin(), reviewApi, ArchiveBrowser(), ReviewPanel(), ArchiveEntry (+3 more)

### Community 123 - "Community 123"
Cohesion: 0.16
Nodes (12): App(), ProtectedRoute(), ErrorBoundary, Props, State, LoginForm(), SidebarProps, useAuth() (+4 more)

### Community 124 - "Community 124"
Cohesion: 0.33
Nodes (19): assert_clean_tree(), cmd_pull(), cmd_push(), cmd_snapshot(), cmd_status(), fetch_upstream(), git(), load_manifest() (+11 more)

### Community 125 - "Community 125"
Cohesion: 0.17
Nodes (17): _addr_line(), build_sample(), _doc_text(), _fingerprint(), main(), main_with_args(), _metadata(), Path (+9 more)

### Community 126 - "Community 126"
Cohesion: 0.24
Nodes (18): all_local_pack_samples(), compliance_local_samples(), corporate_extraction_samples(), _hydrate(), insurance_contrast_samples(), local_pack_status(), _mean(), _perfect_extract_summary() (+10 more)

### Community 127 - "Community 127"
Cohesion: 0.19
Nodes (14): ConveyorAnimation(), ORDER, DocumentCard(), Props, statusIcons, BINS, PipelineBoard(), UploadDropzone() (+6 more)

### Community 128 - "Community 128"
Cohesion: 0.15
Nodes (9): check_phoenix(), phoenix_available(), PhoenixClient, PhoenixStatus, Phoenix / OTLP local trace-sink reader. The llm-entity-extraction pipeline's…, Query project spans as a list of dicts (or None when unavailable). Project name…, True when a Phoenix / OpenInference sink answers on ``base_url``., Best-effort status probe of the local trace sink. (+1 more)

### Community 129 - "Community 129"
Cohesion: 0.27
Nodes (17): bump_version(), check_site_data(), check_state(), current_version(), fail(), main(), main_with_args(), parse_changelog() (+9 more)

### Community 130 - "Community 130"
Cohesion: 0.15
Nodes (17): CorpusUnavailable, _fingerprint(), load_cuad_qa(), load_family_rows(), _normalize_prediction(), Any, Path, RuntimeError (+9 more)

### Community 131 - "Community 131"
Cohesion: 0.16
Nodes (11): explicit, PipelineWebSocket, pipelineWS, wsOrigin(), Layout(), navItems, Sidebar(), useWebSocket() (+3 more)

### Community 132 - "Community 132"
Cohesion: 0.23
Nodes (16): _barh(), _finish(), _fmt(), _grid(), _headroom(), _kfmt(), main(), main_with_args() (+8 more)

### Community 133 - "Community 133"
Cohesion: 0.21
Nodes (16): assert_coverage(), _blind_row(), _gt_row(), main_with_args(), normalize_blind_metadata(), publish(), Path, House cast-safe rules (union keys on every row; dicts/lists -> compact JSON… (+8 more)

### Community 134 - "Community 134"
Cohesion: 0.13
Nodes (12): build_structured_schema(), Build a JSON schema dict for structured output. ``title`` is required by…, _doc_classes_for_prompt(), BaseAgent, Classifies legal documents into mailroom document types. Two classification…, Classify a document and return (doc_type, contract_subtype, confidence,…, Classify and return the raw structured dict (used by eval loops). With…, Prefer the live taxonomy catalog; fall back to the hardcoded table. (+4 more)

### Community 135 - "Community 135"
Cohesion: 0.17
Nodes (6): Event, _main(), OpsMonitor, Pause metadata (actor/reason/expiry) via the TTL-aware helper., Like start(), but exits when ``stop_event`` is set (L-6: signal driven graceful…, run_ops_monitor()

### Community 136 - "Community 136"
Cohesion: 0.17
Nodes (14): classify_topics(), label_content_topic(), _own_body_head(), Subject + forwarded-tail-stripped body head, whitespace-collapsed., Assign the content topic for an index/pipeline row. Ordered scoring (NOT first-…, Label many rows; returns {topic_key: count} (all keys present)., Drop the forwarded-original tail of a reply/forward. A reply that carries a…, _strip_forwarded() (+6 more)

### Community 137 - "Community 137"
Cohesion: 0.23
Nodes (15): _catalog(), clear_prompt_cache(), get_prompt(), iter_prompts(), list_prompts(), _load_template(), _pkg_root(), PromptRecord (+7 more)

### Community 138 - "Community 138"
Cohesion: 0.23
Nodes (15): build_maud_classification_records(), build_records(), download_zip(), load_maud_labels(), load_maud_rows(), main(), Path, Build per-question multi-class classification records from MAUD rows. Each row… (+7 more)

### Community 139 - "Community 139"
Cohesion: 0.14
Nodes (9): LegalBenchAgent, Any, BaseAgent, Model agent for LegalBench runs. Reuses the vendored ``BaseAgent`` machinery —…, One agent instance per task run; answers via structured JSON., LegalBench tasks use the task prompt as-is (no sorter skills)., Yes/no answer with evidence + confidence., One-of-N family classification with confidence. (+1 more)

### Community 140 - "Community 140"
Cohesion: 0.22
Nodes (15): dedicated_suite(), field_types_for_class(), gt_schema_coverage(), list_dedicated_suites(), Any, Dedicated scoring suite for every live mailroom specialist. Dojo…, Mailroom registry row for one live extract class. ``suite_key`` is what…, One registry row per live extract class, in taxonomy order. (+7 more)

### Community 141 - "Community 141"
Cohesion: 0.26
Nodes (13): _client(), _existing_placements(), json_dumps(), main(), _placement_kwargs(), # NOTE: dimension on `model` (the requested model string, e.g., _score_widget(), _spec_to_request() (+5 more)

### Community 142 - "Community 142"
Cohesion: 0.20
Nodes (14): collect_attachments(), discover_dataset_names(), fetch_catalog(), fetch_rows(), main(), materialize_images(), Path, READ-ONLY dataset catalog: GET /v1/dataset (name -> info). Transient-failure… (+6 more)

### Community 143 - "Community 143"
Cohesion: 0.21
Nodes (14): build_corpus(), _extract_sorter_dict(), _log_rows(), main(), main_with_args(), _manifest_rows_by_experiment(), normalize_log_row(), _prompt_version_from_name() (+6 more)

### Community 144 - "Community 144"
Cohesion: 0.22
Nodes (14): confusion_pairs(), main(), main_with_args(), near_miss_traces(), Counter, Random, random_search(), (expected -> predicted) confusion counts from failure rows. (+6 more)

### Community 145 - "Community 145"
Cohesion: 0.16
Nodes (14): committee_accuracy(), Ensemble majority-vote accuracy at K over the task's observations., decoy_mentioned(), decoy_variants(), draw_committee(), _normalize(), Random, Shared Monte Carlo simulation utilities for the experiment-log reasoning… (+6 more)

### Community 146 - "Community 146"
Cohesion: 0.17
Nodes (15): _chunk_config(), _extract_compliance(), _extract_contracts(), _extract_corporate_records(), _extract_correspondence(), _extract_insurance_claims(), _instantiate_specialist(), Name → extract function. Keys MUST match taxonomy ``specialist:`` values. (+7 more)

### Community 148 - "Community 148"
Cohesion: 0.26
Nodes (13): _escape(), generate_pdf_from_text(), _load_manifest(), prepare_samples(), Path, Materialize every manifest row under data/samples/. Returns its path., _client(), _doc_text() (+5 more)

### Community 149 - "Community 149"
Cohesion: 0.28
Nodes (14): _api(), check_payload(), _die(), main(), publish(), Namespace, Path, Validate the Space card + Docker payload. Returns human-readable notes. (+6 more)

### Community 150 - "Community 150"
Cohesion: 0.20
Nodes (12): load_docclass_templates(), Vendored mirror of llm-entity-extraction's docclass prompt family. Byte-synced…, Docclass templates to sync: MAILROOM_DOCLASS_PROMPTS JSON wins., load_prompt_templates(), prompt_name(), Vendored mirror of llm-mailroom's agent prompts (the #1 maintenance duty).…, Templates to sync: MAILROOM_PROMPTS JSON file wins over the mirror., Langfuse prompt-management name for an agent (upstream contract). (+4 more)

### Community 151 - "Community 151"
Cohesion: 0.28
Nodes (14): _api(), check_payload(), _die(), main(), publish(), Namespace, Path, Validate the Space card + Docker payload. Returns human-readable notes. (+6 more)

### Community 152 - "Community 152"
Cohesion: 0.24
Nodes (13): build(), _category_of(), download_and_extract(), _fingerprint(), main(), main_with_args(), parse_test_rows(), Path (+5 more)

### Community 153 - "Community 153"
Cohesion: 0.25
Nodes (13): _archive_cards(), build_qmd(), _card_block(), _cells(), main(), main_with_args(), _open_cards(), _parse_table() (+5 more)

### Community 154 - "Community 154"
Cohesion: 0.29
Nodes (10): LLM-as-a-judge that evaluates extraction completeness against the source…, ComplianceFilingExtraction, ContractExtraction, CorporateRecordExtraction, CorrespondenceExtraction, get_extraction_schema(), InsuranceClaimExtraction, BaseModel (+2 more)

### Community 155 - "Community 155"
Cohesion: 0.19
Nodes (12): attach_run_scores(), ensure_score_configs_if_enabled(), _environment(), legalbench_trace(), Any, question_observation(), Langfuse tracing for LegalBench runs. One trace per run (deterministic seed =…, Open the per-run Langfuse trace (no-op when tracing is disabled). (+4 more)

### Community 156 - "Community 156"
Cohesion: 0.24
Nodes (12): Archived/cataloged but objective misses say it should not stay done., _align_class(), _as_float(), collect_review_causes(), _is_falsey_flag(), _is_true_flag(), Any, Objective review / reconsideration causes. Self-reported… (+4 more)

### Community 157 - "Community 157"
Cohesion: 0.31
Nodes (13): build_cast(), check_api(), check_cast(), main(), _now(), _patch_poller(), _point_visualizer_at_producer(), Any (+5 more)

### Community 158 - "Community 158"
Cohesion: 0.18
Nodes (8): auditApi, api, API_BASE, AuditChain(), COLORS, MetricsDashboard(), AuditEntry, OpsStatus

### Community 159 - "Community 159"
Cohesion: 0.22
Nodes (9): authHeaders(), connectWS(), getJSON(), getToken(), handleResponse(), postJSON(), uploadFile(), Obs (+1 more)

### Community 160 - "Community 160"
Cohesion: 0.29
Nodes (12): blitGid(), collisionGrid(), decodeGid(), findMonitorTile(), GID_MASK, layerByName(), loadImage(), loadTiledOffice() (+4 more)

### Community 161 - "Community 161"
Cohesion: 0.29
Nodes (12): normalize_metadata_rows(), KANBAN-076: make the ``metadata`` column cast-safe for the Hub loader. The…, _blind_row(), _gt_row(), load_v5(), main_with_args(), publish(), Path (+4 more)

### Community 162 - "Community 162"
Cohesion: 0.27
Nodes (12): main(), main_with_args(), pairs_with_shared_docs(), per_class_deltas(), {(model, prompt_version): {filename: correct}} for completed label rows., All (A, B) prompt pairs on the same model with >= min_shared shared docs., Per-class paired deltas for the (A, B) pair (documents whose expected label is…, render_class_report() (+4 more)

### Community 163 - "Community 163"
Cohesion: 0.22
Nodes (12): apply_extraction_guard(), guard_classification(), guard_extraction(), _has_substantive_content(), _is_valid_confidence(), Guardrails for agent outputs. Agents are LLMs — they can return junk even when…, True when the extraction carries at least one populated schema field.…, Validate a specialist's extraction against its schema. Returns {"ok", "issues",… (+4 more)

### Community 164 - "Community 164"
Cohesion: 0.37
Nodes (12): bump_version(), check_state(), current_version(), fail(), main(), parse_changelog(), Path, Return (unreleased_bullets, released_headers). (+4 more)

### Community 165 - "Community 165"
Cohesion: 0.33
Nodes (10): Fetcher, adapt_hub_row(), pipeline_corpora(), Any, Lucius-Morningstar Hugging Face corpora the mailroom can pull onto the floor.…, resolve_corpus(), catalog(), _default_fetch() (+2 more)

### Community 166 - "Community 166"
Cohesion: 0.24
Nodes (11): _date_pair_days(), extraction_diagnostics(), _mean(), _median(), parse_duration_days(), _r2(), Run-level diagnostic metrics for the entity-extraction task. Ported from…, Aggregate the per-row composite into run-level diagnostic metrics. Args: rows:… (+3 more)

### Community 167 - "Community 167"
Cohesion: 0.23
Nodes (5): CompletenessJudge, BaseAgent, Render the task specification (taxonomy doc classes) for the judge., Judge whether the sorter's assigned class matches the taxonomy task…, Judge whether the extracted field values are factually accurate (no…

### Community 168 - "Community 168"
Cohesion: 0.30
Nodes (11): _binary_f1(), _ece(), _mean(), Any, Deterministic scoring for LegalBench runs — every number computed locally. No…, Expected calibration error over confidence/outcome pairs., Accuracy, yes-class F1, macro per-category accuracy, calibration., Strict/equiv family accuracy, macro-F1, per-family breakdown. (+3 more)

### Community 169 - "Community 169"
Cohesion: 0.27
Nodes (4): Any, Protocol, Structural type satisfied by LangfuseSource and PhoenixSource., TraceSource

### Community 170 - "Community 170"
Cohesion: 0.33
Nodes (5): PipelineEventHandler, Any, Path, Translate inbox/archive filesystem events into operator payloads., Watcher

### Community 171 - "Community 171"
Cohesion: 0.45
Nodes (10): cache_dir(), load_floor(), load_run(), persist_floor(), persist_run(), Any, Path, safe_id() (+2 more)

### Community 172 - "Community 172"
Cohesion: 0.31
Nodes (8): download(), extract(), load_manifest(), main(), probe(), Path, Try each url until one yields a complete file at dest., sha256_file()

### Community 173 - "Community 173"
Cohesion: 0.31
Nodes (10): _auth_header(), _create_prompt(), _latest_content(), _load_env_file(), main(), main_with_args(), Path, Parse a KEY=VALUE dotenv file (no interpolation, no export). (+2 more)

### Community 174 - "Community 174"
Cohesion: 0.35
Nodes (10): apply_mutation(), decompose(), llm_propose(), load_manifest(), main(), Path, Return (target_file, registry_dict, test_file) from a family spec., render_clusters() (+2 more)

### Community 175 - "Community 175"
Cohesion: 0.25
Nodes (10): load_record(), main_with_args(), per_doc_field_scores(), per_doc_metric(), Path, Return the LAST experiment-log record with the given name., Map filename -> per-document metric value (rows only; errors excluded)., Map field -> {filename -> field score} across the record's rows. (+2 more)

### Community 176 - "Community 176"
Cohesion: 0.18
Nodes (8): Dedicated docclass prompt variants for every classification-chain role.…, Append the docclass context + specialist rules before the JSON closer., v1 specialist: expanded context + shared rules + role-specific extras., Swap extended context and append role extras on an existing v0 variant., # NOTE: fragment assertions in the test file target SHORT substrings that do, _specialist_docclass(), _specialist_docclass_v1(), _upgrade_docclass_v1()

### Community 177 - "Community 177"
Cohesion: 0.27
Nodes (5): _hash(), MockLegalBenchModel, Any, Deterministic mock model for LegalBench runs (no network, no OpenAI). Answers…, Implements the LegalBenchAgent interface deterministically.

### Community 178 - "Community 178"
Cohesion: 0.29
Nodes (10): bootstrap_ci(), _clean(), delta_significance(), Any, Random, Bootstrap confidence intervals and small-sample delta testing. Ported verbatim…, Coerce a per-document score list to floats, dropping None/non-numeric., Percentile-bootstrap 95% CI over per-document scores. Returns ``{"lo", "hi",… (+2 more)

### Community 179 - "Community 179"
Cohesion: 0.47
Nodes (10): apply_pin(), _bare(), current_pin(), _github_headers(), latest_release_tag(), main(), _normalize_tag(), Path (+2 more)

### Community 180 - "Community 180"
Cohesion: 0.33
Nodes (10): _caption_from_text(), _download(), fetch_atticus(), fetch_legalbench(), fetch_pileoflaw(), main(), Path, Yield (record, url) for courtlistener opinions, streaming + aborting early per… (+2 more)

### Community 181 - "Community 181"
Cohesion: 0.33
Nodes (10): _client(), main(), _parse_since(), datetime, Path, Poll a trace's scores until they arrive or the timeout elapses. LLM-as-a-judge…, sync_logs(), _trace_basics() (+2 more)

### Community 182 - "Community 182"
Cohesion: 0.31
Nodes (9): confusion_slice(), main(), main_with_args(), The alpha fraction of lowest-confidence documents + their simulated per-…, Filenames whose expected label is in the top confusion pairs., render_plan(), tail_slice(), The valid predicted-label vocabulary for a task. Resolution order: the sorter's… (+1 more)

### Community 183 - "Community 183"
Cohesion: 0.29
Nodes (9): _numeric_extra(), Any, Dedicated specialist scoring suites from llm-dojo-scoring 0.11.0.…, Score cleaned intake output against the deterministic clerk gold. Returns the…, Attach intake-suite scores to the active trace (no-op when tracing is off)., Split ``suite.score`` output into the extraction result + numeric extras., score_and_log_intake(), score_intake_suite() (+1 more)

### Community 184 - "Community 184"
Cohesion: 0.40
Nodes (9): cutover_agent(), cutover_all(), list_agents(), list_local_models(), load_config(), main(), recommend_cutover_order(), save_config() (+1 more)

### Community 185 - "Community 185"
Cohesion: 0.36
Nodes (7): _find_electron(), Path, Serve the mailroom and open the hardened Electron shell when available., _repo_root(), run_desktop(), _wait_health(), main()

### Community 186 - "Community 186"
Cohesion: 0.44
Nodes (8): load_manifest(), map_gid_unresolved(), office_dir(), Any, Path, Return GIDs on the shipped map that do not resolve to a manifest tileset., tiles_dir(), tileset_status()

### Community 187 - "Community 187"
Cohesion: 0.53
Nodes (8): fetch(), main(), Any, render_floor(), render_history(), render_inspect(), render_metrics(), render_review()

### Community 188 - "Community 188"
Cohesion: 0.50
Nodes (8): audit_line(), git_blob_sha1(), load_index(), main(), publish_docclass(), publish_pack(), Path, sha256_file()

### Community 189 - "Community 189"
Cohesion: 0.33
Nodes (8): build_sweep_workbook(), main(), main_with_args(), The Notes-column value for a run (explicit map, generic fallback)., Write the sweep workbook; returns the number of rows included., Subtype-classification runs of the given sorter prompt, chronological., run_note(), sweep_records()

### Community 190 - "Community 190"
Cohesion: 0.28
Nodes (8): bool_env(), get_env(), load_env(), Load ``braintrust.env`` then ``.env`` into the environment (idempotent).…, Validate that all given environment variables are set and non-empty. Returns…, Get an environment variable with a default fallback., Get a boolean environment variable., require_env()

### Community 191 - "Community 191"
Cohesion: 0.28
Nodes (7): _append(), _build_versions(), Docclass prompt variants for every mailroom classification-chain role.…, Pure-appended docclass variant: base is a STRICT PREFIX of the result., Derive every variant from the live production template of that role., # NOTE: fragment assertions in tests target SHORT substrings that do not cross, _rules()

### Community 192 - "Community 192"
Cohesion: 0.39
Nodes (8): _client(), _cost_models(), _existing_by_name(), main(), _match_pattern(), _prices_match(), Map model_name -> registry Model for every user-defined entry. Paginates: the…, sync_models()

### Community 193 - "Community 193"
Cohesion: 0.42
Nodes (8): build_report(), _clean_extracted(), _field_score_for(), _fmt_usd(), _json_block(), _load_config(), main(), _manifest_rows()

### Community 194 - "Community 194"
Cohesion: 0.43
Nodes (7): contracteval_records(), display_name(), format_report(), load_records(), main(), main_with_args(), Select ``task: contracteval`` records (newest first).

### Community 195 - "Community 195"
Cohesion: 0.39
Nodes (7): classes_match(), normalize_class(), Any, Classification KPIs after ``merger_agreement`` became a live MAUD class. Dojo…, True when predicted equals expected. MAUD is not CUAD., Run-level exact accuracy. ``aligned_*`` keys equal exact (deprecated)., score_exact_classification()

### Community 196 - "Community 196"
Cohesion: 0.39
Nodes (6): _json(), main(), offline_pins(), probe(), Any, Return a structured probe of both hosted Spaces.

### Community 198 - "Community 198"
Cohesion: 0.57
Nodes (6): download(), extract(), _fmt_mb(), main(), main_with_args(), Path

### Community 199 - "Community 199"
Cohesion: 0.29
Nodes (4): Structured logging setup for Mailroom entrypoints. Configures `structlog` once…, Structlog processor that emits the rendered event dict to a rotating stdlib…, _RotatingFileSink, RotatingFileHandler

### Community 200 - "Community 200"
Cohesion: 0.60
Nodes (5): main(), publish_dataset(), Path, sha256_file(), size_category()

### Community 201 - "Community 201"
Cohesion: 0.40
Nodes (5): family_classification_prompt_v1(), get_prompt(), Versioned LegalBench task prompts. Prompt version = experiment identity in the…, Fill the 25-family list into the multiclass prompt (called per run so the…, Resolve a prompt version to its system-prompt text.

### Community 202 - "Community 202"
Cohesion: 0.40
Nodes (3): AsyncEventBridge, AbstractEventLoop, Watchdog callbacks are sync; publish on the API event loop.

### Community 203 - "Community 203"
Cohesion: 0.70
Nodes (4): load_token(), main(), Path, sha256_file()

### Community 204 - "Community 204"
Cohesion: 0.60
Nodes (4): assign_split(), main(), main_with_args(), Family-wide split rule — identical to build_docclass_merged.assign_split. md5…

### Community 205 - "Community 205"
Cohesion: 0.60
Nodes (4): draw_sample(), main(), main_with_args(), Path

### Community 206 - "Community 206"
Cohesion: 0.40
Nodes (4): _fake_client(), _fake_judge_client(), chat, completions

### Community 207 - "Community 207"
Cohesion: 0.40
Nodes (5): agent-mailroom, llm-dojo-scoring, llm-entity-extraction, mailroom, mailroom-sandbox

### Community 208 - "Community 208"
Cohesion: 0.50
Nodes (3): define_railway, main(), Railway Infrastructure as Code — the LLM-Mailroom project. Railway retired…

### Community 210 - "Community 210"
Cohesion: 0.50
Nodes (4): _prompt_versions(), Prompt versions bound during the run (best-effort; Langfuse-managed prompts…, _bound_prompt_versions(), Version keys currently wired into production / agent defaults. Used for catalog…

## Knowledge Gaps
- **71 isolated node(s):** `Props`, `State`, `WSState`, `ImportMeta`, `ImportMetaEnv` (+66 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2199 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **26 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `BaseAgent` connect `Community 4` to `Community 2`, `Community 69`, `Community 134`, `Community 40`, `Community 9`, `Community 139`, `Community 12`, `Community 75`, `Community 19`, `Community 62`?**
  _High betweenness centrality (0.049) - this node is a cross-community bridge._
- **Why does `SorterAgent` connect `Community 2` to `Community 4`, `Community 6`, `Community 9`, `Community 50`, `Community 18`, `Community 25`?**
  _High betweenness centrality (0.041) - this node is a cross-community bridge._
- **Why does `SorterAgent` connect `Community 25` to `Community 0`, `Community 2`, `Community 67`, `Community 31`?**
  _High betweenness centrality (0.039) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `interpret_trace()` (e.g. with `Generation` and `NodeSpan`) actually correct?**
  _`interpret_trace()` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 5 inferred relationships involving `create_app()` (e.g. with `deque` and `PipelineRun`) actually correct?**
  _`create_app()` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `LangfuseSource` (e.g. with `PipelineRun` and `_recent()`) actually correct?**
  _`LangfuseSource` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Props`, `State`, `WSState` to the rest of the system?**
  _71 weakly-connected nodes found - possible documentation gaps or missing edges._