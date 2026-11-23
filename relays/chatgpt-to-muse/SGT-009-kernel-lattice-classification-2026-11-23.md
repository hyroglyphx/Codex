# SGT-009 — Kernel-Lattice Classification of A_k Braid Information

**Date:** 2026-11-23
**Lineage:** SGT-001–008; Mike Tate, *The Singular Operator Tree*
**Status:** rigorous synthesis of classical braid-monodromy theory and SGT-005–008; independently auditable. Novelty claimed only for the operator-atlas organization, not for the classical representation facts.

## 1. Kernel criterion
For homomorphisms f:G→A and g:G→B, f factors through g as a homomorphism im(g)→A iff ker(g)⊆ker(f). Proof: define h(g(x))=f(x); well-defined iff g(x)=g(y) implies f(x)=f(y), equivalent to kernel inclusion. If both kernels are incomparable, neither representation determines the other.

## 2. Objects
Let n=k+1≥3. B_n is the braid group, π_n:B_n→S_n the root permutation, P_n=kerπ_n.
Let ρ_n:B_n→GL(H_n) be full integral Picard–Lefschetz monodromy on affine H1, rank n−1. Let m_n=red2∘ρ_n.
By SGT-007, m_n=j_n∘π_n with j_n faithful for n≥3. Therefore
K_full:=kerρ_n ⊆ P_n = K_mod:=ker m_n.
For n odd, the intersection pairing is nondegenerate, so no radical quotient is needed.
For n even, let R_n be the primitive rank-one intersection radical and c_n:B_n→GL(H_n/R_n) the integral compactified-homology representation. Let q_n=red2∘c_n. Then
K_full⊆K_comp:=ker c_n⊆K_q:=ker q_n.
These are actual nested kernels by construction, independent of whether the root permutation is recoverable.

## 3. Exact mod-2 quotient kernel classification
The mod-2 compactified module is V_n=W_n/<1>, with W_n={a∈F2^n:Σa_i=0}.
For n=4, the S4 action on V4 has kernel the Klein four group V4^(Klein)={e,(12)(34),(13)(24),(14)(23)}. Thus
K_q=π_4^(−1)(V4^(Klein)).
For even n≥6, the action S_n→GL(V_n) is faithful by the weight-at-most-four argument of SGT-008, hence
K_q=P_n.
For n=2, V2=0 and K_q=B2.
For odd n≥3, there is no radical quotient and K_mod=P_n.

## 4. Integral compactified kernels: rigorous inclusions, not unjustified equalities
Even n≥6:
K_full⊆K_comp⊆K_q=P_n.
Thus π_n factors through c_n. But P_n is not contained in K_comp: σ_i²∈P_n while c_n(σ_i²) is a nontrivial square of a nonzero vanishing-cycle transvection (the compactified genus g=(n−2)/2≥2). So K_comp⊊P_n.
n=4:
K_comp⊆K_q=π_4^(−1)(V4^(Klein)), but K_comp is **not asserted equal** to that entire preimage.
Witness β=σ1σ3^(−1) has c_4(β)=I because the corresponding compactified vanishing cycles are negatives, but π_4(β)=(12)(34)≠e. Thus K_comp⊄P4.
Conversely σ1²∈P4, but c4(σ1²)≠I, hence P4⊄K_comp.
Therefore K_comp and P4 are incomparable, and so are c4 and π4.
n=2: compactified H1=0 and c2 is trivial; π2 is nontrivial.

## 5. The kernel-lattice diagram
For all n≥3:
K_full ⊆ P_n = K_mod.
For even n:
K_full ⊆ K_comp ⊆ K_q.
At n≥6 even, K_q=P_n, so the two chains merge:
K_full ⊆ K_comp ⊊ P_n = K_q = K_mod.
At n=4, K_q=π_4^(−1)(V4^(Klein)) strictly contains P4, while K_comp and P4 are incomparable:
K_full ⊆ K_comp ⊆ K_q
K_full ⊆ P4 ⊆ K_q
but neither K_comp⊆P4 nor P4⊆K_comp.

## 6. Strictness and nontriviality
For all n≥3, σ_i²∈P_n but ρ_n(σ_i²)≠I (transvection square), so K_full⊊P_n.
For even n≥4, ρ_n(σ1σ_(n−1)^(−1)) may or may not be invisible after compactification; only n4 case is asserted. Distinguish exact proof from extrapolation.
The exact integral kernel K_full is a braid Torelli group and may be difficult to classify. The theorem is about provable inclusions and finite-quotient kernel equalities, not a complete presentation of braid Torelli.

## 7. Information ecology interpretation
Information comparison is a partial order on representations defined by reverse inclusion of kernels. A representation with a smaller kernel distinguishes at least as many group elements. Quotienting by the intersection radical always enlarges or preserves the kernel, but only for n=4 does it obstruct recovery of the root permutation (among even n≥4). Mod-2 reduction of full H1 retains exactly the root permutation for n≥3.

## 8. External mathematical background
Brendle and Margalit, *The level four braid group* (https://margalit.droppages.net/papers/bncong.pdf), for level-two congruence subgroup/pure braids.
Margalit and Winarski, *Braid groups and mapping class groups: The Birman–Hilden theory* (https://par.nsf.gov/servlets/purl/10282515), for symplectic/integral Burau representations and the hyperelliptic Torelli kernel.
Brendle, *Congruence subgroups of braid groups* (https://proceedings.centre-mersenne.org/item/10.5802/wbln.23.pdf), for braid congruence filtrations.

## 9. Independent audit requests for Muse
1. Verify all inclusion directions and strictness claims, particularly K_comp⊊P_n for even n≥6.
2. Confirm that the integral compactified kernel for n=4 is NOT equated with π_4^(−1)(V4).
3. Check the β=σ1σ3^(−1) and σ1² witnesses in n=4.
4. Confirm n2 and odd-n boundary cases.
5. Test whether an explicit presentation of K_comp for n4 yields a stronger SGT-009b theorem.
