# THM-ES-001 — Primitive Divisor-Chamber Geometry
**Research timeline branch:** Diophantine Certificate Geometry (independent of Prime-Delay dynamics)
**Author/source:** Mike Tate, *The Pólya–Archimedean Operator Geometry of the Erdős–Straus Equation: Bounded Gates, Primitive Divisor Chambers, and Residue-Fiber Propagation*, July 2026, original 13-page manuscript recovered from ChatGPT Library 2026-11-22.
**Status:** Exact equivalence independently algebraically audited; computational checks n=2..300; universal Erdős–Straus conjecture remains open.

## Theorem: ordered-solution / primitive-divisor-chamber bijection
For n≥2, ordered positive solutions x≤y≤z of 4/n=1/x+1/y+1/z require floor(n/4)+1≤x≤floor(3n/4).
For a fixed such x, let
m=4x−n>0; q=nx; g=gcd(m,q); μ=m/g; ν=q/g; gcd(μ,ν)=1.
Define chamber
C_n(x)={d∈Z_(>0): d|ν², d≡−ν (mod μ), max(1, μx−ν)≤d≤ν}.
Then ordered completions (y,z) are in bijection with d∈C_n(x) via
e=ν²/d, y=(d+ν)/μ, z=(e+ν)/μ.
Exact ordered solution count: N_≤(n)=Σ_(x∈G(n)) |C_n(x)|.

## Independent algebraic audit
Since μ/ν=1/y+1/z, multiplying by νyz and rearranging gives μyz=ν(y+z). Thus
(μy−ν)(μz−ν)=ν².
For positive y,z, each factor is positive because μ/ν>1/y and >1/z. Define d=μy−ν and e=μz−ν. Ordered y≤z implies d≤e and hence d≤ν. x≤y implies d≥μx−ν. Congruence d≡−ν (mod μ) is immediate.
Conversely d|ν² and d≡−ν (mod μ) gives e=ν²/d integer and y integer. Mod μ, de≡ν² and d≡−ν. Since gcd(μ,ν)=1, ν is invertible modulo μ, so e≡−ν (mod μ), hence z integer. Bounds force x≤y≤z. Expanding de=ν² recovers μ/ν=1/y+1/z and the original 4/n equation. Inverse maps exact. **No logical gap found in this central bijection.**

## Independent executable checks
Locally executed exact integer/Fraction-based enumeration for every n from 2 through 300, using x gate, primitive reduction, divisors d≤ν, chamber congruence and bound, exact Fraction identity, and x≤y≤z assertions. All reconstructed certificates passed and every n in the range had at least one witness. This is finite computational evidence, NOT a proof of global existence.
Example: n=5, x=2: m=3, q=10, μ=3, ν=10. d=2 divides 100, d≡−10≡2 mod3, and 1≤d≤10; e=50, y=4, z=20. Thus 4/5=1/2+1/4+1/20. Compact certificate (n,x,d)=(5,2,2).

## Distinct theorem: homothetic inheritance / residue cover
If (x,y,z) solves for n, then (tx,ty,tz) solves for tn. Base decompositions:
4/2=1/1+1/2+1/2;
4/3=1/1+1/4+1/12;
4/5=1/2+1/4+1/20;
4/7=1/2+1/15+1/210.
Therefore every n with gcd(n,210)>1 is solved by scaling. Remaining integers lie in φ(210)=48 unit residue classes modulo 210. This is a residue reduction, not a finite proof of the conjecture.

## Conditional completion and the open frontier
Define S_n={(x,d):x∈G(n),d∈C_n(x)}. For each unit residue r mod210, a total section s_r(k)∈S_(210k+r), or a valid initial seed plus total propagation preserving membership S_(210k+r)→S_(210(k+1)+r), would imply global Erdős–Straus existence. **Existence of those sections/propagators is not established.**
Prioritize:
1. Classify residue classes admitting explicit affine formulas (n,x,d) and prove chamber membership symbolically.
2. Construct executable certificate generator/verifier with exact arithmetic, provenance and witness reconstruction.
3. Study whether residue-orbit symmetries preserve nonemptiness of S_n; avoid assuming a residue action transports certificates.
4. Optimize cover modulus B by cost of surviving φ(B) fibers vs inherited coverage.

## Research indexing
IER: Object=Erdős–Straus equation; Partition=bounded x gates and residue fibers; Representation=primitive μ/ν and divisor chamber; Admissible operations=homothetic scaling, chamber reconstruction, verified fiber propagation; Invariant=de=ν² and gcd(μ,ν)=1; Attractor=repeatable residue-family certificate laws (candidate); Compression=(n,x,d); Regeneration=(x,y,z) exact.
Timeline ID: THM-ES-001, independent branch from dynamical THM-DYN-0001/0002.
Provenance status: recovered original manuscript; independently checked bijection algebra; finite exact numerical checks; universal conjecture explicitly NOT proved.
