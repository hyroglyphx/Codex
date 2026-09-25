# Confidence-Weighted Carrier Lattice v0.1

Status: ADOPTED_EXPERIMENTAL_ARCHITECTURE
Date: 2026-09-24

## Purpose

Convert source-locked linguistic correspondences into a spatial-temporal graph without flattening distinct relation types.

Core rule:

```text
CONFIDENCE IN TRANSLATION / REFERENT / PHONEMIC MAPPING
!=
CONFIDENCE IN ETYMOLOGY / ANCESTRY / TRANSMISSION
```

A strong semantic or same-referent edge must not automatically promote a historical ancestry claim.

## Typed node

```text
NODE = {
  id, language, script, native_form, transliteration,
  period, location, referent, semantic_facets,
  classifier, witness, provenance
}
```

## Confidence vector

Each edge carries a non-compensatory vector:

```text
C = <WIT, REF, PHON, GRAPH, MORPH, SEM, CHRON, GEO, TRANS>
```

where each channel is in [0,1] or Ω when unknown:

- WIT: witness/direct-source confidence
- REF: same-referent confidence
- PHON: phonological mapping confidence
- GRAPH: graphemic/script mapping confidence
- MORPH: morphological compatibility
- SEM: semantic/function equivalence
- CHRON: chronological compatibility
- GEO: geographic/contact compatibility
- TRANS: transport/inheritance/borrowing pathway confidence

Ω must remain unknown and must not be silently converted to 0.5.

## Relation-specific aggregation

A single universal score is forbidden. Compute a scalar only after declaring relation type.

Recommended relation profiles:

```text
SAME_REFERENT_CROSS_SCRIPT:
  REF .30 + WIT .20 + PHON .20 + GRAPH .10 + CHRON .10 + GEO .10

SEMANTIC_TRANSLATION:
  SEM .30 + REF .25 + WIT .20 + MORPH .10 + CHRON .05 + GEO .05 + TRANS .05

ETYMOLOGY:
  PHON .20 + MORPH .20 + WIT .15 + CHRON .15 + GEO .10 + TRANS .20

RECEPTION_ATTRACTION:
  PHON .20 + SEM .20 + WIT .15 + CHRON .15 + GEO .15 + TRANS .15
```

Do not compute when a required channel is Ω unless the relation profile explicitly permits partial scoring.

## Confidence bands

```text
A  0.90-1.00  source-locked / direct anchor
B  0.75-0.89  strong
C  0.55-0.74  supported but incomplete
D  0.35-0.54  exploratory
E  <0.35       resemblance / weak transport
Ω              unresolved
```

These are calibration weights, not frequentist or Bayesian probabilities.

## Spatial-temporal representation

Recommended visualization:

```text
X/Y = learned phonological + semantic distance
Z   = time
color = language/script family
node shape = person/place/title/deity/common noun/operator
edge type = relation operator
edge thickness = relation-specific confidence
edge opacity = witness independence
```

Animate or slice by century. A node may move semantically while retaining carrier continuity.

## Density

A dense node is not merely one with many forms. It should maximize:

```text
independent witnesses
+ script/language diversity
+ explicit crosswalks
+ semantic recurrence
+ chronological depth
+ geographic/contact coherence
- genealogical dependence
- untyped resemblance edges
```

## Promotion rule

Association remains cheap; promotion remains expensive.

Prefer:

```text
SAME ARTIFACT > BILINGUAL/TRILINGUAL > SAME REFERENT MULTILINGUAL > SAME AUTHOR/PERIOD > STRUCTURAL PARALLEL > NAKED RESEMBLANCE
```

## Initial graph families

- ALASHIYA cross-script carrier
- SEMITIC EL / Greek reception
- BR / crossing operator
- LADY/MISTRESS title architecture
- SARDIS multilingual same-referent cluster
- Helli/Selli and NEL/THEL textual/onamastic controls
- SA/SAR receiving-language cluster
- Semitic numeral-two sound-law calibration
- topographic orbits queued for source-lock: Dilmun/Tilmun, Magan/Makkan, Anšan/Anzan, Šušun/Šūšen/Šūšin, Nina/Ninua
