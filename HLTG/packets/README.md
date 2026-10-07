# Portable Research Packets

A packet lets Muse/Jethro, another agent, or a human collaborator work on one bounded problem without requiring the full Codex conversation history.

## Packet contents

- `question.md` — exact bounded research question
- `artifact.json` — canonical artifact metadata and addresses
- `witnesses.json` — source representations and dependency groups
- `transcription.txt` — L1 sign transcription
- `transliteration.txt` — L2 scholarly rendering
- `normalization.txt` — L3 reconstruction, if available
- `known_facts.json` — source-backed anchors only
- `open_questions.json` — unresolved fields
- `candidate_relations.json` — explicit hypotheses, never hidden assumptions
- `bibliography.json` — provenance and source identifiers
- `instructions.md` — method contract

## Method contract

1. Distinguish observation from interpretation.
2. Do not infer ancestry from similarity.
3. Preserve unresolved readings and contradictions.
4. Cite artifact addresses and witness IDs.
5. Record every transformation explicitly.
6. Return counterevidence and alternatives, not only support.
7. Do not count derivative witnesses as independent.
8. Separate text direction from document topology.
9. Function may be recoverable before phonetic decipherment.
10. Translation is a late-stage constrained inference.

## Return format

Agents should return `observations`, `candidate_edges`, `contradictions`, `tests_run`, `best_next_evidence`, and `confidence_changes`. They should not silently modify canonical records.
