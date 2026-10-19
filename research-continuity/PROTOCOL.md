# Continuity and evidence protocol

## Intake
Assign source ID, exact locator, type, observed date, acquisition date, checksum when raw bytes exist, visibility, and ingestion status. If only an excerpt is available, mark `excerpt_only` and never claim full-document coverage.

## Extraction
Each construct has stable ID, aliases, kind, status, source IDs, dependencies, assertions, and validation notes. Separate observed historical facts from contemporary mathematical reconstructions. Proposed operators are not implemented code.

## Search before novelty
Search exact tokens, aliases, lexical variants, and linked dependencies. Classify result: existing, extension, distinct, conflict, or unresolved. A failed search means `not_found_in_searched_subset`, not `unaddressed`.

## Evidence states
`proposed` → `specified` → `implemented` → `tested` → `validated`; also `revised`, `superseded`, `rejected`. Do not automatically promote between states.

## Assessment
Store rubric ID/version, per-component inputs, calculation, provenance, evidence factor inputs, entropy term, coverage, and observed/estimated/scenario type. For PSI-S v3: 100*(.25*SC+.20*RI+.20*CC+.15*MR+.20*HR). For WPS-C v3: 10*PSI_S*(es*er*eh*ep)^(.25)*exp(-delta_entropy/.10). Never equate construct inventory count with PSI-S.

## Coverage
Coverage denominator must be a declared source universe. Unknown/unavailable sources and unindexed periods remain explicit. No percentage if the denominator is unknown. Maintain domain-specific coverage when a known universe becomes available.

## Security
The current Codex repository is public. Do not ingest private conversations, secrets, children's data, or copyrighted full texts here without review. Prefer metadata and approved excerpts; store raw private archive elsewhere.
