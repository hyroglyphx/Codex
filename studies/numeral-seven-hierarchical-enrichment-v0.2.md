# Numeral Seven — Hierarchical Enrichment Study v0.2

Status: ACTIVE / DEPENDENCY-SENSITIVE
Updated: 2026-09-21

Data:
- `data/calibration/numeral-1-10-source-locked-v0.2.yaml`
- `data/calibration/numeral-hierarchical-null-v0.2.yaml`

## 1. What changed from v0.1

The first pilot only covered digits 3–10 across a small set of nodes.

Version 0.2 does four things:

1. extends the matrix to **1–10**;
2. separates **root/stem-normalized** forms from inflected surface forms;
3. adds **Proto-Kartvelian, Uralic branch controls, Hurrian, Etruscan, Basque, and Iberian**;
4. replaces a flat node-counting model with **genealogy/contact dependency scenarios**.

The target feature remains frozen:

```text
STRICT C7
= sibilant / affricated-sibilant onset
  followed later by
  [p, b, f, φ, β, w]
```

No consonant class was added after seeing the expanded matrix.

---

## 2. Morphology correction matters

The most important correction from v0.1 is Egyptian.

If surface numeral forms are counted literally, transparent final `-w` morphology can create extra
sibilant + labial matches.

Therefore the primary lane is now:

```text
ROOT / STEM NORMALIZED
```

rather than raw written surface form.

Under this lane:

```text
Egyptian 7 sfḫ
= strict hit

Egyptian 6 sjs
= not a strict hit

Egyptian 2 sn
= not a strict hit
```

This removes two false positive surface hits without affecting seven.

That is an important successful application of the Arity–Compression / morphology sieve.

---

## 3. Uralic correction

The older project state treated "Proto-Uralic seven" as a broad sibilant + nasal/labial-type node.

Version 0.2 corrects this.

The evidence is better represented as:

```text
Finno-Permic seven
= broad-only branch control

Ugric seven
= strict-looking branch control
  but explicitly contact-sensitive / Iranian-derived in the cited reconstruction tradition
```

Therefore neither is counted as an independent whole-family Proto-Uralic hit.

This reduces apparent independence and improves the genealogy model.

---

## 4. Source-locked matrix result

### Core high-confidence lane

Counted nodes:

- Proto-Semitic
- Egyptian
- Proto-Indo-European
- Sumerian
- Proto-Kartvelian
- Hurrian
- Basque

Root/stem-normalized strict hits:

```text
digit 1   0
digit 2   0
digit 3   0
digit 4   0
digit 5   0
digit 6   1
digit 7   5
digit 8   0
digit 9   0
digit 10  0
```

### Extended candidate lane

Add:
- Etruscan
- Iberian

Then:

```text
digit 6   1
digit 7   7
all other digits 0
```

The extended lane is not treated as equal-confidence evidence because some Etruscan assignments
and the Iberian numeral identifications remain less secure than the core historical/reconstructed nodes.

---

## 5. Dependency scenarios

The exact conditional null preserves each node or dependency-cluster's observed number of hits and
randomizes only the digit positions.

It therefore asks:

> If these historical units had the same number of carrier-like forms, how surprising is it that
> they overlap on the same digit?

It does **not** yet model actual phonotactic generation.

### S0 — naive core row independence

Observed:
- seven receives five hits
- six receives one

Exact look-elsewhere probability:

```text
P(any digit reaches 5 hits) = 0.0002
```

This looks striking but is anti-conservative because it assumes node independence.

### S1 — genealogy/contact clustered

Collapse:

```text
Proto-Semitic + Egyptian
→ Afroasiatic cluster

PIE + Proto-Kartvelian
→ IE/Kartvelian contact-sensitive cluster

Basque + Iberian
→ Vasco-Iberian comparison cluster

Etruscan
→ separate
```

Seven is shared across all four effective clusters.

Exact look-elsewhere probability:

```text
P(any digit reaches all 4 clusters) = 0.002
```

Still strongly concentrated under this specific dependency model.

### S2 — more conservative Mediterranean contact collapse

Collapse Etruscan into the western Afroasiatic/Mediterranean-sensitive cluster:

```text
A = Semitic + Egyptian + Etruscan
B = PIE + Kartvelian
C = Basque + Iberian
```

Seven overlaps all three.

```text
P(any digit reaches all 3 clusters) = 0.02
```

Suggestive.

### S3 — maximal western areal collapse

Treat:

```text
Semitic + Egyptian + Etruscan + Basque + Iberian
```

as one intentionally over-conservative effective observation, with:

```text
PIE + Kartvelian
```

as the second.

Then seven overlaps two effective units.

```text
P(any digit reaches both units) = 0.20
```

Under this extreme collapse the enrichment is not unusual.

---

## 6. The actual uncertainty is now historical dependence

The result is no longer best summarized as:

```text
"Does seven look unusual?"
```

It does.

The decisive question is:

```text
HOW MANY HISTORICALLY INDEPENDENT SEVEN HITS ARE THERE?
```

That is a better problem.

The signal ranges from:

```text
very strong
→ moderate
→ weak
```

depending on how aggressively historically plausible contact/genealogy edges are collapsed.

This means the next major variable is not phonetic resemblance.

It is **historical covariance**.

---

## 7. Matched feature controls

To test feature-selection bias, the same root-normalized matrix was examined with the sibilant-onset
condition held constant while the later segment class changed.

### Strict labial target

```text
6 → 1
7 → 7
```

### Broad labial

```text
3 → 1
6 → 1
7 → 7
```

### Dorsal

```text
6 → 1
7 → 1
```

### Nasal

```text
2 → 1
3 → 1
7 → 2
```

### Rhotic

```text
8 → 2
10 → 1
```

None of these simple alternatives recreates the same seven concentration.

That is encouraging.

But it is not a full feature-selection correction because:
- the alternative classes were not preregistered;
- segment-class base rates differ by language;
- the strict C7 feature itself emerged from prior exploratory work.

---

## 8. Contact-sensitive nodes now become evidence, not contamination

Several nodes are especially valuable because their **dependence** is itself informative.

### Proto-Kartvelian

The reconstruction tradition explicitly discusses Indo-European influence/borrowing for some numerals.
Therefore its seven hit may be:
- inherited Kartvelian,
- borrowed,
- areally reinforced,
- or convergent.

Its value is not lost; its edge type changes.

### Ugric

The strict-looking seven form is treated as Iranian-derived in the cited Uralic tradition.

That makes it a **positive borrowing control**:

```text
a seven carrier can move across language-family boundaries by contact
```

which is directly relevant to interpreting PIE/Semitic and Mediterranean patterns.

### Basque / Iberian

Their relation must remain dependency-sensitive because the Iberian numeral identifications are
partly motivated by Vasco-Iberian comparison.

Counting both as automatically independent would double-count the hypothesis.

---

## 9. Current C7 status

The appropriate project status is:

```text
C7 = SOURCE-STRENGTHENED FEATURE ENRICHMENT
     + DEPENDENCY-SENSITIVE
     + NOT YET PROMOTED TO COMMON ORIGIN
```

The evidence now supports:

```text
seven is unusually concentrated under the frozen carrier
```

more strongly than before.

It does **not** yet support:

```text
all seven forms descend from one ancestral word
```

or:

```text
one historical diffusion path explains every hit
```

The plausible model space remains:

```text
deep inheritance
+ contact diffusion
+ branch borrowing
+ independent convergence
```

with mixture models likely more realistic than any one-process explanation.

---

## 10. Next model

The next null should generate numeral forms through a historical graph rather than merely randomizing
digit positions.

Required parameters:

```text
GENEALOGY TREE
CONTACT EDGES
BORROWING RATE
PHONOTACTIC INVENTORY
RECONSTRUCTION UNCERTAINTY
VALUE-ASSIGNMENT UNCERTAINTY
MISSINGNESS
FEATURE-SELECTION PRIOR
```

Then perform:

```text
simulate numeral systems
→ propagate inheritance
→ allow contact borrowing
→ apply phonological change
→ score frozen carrier
→ compare observed seven enrichment
```

That would finally test whether the observed concentration is unusual **given the kinds of historical
processes actually capable of creating it**.

## Current conclusion

Version 0.2 strengthens the numeral-seven phenomenon while simultaneously making the claim more precise.

The strongest current statement is:

> After morphology normalization, genealogy collapse, branch correction, negative controls, and
> contact-sensitive modeling, numeral seven remains the strongest concentration of the frozen
> sibilant-plus-labial carrier in the current source-locked comparison set; the strength of that
> enrichment depends strongly on how historical dependence among the participating nodes is modeled.

That is a testable result.
