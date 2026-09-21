# First Calibrated Candidate Pass — HSS / QBL / ASIS / Numeral Seven

Status: FIRST PASS FROZEN
Updated: 2026-09-21

Data:
- `registries/calibrated-transform-weights-v0.1.yaml`
- `data/calibration/calibrator-scorecard-v0.1.yaml`
- `data/calibration/candidate-pass-v0.1.yaml`

## Method

This pass separates two questions.

```text
A = ALIGNMENT SUPPORT
How securely do two representations point to the same or corresponding state?

H = HISTORICAL-RELATION SUPPORT
How securely do phonology, morphology, chronology, contact, semantics,
independent witnesses and controls support an actual historical lexical relation?
```

Neither score is a probability.

The weights were frozen before interpreting the candidate family.
They are not retroactively tuned to rescue favored correspondences.

## Calibration basis

| Nexus | A | Primary transform learned |
|---|---:|---|
| Memphis / Rosetta | 0.948 | script/register + semantic address |
| Behistun | 0.925 | temporal/editorial parallax + onomastics |
| Tell Fekheriye | 0.949 | phrase-level operator preservation |
| KTU 5.14 | 0.941 | explicit phonological approximation |
| Ebla lists | 0.918 | sign/readout + lexical equation + copy covariance |

The aggregate mean, 0.936, is descriptive only.
Candidate tests route through the relevant calibrators instead of averaging all witnesses.

---

## HSS / Ear–Understanding–Wisdom lane

### HSS01 — Sumerian semantic address ↔ Akkadian `ḫasīsu`

```text
A = 0.95
H = N/A
STATUS = ANCHORED ALIGNMENT
```

The ancient lexical tradition securely links the Sumerian ear/hearing field with Akkadian
hearing/understanding/wisdom vocabulary.

This is a lexical-equivalence result.
It does not make the Sumerian and Akkadian surface forms cognate.

### HSS02 — Ebla `geštu₃ = ḫa-zi-zu-um` ↔ later Akkadian `ḫasīsu`

```text
A = 0.90
H = 0.73
STATUS = SUPPORTED CANDIDATE
```

This is the strongest new crosswise result from the calibration pass.

Why it rises:
- direct ancient Sumerian–Semitic lexical equation at Ebla,
- semantic identity in the EAR / UNDERSTANDING lane,
- strong Mesopotamian contact and scribal continuity,
- later independent Sumerian–Akkadian lexical alignment.

What remains unresolved:
- exact Eblaite ↔ Akkadian phonological history,
- morphological segmentation,
- status of the z/s correspondence in the relevant lexical family.

Therefore:

```text
ancient crosswalk = strong
specific historical derivation = still to be demonstrated
```

### HSS03 — Akkadian `ḫāsis / ḫasīsu` ↔ Ugaritic `ḫss`

```text
A = 0.71
H = 0.74
STATUS = SUPPORTED CANDIDATE
```

The phonological carrier, wisdom/intelligence semantics, chronology and Ugarit–Akkadian
contact environment all support continued investigation.

Current ceiling is source quality: the Ugaritic lexical interpretation in this pass still relies
on secondary scholarship and should be replaced by a primary grammar/lexicon or direct textual edition.

### HSS04 — deeper `Ḫ-S` kernel beneath `Ḫ-S-S`

```text
A = 0.58
raw H = 0.54
reported H = 0.49
STATUS = LIVE BUT CEILING-LIMITED
```

The calibration system blocks automatic stripping of the final radical.

The kernel remains useful as a discovery hypothesis, but promotion requires:
- attested H-S / H-S-S alternation,
- productive extension/gemination,
- older lower-arity witnesses,
- or recurrent morphology independently licensing the reduction.

---

## QBL orbit

### QBL01 — RECEIVE → QABBALAH / RECEIVED TRADITION

```text
A = 0.94
H = 0.98
STATUS = ANCHORED
```

The lexical receive/transmit pathway is strong and historically distinct from the later chronology
of technical medieval Kabbalah.

This is the calibration anchor for the QBL orbit.

### QBL02 — FACE / CONFRONT → Akkadian `qablu` BATTLE

```text
A = 0.67
H = 0.66
STATUS = SUPPORTED BOUNDARY
```

The semantic operator is coherent:

```text
FACE
-> ENCOUNTER
-> CONFRONT
-> BATTLE
```

But a full comparative Semitic morphological/correspondence demonstration is still needed.

### QBL03 — Akkadian `qablu` MIDDLE / HIPS / WAIST ↔ FACE / RECEIVE orbit

```text
A = 0.43
H = 0.40
STATUS = WEAK / UNRESOLVED
```

This pass deliberately does **not** close the question.

Current dictionaries distinguish the documented Akkadian lexemes, which is evidence that they
are separate lexical nodes in the witnessed language state.

That does not establish that deeper convergence is impossible.

The next discriminating test is therefore:

```text
CENTER / MEDIAN
vs
FACE / INTERFACE / MEETING ZONE
```

using older lexical witnesses, derivational morphology, Sumerographic readout behavior and
comparative Semitic reconstruction.

---

## ASIS carrier

The calibration pass sharply improves the role of ASIS.

It is currently much stronger as a **discovery and false-positive control** than as a historical
etymological carrier.

### Greek `asis` vs onset-stripped Akkadian `ḫāsis`

```text
H = 0.18
NEGATIVE CONTROL
```

### Greek `basis` → ASIS by deleting `b`

```text
H = 0.15
NEGATIVE CONTROL
```

This becomes the canonical arbitrary-onset-stripping failure because the Greek `b` belongs to the
native formation.

### Hebrew `ʿāsīs` vs Akkadian `ḫāsis`

```text
H = 0.22
NEGATIVE CONTROL
```

Restoring the Hebrew initial consonant and native semantic field dissolves the apparent surface match.

### Avestan / Sanskrit ASIS-like comparison

```text
reported H = 0.29
DIRECT COGNACY NOT SUPPORTED IN THIS PASS
```

The specialist Avestan evidence used in this pass does not support the tempting surface equivalence.

### Result

```text
ASIS normalization survives,
but as a DISCOVERY WINDOW rather than an etymology.
```

That is useful: it becomes an adversarial test of whether the pipeline can recover the full native form
after a normalized substring has attracted attention.

---

## Numeral Seven Carrier

Recovered strict carrier:

```text
[SIBILANT] ... [LABIAL]
```

with a broader carrier admitting additional coronal/sibilant and labial classes.

First calibrated pass:

```text
A = 0.61
raw H = 0.52
reported H = 0.49
STATUS = LIVE FEATURE-ENRICHMENT CANDIDATE
```

The ceiling is methodological, not a rejection.

The project already preserved:
- ancestral-node rather than daughter-language counting,
- Sumerian `imin` as a failure,
- strict versus broad carrier classes,
- explicit recognition that contact exposure must be modeled.

What remains before promotion:

```text
freeze 1–10 numeral matrix
-> collapse genealogy
-> model contact
-> frequency-match feature carriers
-> generate null distribution
-> test whether SEVEN is genuinely enriched
```

Until that is done, the observed ordering cannot be called statistically significant.

---

## Crosswise result

The most important methodological outcome is not a single etymology.

It is that the calibration lattice separates four things that previously tended to bleed together:

```text
1. SAME SEMANTIC ADDRESS
2. SAME SURFACE CARRIER
3. ADMISSIBLE HISTORICAL TRANSFORM
4. COMMON HISTORY
```

They are not interchangeable.

The first pass therefore yields:

```text
ANCHOR:
  QBL receive -> qabbalah
  Sumerian ear-field <-> Akkadian hasisu lexical alignment

STRONGEST NEW HISTORICAL CANDIDATES:
  Ebla hazizu lane -> Akkadian hasisu
  Akkadian hasis/hasisu <-> Ugaritic hss

OPEN:
  QBL middle/waist deeper interface hypothesis
  H-S biradical kernel
  numeral-seven enrichment

NEGATIVE / ADVERSARIAL CONTROLS:
  Greek asis
  Greek basis stripped to ASIS
  Hebrew asis
  Avestan/Sanskrit surface collision in this pass

RETAINED HEURISTIC:
  ASIS normalization window
```

This is exactly the desired behavior of the Nexus:
productive candidates survive, weak edges remain visible, and failed edges improve the sieve instead
of disappearing.
