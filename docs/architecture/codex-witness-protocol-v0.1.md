# Codex Witness Protocol v0.1

Status: active design protocol
Updated: 2026-09-22

## Purpose

Codex treats a manuscript, tablet, inscription, monument, reconstruction, image, ritual sequence, or later copy as a **witness-bearing carrier**, not as a conclusion. The protocol preserves what is seen, what is read, what is inferred, and what remains unresolved as separate states.

Core rule:

```
WITNESS -> OBSERVATION -> STRUCTURE -> READING -> INTERPRETATION
        -> EXTERNAL TEST -> PROMOTION / FAILURE / Ω
```

Every arrow is typed and reversible to provenance.

## Why this exists

The working corpus now needs to survive six distinct stress conditions:

1. **Bruce / Askew codices** — heterogeneous works, strata, recensions, ritual/cosmological material, and multiple voices must coexist without forced harmonization.
2. **Rohonc Codex** — structural analysis must remain useful when script/language/semantics are unresolved.
3. **Byblos** — sparse-script inference must separate recurrence, position, graph structure, and candidate readings from decipherment claims.
4. **Esagila witnesses** — text can encode location, institution, construction, measure, and spatial relation; text-to-geometry must preserve each inferential step.
5. **Borsippa witnesses** — restoration, rebuilding, copying, archaizing, and claims about earlier foundations require a transformation genealogy rather than a single timeless monument state.
6. **Knowledge-preservation traditions (Enoch/Seth/Hermes controls)** — stories about knowledge moving across pillars, tablets, inscriptions, books, languages, and generations are useful models for carrier-change and custody, while historical dependence remains separately typed.

## State model

```
CodexState = (
  witness,
  carrier,
  position,
  sequence,
  layer,
  relation,
  reading,
  interpretation,
  measure,
  geometry,
  transformation,
  time,
  provenance,
  confidence
)
```

No field is allowed to silently substitute for another.

### Required separations

- carrier != reading
- reading != language
- literal gloss != contextual translation
- textual claim != historical fact
- measurement claim != metrological interpretation
- metrological interpretation != geometric reconstruction
- restoration claim != demonstrated continuity
- recurrence != decipherment
- resemblance != transmission
- structural analogy != genealogy

## Codex Witness object

Minimum schema:

```yaml
id:
witness_type:
carrier:
date_or_phase:
location_or_address:
source:
observations: []
readings: []
relations: []
uncertainties: []
transformations: []
reconstructions: []
provenance: []
promotion_state:
```

`Ω` is a valid value. Unresolved material must remain queryable rather than being coerced into a reading.

## Transformation vocabulary

The first manuscript/material operators are:

- COPY
- TRANSLATE
- TRANSLITERATE
- RECOMPOSE
- REDACT
- REORDER
- ABBREVIATE
- EXPAND
- REPAIR
- RESTORE
- REBUILD
- RECONSTRUCT
- ARCHAIZE
- REUSE
- RELOCATE
- REINTERPRET
- DEPICT
- MEASURE
- DESCRIBE
- CORROBORATE
- CONTRADICT
- PREDICT
- UNKNOWN_RELATION

These operators describe the edge, not the researcher's preferred conclusion.

## Text -> geometry pipeline

For architectural witnesses:

```
W = textual/material witness
C = explicit claim
M = metrological interpretation
G = geometric reconstruction

W -> C -> M -> G
```

Changing M must invalidate or mark stale every dependent G. A reconstruction therefore remains recomputable.

## Restoration genealogy

A monument is represented as a temporal graph:

```
state(t0)
 -> damage/change
 -> remembered/claimed prior state
 -> restoration or rebuilding(t1)
 -> later witness
 -> reconstruction(t2)
```

Royal, priestly, scribal, antiquarian, or modern claims about prior states are stored as claims with provenance until independently supported.

## Structure-before-semantics mode

For undeciphered or poorly understood material, the protocol permits:

```
glyph -> sequence -> recurrence -> positional role -> graph relation -> Ω
```

No lexical or linguistic assignment is required. Candidate readings must make prospective predictions before promotion.

## Plural-strata mode

Multiple readings can branch from one witness:

```
                     -> Reading A -> Interpretation A
Witness -> Structure -> Reading B -> Interpretation B
                     -> Ω
```

Contradictory branches remain first-class records. Later evidence may promote, merge, supersede, or reject them without deleting their genealogy.

## Carrier topology

Codicological/material topology is evidence. Record when available:

- page/tablet/face/column/line
- adjacency and recurrence
- marginalia/corrections
- scribal or graphic hand changes
- diagrams and image-text relations
- section boundaries
- lacunae/damage
- architectural placement
- foundation/deposition context
- route/orientation
- later relocation or reuse

The carrier itself participates in the state.

## GlyphWalk integration

GlyphWalk is the human-facing witness reader. It should expose:

1. complete source,
2. normalized sign/value,
3. reading/transliteration,
4. literal meaning,
5. contextual translation,
6. uncertainty/alternatives,
7. provenance,
8. CodexState relations,
9. dependent reconstructions.

The interface must never hide unreadable material merely to produce a clean translation.

## Organon / Invariant Forge integration

Organon traverses the Witness-Transformation Graph and asks:

> What survives the declared transformations?

Output categories:

- stable carrier
- stable relation
- stable measure
- stable name/title
- stable function
- changed classifier
- changed readout
- changed geometry
- information loss
- contradiction
- unresolved Ω
- candidate invariant

Invariant Forge promotes only after independent witnesses and adversarial tests.

## TCIM / Nexus compatibility

This protocol extends the existing rule:

> Do not compare words. Compare typed historical transformations and ask what survives them.

Nexus handles carrier/readout/operator transport. Codex Witness Protocol generalizes the same discipline to manuscripts, monuments, reconstructions, ritual sequences, and material history.

## Initial benchmark suite

| Benchmark | Failure mode tested | Required behavior |
|---|---|---|
| Bruce Codex | heterogeneous textual strata | preserve layers/works/voices |
| Askew Codex | recension and ritual-cosmological complexity | branch readings without flattening |
| Rohonc Codex | unresolved script/language | structure-before-semantics + Ω |
| Byblos corpus | sparse undeciphered script | train/validation/holdout discipline |
| Esagila | text-to-space inference | W -> C -> M -> G provenance |
| Borsippa | restoration genealogy | temporal monument graph |
| Enoch/Seth/Hermes preservation motif | carrier/custody transposition | distinguish motif continuity from historical dependence |

## Promotion rule

A candidate may rise only when its predicted consequences survive independent witness checks. Retrospective explanatory fit alone is insufficient.

The protocol therefore treats a codex not as a collection of conclusions, but as a **recoverable field of witnesses, relations, transformations, uncertainty, and return paths**.
