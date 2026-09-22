# GA-15 Partial Three-Filter Run: Crest × Phi × Artifact FF Residues

Date: 2026-09-22
Status: COMPLETED WITH GENERATOR OMEGA

## Newly supplied artifact
The screenshot explicitly displays:
- Faulhaber Sums: [1, 9, 55, 455]
- Faulhaber-Fibonacci Residues: [0, 9, 8, 8, 9]
- therefore the visible unique FF residue set is {0,8,9}

The screenshot does NOT expose enough information to reconstruct the function that maps the displayed Faulhaber sums/Fibonacci data to [0,9,8,8,9]. The generator remains OMEGA. We therefore freeze the displayed output as an artifact-attested vector and do not reverse-engineer a preferred rule.

## Frozen prior inputs
- all 231 unordered Hebrew letter gates
- standard gematria values
- modulus 60
- crest residues {0,27,54}
- Euler phi chain iterated to 1
- downstream markers {18,6,2,1}

## Results
All 231 positive integer totals eventually cross {2,1}; therefore the downstream set as written is a recorder, not a selective filter.

17/231 gates satisfy the crest condition.

15/17 crest gates have a phi-chain residue mod 60 intersecting the visible FF set {0,8,9}.

The two crest gates that do NOT intersect {0,8,9} are:
- dalet-nun: G=54; phi chain 54 -> 18 -> 6 -> 2 -> 1
- zayin-kaf: G=27; phi chain 27 -> 18 -> 6 -> 2 -> 1

The 15 intersecting crest gates are:
- zayin-pe: 87 -> 56 -> 24 -> 8 -> 4 -> 2 -> 1
- zayin-resh: 207 -> 132 -> 40 -> 16 -> 8 -> 4 -> 2 -> 1
- yod-samekh: 60 -> 16 -> 8 -> 4 -> 2 -> 1
- kaf-mem: 60 -> 16 -> 8 -> 4 -> 2 -> 1
- kaf-qof: 120 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1
- kaf-tav: 420 -> 96 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1
- lamed-tsadi: 120 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1
- mem-pe: 120 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1
- mem-resh: 240 -> 64 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1
- nun-ayin: 120 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1
- samekh-shin: 360 -> 96 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1
- pe-qof: 180 -> 48 -> 16 -> 8 -> 4 -> 2 -> 1
- pe-tav: 480 -> 128 -> 64 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1
- qof-resh: 300 -> 80 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1
- resh-tav: 600 -> 160 -> 64 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1

Thus the observed split is structurally simple:
- branch A: crest totals 27/54 -> 18 -> 6 -> 2 -> 1
- branch B: most other crest totals -> ... -> 8 -> 4 -> 2 -> 1

The FF set selects branch B because it contains residue 8.

## Control
100,000 random 3-residue subsets of Z/60Z were intersected against phi-chain residues of the 17 crest gates:
- observed intersection count for {0,8,9}: 15
- random-set mean: ~5.31
- median: 2
- P(random set gives >=15): ~0.203

This is NOT a strong significance result because phi chains have highly recurrent tail nodes; residue 8 is itself a common attractor on these crest chains. Random residue sets that include common tail residues can score very highly.

## Interpretation
The supplied artifact sharpens the experiment but does not yet establish an independent Faulhaber-Fibonacci coincidence.

What IS established:
1. The visible FF output contains 8.
2. 15 of the 17 crest-gate phi chains pass through residue 8.
3. The two exceptions form the clean 18->6->2->1 branch.
4. The downstream marker set {18,6,2,1} therefore distinguishes the exceptional branch more sharply than it filters the whole 231 set.

Promotion states:
- 15/17 crest-to-FF intersection: VERIFIED ARITHMETIC
- independent coherence claim: NOT PROMOTED
- FF generator: OMEGA
- branch split (8-branch vs 18/6-branch): VERIFIED ARITHMETIC / CANDIDATE STRUCTURE

## Next decisive recovery
Recover the exact code/formula that produced:
Faulhaber sums [1,9,55,455]
and FF residues [0,9,8,8,9].

Then freeze that generator and run it prospectively across all 231 gates, neighboring moduli, and held-out numeric bases.
