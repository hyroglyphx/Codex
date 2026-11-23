# THM-DYN-0002 — Flip-Equivalence Classification of Delay Kernels

Date: 2026-11-22 · Status: **corollary-classification of THM-DYN-0001** (dependency recorded; not an independent theorem). Proposed via the ChatGPT relay steward as the node "Flip-Equivalence Geometry," immediately after the Prime-Delay Flip Theorem and its independent audit (2026-11-22). Adjudicated and computed by Muse / Jethro.

## Statement

Fix the local multiplier a ∈ (−1, 1). For finite positive nonincreasing kernels c, d (of any lengths L_c, L_d), define

c ~_F d ⟺ C_odd(c) = C_odd(d), where C_odd(c) = Σ_{j odd} c_j.

Then, by THM-DYN-0001 (ε_c = (1+a)/(2·C_odd), with (1+a)/2 > 0):

**c ~_F d ⟺ ε_c(c) = ε_c(d).**

Equality of the odd-channel invariant is necessary and sufficient for equality of the first positive-coupling stability threshold, within the admissible class and **at fixed a**. (Across different a the implication fails: ε_c mixes (1+a) with 1/C_odd, so equal thresholds at different a do not imply equal C_odd.)

## Content of the classification

- The threshold functional factors through the one-scalar projection C_odd; the flip-equivalence classes are exactly its level sets. The quotient of the admissible kernel space by ~_F is the half-line (0, ∞), coordinatized by C_odd. Class members may differ in length, coefficients, characteristic polynomial, spectrum, and transient behavior — everything except the first stability boundary.
- C_odd-preserving transformations (the classification's working part): (i) any change to even-indexed coefficients that keeps the kernel admissible (positive, nonincreasing); (ii) any redistribution of mass among odd indices preserving their sum, subject to admissibility; (iii) appending a single even-indexed tail coefficient to an odd-length kernel (indices are absolute, so existing parities never shift); (iv) pairwise depth extension by an (odd, even) pair whose odd member is compensated under (ii). A complete parametrization of the admissible part of each level set is elementary but not yet written out.
- What ~_F does **not** preserve: transient spectra, non-flip spectral features, and any nonlinear behavior past the boundary (the period-two branch of THM-DYN-0001's open problem is not classified by C_odd).

## Computed example (Jethro, 2026-11-22; script `flip_equivalence_example.py`)

a = 0.3. Kernel A: L=2, c = (1, 1/2), C_odd = 1. Kernel B: L=3, c = (3/4, 1/2, 1/4), C_odd = 3/4 + 1/4 = 1. Both admissible; ε_c = 0.65 for both.

- Max |root| at ε = 0.5·ε_c: A 0.6663, B 0.7086 — both stable, different margins.
- At ε = ε_c: both exactly 1.0000 (root at λ = −1). At 1.01·ε_c: A 1.0129, B 1.0098 — both unstable.
- Spectra at ε = 0.5·ε_c differ plainly: A {0.666, −0.427 ± 0.248i}; B {0.709, −0.563, −0.167 ± 0.419i} — different degrees, different transients, identical boundary.

## Placement

Registry node THM-DYN-0002, timeline "Flip-Equivalence Geometry," directly after THM-DYN-0001 + audit. It is the natural base for the mod-q residue classification (the q = 2 case of the root-of-unity projection is exactly C_odd / C_even separation) and links to the Invariant Ecology Registry as a worked instance of an invariant-defined equivalence.
