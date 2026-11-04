# HMHK Research Lane — Gauge Geometry, Hopf Fibers, Modular Spectra, and BSD
**Status:** Working research synthesis | **Date:** 2026-11-04 | **Repository:** hyroglyphx/Codex

## Scope and provenance
This chapter continues HKK-01 → HMHK-01 → HMHK-02 and proposes HMHK-03. It synthesizes user-provided transcripts/files: Kaluza–Klein lecture transcript (Jxjdjdn.txt), modular-harmonic RH outline (RH+.txt), modular lemmas/applications (Booze.txt), and BSD outline (BSD stuff(1).txt), together with prior ARGO NAVIS/CIRP/IER work. The source documents contain ambitious proof claims; **neither RH nor BSD is proved by these documents or this integration**. Distinguish established constructions, derived propositions, proposed tests, and unsupported implications.

## HKK-01 — Geometry and gauge symmetry
A five-dimensional metric can be written locally (mostly-minus convention)
```math
d\hat s^2=g_{\mu\nu}(x)dx^\mu dx^\nu-R(x)^2(d\theta+\kappa A_\mu(x)dx^\mu)^2.
```
The cylinder condition is invariance along the circular fiber: `∂_θ ĝ_AB = 0` in adapted coordinates, or invariantly `L_K ĝ=0` for the fiber-generating Killing vector. It does **not** imply constant radius: `∂_θ R=0` need not imply `∂_μ R=0`. The frozen-radion condition is additional. A coordinate change `θ' = θ + λ(x)` induces `A' = A − κ⁻¹dλ`; the combination `dθ+κA` and curvature `F=dA` are invariant.

A standard cylinder's base area `πr²`, circumference `2πr`, volume `πr²h`, and surface area `2πr²+2πrh` are different geometric quantities. The compact Kaluza–Klein fiber is an intrinsic circle; ordinary cylinder surface area is not its defining invariant.

## HKK-01b — Hopf nonuniqueness and global reconstruction
The Hopf bundle `S¹ → S³ → S²` and the trivial bundle `S²×S¹ → S²` have the same local fiber type, and can have equal fiber circumference, but different first Chern numbers: respectively `±1` and `0`. A local connection on a northern patch of the Hopf bundle is `A_N=(1−cosϑ)dφ/2`, with `F=(sinϑ/2)dϑ∧dφ` and `(1/2π)∫_{S²}F=1` under the chosen orientation. The total-space metric may be fiber-invariant even when the bundle is globally nontrivial. On overlaps, fiber coordinates and potentials transform by gauge changes; no single global fiber angle is required.

An explicit 5D example is the pullback bundle over `S²×ℝ^{1,1}`, with total space `S³×ℝ^{1,1}`. This is a mathematical construction, not an empirical model of our universe. Global reconstruction requires curvature, holonomy, characteristic classes, topology and/or spectral probes, not just local circumference and symmetry.

## HMHK-01 — Arithmetic phases and bundle spectra
For residues `r∈ℤ/mℤ`, characters `χ_k(r)=exp(2πikr/m)` obey `χ_k(r+s)=χ_k(r)χ_k(s)` and Fourier orthogonality. They give a rigorous interpretation of residue-phase diagrams, without implying that plots demonstrate dynamical attractors.

For a circle bundle of Chern number `n`, a fiber mode of integer weight `k` gives an associated line bundle of degree `q=nk` (sign subject to convention). On a round sphere of radius `a`, the covariant Laplacian spectrum of the degree-`q` monopole line bundle is
```math
\lambda_{j,q}=\frac{j(j+1)-(q/2)^2}{a^2},\quad j=|q|/2,|q|/2+1,\ldots,
```
with multiplicity `2j+1`; the lowest eigenvalue is `|q|/(2a²)`. This is a calculable baseline. Arithmetic restrictions such as primes or `k mod 72` are *experimental filters*, not physical predictions absent a derived selection rule.

A suitable energy is `E_q[ψ]=∫|∇^{(q)}ψ|² dvol` under `∫|ψ|²dvol=1`; its minimum is the lowest eigenvalue. No connection to zeta-zero critical-line confinement follows without a further theorem.

### Repairs to source lemmas
- Finite residue alphabet **does not imply periodicity of prime-indexed residues**; repeated states alone do not establish a repeating sequence. Lagrange's theorem constrains multiplicative orders of *individual group elements*, not the prime-indexed sequence.
- The expression `Σ_{k≤N}1/k (mod p)` is undefined whenever `p|k`. Define `H_N^(p)=Σ_{1≤k≤N,p∤k}k⁻¹ (mod p)`. For odd primes, the sum over a complete block of `p` increments vanishes, giving `H_(N+p)^(p)=H_N^(p)`.
- Dirichlet's theorem alone establishes infinitely many primes in each coprime residue class; asymptotic equal proportions require the prime number theorem for arithmetic progressions.
- Boundedness, periodicity, geometric embedding, attractor dynamics, fractal scaling, and a zeta-zero theorem are **different propositions**; none follows automatically from the preceding one.
- Source claims of complete RH/BSD proofs, and application percentages, remain unverified.

## HMHK-02 — Elliptic-curve arithmetic transport and BSD
For an elliptic curve `E/ℚ` and a good prime `p`, define `a_p=p+1−#E(𝔽_p)`. Hasse's bound gives `|a_p|≤2√p`, so `a_p=2√p cos θ_p` for a Frobenius angle `θ_p∈[0,π]`. The good-prime local factor is
```math
L_p(E,s)=(1-a_pp^{-s}+p^{1-2s})^{-1}.
```
The curve's global L-function includes appropriately modified factors at bad primes. The BSD rank statement predicts `rank E(ℚ)=ord_{s=1}L(E,s)`. This is a conjectural global identification, not a consequence of residue clustering or toroidal visualization. The complex torus `E(ℂ)≅ℂ/Λ`, the Hopf circle bundle, and a modular residue phase circle are distinct objects; connect them only via specified maps.

For a finite predetermined set of good primes `P`, weights `w_p`, modulus `m`, and integer `k`, define the experimental statistic
```math
S_{m,k}(E;P)=\sum_{p\in P} w_p e^{2\pi i kp/m}\frac{a_p}{2\sqrt p},\qquad \mathcal E_{m,k}=|S_{m,k}|^2.
```
**Proposition (proved):** This statistic is invariant under a change of Weierstrass model by a `ℚ`-isomorphism, provided the primes, weights, modulus and index are held fixed. Reason: the local Frobenius traces at good primes are isomorphism invariants. **Not proved:** that this statistic predicts rank, analytic vanishing order, or BSD.

Compare curves with known rank and suitable controls for conductor, CM status, sample size, bad primes, and residue-class biases. For non-CM elliptic curves over `ℚ`, the Sato–Tate distribution supplies a baseline for Frobenius angles. A numerical experiment must not substitute finite Euler-product truncation at `s=1` for analytic continuation.

## HMHK-03 — Proposed arithmetic holonomy comparison
Geometric holonomy of a connection around loops and Frobenius conjugacy classes in arithmetic Galois representations are different constructions. Both yield conjugacy-invariant data, but a correspondence requires a functor, comparison theorem, or explicit representation-theoretic map. Research question: which classes of local arithmetic observations, global bundle invariants, and spectral probes suffice to reconstruct a specified elliptic-curve invariant? State the observation class and admissible equivalence before claiming sufficiency.

## CIRP / IER registry
- **Object:** circle bundle / elliptic curve / associated line bundle.
- **Partition:** base, fiber, local arithmetic reductions, global analytic data.
- **Representations:** metric, gauge potential, Chern class, Fourier characters, Frobenius traces, L-function.
- **Admissible operations:** gauge transformations, change of trivialization, isomorphism of elliptic-curve models, Fourier transform, covariant differentiation.
- **Verified invariants:** curvature under U(1) gauge change; first Chern class; Frobenius traces under rational isomorphism; specified spectral eigenvalues.
- **Candidate observables:** modular phase energies and cross-curve spectral correlations.
- **Failure modes:** confusing local with global; identifying distinct integer labels; interpreting visualization as proof; inferring universal zero or rank theorems from bounded finite data.

## Immediate test plan
1. Implement Hopf/trivial-bundle connections and numerically integrate `F/(2π)` over the sphere; recover Chern numbers 1 and 0.
2. Compute covariant-Laplacian low eigenvalues for `q=nk` and verify exact formula.
3. Compare `k mod 72` against multiple control moduli; predeclare the statistic and correction for multiple comparisons.
4. Enumerate `#E(𝔽_p)` for sample curves and compute `S_{m,k}`; verify invariance under alternate rational Weierstrass models.
5. Run rank-labeled comparisons with held-out curves, negative controls and uncertainty intervals.
6. Maintain separate proof obligations for any proposed RH or BSD implication.

**Series status:** HKK-01 (geometry) → HMHK-01 (spectral arithmetic) → HMHK-02 (elliptic transport) → HMHK-03 (arithmetic holonomy; proposed). This chapter records integration and test design, not completed computational validation.
