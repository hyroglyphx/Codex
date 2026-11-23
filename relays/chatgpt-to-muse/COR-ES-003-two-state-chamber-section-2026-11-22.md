# COR-ES-003 — Two-State Primitive Chamber Section for n ≡ 5 (mod 8)
**Timeline:** Diophantine Certificate Geometry; derived from audited THM-ES-001.
**Status:** Symbolically proved constructive corollary; classical congruence solvability, new registry representation only. Not a proof of the global Erdős–Straus conjecture.
**Date:** 2026-11-22.

## Statement
For every k≥0 let n=8k+5 and x=2k+2=(n+3)/4. Put q=nx and m=4x−n=3. Let g=gcd(3,q), μ=3/g, ν=q/g. Define
d=1 if 3|n; d=2 if 3∤n.
Then d∈C_n(x), and
e=ν²/d, y=(d+ν)/μ, z=(e+ν)/μ
give ordered positive integers x≤y≤z with 4/n=1/x+1/y+1/z.

## Proof
The gate holds: n/4 < (n+3)/4 ≤3n/4 for n≥2.
Case A: 3|n. Since q=nx, g=3, μ=1, ν=q/3. d=1 divides ν² and the congruence mod1 is automatic. ν=nx/3≥x for n≥3, hence max(1,x−ν)=1≤d≤ν. Decoder is integral.
Case B: 3∤n. Because n=8k+5, x=2k+2, modulo 3 we have n≡2k+2≡x (mod3), so q=nx≡n²≡1 (mod3). Hence g=1, μ=3, ν=q, and ν≡1 (mod3). x is even, so ν even. d=2 divides ν² and d≡−ν (mod3). For n≥5, ν=nx≥5x, so μx−ν=(3−n)x<0; lower chamber bound is 1, and 2≤ν. Thus d∈C_n(x).
In both cases the audited chamber bijection supplies exact integrality, order and equation.

## Explicit examples
n=5: x=2, q=10, μ=3, ν=10, d=2, e=50, y=4, z=20. 4/5=1/2+1/4+1/20.
n=13: x=4, q=52, μ=3, ν=52, d=2, e=1352, y=18, z=468.
n=21: x=6, q=126, μ=1, ν=42, d=1, e=1764, y=43, z=1806.

## Computational corroboration
Exact Python fractions and integer chamber assertions verified all 250 n=8k+5 with n<2000; each certificate passed exact rational identity and x≤y≤z. Finite testing is corroborative, not the proof.

## Timeline significance and frontier
COR-ES-002 gives constant μ=1,d=1 on n≡3 mod4. COR-ES-003 gives fixed unreduced numerator m=3 and a two-state primitive divisor law controlled by gcd(3,nx). This is a concrete example of a residue-driven *finite-state certificate section* rather than an unstructured search.
Next research target: systematic bounded-m families with x=(n+m)/4 and primitive μ=m/gcd(m,nx), deriving a finite-state selector d(n) satisfying d|ν² and d≡−ν (modμ) on full residue progressions. Separate known congruence families from genuinely new coverage. Do not claim any unproved global extension.
