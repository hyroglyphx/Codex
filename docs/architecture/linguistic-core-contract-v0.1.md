# Linguistic Core Contract v0.1

Status: CANONICAL_ARCHITECTURAL_CONSTRAINT
Date: 2026-09-22

## Principle

Codex treats linguistic transformation as a core analytical substrate, not a downstream example domain.

The project kernel must preserve the distinction among:
- carrier/script;
- phonological form;
- graphemic form;
- morphology;
- syntax;
- semantic function;
- register;
- historical phase;
- geography/contact field;
- provenance/witness;
- culture-specific numeric encoding when historically licensed.

Core comparative rule:

> Do not compare words. Compare typed historical transformations and ask what survives them.

## Typed linguistic state

For linguistic and textual objects, the minimum state is:

```
L = (carrier, grapheme, phonology, morphology, syntax, semantics,
     role, location, time, classifier, provenance)
```

Optional historically licensed channels include numeric value, prosody/meter, embodied idiom, onomastic role, and scribal readout.

This is compatible with TCIM's typed state and the broader Structural Continuation state. No compression step may erase stem/ending, language/script, inherited/borrowed, source/translation, or attested/reconstructed distinctions.

## Rosetta triangulation

The project's preferred positive calibration is redundant independent witness:

```
Witness A --T_a--> I
Witness B --T_b--> I
Witness C --T_c--> I
```

The invariant I is promoted only to the level supported by the transformations and witnesses. Rosetta/Memphis, Behistun, Tell Fekheriye, Karatepe/Cinekoy, Letoon, Pyrgi, Ebla lexical lists, Ugaritic multilingual material, and related nexus objects provide controls for real historical representation change.

## Independence and ancestry

Count ancestral/transmission nodes, not modern daughter languages, when assessing comparative independence.

Every proposed edge must be typed, including:
- inheritance;
- borrowing/calque;
- parallel-law convergence;
- contact restructuring;
- replacement;
- carrier erosion;
- analogy;
- script/mode transposition;
- readout transposition;
- translation;
- recension/recomposition;
- classifier transfer;
- candidate resemblance.

Unlabeled resemblance arrows are inadmissible.

## ECVR / admissibility

A candidate relation should be evaluated jointly against historically relevant channels:

```
P(x) phonology
G(x) graphemic form
M(x) morphology
S(x) semantic function
L(x) location/contact
T(x) chronology
K(x) script/register/classifier
W(x) witness/provenance
N_c(x) culture-specific numeric value, only when independently licensed
```

Numeric agreement is supporting evidence only under the historically appropriate value system and chronology.

## Transformation spine

Linguistic work feeds the central Codex pipeline:

```
WITNESS
-> NORMALIZE WITHOUT FLATTENING
-> TYPE CARRIER/LANGUAGE/SCRIPT
-> DECLARE TRANSFORMATION
-> ALIGN
-> TRACK LOSSES/GAINS
-> EXTRACT CANDIDATE INVARIANT
-> TEST AGAINST INDEPENDENT WITNESSES
-> NULL / HOLDOUT
-> RETURN TO SOURCE
```

## Required controls

1. Stem versus ending must remain separable.
2. Semantic similarity cannot substitute for regular sound correspondence.
3. Graphic similarity cannot substitute for phonological or historical linkage.
4. Translation equivalence cannot be silently recoded as etymology.
5. Syncretism is graph merging, not automatically ancestry.
6. Exonym, title transfer, taboo replacement, functional equivalence, and visual resemblance remain distinct operators.
7. Spatial comparison must respect chronology and, where relevant, coordinate/precession changes.
8. Ancient alphanumeric systems remain culture-specific unless a transmission mechanism is independently supported.
9. Undeciphered scripts retain Ω where the crosswalk is insufficient.
10. At least three genuinely independent witnesses are preferred before promoting broad cross-domain relations.

## Integration obligations

The following are core dependencies, not optional side modules:
- language-coverage-registry;
- translation-transposition-bridges;
- Rosetta Nexus calibration;
- adjacent-language lattice;
- numeral source-lock and hierarchical-null work;
- ECVR/TCIM comparative operators;
- scriptural/textual transmission spine;
- decipherment benchmarks;
- prosodic, referential, root/operator, arity-compression, and multimodal language transforms.

Every future Organon experiment involving historical symbols, names, texts, scripts, etymologies, translations, divine names, numerals, or encoded language must route through this linguistic core before cross-domain promotion.

## Cross-language disambiguation / backprojection

When the same referent is independently attested in multiple contemporary or near-contemporary languages, those external forms should constrain ambiguous readings in the receiving language.

Canonical model:

```text
REFERENT R
  -> source-language form L1
  -> neighboring-language form L2
  -> imperial/administrative form L3
  -> Greek form G
```

Do not evaluate `G` in isolation when `L1/L2/L3` exist.

Instead infer the transformation envelope:

```text
G ~ T(L1,L2,L3)
```

where `T` includes only historically observed adaptations:
- cluster simplification;
- epenthesis/vowel insertion;
- consonant substitution within target phonology;
- loss of sounds unavailable in the receiving language;
- case/declensional accommodation;
- metathesis only when independently licensed;
- scribal/transliteration conventions.

Example positive control:

```text
Lydian Śfard / Śfarvad
Old Persian Sparda
Hebrew/West-Semitic Sepharad
Greek Sardis
```

The convergence of independent external forms strongly constrains the Greek reading and shows that Greek `Sar-` can be a receiving-language outcome of a denser `Sf-/Sp-` onset.

Therefore:

```text
MULTILINGUAL_CONVERGENCE
> SINGLE-LANGUAGE ETYMOLOGICAL AMBIGUITY
```

for identifying the historical carrier and admissible transformation class.

This does not mean every external form is equally independent. Genealogy, borrowing, scribal dependence, chronology, and referent identity must still be typed.

### Manuscript-emendation rule

When a Greek manuscript reading is disputed, seek external-language forms of the same person, family, place, title, or office before preferring an editorial emendation.

```text
TRANSMITTED_GREEK
vs
EDITORIAL_EMENDATION
```

should be tested against:

```text
external onomastic witnesses
+ local-language inscriptions
+ imperial administrative forms
+ bilingual/trilingual monuments
```

If these converge on one consonantal/phonological architecture, they materially reduce the ambiguity.

Absence of such external witnesses leaves the ambiguity open; it does not authorize replacing the transmitted form by editorial preference alone.


## Same-referent micro-calibrations: NEI/NI and KA/CA

Two ancient names in Solon's Egypt verse provide compact controls for cross-script comparison:

```text
Greek Νεῖλος / Neilos -> Latin Nīlus
Greek Κάνωβος / Κάνωπος -> Latin Canopus
```

Use these only at the level they demonstrate:

- `NEI -> NI`: same-referent Greek-to-Latin vowel/readout compression in the Nile name;
- `K -> C`: ordinary Greek-kappa to Latin-C orthographic adaptation in Canopus;
- `-b-/-p-`: an internally attested Greek variant in the Canopus carrier.

These controls license carrier flexibility without licensing unrelated consonant substitutions.

General rule:

```text
PROMOTE A TRANSPOSITION
ONLY TO THE LEVEL DEMONSTRATED BY SAME-REFERENT WITNESSES
```


## DIA-01 — Stage-specific pronunciation

For diachronic carrier comparison:

```text
MODERN PRONUNCIATION != HISTORICAL CARRIER BASELINE
```

Require, where available:

```text
SOURCE FORM
-> INTERMEDIATE ORTHOGRAPHIC FORMS
-> INTERMEDIATE PHONOLOGICAL STATES
-> MODERN FORM
```

Do not use a modern pronunciation either to establish or reject an ancient phonemic relationship when the language has undergone substantial regular sound change. French `oi -> /wa/` and widespread final-consonant loss are canonical controls.


## DIA-02 — Diachronic phonemic convergence

Different historical carriers may become more similar through independent sound change:

```text
A_old != B_old
A_old -> A_late
B_old -> B_late
A_late ~ B_late
```

Therefore:

```text
LATE PHONEMIC PROXIMITY
!=
COMMON ORIGIN
```

but it is valid evidence for later reception, punning, folk association, or semantic attraction.

Canonical exploratory control:

```text
Tricasses -> Trecae / Treies / Troyes
Θρᾴκη -> Thracia / Threcia / Threce
```
