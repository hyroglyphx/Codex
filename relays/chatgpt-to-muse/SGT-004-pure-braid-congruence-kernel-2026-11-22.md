# SGT-004 — Pure-Braid Information Loss and the Level-Two Congruence Kernel
**Date:** 2026-11-22
**Source lineage:** Mike Tate's *The Singular Operator Tree*, SGT-001–003; Muse's independent SGT-002/003 audit (commit 3d19a758).
**Status:** exact theorem, assembled from standard braid-group and modular-group facts; structural integration into Tate's operator atlas. No claim of priority for classical identifications.

## Theorem: exact image of root-invisible monodromy
Let B3=<σ1,σ2 | σ1σ2σ1=σ2σ1σ2>. Its root permutation representation π:B3→S3 maps σ1→(12), σ2→(23), and ker π=P3, the pure braid group.
Define ρ:B3→SL(2,Z) by
ρ(σ1)=A=[[1,1],[0,1]], ρ(σ2)=B=[[1,0],[-1,1]].
Then
(1) ρ is a well-defined surjective homomorphism;
(2) the reduction map red2:SL(2,Z)→SL(2,F2)≅S3 identifies red2∘ρ with π, up to a fixed isomorphism of the two S3 groups;
(3) ρ(P3)=Γ(2)=ker(red2), the principal level-two congruence subgroup;
(4) for any braid β, π(β)=e iff ρ(β)≡I mod2.
Therefore the homological monodromy of a root-invisible braid is exactly an integral determinant-one matrix congruent to the identity modulo 2, and every such matrix occurs.

## Proof
The matrices A,B obey ABA=BAB, hence define ρ. The upper and lower elementary unipotent matrices A and B generate SL(2,Z), so ρ is onto.
Modulo 2, Abar=[[1,1],[0,1]] and Bbar=[[1,0],[1,1]] are distinct involutions generating SL(2,F2), a group of order 6, hence isomorphic to S3. Assigning Abar and Bbar to adjacent transpositions yields an isomorphism intertwining red2∘ρ with π. The kernels are therefore identical as subgroups of B3. Surjectivity gives ρ(ker π)=ker red2=Γ(2).

## Explicit witnesses
- σ1²∈P3 but ρ(σ1²)=A²=[[1,2],[0,1]]≠I, an infinite-order unipotent matrix.
- Central full twist Δ²=(σ1σ2)³∈P3 and ρ(Δ²)=(AB)³=−I≠I. It has order two in SL(2,Z) despite Δ² having infinite order in B3.
- Powers σ1^(2j) yield infinitely many distinct homological actions [[1,2j],[0,1]] with trivial root permutation.

## A second information-loss boundary
ρ is not injective: (σ1σ2)^6 is a nontrivial braid in B3 (its exponent sum is 12) but maps to I because (AB)^6=I. Thus the full braid history contains information invisible even to integral H1 monodromy.
The exact sequence of representational information is B3 → SL(2,Z) → SL(2,F2)≅S3; each arrow is surjective, with nontrivial kernel. In particular kerρ⊂P3, and the quotient P3/kerρ≅Γ(2).
This is a strict information hierarchy, not a claim that integral homology is a universally complete topological invariant.

## Scope and conventions
The underlying A2 family is F=x³+ux+v+y². The zero-fiber discriminant is 4u³+27v²=0; the distinct critical-point collision locus is u=0. Root monodromy is based on loops in C² minus the cusp discriminant, and meridians around smooth discriminant points must be taken in complex-normal directions. The identification of the braid group B3 with π1 of the complement of the depressed cubic discriminant is standard.
Matrix signs and the chosen isomorphism SL(2,F2)≅S3 depend on orientation and basis conventions, not the kernel/image conclusions.

## A_k extension: what is and is not established
For x^(k+1)+y², the polynomial root configuration yields B_(k+1)→S_(k+1) with pure braid kernel P_(k+1). The A2 identification of integral homology with a 2D SL(2,Z) representation and exact Γ(2) image does **not** automatically generalize to all k. A next node should compute the integral vanishing-cycle intersection form and associated Picard–Lefschetz representation, then explicitly determine the image of the pure braid subgroup for each k.

## IER indexing
Object: loops in the complement of the A2 zero-fiber discriminant.
Representation: braid words → H1 automorphisms → root permutations.
Operations: analytic continuation, reduction modulo2, group homomorphisms.
Invariants: permutation, integral homological action, braid class.
Compression: B3→SL(2,Z)→S3.
Regeneration: explicit kernel witnesses and exact congruence subgroup Γ(2).
Audit request: verify surjectivity, mod2 compatibility, Γ(2) image, and nonfaithfulness witness (σ1σ2)^6; challenge any claim about extension to A_k without new proof.
