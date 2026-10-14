# CYP-NEXUS Benchmark Suite

**Status:** ACTIVE regression suite. Promoted 2026-10-06 from MUSE-CYP-PASS-001
through PASS-004 (user directive: close the gate, no PASS-005).
**Commits:** PASS-001 `854ffe9` · PASS-002 `b753709` · PASS-003 `0a849c3` ·
PASS-004 `e2eb570`, all on branch `muse-cyp-pass-001`.

## Governing rule (user, 2026-10-06)

> **Admissibility before scoring.** A hypothesis enters a regeneration test
> only when the held-out witness contains the minimum observable
> feature-space required to falsify or support it. Otherwise the outcome is
> UNSCORABLE, not zero evidence.

Established by PASS-004: the H1-minimal constraint requires {ri,si}; the
Perdrizet inventory lacks them; 0/2000 nulls are degenerate because
randomization cannot test a constraint whose necessary carrier inventory is
absent. Perdrizet supplies neither confirmation nor contradiction.

## The seven regression tests

| # | Test | What it guards | Frozen expectation | Packet |
|---|------|----------------|--------------------|--------|
| B1 | Blind recovery from known Greek | Blind-then-reveal discipline | ka-se=16; formula 4x; Onasil- alternations; freeze hash stable | PASS-001 |
| B2 | Carrier reconstruction | Sign-level calibration honesty | 815/934 = 87.26%, exact numerator/denominator, defined match categories | PASS-001/002 |
| B3 | Null-detector rejection | Processors must earn their vote | Stem/tail detector: fires at cap on shuffled ICS 217 → RETIRED_FOR_CURRENT_PIPELINE | PASS-002/003 |
| B4 | Witness corruption detection | Transcription fidelity | `va`→`wa` hard error caught; ICS 217 audit: 10 discrepancies, 0 sign-value differences | PASS-002 |
| B5 | Bilingual functional alignment | Alignment without laundering | H1 (E1g5 ↔ Ἀρίστωνα) MEDIUM, beats counterfactuals p<0.05; claim-types distinct; `-se` accusative demoted on 3-vs-2 counts | PASS-003 |
| B6 | Dependency-aware historical holdout | Temporal independence | Meister-1911 frozen readings (O_1911 ⊥ H_1914+); pre/post-1914 stratification; independence stratum clean | PASS-004 |
| B7 | Unscorable-out-of-inventory | Admissibility before scoring | ICS 195: {ri,si} ⊄ inventory → UNSCORABLE, not zero evidence | PASS-004 |

## Adversarial demonstration (preserved)

The `-se` episode: an attractive grammatical interpretation (accusative
marker) arose during PASS-003, encountered contrary counts (3 Eteocypriot
`-se` finals vs 2 Greek accusatives), and was demoted to UNKNOWN rather than
patched. This is the system working as designed — keep it beside the H1
result as the paired example.

## Running the suite

`./run-benchmarks.sh` verifies the sha256 of every frozen artifact against
`expected-hashes.sha256` and checks the recorded expectations. Any hash
mismatch or expectation drift fails the suite loudly — investigate before
any downstream work consumes these artifacts.

Re-execution commands for the deterministic components are recorded in each
packet's return contract (reproduction records with seeds). Re-running is
encouraged when the environment changes; hash stability is the primary gate.
