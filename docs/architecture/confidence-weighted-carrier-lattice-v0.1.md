# Confidence-Weighted Carrier Lattice v0.1

**Date:** 2026-09-24
**Status:** ACTIVE / ARCHITECTURE

## 1. Principle

The corpus is mature enough to assign confidence, but confidence must attach to a specific claim-layer rather than to a whole term.

Do not write:

```text
Alašiya = 0.83 confidence
```

Write:

```text
REFERENT_IDENTITY(Akkadian Alašiya, Egyptian ʾirs3) = very high
PHONEME_MAPPING(š, Egyptian s/r rendering) = medium-high
EXACT_LOCAL_PRONUNCIATION = low-medium
ETYMOLOGY(allai -> Alašiya) = low
```

A single form can be highly secure as a referent while uncertain in pronunciation, morphology, or ultimate etymology.

## 2. Claim vector

Every node or edge may carry the following confidence dimensions:

```text
C = [
  REF,   # same referent / identity
  READ,  # reading / transliteration
  PHON,  # phoneme reconstruction
  SEM,   # semantic gloss / function
  MORPH, # morphological segmentation
  TIME,  # dating / chronological placement
  GEO,   # geographic localization
  FUNC,  # institutional / ritual / political function
  TRNS,  # transmission / borrowing / reception pathway
  ETYM   # historical etymology
]
```

Use null when a dimension is not being asserted.

## 3. Weight bands

Prefer intervals/bands over false point precision.

```text
A / 0.90-1.00  DIRECT ANCHOR
  same artifact, explicit ancient gloss, bilingual equation, secure same-referent crosswalk

B / 0.75-0.89  STRONG
  multiple independent same-referent witnesses, secure internal corpus recurrence, strong geographical/chronological lock

C / 0.55-0.74  MODERATE
  licensed phonological mapping, convergent contextual evidence, plausible transmission path

D / 0.30-0.54  WEAK-PLAUSIBLE
  meaningful structural/phonemic/semantic convergence but incomplete bridge

E / 0.10-0.29  EXPLORATORY
  resemblance or hypothesis with some constraints but no decisive transmission evidence

F / 0.00-0.09  UNSUPPORTED / CONTROL
  useful as adversarial comparison or rejected equation
```

Do not automatically multiply dimensions together. The vector is primary; a scalar summary is optional.

## 4. Evidence operators

Evidence weight should be raised by independence and lowered by genealogical dependence.

Positive evidence classes:

```text
E1 same artifact / bilingual equation
E2 explicit ancient gloss or translation
E3 same referent in independent scripts/languages
E4 repeated internal corpus behavior
E5 lawful phonological transform
E6 geographic coincidence independently established
E7 chronological overlap
E8 institutional/functional correspondence
E9 archaeological localization
E10 later local survival with continuity constraints
```

Penalty classes:

```text
P1 modern spelling resemblance only
P2 modern pronunciation projected backward
P3 dependent daughter-language duplication
P4 circular etymological argument
P5 semantic match without carrier evidence
P6 geographic match without chronology
P7 same author/source repeated as if independent
P8 uncertain reading treated as fixed
```

## 5. Micro-anchors

A foothold may be only one word, one phoneme mapping, one determinative, or one explicit gloss.

Define:

```text
MICRO_ANCHOR = smallest source-locked correspondence that constrains the larger graph
```

Examples:

- one bilingual name equation;
- one same-artifact docket;
- one determinative attached to a place-name;
- one recurring scribal spelling;
- one ancient lexical gloss;
- one securely localized tablet clay source;
- one phoneme correspondence repeated across same-referent names.

Micro-anchors should never be inflated into full etymologies, but they can constrain neighboring hypotheses.

## 6. Spatial-temporal representation

Represent each attested form as a typed node:

```text
N = {
  form,
  normalized_form,
  language,
  script,
  source,
  date_start,
  date_end,
  latitude,
  longitude,
  polity_or_region,
  semantic_tags,
  institutional_tags,
  confidence_vector
}
```

Represent each proposed relation as a typed edge:

```text
E = {
  source_node,
  target_node,
  operator,
  transformation,
  evidence_ids,
  independence_group,
  confidence_vector,
  status
}
```

Recommended geometry:

```text
X,Y = geography
Z   = time
node radius = source confidence / attestation density
edge thickness = relation confidence
edge type = translation / borrowing / phoneme-map / classifier-shift / title-rebinding / local-survival
```

This produces a 4D conceptual object: geographic network changing through time.

## 7. Confidence is local and updateable

Never freeze a term at one global confidence.

Example:

```text
Alašiya <-> Egyptian ʾirs3
REF  = A
READ = A/B
PHON = B/C
TIME = A
GEO  = B
ETYM = null
```

while:

```text
Alašiya <- Hurrian allai
REF  = null
PHON = C/D
SEM  = C
MORPH = D
TRNS = D/E
ETYM = E/D
```

## 8. Propagation rule

A strong node can constrain adjacent weak edges, but confidence must not propagate automatically.

```text
ANCHOR(A,B) high
+ C resembles B
does not imply
ANCHOR(A,C) high
```

Instead:

```text
high-confidence anchor narrows allowable transformations
-> candidate edge is retested
-> candidate confidence updates only if it satisfies those transforms
```

## 9. Suggested scalar summary

When a map needs one visual weight, compute a conservative summary from asserted dimensions only:

```text
S = weighted_median(REF, READ, PHON, SEM, MORPH, TIME, GEO, FUNC, TRNS, ETYM)
```

Recommended default weights:

```text
REF  3
READ 2
PHON 3
SEM  2
MORPH 2
TIME 2
GEO  2
FUNC 1
TRNS 3
ETYM 4
```

For a pure translation map, raise SEM/FUNC. For a phonemic map, raise PHON/READ. For ancestry/etymology, ETYM/TRNS dominate.

## 10. Working rule

```text
FEW SECURE WORDS
+ SECURE PHONEME APPROXIMATIONS
+ DATE
+ PLACE
+ TYPED TRANSFORM
=
ENOUGH TO BUILD A CONSTRAINED LATTICE
```

The lattice is not a proof engine by itself. It is a way to preserve what is known, expose where uncertainty lives, and make future evidence update the correct part of the model.
