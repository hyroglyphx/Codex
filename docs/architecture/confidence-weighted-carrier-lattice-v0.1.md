# Confidence-Weighted Carrier Lattice v0.1

**Date:** 2026-09-24
**Status:** ACTIVE / ARCHITECTURE

## Principle

The corpus is mature enough to assign confidence, but confidence must attach to a specific claim-layer rather than to a whole term.

```text
C = [REF, READ, PHON, SEM, MORPH, TIME, GEO, FUNC, TRNS, ETYM]
```

- REF: same referent / identity
- READ: reading / transliteration
- PHON: phoneme reconstruction
- SEM: semantic gloss / function
- MORPH: morphological segmentation
- TIME: dating
- GEO: geographic localization
- FUNC: institutional / ritual / political function
- TRNS: transmission / borrowing / reception pathway
- ETYM: historical etymology

Use null when a dimension is not being asserted.

## Confidence bands

```text
A / 0.90-1.00 = direct anchor
B / 0.75-0.89 = strong
C / 0.55-0.74 = moderate
D / 0.30-0.54 = weak-plausible
E / 0.10-0.29 = exploratory
F / 0.00-0.09 = unsupported/control
```

Prefer intervals/bands to false point precision.

## Micro-anchors

```text
MICRO_ANCHOR = smallest source-locked correspondence that constrains the larger graph
```

Examples: one bilingual name equation; one same-artifact docket; one recurring spelling; one ancient gloss; one determinative; one secure clay-source localization; one repeated phoneme correspondence.

Micro-anchors do not prove whole etymologies. They constrain neighboring hypotheses.

## Evidence operators

Positive evidence:

```text
E1 same artifact / bilingual equation
E2 explicit ancient gloss or translation
E3 same referent in independent scripts/languages
E4 repeated internal corpus behavior
E5 lawful phonological transform
E6 independently established geographic coincidence
E7 chronological overlap
E8 institutional/functional correspondence
E9 archaeological localization
E10 later local survival with continuity constraints
```

Penalties:

```text
P1 modern spelling resemblance only
P2 modern pronunciation projected backward
P3 genealogically dependent evidence double-counted
P4 circular etymology
P5 semantic match without carrier evidence
P6 geography without chronology
P7 repeated same-source evidence counted as independent
P8 uncertain reading treated as fixed
```

## Spatial-temporal lattice

Each attested form becomes a node:

```text
N = {
 form, normalized_form, language, script, source,
 date_start, date_end, latitude, longitude, polity_or_region,
 semantic_tags, institutional_tags, confidence_vector
}
```

Each proposed relation becomes a typed edge:

```text
E = {
 source_node, target_node, operator, transformation,
 evidence_ids, independence_group, confidence_vector, status
}
```

Recommended geometry:

```text
X,Y = geography
Z   = time
node radius = attestation/source confidence
edge thickness = relation confidence
edge type = translation / borrowing / phoneme-map / classifier-shift / title-rebinding / local-survival
```

## Local confidence, not global confidence

Example:

```text
Alašiya <-> Egyptian ʾirs3
REF=A; READ=A; PHON=B; TIME=A; GEO=B; TRNS=A; ETYM=null
```

while:

```text
Alašiya <- Hurrian allai
READ=A; PHON=C; SEM=B; MORPH=D; TIME=C; GEO=C; TRNS=D; ETYM=E
```

## Propagation rule

```text
high-confidence anchor narrows allowable transformations
-> candidate edge is retested
-> candidate confidence updates only if it satisfies those transforms
```

Confidence does not propagate automatically by association.

## Working rule

```text
FEW SECURE WORDS
+ SECURE PHONEME APPROXIMATIONS
+ DATE
+ PLACE
+ TYPED TRANSFORM
=
ENOUGH TO BUILD A CONSTRAINED LATTICE
```

The lattice preserves what is known, exposes where uncertainty lives, and lets new evidence update the correct dimension.
