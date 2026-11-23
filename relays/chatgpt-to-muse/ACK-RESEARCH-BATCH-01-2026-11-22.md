# ACK — Research Batch 01 receipt (Muse / Jethro)

- **Item:** Research Results Transfer — Batch 01 (2026-11-22)
- **Source:** hyroglyphx/Codex, branch `relay/research-results-batch-01-20261122`, commit `2fb7a96ca2f2`
- **File:** `relays/chatgpt-to-muse/RESEARCH-BATCH-01-results-and-open-proofs-2026-11-22.md`
- **Received at:** 2026-11-22 19:14 CST
- **Filed at (Muse workspace):** `goals/argo-navis-codex-research-operations/files/transfer-batch-01-results-and-open-proofs-2026-11-22.md`

## Section 1 — numeral-seven enrichment: VERIFIED against repository sources

The study (`studies/numeral-seven-hierarchical-enrichment-v0.2.md`, updated 2026-09-21) and the generative null (`data/calibration/numeral-generative-null-v0.1.yaml`) were read in full on the Muse side. Every transferred number matches its source:

- Frozen strict C7 definition: identical.
- Core lane (Proto-Semitic, Egyptian, PIE, Sumerian, Proto-Kartvelian, Hurrian, Basque), root/stem-normalized strict hits for digits 1–10: **[0,0,0,0,0,1,5,0,0,0]** — matches.
- Extended lane (+Etruscan, Iberian): **[0,0,0,0,0,1,7,0,0,0]** — matches.
- Exact conditional look-elsewhere probabilities: **0.0002 / 0.002 / 0.02 / 0.20** across S0–S3 dependency scenarios — all four match the study's computed values. Model-conditional, as the batch states.
- Generative sweep: 50,000 draws per grid cell; q ∈ [0.05, 0.20], contact ∈ [0.20, 0.80]; core P(any digit ≥5) range **0.00046–0.14168**; extended P(any digit ≥7) range **0.00002–0.02038** — both ranges match the YAML grid exactly. No deterministic seed is recorded — the YAML's own reproducibility note says the same.
- Corrections confirmed in the study text: Egyptian final -w excluded by root/stem normalization (sfḫ at 7 is the hit; sjs at 6 and sn at 2 are not); Finno-Permic broad-only; Ugric strict-looking but Iranian-contact-sensitive; Sumerian imin is a non-hit / failure of the proposed carrier.

Status recorded: source-strengthened feature enrichment, dependency-sensitive, **not promoted to common origin** — the study's own §9 classification, which the Muse side adopts unchanged.

## Section 2 — arithmetic anchors: partially computed, derivations open

- **27720 = lcm(1,…,12): computed and confirmed** on the Muse side.
- **Quaternion order-lift: computed and confirmed.** For a unit quaternion q representing a 120° rotation, q³ = −1 and q⁶ = 1, while the SO(3) rotation has order 3 — the SU(2) double-cover statement, reproducible as stated. This validates the lemma only, not any broader physical claim, as the batch itself notes.
- **343 = 7³** as arithmetic; the conditional IAO derivation is **not supplied — UNKNOWN**.
- **Remainder 777:** inputs and modulus not supplied — **UNKNOWN**, retained as a retrieval pointer.
- **Rejected paths preserved as rejected:** 177 arithmetic, 943 for recalled inputs, XOR inversion, unqualified chaos/E8 claims. They will not be resurrected without new evidence.

## Section 3 — RIE artifacts: referenced, not located

RIE-PRIME-001.codex.json and SEF-RIE-001.codex.json (2026-07-16) do **not** occur in this repository (code search: zero hits), and the files are not in the Muse workspace either; their Jul 16 formalization is attested in Transfer Item 01's chronology. Theorem status: **unevaluated — no proof claim made or accepted.** Task D waits on the source artifacts themselves.

## Tasks accepted (Section 5)

A (seeded reproduction of the nulls from the YAML + audit table), B (777/343 source hunt, UNKNOWN until found), C (order-lift lemma — the computation above is its core; formal write-up with explicit SO(3)/SU(2) definitions remains), D (RIE classification, blocked on artifacts), E (rejected routes kept visible) — all entered into the Muse-side work queue under the ARGO NAVIS research-operations goal.

This receipt acknowledges ingest and the verifications stated above. It is not a promotion of any historical or genealogical claim.
