# GA-14 Null Battery: 231 Gates / mod-60 Crest v0.1

Date: 2026-09-22
Status: COMPLETED / CORRECTION ISSUED

## Frozen inputs
- Hebrew standard gematria values: 1..10, 20..100, 200,300,400
- Sefer Yetzirah classes:
  - Mothers: aleph, mem, shin (3)
  - Doubles: bet, gimel, dalet, kaf, pe, resh, tav (7)
  - Simples: remaining 12
- all 231 unordered letter pairs
- experimental crest condition: (v_i+v_j) mod 60 in {0,27,54}

## Correction
An earlier exploratory summary misclassified several letters when reporting sector enrichment. Recomputing with the frozen 3/7/12 classes gives NO S-S enrichment.

Correct crest distribution:
- M-M: 0 / 3
- M-D: 3 / 21
- M-S: 1 / 36
- D-D: 3 / 21
- D-S: 7 / 84
- S-S: 3 / 66
Total: 17 / 231

S-S vs non-S-S Fisher exact two-sided p = 0.4079076760.

## Random 3/7/12 partition control
100,000 random partitions preserving class sizes 3/7/12:
- observed S-S crest hits: 3
- null mean: 4.85973
- null median: 5
- 95% interval: 1..10
- P(null S-S hits >= observed): 0.88255

Conclusion: observed S-S count is ordinary under random class assignment.

## Shuffled-value control
100,000 permutations of the 22 gematria values across fixed letter classes:
- total crest count remains 17 because all unordered value-pairs are still enumerated
- observed S-S hits: 3
- null mean S-S hits: 4.86904
- P(null >= observed): 0.88194

Conclusion: no class/value enrichment.

## Neighboring modulus robustness
Using the same fixed residue set {0,27,54}:

m=57: total 4, S-S 1
m=58: total 11, S-S 2
m=59: total 8, S-S 1
m=60: total 17, S-S 3
m=61: total 7, S-S 0
m=62: total 7, S-S 0
m=63: total 10, S-S 1

The m=60 total is locally high, but the fixed residues are themselves defined in the mod-60 experiment, so this is descriptive rather than an independent significance test.

## Random residue-set control at modulus 60
100,000 random 3-residue subsets of Z/60Z:
- observed {0,27,54} gate count: 17
- null mean: 11.55475
- null median: 9
- 95% interval: 5..26
- P(random triplet count >= 17): 0.2482

Individual observed residue frequencies:
- residue 0: 13
- residue 27: 3
- residue 54: 1

Residue 0 drives most of the crest count.

## Result
The previously reported S-S concentration does not survive correct class assignment and is rejected.

The mod-60 crest set yields 17/231 gates, but this count is not unusual under random 3-residue controls (empirical p ~ 0.248). Its apparent strength is mostly the residue-0 component, compatible with the decimal structure of standard gematria.

Promotion state:
- S-S enrichment: REJECTED
- mod-60 crest anomaly: NOT PROMOTED
- exact 231 enumeration: VERIFIED
- null-preserving Gate Algebra workflow: PASSED

## Next test
Freeze and recover the exact historical project definition of the Faulhaber-Fibonacci residue generator and phi-chain filter, then test their JOINT intersection prospectively. Do not tune residues after observing the 231-gate table.
