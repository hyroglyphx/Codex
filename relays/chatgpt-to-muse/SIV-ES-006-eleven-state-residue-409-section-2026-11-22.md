# SIV-ES-006 — An Eleven-State Primitive-Chamber Section for n ≡ 409 (mod 840)
**Timeline:** Diophantine Certificate Geometry, after THM-ES-001 and SIV-ES-004.
**Date:** 2026-11-22.
**Status:** exact proved infinite-family section, not a global Erdős–Straus proof.

## Theorem
For every t≥0 set n=840t+409, x=210t+105=(n+11)/4, m=11, q=nx, g=gcd(11,q), μ=11/g, ν=q/g. Let s=t mod11 and select d from this table:

| s | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| d | 21 | 35 | 63 | 105 | 7 | 1 | 7 | 105 | 63 | 35 | 21 |

Then d∈C_n(x) for every t≥0. In particular, e=ν²/d, y=(d+ν)/μ, z=(e+ν)/μ yield positive integers x≤y≤z and 4/n=1/x+1/y+1/z.

## Proof
n=409+840t, x=105+210t=105(1+2t). Thus m=4x−n=11, and n≥409 ensures n/4<x≤3n/4.
Modulo 11, n≡2+4t=2(1+2t), x≡6+t=6(1+2t) (since 105≡6 and 210≡1 mod11). Hence 11|nx iff 1+2t≡0 mod11, namely t≡5 mod11.
If t≡5 mod11, g=11 and μ=1, so the congruence is automatic. Also x/11 is an integer multiple of 105; hence ν=nx/11 is a multiple of 105.
Otherwise g=1, μ=11, ν=nx, also a multiple of 105. In all states 105|ν, and every tabulated d divides 105², so d|ν².
For t not ≡5 mod11, ν≡(2+4t)(6+t)≡(1+2t)² mod11 (since 2·6≡1 mod11). The ν residues for t=0..10 are [1,9,3,5,4,0,4,5,3,9,1]. The chosen d residues mod11 are [10,2,8,6,7,1,7,6,8,2,10], so d≡−ν mod11 in all states where μ=11; the t=5 state has μ=1.
Finally μx−ν=(11−n)x/g<0 and all d≤105≤ν (already at t=0 ν=409·105), so max(1,μx−ν)=1≤d≤ν. Every chamber condition holds. THM-ES-001 reconstructs ordered witnesses. QED.

## Example
At t=0, n=409, x=105, μ=11, ν=42945, d=21. e=ν²/21, y=(ν+21)/11, z=(e+ν)/11 are integers and satisfy the equation exactly.

## Coverage bookkeeping
This proves one of the 17 residual classes remaining after SIV-ES-004 and COR-ES-005, increasing the present construction's coverage to **32 of 48 residual classes mod840**. The 16 not yet covered by the registered sections are:
1,121,169,241,289,337,361,457,481,529,577,601,649,697,769,817.
'Uncovered' refers to these specific constructions, not to existence of Egyptian-fraction solutions.

## Structural mechanism
This is a finite-state certificate section: an affine x gate, fixed unreduced numerator m=11, a period-11 selector d(s), and a fixed divisor reservoir 105². The proof relies on an exact modular identity ν≡(1+2t)² (mod11) outside the primitive-reduction state and 105|ν in every state. It exemplifies residue-fiber transport with an actual invariant-preserving decoder.

## Next
Find additional finite-state selectors on remaining classes, ideally one uniform parameterization covering multiple classes. Test periodicity symbolically by checking all residue states and divisibility over the entire progression; finite initial testing alone is insufficient.
