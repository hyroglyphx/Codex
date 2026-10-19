# ARGO NAVIS — Research Continuity Kernel (RCK)

Version: 0.1.0 | Initialized: 2026-10-19 | Status: scaffold, not fully ingested

## Mission
Make research continuity independent of any one chat's memory. Raw sources remain authoritative; summaries, constructs, scores and retrieval indexes are derived and versioned. Missing evidence must never be interpreted as nonexistent research.

## Directory map
- `schema.json` — JSON Schema for source, construct, assessment, and coverage records.
- `registry.json` — initial construct and operator ledger (seeded from explicitly supplied conversation material).
- `sources.json` — source manifest and ingestion/coverage status.
- `assessments.json` — dated PSI assessments, with observation-vs-estimate distinction.
- `PROTOCOL.md` — retrieval, novelty, provenance, and validation protocol.
- `continuity.py` — standard-library validation, keyword lookup, and coverage reporting.

## Operating contract
1. Preserve original records and stable source references before extracting claims.
2. Separate **source witnessed**, **user-supplied excerpt**, **analyst reconstruction**, and **tested result**.
3. A construct can be proposed or specified without being implemented or validated.
4. Record unknown corpus extent as unknown; never silently score it as complete.
5. Do not replace existing IER, ECVR, TCIM, or PSI conventions: link to them and record rubric versions.
6. No new PSI score without stored inputs, evidence factors, corpus snapshot and coverage statement.

## Quick start
```bash
python research-continuity/continuity.py validate
python research-continuity/continuity.py search HETEROGRAM
python research-continuity/continuity.py coverage
```

This first commit creates a functional manifest and local query tool, **not** an automatic ChatGPT conversation exporter. Historical chat ingestion requires exported source records or an authorized source connector. Sensitive raw conversations should not be committed to a public repository; store private source material in a private repository or encrypted storage and keep only nonsensitive references here.
