# Linguard Admissibility Recovery v0.1

Status: ADOPTED_LEGACY_RECOVERY  
Date: 2026-09-23  
Source family: Linguard Admissibility Corpus + Comparative Vocabulary Corpus  
Scope: Linguistic Core / ASL / Nexus / ECVR / TCIM

## Purpose

Recover high-value linguistic controls from the August–September 2026 Linguard corpus that are not yet explicit in the current Codex architecture.

This supplement does not replace ASL-W4.3. It sharpens the discovery and witness layers beneath W4.3's path-specific promotion rules.

## 1. Full-form priority

The complete historical form remains the primary comparison object.

```
FULL_FORM
!= ROOT
!= SKELETON
!= WINDOW
!= NORMALIZED_FORM
```

A later segmentation or root analysis may add structure, but it may not overwrite the attested form.

## 2. Open segmentation

Do not privilege a favored cut before evidence.

For a form X, generate bounded overlapping windows:

```
WIN2, WIN3, WIN4, WIN5, ...
```

Windows are discovery objects, not etymologies.

A segmentation earns promotion only through independent support from morphology, historical phonology, scribal practice, recurrence, or context.

## 3. Discovery / verification split

Discovery maximizes candidate generation.

Verification applies:
- chronology;
- provenance;
- regular sound change;
- morphology;
- syntax;
- contact;
- null models;
- alternative segmentations;
- witness independence.

```
DISCOVERY freedom
!=
PROMOTION freedom
```

## 4. Chronology as claim-specific cost

Chronological distance does not erase a structural comparison.

But for a historical relation type whose path requires chronology, a failed chronological gate blocks that promotion.

Therefore:

```
chronology may permit STRUCTURAL_COMPARISON
while blocking HISTORICAL_TRANSMISSION
```

This reconciles Linguard's "cost, not veto" search rule with ASL-W4.3's mandatory T dimension for historical promotion paths.

## 5. No deed-transfer model

Cultural and linguistic transport is not restricted to one clean A -> B handoff.

Allowed configurations include:
- bilingual contact;
- bidirectional borrowing;
- layered transmission;
- institutional custody;
- regional diffusion;
- scribal transmission;
- recurrent reanalysis;
- independent convergence.

Each route remains separately typed.

## 6. Carrier loss is information

A receiving language or script may collapse distinctions.

Examples of carrier-loss dimensions include:
- phoneme mergers;
- weak-consonant loss;
- vowel neutralization;
- orientation loss;
- morphology hidden by script;
- semantic narrowing.

The lost distinction must be recorded rather than normalized away.

Add:

```
LOSS_RECORD = preserved + merged + deleted + added + uncertain
```

## 7. Foreign-phoneme approximation

When a receiving language lacks a source phoneme, approximation must be modeled through the receiving inventory and phonotactics rather than free substitution.

Every approximation edge should record:

```
source_feature
receiver_inventory
repair_strategy
resulting_form
confidence
```

## 8. Semantic envelope

A one-word gloss is an index, not the historical object.

Store the attested semantic range before selecting a comparison sense.

```
SEMANTIC_ENVELOPE
-> context-selected sense
```

not:

```
English gloss -> assumed lexical identity
```

## 9. Administrative / deictic semantics

Ethnonyms, territorial labels, and jurisdictional terms may originate inside systems of:
- tribute;
- taxation;
- land;
- allegiance;
- service;
- warfare;
- debt;
- administration.

For each such label, ask:

```
who named whom?
from which center?
for which institutional purpose?
```

Directional labels are viewpoint-dependent.

## 10. Referent migration

A historically connected form may successively denote:

```
PERSON
-> LINEAGE
-> PEOPLE
-> KINGDOM
-> PROVINCE
-> LANGUAGE
-> RELIGIOUS/CULTURAL IDENTITY
```

Each referent type is a separate state.

String continuity does not imply referent continuity.

## 11. Secondary convergence

Later forms can become more similar than earlier forms through independent transmission or normalization.

Therefore:

```
late resemblance
!=
primordial identity
```

Run the full phase history before promoting a late surface match.

## 12. Resegmentation as historical data

Folk etymology, phonotactic repair, lexical attraction, and later reinterpretation can create new meaningful boundaries.

A historically secondary segmentation may still be culturally real.

Store:

```
ORIGINAL_MORPHOLOGY
LATER_RESEGMENTATION
REANALYSIS_DATE
REANALYSIS_CONTEXT
```

separately.

## 13. Operator persistence

Across translation and language change, the durable feature may be a function or relation rather than wording.

Examples:
- command;
- kingship;
- crossing;
- witness;
- generation;
- judgment.

This feeds the existing Structural Continuation and typed-operator layers.

## 14. Linguistic state extension

Extend the current linguistic state with non-compensatory metadata:

```
L* = (
  carrier,
  grapheme,
  phonology,
  morphology,
  syntax,
  semantics,
  role,
  location,
  time,
  classifier,
  provenance,
  full_form,
  vocalization_state,
  segmentation_state,
  semantic_envelope,
  transport_loss,
  reanalysis_history
)
```

## 15. New control cases

Promote these as reusable controls:
- ABRAM full-form vs overlapping-window discovery;
- Akkadian weak-root / weak-consonant behavior;
- AMURRU as directional/administrative label;
- ḪABIRU as social classifier before ethnonym equation;
- YEHUDAH -> YEHUD -> IOUDAIA/IUDAEA/JUDEA as referent/carrier migration;
- GUDEA/JUDEA as secondary-convergence control;
- MARDUK written logogram vs spoken-name distinction;
- SA.GAZ vs Ḫabiru as logogram/readout separation.

## Governing rule

> Preserve the full form, generate comparisons freely, and promote only the segmentation, transport, and referent path that survives native morphology, chronology, provenance, and controls.
