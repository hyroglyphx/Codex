# Prime-Delay Flip Theorem — Independent Audit (Muse / Jethro)

Date: 2026-11-22 · Object: THM-DYN-0001-v1.0, as transferred on branch `relay/prime-delay-native-proof-20261122` (commit acbf752). Audit script: Muse workspace `hidden_files/prime-delay-audit/audit_prime_delay.py` (seeded; all quantities computed from the definitions).

## Verdict

**The proof as transcribed is correct and complete. No substantive correction found.** The claim — Schur stability iff 0 ≤ ε < (1+a)/(2·C_odd) for finite positive monotone kernels — stands as an exact finite-depth theorem. Two steps the manuscript asserts without showing the estimate are supplied below; both close in the theorem's favor.

## Step-by-step adjudication

- **Unit-circle equations** (steps 1–2): verified algebraically. Dividing by λ^L gives λ − a + εΣc_j(1 − λ^{−j}) = 0; real/imaginary parts are as stated.
- **Trig identity** (step 3): sin θ(1 − cos jθ) + (1 − cos θ) sin jθ = 4 sin x sin(jx) sin((j+1)x), x = θ/2 — verified symbolically by hand and numerically (max discrepancy 1.9e-14 over 4,000 draws).
- **Positivity lemma** (step 4): the closed form T_m(x) = [(m+1) sin 2x − sin(2(m+1)x)] / (4 sin x) matches its defining sum (max discrepancy 1.8e-14). Strict positivity on the open interval 0 < x < π/2 follows analytically: with t = 2x ∈ (0, π), the numerator is positive because sin((m+1)t) < (m+1) sin t there — the strict Chebyshev bound |sin nt| < n sin t on (0, π) for n ≥ 2 (immediate when sin((m+1)t) ≤ 0). Numerical scan (m = 1..300, 20,000-point grid) found no interior zero or negative; the infimum is the endpoint limit x → π/2⁻ (e.g. T_2 = 2 sin²(2x) cos x → 0), which is the λ = −1 case handled separately. Abel summation then gives Q_L > 0 under c_1 ≥ … ≥ c_L > 0, as claimed.
- **Elimination** (step 5): εQ_L = (a − 1) sin θ, i.e. a − 1 = Q_L/(−B_L); with Q_L > 0 and B_L < 0 this forces a > 1 — contradiction. No nonreal unit-circle crossing at any ε > 0. Correct.
- **Real crossings** (step 6): λ = 1 forces a = 1, excluded. At λ = −1 only odd j contribute (1 − (−1)^j ∈ {0, 2}), giving ε_flip = (1+a)/(2C_odd) exactly. Correct — the parity reduction is exact, not asymptotic.
- **Transversality** (step 7): F_ε = 2C_odd as stated. F_λ > 0, asserted in the manuscript, is proven by the pairing bound: S = Σ_j (−1)^{j+1} j c_j ≥ −C_odd, because each even term satisfies 2k·c_{2k} ≤ 2k·c_{2k−1} = (j+1)c_j over odd j = 2k−1 (monotonicity). Hence F_λ = 1 + ε_flip·S ≥ 1 − (1+a)/2 = **(1−a)/2 > 0**, and dλ/dε = −2C_odd/F_λ < 0: the root crosses outward. Numerically, min(F_λ − (1−a)/2) over 20,000 random monotone kernels = +3.5e-4 ≥ 0.

## Low-depth root examples (computed)

Prime weights s = 2 (c_j = p_j^{−1}), roots of P_L computed directly:

- a = +0.3: L=1 and L=2 share ε_c = 1.3000 (C_odd = 0.5 both — pairwise depth invariance confirmed numerically); L=3: ε_c = 0.9286 (C_odd = 0.7). Max |root|: < 1 at 0.99·ε_c, exactly 1.0000 at ε_c with a root at −1 to machine precision, > 1 at 1.01·ε_c, in every case.
- a = −0.4: ε_c = 0.6000 (L=1, 2), 0.4286 (L=3); same crossing behavior.

## Scope, kept exact

The theorem concerns the **delay index's parity**, not prime-numbered times — the manuscript's own distinction, preserved. The nonlinear period-two branch (normal-form coefficient β_F) remains conjectural; infinite-memory stability is not proved by the finite-depth limit (for 1 < s ≤ 2 the finite-depth thresholds → 0 as depth grows, which is a statement about the finite results, not an infinite-depth theorem). The root-of-unity extension (residue-class sums W_r^(q), q = 2 recovering parity) and the flip-equivalence classification of kernels (c ~_F d iff C_odd agrees) are well-posed open directions, now the lane's priority per the transfer.
