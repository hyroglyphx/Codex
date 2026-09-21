# Evidence Spine and Product-Layer Architecture

Status: **Recovered from supplied September 2026 artifacts + integrated into Codex**

## Core contract

Every surface in the system preserves the same evidentiary contract:

1. exact witness,
2. typed relation,
3. declared transformation,
4. explicit uncertainty,
5. return path to source.

This is the **evidence spine**.

Products are not separate truth systems. They are different views and interaction layers over the same validated records.

## Shared method

```text
WITNESS
  ↓
TYPE
  ↓
ADMIT
  ↓
TEST
  ↓
EXPLAIN
  ↓
RETURN
```

### WITNESS
Preserve source, carrier, layout/context, provenance, and uncertainty.

### TYPE
Name the relation instead of collapsing it into identity.

### ADMIT
Allow only historically, formally, or empirically defensible transformations.

### TEST
Use nulls, controls, independent routes, held-out evidence, genealogical collapse, and withheld prediction.

### EXPLAIN
Expose what is known, inferred, competing, unresolved, or rejected.

### RETURN
Make source, transformation chain, reason trace, and failures reconstructible.

## Product layers

### 1. Nexus Corpus — research memory
Owns witnesses, lexical/script records, transformations, bridge corpora, controls, failures, and unresolved candidates.

### 2. Inference Engine — analysis
Owns typed states, admissibility, transformation cost, proximity, confidence dimensions/ceilings, null tests, genealogy/contact corrections, blind discovery, and reason traces.

### 3. GlyphWalk — reading and pedagogy
Owns complete-text-first guided reading. It exposes:
- complete source,
- normalized value,
- reading/transliteration,
- literal and contextual meaning,
- uncertainty,
- provenance and method notes.

It may change granularity (sign / word / section) but must not hide the complete witness.

### 4. Transposition Atlas — exhibit and comparative research surface
Owns comparative transformations, typed relation panels, multi-language matrices, historical nexus zones, carrier/operator visualizations, controls, and published validation notes.

## Canonical historical state

The language-history engine treats a historical object as a typed transportable state rather than a naked string.

```text
H = (
  carrier,
  grapheme,
  phonology,
  morphology,
  semantic_envelope,
  operator,
  chronology,
  geography,
  witness
)
```

Expanded corpus record:

```text
R = (
  language,
  ancestral_node,
  script,
  exact_form,
  phonology,
  morphology,
  semantic_vector,
  operator,
  date,
  place,
  nexus,
  contact,
  witness,
  status
)
```

The governing kernel remains:

> Do not compare words. Compare typed historical transformations and ask what survives them.

## Distinctions that must never be silently collapsed

```text
carrier != reading != language != semantic address
surface similarity != genealogy
observable proximity != ancestry != borrowing != phonetic identity
graphic persistence != phonetic persistence
historical continuity != whole-word identity
```

## Transformation discipline

Each edge must state its type. Candidate edge types include:

- inheritance
- borrowing
- scribal transport
- translation
- functional equivalence
- parallel readout
- carrier transposition
- phonological transformation
- morphological transformation
- numeric projection
- iconographic continuity
- ritual / institutional transport
- structural analogy
- independent convergence
- later semantic back-projection

A relation may remain a resemblance, analogy, or candidate indefinitely. Promotion is never required.

## Confidence is a vector

A single scalar confidence is insufficient for this domain.

```text
Q = (
  witness,
  reading,
  segmentation,
  phonology,
  semantics,
  chronology,
  relation
)
```

A record can therefore be securely attested but uncertainly segmented, or chronologically secure while the proposed relation remains speculative.

## Closed learning loop

```text
INGEST COMPLETE WITNESS
        ↓
GENERATE TYPED INTERPRETATIONS
        ↓
TEST / SCORE / WITHHOLD
        ↓
TEACH THE REASONING
        ↓
RETURN FAILURES + CORRECTIONS TO CORPUS
        ↓
RE-ANALYZE
```

Failures and negative controls strengthen later analysis instead of disappearing.

## Integration with Codex relay

```text
Nexus Corpus
  ↓ witness / record
Confluence
  ↓ OrganonEvent
Relay Kernel
  ↓ normalized state
Nexus / Inference Engine
  ↓ typed candidate relations
Council + Adversary
  ↓ tests / ablations / controls
Organon
  ↓ WorkPacket
Builder
  ↓
GlyphWalk / Atlas / research outputs
  ↓ ResultPacket
Relay Kernel
  ↓
Corpus correction / promotion / unresolved queue
```

## Immediate implementation target

Freeze a shared witness/comparison record before building additional views.

The first end-to-end test must take **one complete witness** through:
1. source ingestion,
2. record normalization,
3. typed inference,
4. control/null evaluation,
5. GlyphWalk rendering,
6. Atlas comparative rendering,
7. failure/correction return,
8. provenance reconstruction.

This becomes the product-facing counterpart of Δ-001.


## Arity, compression, and multimodal synchronization

The evidence spine now treats representational resolution as a first-class coordinate.

For linguistic/script witnesses, keep separate:

```text
graphic arity
phonological load
root/radical arity
morphological complexity
semantic compression
classifier/context load
```

A one-sign carrier may encode a logogram, one consonant, multiple consonants, a syllable, or another active role. The system must not infer root structure from sign count.

New rule:

```text
spectral order != chronological order
unless independently demonstrated
```

The relay also supports multimodal state records in which sound, sign/seal, number, gesture, sequence and spatial address can converge on one state target.

```text
multimodal agreement -> stronger state constraint
multimodal agreement != proof of hidden substrate
```

Validation can therefore include:
- cross-modal agreement/conflict,
- transformation covariance,
- cycle consistency,
- divergence rate,
- ontology-claim ceiling.

See:
- `studies/arity-compression-spectral-language-sieve.md`
- `studies/multimodal-synchronous-state-harmonics.md`


## Rosetta Nexus calibration objects

Multilingual stelae, tablets, statues, monumental inscriptions, lexical lists, and distributed parallel texts are treated as **calibration objects** rather than merely as examples.

The dedicated registry is:

`registries/rosetta-nexus-calibration.yaml`

### Parallax coordinate

Each witness receives a representation-distance class independent of confidence:

```text
PX0 same occurrence / multiple roles
PX1 same object / script-register shift
PX2 same object / cross-language
PX3 co-located parallel object set
PX4 same text-event / distributed objects
PX5 explicit scribal crosswalk
PX6 archival or recensional relay
PX7 structural control only
```

### Alignment coordinate

Each relation also records the scale at which correspondence is being tested:

```text
G0 sign/grapheme
G1 phoneme/syllable
G2 lexeme/name
G3 phrase/formula
G4 clause/sentence
G5 proposition
G6 section
G7 document/event
```

### Required sieve variables

The shared record may now include:

- nexus ID and object ID,
- carrier class and material substrate,
- object count and co-location,
- spatial layout and reading direction,
- languages, scripts, and registers,
- parallax level,
- alignment granularity,
- crosswalk explicitness,
- parallelism type,
- same-referent / same-proposition / same-lexicalization flags,
- translation-direction status,
- anchor classes such as names, titles, dates, numerals, divine names, legal formulae, repeated formulae, and rare lexemes,
- omission / expansion / reordering,
- damage and completeness,
- transform vectors across script, phonology, morphology, syntax, semantics, register, and institution,
- covariance,
- cycle/path consistency,
- divergence rate,
- residue and conflict,
- negative controls,
- evidence class,
- calibration weight,
- ontology-claim ceiling.

### Calibration rule

```text
explicit ancient crosswalk
>
retrospective resemblance
```

for learning transformation behavior.

A same-object or same-event witness is never flattened automatically into literal translation. The engine preserves divergence at the finest defensible alignment granularity.
