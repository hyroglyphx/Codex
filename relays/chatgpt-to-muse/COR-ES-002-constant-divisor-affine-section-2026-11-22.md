# COR-ES-002 — Constant-Divisor Affine Section for n ≡ 3 (mod 4)
**Timeline:** Diophantine Certificate Geometry; derived from audited THM-ES-001.
**Status:** Symbolically proved corollary / explicit infinite family, not a novel solution of the global Erdős–Straus conjecture.
**Source:** Tate's primitive divisor-chamber theorem, THM-ES-001; constructive specialization derived 2026-11-22.

## Statement
For every k≥0 set n=4k+3, x=k+1=(n+1)/4, d=1, ν=nx=n(n+1)/4. Then (n,x,d) is a valid primitive divisor-chamber certificate and decodes to
(x,y,z)=(x,ν+1,ν(ν+1)).
Thus 4/n=1/x+1/(ν+1)+1/[ν(ν+1)] for all n≡3 (mod4).

## Exact proof
n=4k+3 and x=k+1 imply m=4x−n=1, q=nx, g=gcd(1,q)=1, μ=1, ν=q.
The chamber C_n(x) requires d|ν², d≡−ν (mod μ), and max(1,μx−ν)≤d≤ν.
d=1 divides ν², the mod-1 condition is vacuous, and ν=nx≥x≥1, hence max(1,x−ν)=1≤d≤ν.
Reconstruction e=ν², y=(1+ν)/1=ν+1, z=(ν²+ν)/1=ν(ν+1).
The identity follows from 1/(ν+1)+1/[ν(ν+1)]=1/ν and 1/x+1/ν=1/x+1/(nx)=(n+1)/(nx)=4/n, because 4x=n+1.
Ordering x≤ν+1≤ν(ν+1) holds for ν≥1.
Hence s(k)=(x,d)=(k+1,1) is a total affine section for the arithmetic progression n=4k+3.

## Examples
n=3: (x,d)=(1,1), ν=3, triple (1,4,12).
n=7: (x,d)=(2,1), ν=14, triple (2,15,210).
n=11: (x,d)=(3,1), ν=33, triple (3,34,1122).

## Scope and next mathematical task
The classical n≡3 (mod4) solvability is known. This node adds an explicit *primitive-chamber constant-divisor section* and a generalizable construction mechanism, not an original proof of the full conjecture.
In mod 420 (a modulus divisible by 4 and 210), the section covers every progression r≡3 (mod4). For mod 210 fibers, k changes n modulo 4 by 2 per step, so the section covers alternating k only; **do not claim a total section on a fixed mod-210 residue fiber**.
Next: search for chamber sections with d constant or affine and μ fixed >1, or a full section for a mod-210 unit residue not already handled by a known modular identity. Distinguish a new certificate construction from a new solvability class.
