# Prosodic Pace and Recursive Text Construction

Status: ACTIVE CROSS-CORPUS METHOD
Updated: 2026-09-21

## Core distinction

Textual continuity can preserve or alter:
1. lexical meaning,
2. operator sequence,
3. formulaic recurrence,
4. syntactic pacing,
5. prosodic cadence,
6. strict meter.

These must not be collapsed.

```text
meaning preservation != meter preservation
operator preservation != lexical preservation
formula recurrence != identical wording
cadence similarity != shared metrical system
```

## Homeric control

Homer supplies an explicit quantitative metrical baseline:
- long/short syllables,
- dactylic hexameter,
- formulae fitted to metrical slots,
- recurring epithets and phrase-shapes.

A translation may preserve:
- semantic content,
- formula position,
- narrative operator,
while losing:
- quantitative meter,
- foot structure,
- caesura pattern,
- formulaic timing.

This loss is measurable.

## Biblical / scriptural comparison

Hebrew biblical texts should not be forced into Greek dactylic hexameter.

Instead measure:
- parallelism,
- cola,
- repeated openings/closures,
- genealogical reset formulae,
- refrain structures,
- legal/narrative recapitulation,
- clause-length distributions,
- stress/cadence where recoverable,
- syntactic pacing,
- repetition interval.

For each passage define a pace signature:

```text
P(X) = (
  syllable_or_mora_profile,
  clause_lengths,
  cola,
  repetition_positions,
  formula_density,
  pause_boundaries,
  parallelism,
  meter_if_attested
)
```

A translation produces:

```text
P_source --tau--> P_target
```

and the residual can be measured independently of semantic fidelity.

## Recursive textual construction

### Genesis
Creation, genealogy, catastrophe, covenant, and ancestry repeatedly reset the narrative into new ordered states.

### Deuteronomy
Treat as a recapitulative/covenant-renewal text:
```text
prior event/law
→ retelling
→ readdress to a new generation
→ renewed covenantal state
```

It is structurally restart-like, but is not literally a re-performance of Genesis.

### Jubilees / "Little Genesis"
Treat as rewritten scripture:
```text
Genesis + early Exodus
→ chronological re-indexing
→ legal/calendar expansion
→ rewritten narrative
```

Its jubilee/week chronology makes recurrence itself part of the carrier.

## New metric: Pace Residual

For aligned source/target sections:

```text
R_pace = distance(P_source, P_target)
R_sem  = semantic/operator distance
```

This creates four useful quadrants:

1. low R_sem / low R_pace — content and pace both conserved
2. low R_sem / high R_pace — meaning retained, pace lost
3. high R_sem / low R_pace — rhythm retained while content shifts
4. high R_sem / high R_pace — substantial recomposition

## Controls

Ancient Greek meter must be modeled quantitatively, not with English stress templates.

Required controls:
- same-meter unrelated Greek verse,
- shuffled text preserving line length,
- same-length non-metrical prose,
- translation with matched content but different meter,
- translation retaining meter but altering wording.

## Immediate benchmark: PACE-01

Select:
- one Homeric hexameter passage,
- one Hebrew poetic passage,
- one Septuagint rendering,
- one Targumic rendering,
- one Vulgate rendering,
- one Jubilees rewritten parallel where available.

Store:
- exact witness,
- syllable/mora segmentation,
- clause/colon boundaries,
- meter if valid,
- formula positions,
- operator sequence,
- semantic alignment,
- pace residual,
- confidence.

The purpose is not to prove identical meter across traditions. It is to detect which temporal/formulaic constraints survive, disappear, or are regenerated during translation and rewriting.


## Dependency-corrected pace evidence

The numeral and translation-genealogy work adds an important correction.

Several translations or manuscripts may preserve the same pacing feature because they descend from one intermediary.

Therefore:

```text
raw number of pace matches
!=
number of independent pace witnesses
```

Add:

```text
D_pace = dependency graph among witnesses
N_eff  = effective independent pace witnesses
```

For every apparent cross-language cadence survival, ask:

1. direct from source?
2. mediated through an earlier translation?
3. copied from a shared recension?
4. independently regenerated from the same source structure?
5. target-language formula imposed by convention?

### Revised pace confidence

```text
PACE_SUPPORT
=
pace_similarity
× witness_independence
× source_alignment
× native-meter_or_formula_fit
```

This prevents ten descendant translations of one Latin rendering from outweighing one genuinely independent Syriac or Greek witness.

## Prediction test

The Hittite decipherment calibration adds:

```text
prediction > recognition
```

Apply this to pace.

A proposed pacing rule should predict:
- formula placement,
- pause boundaries,
- recurrence positions,
- line/colon lengths,
- or target-language restructuring

outside the passage that generated the hypothesis.

If it only explains one hand-picked passage, retain it as descriptive rather than structural.

## Operator order

For pace comparison, use:

```text
freeze witness
→ establish dependency
→ identify language-native prosody
→ segment syntax/cola
→ align semantic operators
→ calculate pace residual
```

Do not impose an English stress template before establishing the native prosodic system.
