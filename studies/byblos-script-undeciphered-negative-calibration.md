# Byblos Script — Undeciphered Negative Calibration and Sign-Inventory Sieve

Status: ACTIVE / NEGATIVE DECIPHERMENT CONTROL
Updated: 2026-09-22

## Purpose

Use the Byblos script as the inverse control to Rosetta, Behistun, KTU 5.14, Ebla, and Hittite.

Those successful or partly successful calibration cases have one or more of:
- explicit bilingual/trilingual equivalence,
- known language,
- known semantic anchors,
- lexical crosswalks,
- large comparative corpora,
- or corpus-wide morphological confirmation.

Byblos has none of these securely enough to force a decipherment.

Therefore its proper role in the Nexus is:

```text
SMALL CORPUS
+ UNCERTAIN SIGN INVENTORY
+ UNKNOWN LANGUAGE
+ NO SECURE BILINGUAL
+ MULTIPLE PLAUSIBLE SCRIPT MODELS
→ DECIPHERMENT CLAIM CEILING
```

This makes Byblos a high-value adversarial control.

---

## 1. Current scholarly status

Recent specialist overviews continue to treat the Byblos script as undeciphered.

Vita & Zamora (2018) describe:
- roughly fifteen texts in the current corpus,
- a pictographic signary,
- probably around one hundred signs,
- a likely syllabic structure,
- Egyptian inspiration as plausible,
- no internal evidence sufficient to identify the language as Northwest Semitic,
- no accepted decipherment.

Ben Haring (2024) likewise describes fourteen certain inscribed stone/metal artefacts, with a few possible additional pieces, and emphasizes that the writing remains unreadable.

Primary modern references:
- Juan-Pablo Vita & José-Ángel Zamora, "The Byblos Script" (2018)
- Ben Haring, "The Byblos Script" in *Byblos: A Legacy Unearthed* (2024)
- Mnamon, Byblos (Pseudo-hieroglyphic), updated 2022

---

## 2. Corpus geometry

Dunand's principal corpus included:
- 2 stone stelae/fragments,
- 2 bronze tablets,
- 4 bronze spatulae,
- 2 stone fragments probably from one stela,

with later fragmentary additions.

The long bronze tablets carry most of the repeated material.

This matters because:

```text
medium
!=
ductus
!=
sign identity
```

A sign on stone can look different from the same sign on bronze.

Therefore a raw "114 signs" count is not a secure phonological inventory.

---

## 3. The uploaded sign chart

The supplied chart is the familiar revised Byblos sign-list visualization based on Dunand's corpus.

Each cell encodes four independent variables:

```text
upper-left  = graphic sign
lower-left  = Dunand sign code
lower-right = token frequency
upper-right = media distribution
              T = tablet
              S = spatula
              M = monument
```

That is extremely useful for the Nexus because the image is already a compact multidimensional state table.

But the chart is **not a phonetic key**.

The red labels such as E15, G17, B3, etc. are catalogue identifiers, not readings.

### Important consequence

```text
SIGN ID
!=
PHONETIC VALUE
```

The chart can support:
- frequency analysis,
- positional analysis,
- medium-conditioned allography,
- sign-cluster analysis,
- repeated-sequence analysis,

before any phonetic assignment is attempted.

---

## 4. Inventory-collapse problem

Dunand counted 114 signs.

Later scholarship has repeatedly warned that:
- damaged forms may have been counted separately,
- monumental and cursive variants may inflate the inventory,
- some forms may be allographs rather than distinct graphemes.

Thus define:

```text
N_surface
= observed graphic forms

N_grapheme
= hypothesized normalized sign inventory

N_value
= number of distinct functional/phonological values
```

and require:

```text
N_surface >= N_grapheme >=? N_value
```

without assuming equality.

The chart itself visually reinforces this problem because related-looking signs recur with different Dunand codes and different media distributions.

---

## 5. Medium-conditioned allography

Add:

```text
ALLOGRAPH(sign, medium)
```

where medium can be:
- tablet,
- spatula,
- monument/stone.

A candidate variant cluster should only be collapsed if it survives tests such as:

1. mutually exclusive or near-exclusive distribution,
2. compatible positional behavior,
3. compatible neighboring-sign distributions,
4. graphic transform plausibility,
5. medium dependence,
6. no sequence contradiction.

This is exactly analogous to the earlier correction:

```text
surface morphology
!=
root
```

Now:

```text
surface glyph
!=
grapheme
```

---

## 6. Script-type inference without reading

The sign count is too large for an ordinary consonantal alphabet and too small for an unrestricted logographic system.

That makes a syllabic or mixed system plausible.

But:

```text
inventory size
→ script-type prior
```

not:

```text
inventory size
→ phonetic decipherment
```

The project should therefore assign probabilities to competing models:

```text
M1 = syllabary
M2 = consonant+vowel marked system
M3 = mixed syllabic/logographic
M4 = other mixed system
```

and test them against sequence statistics.

---

## 7. Language prior versus internal evidence

Byblos lies in a Northwest Semitic cultural zone and had deep Egyptian contact.

That gives useful priors.

But Vita & Zamora explicitly warn that the language itself is not internally established.

Therefore:

```text
GEOGRAPHIC LANGUAGE PRIOR
!=
LANGUAGE IDENTIFICATION
```

This is a direct control against one of the most dangerous decipherment errors:
choosing the desired language first and making sign values fit it afterward.

---

## 8. Why earlier decipherments do not count as solved

Dhorme, Mendenhall, Best, Woudhuizen, Garbini and others proposed very different readings.

The same tablet has been interpreted in radically different genres.

That is strong evidence that the corpus does not yet constrain the solution space tightly enough.

Thus:

```text
plausible reading
!=
decipherment
```

A decipherment must predict material not used to construct the key.

---

## 9. New Nexus operator — HOLDOUT DECIPHERMENT TEST

Define:

```text
TRAIN
= subset of inscriptions used to infer sign classes/values

HOLDOUT
= inscription not used during inference
```

A valid decipherment proposal must predict on the holdout:

- recurring sign sequences,
- word/phrase boundaries,
- grammatical recurrence,
- expected proper names or formulae,
- sign-value consistency,
- directionality,
- medium variants.

Formally:

```text
DECIPHERMENT_SCORE
=
fit(training)
× prediction(holdout)
× cross-text consistency
× morphological coherence
× external historical plausibility
```

A model that only fits the training text is not promoted.

---

## 10. New Nexus operator — VALUE ASSIGNMENT ENTROPY

For each normalized sign:

```text
V(s) = {candidate values}
```

Define uncertainty:

```text
H_value(s)
```

high when many values remain compatible.

The goal is not to assign a value quickly.

The goal is to reduce uncertainty through independent constraints.

This is the exact inverse of overconfident decipherment.

---

## 11. Sequence-first workflow

For Byblos the correct order is:

```text
LOCK CORPUS
→ NORMALIZE MEDIA/ALLOGRAPHS
→ COUNT SIGN FREQUENCIES
→ POSITIONAL DISTRIBUTION
→ BIGRAM/TRIGRAM GRAPH
→ REPEATED SEQUENCE CLUSTERS
→ WORD-DIVIDER / BOUNDARY MODEL
→ SCRIPT-TYPE MODEL
→ LANGUAGE-AGNOSTIC STRUCTURE
→ ONLY THEN test language hypotheses
→ HOLDOUT PREDICTION
```

Do not begin with:
- guessed Egyptian picture-values,
- guessed Phoenician cognates,
- or modern visual resemblance.

---

## 12. Relation to Hittite decipherment

Hittite succeeded because:

```text
known script
+ known semantic logograms
+ cognate hypotheses
+ morphology
+ syntax
+ corpus-wide propagation
```

Byblos lacks the secure anchor layer.

Therefore Byblos is the negative control for:

```text
how much can be inferred
before semantic anchors exist?
```

This should become a formal calibration pair:

```text
HITTITE
= anchored unknown-language decipherment

BYBLOS
= unanchored unknown-script/unknown-language inference
```

---

## 13. Relation to Rosetta Nexus

Rosetta and the multilingual calibration family show how rapidly uncertainty collapses when independent crosswalks exist.

The uploaded multilingual-inscription reference itself emphasizes that multilingual inscriptions are especially important for decipherment, and lists cases such as Behistun, Karatepe, Rosetta, Tell Fakhariya, Ebla and Ugarit.

Byblos is what happens when that crosswalk is missing.

Therefore add a new parallax condition:

```text
PX-N0 = NO EXPLICIT CROSSWALK
```

This is not "low confidence" by itself.
It is a structural property of the evidence environment.

---

## 14. New sieve variables

```text
SIGN_CATALOG_ID
TOKEN_FREQUENCY
MEDIA_DISTRIBUTION
POSITIONAL_DISTRIBUTION
ALLOGRAPH_CLUSTER
DAMAGE_STATE
DIRECTION
SEQUENCE_RECURRENCE
BOUNDARY_CANDIDATE
SCRIPT_TYPE_PRIOR
LANGUAGE_PRIOR
INTERNAL_LANGUAGE_EVIDENCE
VALUE_ASSIGNMENT_ENTROPY
TRAINING_TEXTS
HOLDOUT_TEXTS
HOLDOUT_PREDICTION_SCORE
DECIPHERMENT_PROPOSAL_ID
PROPOSAL_DEPENDENCY
CLAIM_CEILING
```

---

## 15. New recursive consequences

### Arity-compression

Byblos becomes a direct test of whether:
- ~100 surface signs collapse toward a smaller grapheme inventory,
- grapheme count supports syllabic structure,
- sign complexity correlates with frequency or medium.

### Ancient-script lattice

Byblos should be treated as a first-class undeciphered-script node with:
- exact-sign lane,
- variant-cluster lane,
- sequence lane,
- medium lane,
- cross-script visual comparison lane,
- **no phonetic promotion without holdout success**.

### Hittite

Strengthens the rule:

```text
prediction > resemblance
```

### Rosetta

Strengthens the inverse rule:

```text
explicit ancient crosswalk
dramatically lowers decipherment entropy
```

### Numeral/null discipline

Any Byblos sign-value hypothesis must be frozen before testing on holdout inscriptions.

---

## 16. Current classification

Attested:
- small corpus on stone and bronze,
- roughly one hundred observed sign types,
- medium-dependent graphic variation,
- predominantly right-to-left writing,
- repeated sequences,
- no accepted decipherment.

Derived:
- syllabic or mixed phonographic system is plausible from inventory scale.

Candidate:
- Northwest Semitic language,
- specific Egyptian-derived values,
- any published full decipherment.

Rejected as current project state:
- treating a proposed decipherment as established fact.

## Governing rule

```text
BYBLOS IS NOT A FAILED ROSETTA.

IT IS THE CONTROL CASE FOR
WHAT THE NEXUS MUST REFUSE TO INVENT
WHEN ROSETTA-LIKE ANCHORS ARE ABSENT.
```
