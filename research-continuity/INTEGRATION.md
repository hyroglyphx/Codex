# Cross-project integration map — 2026-10-19

## Reconciliation decision
RCK is **not** a new competing canonical state machine. It is a source-index, retrieval-coverage and assessment layer over the existing Codex **Reuptake / Relay Kernel**.

## Existing canonical contracts (verified in Codex)
- `docs/architecture/research-platform.md`: Confluence → Relay Kernel → Nexus → Council → Adversary → Organon → Builder → ResultPacket → Relay.
- `docs/protocols/invariant-ecology-registry.md`: IER object tuple (O,P,R,A,I,T,C,G), source and negative-control requirements.
- `docs/state/2026-09-20-reconciled-research-state.md`: recovered/reconstructed/generated/missing distinction, immutable OrganonEvents, authority and promotion rules.
- `Reuptake/state/current.json`: current-state snapshot; not an exhaustive index of every historical conversation.
- `Reuptake/provenance/event-log.jsonl`: append-only event log; do not overwrite from RCK.
- `benchmarks/delta-001/README.md`: historical reconciliation benchmark.

## RCK adapter contract
1. `sources.json` indexes original witnesses and records what was actually ingested.
2. `registry.json` is a **discovery index**, not a replacement for canonical IER or Relay claims. Its simple statuses are provisional until reconciled with canonical maturity/authority.
3. Canonical event transitions remain in `Reuptake/provenance/event-log.jsonl` using OrganonEvent schema; RCK must never edit history in place.
4. Existing source/claim authority levels L0–L4 and promotion states OBSERVED→CANDIDATE→TESTED→CORROBORATED→CANONICAL remain authoritative.
5. `assessments.json` contains reproducible PSI measurements or explicitly labeled scenarios/estimates, with coverage unknown when source universe is unknown.
6. Future adapters should link RCK record IDs to `event_id`, `object_id`, `claim_id`, and exact file/commit locators; do not manufacture IDs for historic records.

## Other connected repository examined: hyroglyphx/Website-Works
The root tree currently lists:
- `Codex_Core_Package.zip`
- `anamnesis-chat-plugin (2).zip`
- `ghat-harmonic-interpreter-clean.zip`
- `.github/workflows/blank.yml`

These ZIP contents were **not inspected** through the available GitHub text connector; no functionality is attributed to them on filenames alone. They are candidates for a future audited integration: Anamnesis for chat intake, Codex Core for schema/architecture, GHAT for operator execution. Do not import executable packages until reviewed and tested. Do not copy private conversation content into this public repository.

## Compatibility requirement
Maintain an explicit distinction between (a) known missing source material and (b) work never performed. A zero-result search over a partial index cannot establish nonexistence.
