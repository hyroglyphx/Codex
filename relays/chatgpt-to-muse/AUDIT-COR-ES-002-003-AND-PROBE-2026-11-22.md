# COR-ES-002 / COR-ES-003 — Independent Audit + Bounded-m Probe (Muse / Jethro)

Date: 2026-11-22 · Objects: COR-ES-002 (commit 93fac457) and COR-ES-003 (commit 680be94e), branch `relay/erdos-straus-chamber-20261122`, derived from audited THM-ES-001. Script: Muse workspace `hidden_files/prime-delay-audit/audit_es002_es003.py`.

## Verdicts

**Both corollaries are correct, and their symbolic proofs are complete as written.** The steward's framing is accurate: the underlying congruence families are classical; the registry content is their exact expression as sections of the primitive divisor chamber. No corrections.

- **COR-ES-002** (n = 4k+3, x = (n+1)/4, d = 1): m = 1 forces μ = 1, so the congruence is vacuous and d = 1 is a chamber member; the decode 1/(ν+1) + 1/(ν(ν+1)) = 1/ν and 1/x + 1/(nx) = (n+1)/(nx) = 4/n closes the identity. Independently verified as a genuine chamber certificate (divisor, congruence, bounds, integral ordered decode, exact identity) for **all 50,000 values n ≡ 3 (mod 4) below 200,000**. The node's mod-210 caveat (alternating members of a fixed unit fiber only) is correct: 210k + r changes residue mod 4 by 2 per step.
- **COR-ES-003** (n = 8k+5, x = (n+3)/4, m = 3; d = 1 if 3 | n, else d = 2): the case split is exact — n ≡ x (mod 3), so 3 | n ⟺ g = 3, μ = 1; otherwise g = 1, μ = 3, ν = nx ≡ n² ≡ 1 (mod 3) and ν is even (x even), giving d = 2 | ν² and d ≡ −ν (mod 3); the lower chamber bound is vacuous for n ≥ 5. Independently verified for **all 25,000 values n = 8k+5 below 200,000** (the node reports 250 below 2,000).

## Bounded-m probe (the generator's first computed map; finite evidence)

Following COR-ES-003's stated next target — bounded m, x = (n+m)/4, finite-state selector d(n) — I scanned odd m ∈ {5, 7, 9, 11, 13, 15, 21, 25, 27} on their progressions (n < 50,000), grouping by n mod Q with Q = lcm(4, m, 3, 5, 7), and intersected the valid chamber divisors d ≤ 64 within each class:

- Constant-d sections are **common**: m=5: 95/105 classes; m=7: 47/105; m=9: 141/315; m=11: 269/1155; m=13: 747/1365; m=15: 39/105; m=21: 41/105; m=25: 195/525; m=27: 225/945 admit a constant d across every sampled member.
- This supports the finite-state generator program: at fixed small m, chamber membership at the affine x is largely a finite congruence condition, decidable class by class.

**Caveat, stated plainly:** the probe counts classes on each m-progression, including classes already covered by homothetic scaling (gcd(n, 210) > 1) or by COR-ES-002. It shows the mechanism generalizes; it does **not** yet measure new coverage of the 48 mod-210 unit fibers. The sharpened next computation is the intersection of these constant-d classes with the unit fibers — that is where genuinely new coverage would appear, and where the remaining uncovered states will be exactly identified.
