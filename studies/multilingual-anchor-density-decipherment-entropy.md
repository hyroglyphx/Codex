# Multilingual Anchor Density and Decipherment Entropy

Status: ACTIVE / CROSS-CORPUS CALIBRATION
Updated: 2026-09-22

## Purpose

The newly supplied multilingual-inscription survey and the Byblos sign chart together expose a useful contrast:

```text
MULTILINGUAL / MULTISCRIPT NETWORK
→ many external constraints
→ lower decipherment entropy

ISOLATED UNDECIPHERED CORPUS
→ few external constraints
→ high decipherment entropy
```

This is not a claim that multilingual inscriptions automatically solve a script.

It is a graph-theoretic calibration principle.

---

## 1. Positive anchor network

The supplied survey explicitly treats multilingual inscriptions as important for decipherment and the study of languages with small/repetitive corpora.

It lists, among others:

- Behistun: Old Persian, Elamite, Babylonian
- Rosetta: Egyptian hieroglyphic + Demotic + Greek
- Karatepe: Phoenician + Hieroglyphic Luwian
- Tell Fakhariya: Aramaic + Akkadian
- Ebla: Sumerian + Eblaite
- Ugarit bilinguals across Akkadian/Hittite, Akkadian/Luwian, Sumerian/Akkadian, Ugaritic/Akkadian
- Aphek trilingual lexicon: Sumerian + Akkadian + Canaanite
- Ugarit trilingual and quadrilingual lexical/literary combinations

This means Ugarit is not merely one bilingual object.

It is a **multilingual archive hub**.

---

## 2. Graph model

Represent a calibration environment as:

```text
G = (V, E)
```

where:

```text
V = language / script / register / witness states
E = explicit historical crosswalks
```

For a target undeciphered system U define:

```text
degree(U) = number of secure external crosswalk edges
```

and:

```text
anchor_specificity(U)
= how fine-grained those crosswalks are
```

Examples:

```text
document-level parallel
phrase-level parallel
lexical equation
sign equation
pronunciation gloss
```

Then a first-order decipherment prior is:

```text
DECIPHERMENT_ENTROPY
∝
1 / (
  crosswalk_degree
  × anchor_specificity
  × witness_quality
  × corpus_covariance
)
```

This is descriptive, not a probability formula.

---

## 3. Ugarit as a high-degree hub

The supplied survey lists multiple Ugaritic bilingual/trilingual/quadrilingual combinations.

Therefore Ugarit should be represented as:

```text
Ugaritic
↔ Akkadian
↔ Sumerian
↔ Hurrian
↔ Hittite
↔ Luwian
```

through multiple distinct artifacts and genres.

The important point is not that every language pair has a direct edge.

It is that the archive provides multiple intersecting paths.

That creates:

```text
CYCLE CONSISTENCY
```

possibilities.

If:

```text
Ugaritic A
→ Akkadian B
→ Sumerian C
```

and another lexical list gives:

```text
Ugaritic A
→ Sumerian C
```

the cycle becomes a strong calibration object.

---

## 4. Aphek as compact lexical Rosetta

The Aphek-Antipatris trilingual lexicon is especially important because it combines:

```text
Sumerian
Akkadian
Canaanite
```

inside a lexical rather than monumental genre.

That makes it potentially useful for:

- Semitic lexical calibration,
- Canaanite readout,
- Sumerogram-to-Semitic mapping,
- scribal pedagogy,
- cross-language lexical covariance.

It should therefore be separated from large political inscriptions.

---

## 5. Byblos as the low-degree control

The Byblos script corpus has:
- a small number of texts,
- no secure bilingual/trilingual anchor,
- uncertain sign normalization,
- unknown language,
- no accepted decipherment.

So its graph degree is approximately:

```text
degree(Byblos) ≈ 0
```

for secure explicit crosswalks.

This makes it the ideal inverse calibration to Ugarit.

### Ugarit

```text
high crosswalk degree
+ multiple languages
+ multiple genres
+ scribal lexical apparatus
→ low relative decipherment entropy
```

### Byblos

```text
low crosswalk degree
+ small corpus
+ unknown language
+ allograph uncertainty
→ high decipherment entropy
```

---

## 6. New variable — ANCHOR DENSITY

Define:

```text
AD(U) = weighted number of secure anchors per corpus unit
```

Possible anchor weights:

```text
sign equation            highest
pronunciation gloss      very high
lexical equation         high
phrase parallel          high
proposition parallel     medium-high
shared proper name       medium
generic thematic match   low
visual resemblance       very low
```

A high raw number of weak anchors should not outrank a small number of explicit ancient equations.

---

## 7. New variable — CROSSWALK DEGREE

```text
CD(U) = number of historically secure representation states connected to U
```

This must be dependency-corrected.

Ten copies of the same bilingual school list do not equal ten independent crosswalks.

So:

```text
CD_eff
=
independent crosswalk lineages
```

---

## 8. New variable — CROSSWALK DEPTH

Define:

```text
X0 = no explicit crosswalk
X1 = shared context/proper name
X2 = proposition parallel
X3 = phrase/formula parallel
X4 = lexical equation
X5 = sign/value/pronunciation equation
```

This is orthogonal to confidence.

A badly preserved sign equation can be X5 but low-confidence.
A perfectly preserved thematic parallel can be X1 but high-confidence.

---

## 9. New variable — DECIPHERMENT ENTROPY

For target system U:

```text
H_D(U)
```

is not computed yet as a formal Shannon entropy.

It is a typed uncertainty state over:

- sign inventory,
- sign values,
- word boundaries,
- directionality,
- script type,
- language identity,
- morphology,
- syntax,
- semantics.

The goal of each independent crosswalk is:

```text
H_D(U) ↓
```

Rosetta lowered several dimensions at once.

KTU 5.14 lowers sign/pronunciation uncertainty.

Ebla lexical lists lower lexical-address uncertainty.

Hittite logograms lowered semantic uncertainty while leaving language identity initially open.

Byblos currently lacks that kind of entropy-collapse event.

---

## 10. Recursive consequence for prior calibration nodes

### Rosetta
Reclassify as:
```text
high AD
high CD
high X-depth
```

### Behistun
High CD + temporal parallax.

### Tell Fekheriye
Lower CD but excellent phrase-level X-depth.

### KTU 5.14
Very high X-depth at sign/pronunciation level.

### Ebla
Very high X-depth at lexical/readout level.

### Hittite
Initially low external crosswalk density, but internal heterograms + Indo-European covariance progressively lowered entropy.

### Byblos
Low CD / low AD / X0 explicit-crosswalk state.

This makes successful versus unsuccessful decipherment comparable in one framework.

---

## 11. New prediction

If the model is useful, then systems with:

```text
high CD_eff
+ high X-depth
+ enough corpus covariance
```

should be disproportionately easier to decipher than systems lacking those properties.

This prediction can be tested on:
- Egyptian,
- Old Persian,
- Cypro-Syllabic,
- Luwian,
- Phoenician,
- Pyu,
- Maya,
- versus Byblos, Linear A, Indus, Proto-Elamite, etc.

That would turn the Rosetta Nexus into a general decipherment-science framework.

## Governing rule

```text
THE VALUE OF A ROSETTA OBJECT
IS NOT THAT IT IS MULTILINGUAL.

ITS VALUE IS THAT IT ADDS
HIGH-SPECIFICITY EDGES
TO THE DECIPHERMENT GRAPH.
```
