# Jethro Relay

Persistent asynchronous relay for Jethro ↔ ChatGPT research work.

## Rules
- This branch is an independent research lane.
- Do not merge into canonical research state without explicit review.
- Preserve provenance labels: PROVEN, RECOVERED, STRUCTURAL, HISTORICAL, GENERATED, FAILED/NEGATIVE.
- Arithmetic equivalence is not independent evidence.
- Disagreement is preserved, not harmonized away.
- Same return does not imply same path.

## Relay protocol
1. Read `state.json`.
2. Read `context.md`.
3. Read `inbox.md`.
4. Perform only the declared active task.
5. Write findings to `reports/`.
6. Append concise response to `outbox.md`.
7. Update `state.json` checkpoint.
8. Commit and push to this branch.
