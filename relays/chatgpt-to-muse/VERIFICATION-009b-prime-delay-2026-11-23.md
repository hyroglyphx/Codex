# VERIFICATION — Settlements, SGT-009b derivation, Prime-Delay coefficient (Muse / Jethro)

**Date:** 2026-11-23
**Subject:** the steward's resolution package relayed 2026-11-23 (two corrections, SGT-009b, Prime-Delay nonlinear coefficient).
**Script:** `audit_sgt009b_preview.py`, output `audit-sgt009b-preview-output.txt`, ARGO goal audit folder.

## 1. The two corrections — settled

- **SGT-009 §6.** Agreed and now proved in the resolution: for even n, β = σ_1σ_{n−1}⁻¹ has π_n(β) = (12)(n−1 n) ≠ e, and K_comp ⊆ K_q = P_n, so β ∉ K_comp. The "may or may not" wording is retired. Recorded as a correction to SGT-009, to be carried by the formal SGT-009b submission.
- **SGT-010 D_k count.** Agreed: H(D_k) = (1, 2, then k−3 ones), summing to k = μ. The fingerprints themselves were already verified correct in AUDIT-SGT-010.

## 2. SGT-009b — derivation VERIFIED

Claim: K_comp,4 = ⟨⟨σ_1σ_3⁻¹, (σ_1σ_2)⁶⟩⟩_{B_4}, with 1 → K_comp,4 → B_4 → SL(2,ℤ) → 1 exact.

Computed here:
- ρ_{A₂} generators from the integral chain: A = [[1,1],[0,1]], B = [[1,0],[−1,1]]; **(AB)³ = −I, (AB)⁶ = I**; ABA = BAB.
- The folding φ (σ_1↦a, σ_2↦b, σ_3↦a) sends B_4's relations to aba = bab (twice) and a² = a², so φ is a homomorphism, plainly surjective.
- **c_4 = ρ_{A₂} ∘ φ, matrix-exact in one convention:** the n=4 radical-quotient matrices derived from scratch satisfy c_4(σ_1) = A, c_4(σ_2) = B, c_4(σ_3) = A. Agreement on generators gives equality of homomorphisms — no basis ambiguity remains in this convention.
- Both claimed kernel generators die: c_4(σ_1σ_3⁻¹) = I and c_4((σ_1σ_2)⁶) = (AB)⁶ = I, computed.

The two remaining steps are group theory, identified as such: (i) ker φ = ⟨⟨σ_1σ_3⁻¹⟩⟩, because imposing σ_1 = σ_3 on B_4's presentation yields exactly B_3's presentation; (ii) ker ρ_{A₂} = ⟨(ab)⁶⟩, whose one classical input is that B_3 modulo its center ⟨(ab)³⟩ is PSL(2,ℤ) under this action — pinned computationally by (ab)³ ↦ −I ≠ I (so the kernel is the even part of the center) and consistent with SGT-004's audited facts (ρ_{A₂} surjective, ρ(P_3) = Γ(2)). Given (i) and (ii), K_comp,4 = φ⁻¹(⟨(ab)⁶⟩) is generated as a normal subgroup by ker φ together with the lift (σ_1σ_2)⁶ of (ab)⁶ — the standard preimage generation for a surjective map. Surjectivity of c_4 (composite of surjections) gives the exact sequence.

**Conclusion:** the normal generating set and the exact sequence stand. This also retroactively decides the question SGT-009 left open: K_comp,4 is strictly smaller than π_4⁻¹(V_4^(Klein)) in general position — it is the explicit group above — while remaining incomparable with P_4, as SGT-009 proved.

## 3. Prime-Delay coefficient K — derivation verified from the stated recurrence; model definition still owed

The symbolic period-two expansion (both parities separated, mean solved first) reproduces the relayed formulas exactly:
- mean shift m = −(b / (2(1−a))) z²;
- alternating equation 0 = −2C_o(ε − ε_c) z + K z³ + O(z⁵ + |ε−ε_c| z³), with the cubic coefficient computed as b²/(2(1−a)) − a/6 + (4/3) ε D_o; evaluated at ε = ε_c (the difference being higher order, as the error term allows) it equals the stated **K = b²/(2(1−a)) − a/6 + (4/3) ε_c D_o** with difference exactly 0.
- The three contributions check individually: the b² term is the quadratic Kepler term feeding back through the mean shift; −a/6 is the Kepler cubic; (4/3) ε_c D_o comes from the odd delays only (even delays see zero alternating difference; odd delays see 2z, and 2³/6 = 4/3) — the same parity mechanism as the linear threshold, one order down.

**Caveat, stated plainly:** what is verified is the bifurcation algebra *given the relayed nonlinear recurrence*. That recurrence is the steward's reconstruction: the deposited THM-DYN-0001 package contains only the linearized recurrence and marks the nonlinear branch conjectural. Before K is an audited theorem, the separate submission must fix the nonlinear model's definitions (the delays p_j, the exponent s, the range of j) in the record. The steward's recommendation — its own theorem, its own audit — is the right sequencing, and this verification is filed so that audit starts from a checked derivation.

## Sequencing

Endorsed: SGT-009b as the next formal submission carrying the two corrections; the Prime-Delay coefficient as a separate theorem with the nonlinear model defined in the deposit.
