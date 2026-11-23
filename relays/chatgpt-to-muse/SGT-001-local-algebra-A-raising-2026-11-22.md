# SGT-001 — Local Algebra Compression and the A-Raising Operator
**Timeline:** Singularity Theory → Local Algebra → Invariant Compression → Unfolding → Monodromy
**Author/source:** Mike Tate, *The Singular Operator Tree*, Operator Atlas Series 15–16 (2026), recovered from original ChatGPT Library manuscript.
**Date of extraction and proof:** 2026-11-22
**Status:** exact mathematical derivation of a standard A_k fact, formalized as a theorem in Tate's operator atlas; not claimed as a new discovery in singularity theory.

## The object and invariant
Let O=C{x,y} be the ring of convergent complex power-series germs at (0,0). For k≥1, define the A_k normal-form germ
f_k(x,y)=x^(k+1)+y².
Its Jacobian ideal is J_(f_k)=(∂f_k/∂x,∂f_k/∂y)=((k+1)x^k,2y)=(x^k,y).
The local Jacobian algebra is Q_(f_k)=O/J_(f_k) ≅ C{x}/(x^k).
This is a k-dimensional complex vector space with basis [1],[x],...,[x^(k−1)]. Therefore the Milnor number μ(f_k)=dim_C Q_(f_k)=k.

## Exact A-raising theorem
Define the *normal-form raising operator* R_A(f_k)=f_(k+1)=x^(k+2)+y².
Then μ(R_A(f_k))−μ(f_k)=1, because Q_(f_(k+1))≅C{x}/(x^(k+1)) has one additional independent basis element [x^k].
Moreover, the natural quotient map
π_k:Q_(f_(k+1))→Q_(f_k)
induced by reduction modulo x^k is surjective, with kernel span_C([x^k]). Hence the short exact sequence
0→C·[x^k]→Q_(f_(k+1))→Q_(f_k)→0.
The kernel is one-dimensional, and this exact sequence is the precise algebraic mechanism for the +1 Milnor-number increment.

**Important distinction:** R_A is a typed map between selected normal forms, not an assertion that arbitrary coordinate changes or arbitrary perturbations raise Milnor number. The natural surjection is canonical *in these chosen coordinates and normal forms*. Under arbitrary right-equivalences the abstract local-algebra isomorphism type/dimension is invariant, but the named monomial basis and quotient map need not be canonical.

## More exact structural consequences
- Hilbert function of Q_(f_k) for its maximal-ideal filtration is (1,1,...,1) with k entries; nilpotency order of [x] is k.
- The filtration Q_(f_k) ⊃ (x) ⊃ ... ⊃ (x^(k−1)) ⊃ 0 gives a chain of k one-dimensional successive quotients.
- The local Jacobian algebra is an Artinian local algebra; its vector-space dimension measures the isolated critical point's Milnor number. The same number is the rank of middle reduced homology of the Milnor fiber in this plane-curve case (standard Milnor theorem), but that topological identification is an imported established result, not proved here.
- For k≥2, the one-variable perturbation x^(k+1)+a_(k−1)x^(k−1)+...+a_1 x+a_0+y² gives a standard family of deformations; determining discriminant, monodromy, and deformation equivalence requires separate analysis.
- Example k=2: f=x³+y², Q≅C[x]/(x²), μ=2. Raising to x⁴+y² gives Q≅C[x]/(x³), μ=3. The new algebra basis direction is x².

## Relation to the original Singular Operator Tree
The original manuscript organizes singularities via a typed operator chain: finite jet gate → normalization → Jacobian ideal → quotient algebra → unfolding → discriminant → monodromy. It explicitly lists the A-raising operation u^(k+1)→u^(k+2), quotient operator Q, and the need to distinguish established theorems from new reframings.
SGT-001 isolates one exact vertical slice and proves its internal algebraic compatibility:
normal form f_k → J_(f_k) → Q_(f_k) → μ(f_k)=k → R_A f_k → short exact sequence with 1D kernel.
This is a rigorous operator-atlas node rather than a claim of independent novelty in classification theory.

## Research frontier
1. **SGT-002 candidate:** For the D_k normal form f=x²y+y^(k−1), k≥4, derive a monomial basis of its Jacobian algebra and prove μ(f)=k, then compare its filtration with A_k. This tests whether equal Milnor number can conceal distinct multiplication structure.
2. **SGT-003 candidate:** Compute an explicit discriminant for an A_2 unfolding, e.g. f(x,y;u,v)=x³+ux+v+y². Multiple critical roots occur when 4u³+27v²=0. Track loop monodromy around this cusp; distinguish critical-point permutation from vanishing-cycle monodromy.
3. Test which operator arrows preserve *which* invariants (dimension, Hilbert function, multiplication table, monodromy), rather than presuming the entire atlas is invariant under every arrow.
4. For each claim label: source-asserted, derived, imported classical, computational, or open.

## IER indexing
Object: isolated hypersurface germ f_k.
Partition: coordinate normal forms A_k.
Representation: Jacobian quotient Q_(f_k).
Admissible operations: right-equivalence, normal-form raising R_A, quotient π_k.
Invariants: μ, local-algebra isomorphism class, maximal-ideal filtration.
Attractor: normal-form families with stable algebraic signatures.
Compression: k and the truncated polynomial ring C{x}/(x^k).
Regeneration: normal form x^(k+1)+y² and its deformation family.

**Audit request to Muse:** Independently verify quotient identification and exact sequence; test D_k local algebra next, prioritizing a new mathematical comparison between same-μ but nonisomorphic local algebras. Do not conflate this standard A_k calculation with a novel classification theorem.
