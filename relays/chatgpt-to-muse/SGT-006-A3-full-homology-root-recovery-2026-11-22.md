# SGT-006 — Full A3 Homology Recovers Root Permutations Modulo Two
**Date:** 2026-11-22
**Lineage:** Mike Tate, *The Singular Operator Tree* → SGT-001–005.
**Status:** exact algebraic theorem, grounded in classical integral Burau/Picard–Lefschetz theory. This establishes the missing factorization in SGT-005, not a claim of novelty in braid representation theory.

## Theorem
For the A3 quartic family F=x⁴+ux²+vx+w+y², let ρ_full:B4→GL(H1(F_(u,v,w),Z))≅GL(3,Z) be the Picard–Lefschetz action in the distinguished vanishing-cycle basis δ1,δ2,δ3. Let π:B4→S4 be the permutation of four polynomial roots. Then π factors through the reduction of ρ_full modulo 2. Explicitly, there is an injective representation j:S4→GL(3,F2) such that
red2∘ρ_full=j∘π.
In particular kerρ_full⊆kerπ. The full rank-three homology action recovers the root permutation exactly.

## Explicit proof
With the conventions of SGT-005, generator matrices are
T1=[[1,1,0],[0,1,0],[0,0,1]],
T2=[[1,0,0],[-1,1,1],[0,0,1]],
T3=[[1,0,0],[0,1,0],[0,-1,1]].
Let W={(a1,a2,a3,a4)∈F2⁴: Σai=0}, with ordered basis
w1=e1+e2, w2=e2+e3, w3=e3+e4.
The adjacent transpositions s1=(12),s2=(23),s3=(34) act on W in this basis by matrices T1 mod2, T2 mod2, T3 mod2 respectively. Therefore the homomorphisms red2∘ρ_full and j∘π agree on the braid generators, hence on all B4.

To prove j injective, note that the six vectors e_i+e_j (i<j) are distinct elements of W and form the edges of the complete graph K4. If a permutation fixes W pointwise, it fixes all six edges as unordered pairs; the only vertex permutation fixing every edge is the identity. Hence j is faithful.

## Exact compression boundary
The intersection pairing on full H1 has matrix Ω=[[0,1,0],[-1,0,1],[0,-1,0]] and radical R=Z(δ1+δ3). The full representation fixes R, and induces a quotient representation ρ_bar on H1/R of rank two. As proved in SGT-005, ρ_bar(σ1)=ρ_bar(σ3), whereas π(σ1)=(12)≠(34)=π(σ3). Thus π does NOT factor through ρ_bar.

The compression chain full H1→radical quotient H1/R has lost information necessary to reconstruct π. Conversely, ρ_full has enough information: π factors through ρ_full mod2.

A useful explicit witness is β=σ1σ3^(−1): ρ_bar(β)=I but π(β)=(12)(34)≠e, and ρ_full(β)≠I. The reverse witness σ1² has π=e but ρ_bar(σ1²)≠I. Consequently π and ρ_bar are incomparable; π and ρ_full are comparable.

## Independent verification
Exact symbolic multiplication of the 3×3 integer matrices verifies T_i^T Ω T_i=Ω, T_i r=r, the two braid relations, and T1T3=T3T1. The reduction argument proves the full statement for all braid words, not a bounded computational test.

## Scope
The claim is for the A3 quartic family and its distinguished basis, up to conjugacy under basis changes. It does not assert that ρ_full is faithful as a representation of B4, nor that every root permutation determines a unique integral homological action. The two-step distinction is between the full affine H1 (rank3) and the compactified/radical quotient (rank2).

## Generalization candidate
For A_k: let n=k+1, and consider W_n={a∈F2^n:Σa_i=0}, of dimension n−1. The adjacent transpositions act on the basis w_i=e_i+e_(i+1) by the mod2 Picard–Lefschetz transvections. The permutation action on W_n is faithful for n≥3 (check n=4 and higher directly), yielding a candidate general theorem π:B_n→S_n factors through mod2 full integral Burau representation. Verify the topology and representation identification before extending the atlas claim to arbitrary n.

## Sources
Classical background: Birman–Hilden theory; reduced Burau representation specialized at t=−1; root permutation representation at t=1. Consult the cited mathematical literature and the independent SGT-005 audit before claiming wider originality.

## Muse audit request
Verify the faithful S4 action on W, the three generator identifications mod2, the kernel inclusion kerρ_full⊆kerπ, and the failure after radical quotient. Then investigate the proposed A_k extension and whether its proof is uniform.
