# Positive–Negative Decipherment Experiment — Ugarit vs Byblos

Status: FIRST COMPARATIVE PASS COMPLETE
Updated: 2026-09-22

Inputs:
- `data/calibration/byblos-sequence-graph-v0.1.json`
- `data/calibration/ugarit-multilingual-cycle-consistency-v0.1.yaml`
- `studies/byblos-script-undeciphered-negative-calibration.md`
- `studies/multilingual-anchor-density-decipherment-entropy.md`

## Experimental question

What changes when two ancient writing environments have superficially similar ingredients — cuneiform-adjacent scribal cultures, small specialist corpora, repeated signs — but radically different crosswalk structure?

The comparison is:

```text
UGARIT
= high crosswalk degree
+ multiple languages
+ alphabetic and syllabic encodings
+ lexical equations
+ pronunciation scaffold
+ repeated polyglot copies

BYBLOS
= low crosswalk degree
+ unknown language
+ no secure bilingual
+ uncertain allograph normalization
+ small corpus
```

This is not a ranking of civilizations or scripts.
It is a calibration of evidence geometry.

---

## 1. Byblos sequence graph

For v0.1, only Dunand-coded tokens from tablet c were admitted to the training graph.

Known coded tokens:

```text
224
```

Observed catalogue nodes:

```text
52
```

Unique directed bigram edges:

```text
161
```

Token-distribution entropy:

```text
5.180429 bits
```

The public transcription exposes 224 coded tokens while secondary corpus descriptions often call the tablet 225 characters long.

The discrepancy is preserved rather than silently "fixed."

### High-frequency training nodes

```text
E7   19
D3   14
G8   13
G17  11
E14  10
E8   10
B11   8
E19   8
```

### Strong repeated local structures

```text
G13 → B11 → A10
```

occurs five times.

```text
G13 → B11 → A10 → G17 → E22
```

occurs three times.

A longer twelve-sign sequence:

```text
E1 → G8 → D1 → B9 → B3 → D3 → A3
→ G13 → B11 → A10 → G17 → E22
```

occurs twice.

The final training line contains a sevenfold E19 run after G17.

These are **structural observations only**.

They are not words, numerals, names, or grammatical morphemes until independent evidence establishes such a function.

---

## 2. Boundary candidate

E22 occurs at five line endings in tablet c.

That makes E22 a candidate for testing boundary-conditioned behavior.

It does **not** mean:

```text
E22 = punctuation
```

or:
```text
E22 = grammatical ending
```

The prediction is merely:

> if E22 has a true boundary-related function, its line/phrase-final enrichment should persist beyond tablet c.

This is exactly the kind of prediction the validation/holdout design can test.

---

## 3. Holdout discipline

Training:

```text
tablet c
```

Non-blind validation:

```text
tablet d
```

Blind holdout:

```text
spatula i
```

The spatula sequence remains uninspected for model tuning.

Before it is opened, v0.1 freezes:

- graph construction,
- catalogue-sign treatment,
- variant non-collapse,
- boundary candidate E22,
- recurrent sequence inventory,
- no phonetic assignments.

Any future reading proposal must therefore predict the holdout rather than reinterpret it after inspection.

---

## 4. Ugarit cycle graph

Ugarit supplies the opposite evidence geometry.

Specialist sources document:
- alphabetic Ugaritic,
- syllabically written Ugaritic,
- Akkadian,
- Hurrian,
- Sumerian,
- additional Hittite/Luwian archive states,
- polyglot lexical tables,
- KTU 5.14 pronunciation equivalences.

The first graph contains these key states:

```text
SUMERIAN syllabic/logographic
        ↕
AKKADIAN syllabic
        ↕
HURRIAN syllabic
        ↕
UGARITIC syllabic
        ↕
UGARITIC alphabetic
```

The important point is that some paths encode **semantic equivalence**, while others encode **sound/script correspondence**.

They therefore provide partially independent constraints.

---

## 5. Anchored lexical cycle — bnš / bunušu

An especially useful cycle is:

```text
alphabetic Ugaritic bnš
        ↓
syllabic Ugaritic bu-nu-šu
        ↓
Akkadian a-mi-lu
        ↓
semantic address MAN
        ↓
alphabetic Ugaritic bnš
```

CDLI RS 20.149 directly preserves the Akkadian/Hurrian/Ugaritic lexical row, including Ugaritic `bu-nu-šu`.

Specialist Ugaritic grammars independently connect the alphabetic form `bnš` with syllabic `bu-nu-šu`.

So the loop crosses:

```text
script
→ phonological explicitness
→ lexical equivalence
→ semantics
→ script
```

without requiring any one representation to carry every coordinate.

This is a genuine cycle-consistency calibration object.

---

## 6. Cross-granularity cycle

KTU 5.14 adds another route:

```text
Ugaritic alphabetic consonant
→ Akkadian syllabic pronunciation approximation
```

while the polyglot vocabularies provide fully vocalized Ugaritic words in syllabic cuneiform.

The combined structure is:

```text
alphabetic Ugaritic
→ sign-level syllabic approximation
→ syllabic Ugaritic lexical forms
→ alphabetic Ugaritic lexical forms
```

This cycle is **multiscale** rather than line-for-line.

It tests whether independently transmitted sound and lexical constraints are mutually compatible.

---

## 7. Copy covariance

Specialist grammar literature reports eight copies of a Sumerian–Akkadian–Hurrian–Ugaritic vocabulary.

That changes the statistical treatment.

The eight copies are:

```text
one scribal covariance family
```

not eight independent confirmations.

But their differences are useful.

They can measure:
- orthographic variation,
- omission,
- damage,
- lexical replacement,
- column loss,
- copying stability.

This is the same dependency correction already used in the numeral-seven and translation-genealogy work.

---

## 8. Positive–negative contrast

### Ugarit

When one edge is uncertain, other graph paths can constrain it.

```text
EDGE UNCERTAIN
→ alternate route
→ cycle residual
→ accept / revise
```

### Byblos

There is currently no comparable external cycle.

So:

```text
EDGE GUESS
→ no external closure path
→ high value-assignment entropy
```

That is why a superficially plausible Byblos reading must remain weak until it predicts unused text.

---

## 9. New general law

The experiment suggests:

```text
DECIPHERMENT POWER
does not scale simply with
NUMBER OF SIGNS
or
NUMBER OF LANGUAGES.
```

It scales with the ability to form **independent constraint cycles**.

Define:

```text
CYCLE RANK
= number of nonredundant representation paths
  that return to a compatible state
```

A high-degree graph with no independent cycle may still be fragile.

A smaller graph with a sign-level and lexical-level independent loop can be extremely powerful.

Thus extend:

```text
DECIPHERMENT ENTROPY
↓ as
CYCLE RANK
↑
```

subject to dependency correction.

---

## 10. Immediate testable predictions

### Byblos

The frozen graph predicts:
1. E22 should show unusual boundary behavior outside tablet c if its training enrichment is structural.
2. The long recurrent E1…E22 sequence should appear as a reusable formula or fail cleanly outside training.
3. Prime-marked sign variants should exhibit compatible adjacency distributions if they are true allographs.
4. High-degree nodes such as E7 should remain distributionally broad across held-out material if they encode common syllabic/grammatical functions.
5. A proposed decipherment that destroys these graph regularities should lose score.

### Ugarit

The graph predicts:
1. syllabic Ugaritic forms should constrain vowels hidden by alphabetic Ugaritic;
2. KTU 5.14 sound-class approximations should not conflict systematically with syllabic lexical spellings;
3. lexical rows surviving in multiple polyglot copies should close semantically across Sumerian/Akkadian/Hurrian/Ugaritic paths;
4. copy divergence should cluster in identifiable orthographic/damage/lexical dimensions rather than random contradiction.

---

## 11. Consequence for the Nexus

The previous slogan:

```text
prediction > recognition
```

can now be sharpened:

```text
PREDICTION
+
INDEPENDENT CYCLE CLOSURE
>
POST-HOC READING
```

That becomes the governing standard for undeciphered-script work.

## Current result

```text
BYBLOS:
structure detected,
reading withheld.

UGARIT:
multiple historical crosswalks,
cycle testing available.

EXPERIMENT:
the difference is not intelligence or imagination;
it is constraint geometry.
```
