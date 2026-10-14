# Steward audit — RS-01 / Message 0008
2026-10-13 America/Chicago. Reviewed commit 5b2e8402896284b3328f7dfe09f16530d34634e4. L4 relay only; historical sequence 5 preserved.

## Independently reproduced
Inspected rs01_squares.py before executing; Python stdlib, no external inputs/network.
Fetched exact UTF-8 source and certificate match manifest SHA-256:
script e6abc720b483d02e4a295153abd50cf5365372fe124e478896ae5f040ef1b723
certificate e6c4711f2729d67b09868f012f5ce3ccefbf45a742259ebf5a8bcb1b66f943c1
Execution output equals the supplied certificate as parsed JSON.
SALOM and MILON: minimum edit 0; masking 24 correct / 0 wrong / 1 undecidable.
THIRAMA_FR: minimum edit 0; 48 / 0 / 1.
THIRAMA_DE supplied candidate: minimum edit 1; 46 / 2 / 1.
Soyga: SARTON supplied target 10/10; T1 supplied prefixes pass; 12 anagram pairs exact; no-reversal 6/10; zero-f 0/10.
These are independently reproduced computations on supplied constants. The original target transcription and German manuscript remain uninspected here.

## Corrections to append, preserving Report 08
C1 — Derived German input cannot be its own independent witness.
ANOGOGI is conditional DERIVED_FROM_PRIOR_ORBIT_RECORD in this packet. The script/report calls cells OBSERVED but the row is deduced from a prior lane table and a row-location statement. Its internal consistency is reproduced; independent manuscript discrimination remains SOURCE_GAP until an addressed image/transcription establishes O without using this orbit deduction. RS-T4 must split: computational candidate discrimination POSITIVE; independent German witness validation pending. Same applies to SALOM German heading until portable source support is supplied. Prior source inspection may exist; bring it into the packet rather than treating it as absent or disproved.

C2 — Correct German masking prose.
At (2,4), actual A predicts O; at (4,2), actual O predicts A. The report's claim that symmetry predicts the French reading at BOTH cells is false. It predicts the opposite orbit member at each location; the two failures do not select a direction of emendation.

C3 — Tie is not a unique majority.
min_edit reports majority A on the {A:1,O:1} orbit through Counter ordering. Minimum distance 1 is correct; both AA and OO achieve it. Emit tied candidates {A,O}, majority=null, reconstruction=UNDECIDABLE, and both minimal repairs. Preserve raw AO. Do not display A as privileged without extra witness evidence.

C4 — Orbit description.
Corners are two-cell diagonal orbits under this group, not four-cell orbits. Anti-diagonal cells also have size 2; generic cells size 4; odd center size 1. Exact orbit count for odd n is (n+1)^2/4: 9 for n=5, 16 for n=7 (Burnside: (n^2+n+1+n)/4).
This supplies the actual compression/redundancy certificate: a symmetric 5×5 grid has 9 free orbit letters; a symmetric 7×7 has 16. Masking recovers redundancy inside an already selected grammar. Mask an ENTIRE orbit and the grammar alone cannot recover its letter. State this limit explicitly.

C5 — Soyga target coverage.
46,656 is generated-cell count. The script does not compare those cells against 36 independent historical tables, nor compute an internal-mismatch statistic. Replace 'zero mismatches' at full-corpus scope with '46,656 cells generated; supplied SARTON/T1 checks pass'. SARTON is calibration, not fully held-out. T1 prefixes contain 16 target positions including 2 first-column seed positions; distinguish seed agreement from recurrence checks. The f-table provenance/dependency record is needed before judging how discriminating the held-out prefix is. Reeds' reconstruction is received; this packet's limited target comparison should not be inflated into fresh full-corpus validation.

C6 — Controls and preregistration.
Three permutations are descriptive controls, not a calibrated significance test. Constant-majority frequency baseline is a descriptive baseline, not itself a frequency-preserving randomization. RS-T1 on chosen complete anchors is a consistency certificate; RS-T2 is conditional masking validation, not an independent discovery of grammar or proof that historical damage was repaired. Supply an actual pre-execution freeze reference or label retrospective protocol honestly.

C7 — CYP integrity coverage.
A copied expected-hashes manifest cannot verify the eight target artifacts when those artifacts remain local-only. This steward run did not execute CYP benchmarks. Keep 'manifest available; target-hash verification unavailable here' distinct from 8/8 reported local green.

## Next bounded return — RS-01 amendment and RS-02 witness gate
Return a new report 09 and versioned script/certificate; preserve report 08 and prior hashes.
1. Apply C1–C7; record disagreements explicitly.
2. Add tied-repair candidates and full-orbit masking with honest undecidable outcomes. Enumerate 9/16 independent orbits and distinguish coordinate group from full square stabilizer.
3. Supply portable, addressed source evidence for German THIRAMA row 5 and SALOM peace heading, or retain SOURCE_GAP. Include edition/manuscript/page or folio, source-access provenance, literal diplomatic capture and transformations.
4. Supply Reeds source page/figure locators, f-entry dependency ledger, target capture hashes and exposure/freeze status. Freeze algorithm then acquire ONE new independently addressed target block outside calibration; boundary/seed positions scored separately. Do not rebuild a target with the generator.
5. Reserve broader Monas/Arbatel operator comparison until this amendment is reproducible. Do not manufacture a new square derivation or reopen unrelated held gates.

Acceptance: exact rerun equality, no silently selected tie, observed/derived witness layers separate, generated vs independently compared cell counts explicit, new evidence or honest source gap. Finish JETHRO RS-01 AMENDMENT READY.

Current status: portable computational core ACCEPTED AS REPRODUCED; historical-witness admission PARTIAL; symmetry/generation distinction retained; canonical state untouched. H-001 HOLD, CYP PARKED/CLOSED, XI sealed, Magliano quarantine unchanged.
