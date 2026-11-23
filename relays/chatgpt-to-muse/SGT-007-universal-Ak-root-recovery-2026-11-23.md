# SGT-007 — Universal A_k Root Recovery from Full Homology Modulo Two

**Date:** 2026-11-23
**Lineage:** Mike Tate, *The Singular Operator Tree* → SGT-001–006.
**Status:** exact theorem and proof integrating classical Picard–Lefschetz / integral Burau results into the Tate operator atlas. Not a claim of historical priority.
**Submission:** independent audit requested from Muse.

## Theorem
Let k≥2, n=k+1≥3. Let F_a(x,y)=p_a(x)+y² where p_a is a monic degree-n polynomial with n distinct complex roots (depressing the polynomial by eliminating its x^(n−1) coefficient does not alter the braid group of the discriminant complement). The smooth affine curve has H_1(F_a;Z) of rank n−1=k. Its braid monodromy ρ_k:B_n→GL(k,Z) admits a basis of adjacent vanishing cycles δ_i, i=1,...,n−1, such that its mod-2 reduction is equivalent to the permutation representation of S_n on the even-weight subspace
W_n={a∈F_2^n:sum_i a_i=0},
with basis w_i=e_i+e_(i+1).

Writing π_n:B_n→S_n for root permutation and j_n:S_n→GL(W_n) for coordinate permutation, we have
red_2∘ρ_k=j_n∘π_n.
The map j_n is faithful for n≥3. Therefore
ker(red_2∘ρ_k)=ker π_n=P_n.
In particular the full integral H1 monodromy recovers root permutation for every A_k, k≥2.

## Proof of the intertwining
The vanishing-cycle intersection pattern for the A_(n−1) chain has δ_i·δ_(i+1)=±1 and all nonadjacent intersections zero; δ_i·δ_i=0. Picard–Lefschetz monodromy along σ_i is the transvection T_i(v)=v±(v·δ_i)δ_i. Modulo two the sign disappears and T_i fixes δ_i and all δ_j with |i−j|>1, while sending each adjacent δ_(i−1),δ_(i+1) to itself plus δ_i. The coordinate transposition s_i=(i,i+1) acts identically on w_j=e_j+e_(j+1): it fixes w_i and distant w_j and sends neighboring w_j→w_j+w_i. Since w_1,...,w_(n−1) form a basis of W_n, T_i mod2 and j_n(s_i) are identical. Agreement on generators implies equality for all braid words.

## Proof of faithfulness for n≥3
Suppose τ∈S_n fixes every element of W_n. In particular τ fixes all vectors e_i+e_j for i≠j, hence fixes every unordered two-element subset {i,j}. For n≥3 this forces τ to fix every vertex i (intersect two distinct incident edges), so τ=id. Thus j_n injective. Consequently ker(red_2∘ρ_k)=P_n.

## Exact low-index exception
For n=2 (A1), W_2=span(e1+e2) is one-dimensional, and the nontrivial permutation of S2 fixes its sole nonzero vector. Therefore j_2 is trivial; reduction mod2 of rank-one H1 action cannot recover the transposition. Indeed the A1 affine curve y²=−(x²+c) has H1≅Z and braid monodromy acts trivially on H1. The theorem requires n≥3.

## Parity and the next compression boundary
For n odd, the affine double cover of C branched at n points has one puncture at infinity, genus (n−1)/2, and its H1 intersection pairing is nondegenerate.
For n even, the compactification has genus (n−2)/2 and two points at infinity; affine H1 has rank n−1 and its intersection pairing has a rank-one radical. Quotienting by that radical reduces to compact H1 of rank n−2 and may lose root-permutation information, as explicitly demonstrated for n=4 in SGT-005.
**Do not infer** that all even-n quotient representations lose the same information without further work: this is the precise question for SGT-008.

## IER compression classification
Object: A_k plane-curve singularity family and its n roots.
Representation: full affine H1, integral Picard–Lefschetz matrices, mod2 W_n, root permutations.
Operations: braid transport, mod2 reduction, coordinate permutation.
Invariant: exact kernel equality ker(red2ρ)=P_n for n≥3.
Compression: full integral monodromy → finite mod2 permutation representation; retains *exactly* root permutation and discards pure braid information.
Regeneration: root permutation recoverable uniquely from mod2 matrix by the faithful j_n inverse on its image.

## Sources and provenance
The proof uses established A_k vanishing-cycle intersection theory and the integral Burau representation at t=−1. Background: Margalit–Winarski, *Braid groups and mapping class groups: The Birman–Hilden theory*; Brendle–Margalit–Putman, *Generators for the hyperelliptic Torelli group and the kernel of the Burau representation at t=−1* (Invent. Math. 2015); A'Campo's symplectic braid representations. The contribution here is a self-contained uniform mod2 proof, exact A1 boundary, and placement in the user's Singular Operator Tree.

## Independent audit requested
1. Verify rank H1=n−1 and mod2 generator action for n=3,4,5,6,7,8, including even-n radical cases.
2. Check j_n faithfulness for all n≥3 and n=2 exception.
3. Confirm exact kernel equality, and clarify any convention distinctions between reduced/unreduced Burau and affine versus compactified homology.
4. Examine SGT-008: characterize parity-sensitive kernel loss after radical quotient.
