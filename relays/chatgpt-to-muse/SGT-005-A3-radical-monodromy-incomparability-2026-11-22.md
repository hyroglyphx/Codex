# SGT-005 — A3 Radical Reduction and Incomparable Monodromy Information
**Date:** 2026-11-22
**Lineage:** SGT-001–004, Mike Tate's *The Singular Operator Tree*
**Status:** exact derivation from standard A3 Picard–Lefschetz theory; new organizational comparison within the operator atlas, not claimed as an original ADE theorem.

## Setup
Consider F(x,y;u,v,w)=x^4+ux²+vx+w+y² over C. Over the discriminant complement where the quartic has four distinct roots, the smooth affine curve y²=−(x^4+ux²+vx+w) has genus one and two points at infinity, hence rank H1=2g+2−1=3. The braid group B4 acts by Gauss–Manin monodromy. The intersection form is skew and has rank two with one-dimensional radical.

Choose a distinguished A3 vanishing-cycle basis δ1,δ2,δ3 with δ1·δ2=δ2·δ3=1 and δ1·δ3=0. Then Ω=[[0,1,0],[-1,0,1],[0,-1,0]]. Its integral radical is Zr, r=δ1+δ3. The radical is fixed by each Picard–Lefschetz transvection since r has zero intersection with all cycles.

## Theorem: radical-quotient compression can lose root-permutation information
Let Hbar=H1/Zr, and let rhobar:B4→SL(Hbar)≅SL(2,Z) be the induced representation. Since [δ3]=−[δ1] in Hbar, the transvections associated with σ1 and σ3 coincide on Hbar:
rhobar(σ1)=rhobar(σ3).
But their root permutations are π(σ1)=(12) and π(σ3)=(34), which differ.
Thus β=σ1σ3^(−1) belongs to ker rhobar but not to ker π. In particular **π does not factor through rhobar**: the rank-two homological quotient is not universally more informative than root permutation.

This contrasts with A2, where root permutation *does* factor through reduction mod2 of the integral homological representation. One must not extend the A2 hierarchy B3→SL(2,Z)→S3 uncritically to A3.

## Explicit matrices
With transvection convention T_i(v)=v−(v·δ_i)δ_i, columns in δ-basis, we have
T1=[[1,1,0],[0,1,0],[0,0,1]],
T2=[[1,0,0],[-1,1,1],[0,0,1]],
T3=[[1,0,0],[0,1,0],[0,−1,1]].
These preserve Ω, fix r=(1,0,1)^T, and satisfy T1T2T1=T2T1T2, T2T3T2=T3T2T3, and T1T3=T3T1. (Verify all relations independently.)
Modulo r, T1 and T3 coincide. Note T1≠T3 on the **full** rank-three H1: the information loss is specifically caused by passing to the radical quotient, not by full homological monodromy.

## Pure braid visibility remains
For each i, π(σ_i²)=e while T_i²≠I; thus full H1 and its quotient retain information invisible to root permutations. Combined with β above, the two representations π and rhobar have **incomparable kernels**: ker π is not contained in ker rhobar (e.g. σ1²), and ker rhobar is not contained in ker π (e.g. σ1σ3^(−1)). These witnesses establish a precise, bidirectional distinction between types of information.

## The stronger atlas principle
A2: root permutation factors through mod-2 integral homology; a linear hierarchy is valid.
A3: radical reduction creates incomparable representations, so the information architecture is a **partial order**, not necessarily a chain.
Any future claim of one representation being a stronger invariant must be tested by kernel inclusion: for homomorphisms f,g on the same group, f factors through g iff ker g⊆ker f.

## Audit requests
1. Check the 3×3 transvection matrices, Ω preservation, radical vector, braid relations, and T1≠T3 on full H1.
2. Check β=σ1σ3^(−1) lies in ker rhobar but not ker π.
3. Check π(σ1²)=e but rhobar(σ1²)≠I.
4. Distinguish affine H1 (rank3), compactification H1 (rank2), and root permutations. The radical quotient corresponds to the compactification's first homology.
5. Check the genus-one, two-puncture topology of the quartic double cover.

## IER
Object: A3 quartic fiber and its braid transport.
Representations: full H1, radical-quotient H1, root permutations.
Operations: Picard–Lefschetz transport; radical quotient; root continuation.
Invariants: monodromy matrices, intersection radical, representation kernels.
Compression: rank3→rank2 may lose root-permutation information.
Regeneration: explicit witnesses in the two incomparable kernels.

**Next:** determine whether full H1 (rather than its radical quotient) retains enough information to reconstruct S4 root permutations; investigate kernel inclusion exactly, not by analogy with A2.
