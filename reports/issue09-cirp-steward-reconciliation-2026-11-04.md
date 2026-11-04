# CIRP — steward reconciliation note after Jethro pass (2026-11-04)

Source: user-supplied Jethro report for Codex Issue #9. This note records the supplied audit, not an independent execution of Jethro's script.

## Accepted / incorporated
- Primitive periodic orbits via c_m=(1/m)Σ_{d|m} μ(m/d) tr(A^d), not simple cycles. Multigraphs require explicit edge-shift convention.
- Power traces determine characteristic polynomial/spectrum but not arbitrary graph identity. Reversal, nilpotent, and cospectral counterexamples are standing controls.
- The derivative of tr((A+tvu^T)^2) at zero is 2u^TAv; n² independent scalar *linear* probes are necessary and sufficient for unrestricted labeled n×n matrices.
- C₂∨C₃ vertex wedge (cycles share one vertex) has first nonzero trace defect Δ₅=5, while Δ₆=0. The original issue packet omitted exact edge set; this example is a new explicit reference instance. Defect measures new closed walks, not the fact of gluing.
- Identity loss, observation compression, invariant transport, and noninjective state evolution must be kept distinct.
- RH spectral realization/positivity remains unproved.

## Corrections / qualifications
1. Unlabeled reconstruction modulo graph isomorphism is well-defined. A coordinate-probe protocol presupposes labels, but permutation-invariant probes may be defined. Minimality must name probe class, response alphabet, and cost model.
2. 'Exactly n spectral numbers' refers to n scalar power traces sufficient to recover the characteristic polynomial over characteristic zero, not a universal information-theoretic minimum under arbitrary nonlinear/real-valued measurements.
3. The n² lower bound applies to unrestricted matrix spaces with scalar *linear* probes. It does not automatically extend to discrete adjacency matrices, sparse matrices, nonlinear probes, or arbitrary infinite-precision scalar encodings.
4. For finite-outcome probes on graphs with **exactly** s edges, the rigorous counting bound is k≥ceil(log_q binomial(n²,s)) for q-ary outputs. For **at most** s edges, replace the binomial by Σ_{j=0}^s binomial(n²,j), and exclude loops if the graph model disallows them.
5. Do not label the edge-shift primitive orbit identity as the Ihara zeta formula without specifying nonbacktracking conventions; Artin–Mazur / dynamical graph zeta is the closer direct match.
6. No local execution of the supplied Jethro script has been independently performed in this steward pass; reported test receipts are attributed to Jethro.

## Muse request
Please return an independent literature/mechanism survey, explicitly contrasting dynamical graph zeta with Ihara, observability and active probe design, graph reconstruction modulo isomorphism, gluing and local-to-global sheaf compatibility, and physical scattering vs reduced-channel information. Respond with provenance and adversarial counterexamples.

## Next tests
- Exact primitive edge-orbit enumeration for multigraph [[0,2],[2,0]].
- Exact wedge C₂∨C₃ defects m=1..12 with explicit edges.
- Cospectral star vs square+isolated graph and A vs Aᵀ.
- Probe rank, sparse q-ary information bound, and invariant probe reconstruction under relabeling.

Status: Jethro pass received **via user report**; Muse independent pass pending; reconciliation not yet bilateral.
