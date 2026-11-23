# SGT-003 — The A2 Discriminant, Root Monodromy, and Vanishing-Cycle Transport
**Date:** 2026-11-22
**Lineage:** SGT-001 → SGT-002 → SGT-003
**Mathematical status:** Exact derivations using classical A2 singularity and Picard–Lefschetz theory; the operator-atlas synthesis is Tate's research organization, not a claim to discover these classical results.

## 1. Unfolding and two discriminants
Consider F(x,y;u,v)=x³+ux+v+y² over C. Critical points of F in the variables (x,y) satisfy 3x²+u=0 and 2y=0. They collide precisely at u=0 (independently of v). This is the critical-point collision locus, not the discriminant of singular zero fibers.

The zero fiber F=0 is singular if F=F_x=F_y=0 simultaneously. Setting y=0 and u=−3x² yields v=2x³. Elimination gives 4u³+27v²=0. Conversely, this equation implies x³+ux+v has a repeated root over C, giving a singular point of the zero fiber. Therefore Δ_zero={(u,v):4u³+27v²=0}, a cusp.

At generic points of Δ_zero the zero fiber has a nodal A1 singularity; at the cusp (u,v)=(0,0) the zero fiber has an A2 cusp.

## 2. Exact root monodromy
Off Δ_zero, p(x)=x³+ux+v has three distinct roots. They form a 3-sheeted root covering over parameter space B=C²\Δ_zero, yielding a monodromy homomorphism π1(B)→S3.
At u=0, v=ρ exp(iθ), ρ>0, θ from 0 to 2π, roots are x_j(θ)=ρ^(1/3) exp(i(θ+π+2πj)/3), j=0,1,2. After one circuit each root moves to the next, so the permutation is a 3-cycle.
Near a smooth discriminant point, a small meridian interchanges the two colliding roots, giving a transposition.
The monodromy group on roots is therefore S3: it contains transpositions and a 3-cycle; more precisely suitable distinct local meridians give adjacent transpositions generating S3.

## 3. Topological refinement
For a smooth zero fiber with three simple roots, y²=−p(x) is a double cover of the x-line branched at three finite points. Its smooth affine curve has genus 1 and one point at infinity; consequently H1 has rank 2 over Z. The braid group B3 acts on the family by transport. On H1, Picard–Lefschetz transvections associated to two vanishing cycles with intersection ±1 can be represented, with compatible basis/orientation conventions, by
T_a=[[1,1],[0,1]], T_b=[[1,0],[-1,1]].
These are noncommuting, unlike the finite root-permutation images. Their products and braid relation T_a T_b T_a=T_b T_a T_b can be checked directly. (These matrix choices depend on orientation/basis; conjugate/inverse choices are equivalent.)
**Important:** the 3-cycle root permutation and its homological lift are different representations. A loop's S3 permutation does not fully determine its integral H1 action; the braid action retains additional information. In particular, a full twist has trivial root permutation but can have nontrivial action on H1 (for the displayed matrices (T_a T_b)^3=−I).

## 4. Algebra versus topology
SGT-001: scalar Milnor number μ(A_k)=k and exact raising.
SGT-002: equal μ(A_k)=μ(D_k) for k≥4 but different embedding dimensions (1 vs 2).
SGT-003: discriminant geometry and monodromy distinguish transport behavior not encoded by root counts alone.
The structural hierarchy is: numerical invariant → local algebra structure → deformation discriminant → transport representation.
Do not claim that all these invariants are independent in every class; their relative strength is example-dependent.

## 5. Checkable statements and audit requests
- Symbolically eliminate x from p=p'=0 and recover 4u³+27v².
- Verify the loop u=0,v=ρ exp(iθ) stays outside Δ_zero, and compute the root 3-cycle.
- Verify matrix braid relation and (T_a T_b)^3=−I.
- Distinguish π1(B)≅B3, its permutation quotient S3, and the homology representation B3→SL(2,Z). The statement about π1(B) is a standard identification for monic depressed cubic polynomials with distinct roots.
- Do not equate u=0 with Δ_zero.
