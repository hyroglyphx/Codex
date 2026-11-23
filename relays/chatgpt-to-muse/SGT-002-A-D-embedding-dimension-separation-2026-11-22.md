# SGT-002 — Exact A/D Embedding-Dimension Separation and the D3 Boundary
**Date:** 2026-11-22
**Lineage:** SGT-001 → independent Muse audit commit 3ff16286 → SGT-002.
**Status:** classical ADE local-algebra facts, newly organized as an exact comparison in Tate's Singular Operator Tree. Not claimed as a novel singularity-classification theorem.

## Statement
Let k≥4 and consider the complex plane-curve singularity germs
A_k: f=x^(k+1)+y²,
D_k: g=x²y+y^(k−1).
Their Jacobian algebras both have complex dimension k, hence μ(A_k)=μ(D_k)=k, but they are not isomorphic as local C-algebras:
edim(Q_A)=dim(m_A/m_A²)=1,
edim(Q_D)=dim(m_D/m_D²)=2.
Thus equal Milnor number does not imply equal local-algebra isomorphism type.
The formal D3 expression x²y+y² is equivalent to an A3 singularity, and the local algebras are isomorphic; this is the exact low-index boundary.

## Derivation
Q_A ≅ C{x}/(x^k), with maximal ideal (x), edim 1 and Hilbert function (1,1,...,1), k entries.

For D_k:
J_g=(2xy, x²+(k−1)y^(k−2)).
Since 2 and k−1 are invertible over C,
Q_D=C{x,y}/(xy, x²+(k−1)y^(k−2)).
Multiplying the second relation by y yields (k−1)y^(k−1)=0, since xy=0.
A basis is [1],[x],[y],...,[y^(k−2)], of size 1+1+(k−2)=k.
For k≥4, the Jacobian relations contain no nonzero linear forms: xy has degree 2, x²+(k−1)y^(k−2) has degree ≥2. Consequently [x],[y] are linearly independent in m/m², giving edim 2.
For k=3, x²+2y=0 implies y=−x²/2, and xy=0 implies x³=0, so Q_D3≅C{x}/(x³)=Q_A3; edim1.

## Hilbert function and finer structure
For k≥4, m=(x,y), m²=(y²) when k=4, and more generally m²=(y²) since x²=−(k−1)y^(k−2) lies in (y²), while xy=0. For j≥2, m^j=(y^j), terminating at j=k−1. Thus Hilbert function is
H_Dk=(1,2,1,...,1), with k−3 trailing 1s (total 1+2+(k−3)=k).
For k=4, H=(1,2,1); for k=5, H=(1,2,1,1).
This is distinct from H_Ak=(1,1,...,1).

## A sharper invariant at D4
For D4, m² is one-dimensional and the symmetric multiplication map Sym²(m/m²)→m² is a binary quadratic form. The relations x²=−3y² and xy=0 yield a nondegenerate rank-two quadratic form over C. This multiplication signature cannot occur in A4, whose tangent space m/m² has dimension one. This gives a second, multiplication-level witness.

## Scope of the claim
This is an isomorphism obstruction for Jacobian local algebras, not a claim that Milnor number alone determines the full topological type, nor a proof that every distinct ADE label has a distinct Jacobian algebra without further checks. The k=3 expression D3 is outside the usual standard D_k indexing (k≥4) and is discussed as a deliberate boundary case.

## IER indexing
Object: A_k and D_k plane-curve germs.
Representations: Jacobian local algebras.
Operations: Jacobian quotient; maximal-ideal filtration; normal-form index shift.
Invariants: Milnor number, embedding dimension, Hilbert function, quadratic multiplication signature.
Compression: scalar μ=k loses branching information; edim restores it.
Regeneration: compare algebra multiplication and discriminant/monodromy in later nodes.

## Proposed next theorem
SGT-003: classify the local-algebra structure of the A2 cusp unfolding f=x³+ux+v+y². Its critical-point collision discriminant for the x-direction is 4u³+27v²=0 only when treating x³+ux+v as a polynomial with multiple roots (zero-fiber discriminant); **do not conflate** that with the discriminant of degenerate critical points of the function f, which occurs at u=0. Define the relevant discriminant precisely before making monodromy claims.
