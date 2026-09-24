# Strabo: Name, Geography, and Transmission Operators v0.1

**Date:** 2026-09-24  
**Status:** FIRST SOURCE-LOCKED PASS  
**Scope:** Strabo Geography as an ancient meta-source for name adaptation, textual ambiguity, exonymic compression, title persistence, prestige-name transfer, multilingual macro-classifiers, and fabricated etymological geography.

## Why Strabo matters

Strabo repeatedly does more than list names. He explicitly discusses how foreign names are altered in Greek, how manuscript ambiguity is tested against geography and related names, how commentators can invent place-names to rescue literary interpretations, how prestigious names migrate to new geographies, how broad ethnographic labels cover many languages, how titles persist after political structures change, and how older tribal distinctions can survive after language/custom differences disappear.

## 1. XVI.4 — foreign-name adaptation is explicit

Strabo says that changes in names, especially foreign names, are numerous. His examples include:

```text
Aramaeans -> Greek Arimaeans / Arimi
Dareios -> Darieces
Parysatis -> Pharziris
Athara -> Atargatis -> Derceto in Ctesias
```

Add:

```text
TRN-05 = FOREIGN_NAME_RECEIVING_LANGUAGE_ADAPTATION
```

Rule:

```text
same referent
+ foreign phonology
+ Greek readout
!= surface-form identity
```

## 2. VII.7 — Helli / Selli as an ancient backprojection problem

At Dodona, Strabo explicitly says the text does not permit certainty between Helli and Selli. He then reports attempts to adjudicate the reading using Hellopia, the Selleeis river, regional geography, and other poetic witnesses.

```text
AMBIGUOUS FORM
-> RELATED PLACE/PERSON/WORD FORMS
-> GEOGRAPHIC CONTROL
-> WITNESS COMPARISON
-> WEIGHTED READING
```

Add:

```text
TXT-01 = GEOGRAPHIC_TEXTUAL_BACKPROJECTION
```

This is directly relevant to the exploratory NEL/THEL lane.

## 3. XIII.1.45 — negative control against overfitting

Strabo attacks commentators who, in his view, fabricated names such as Alizonium and Argyria to force geography to fit Homeric phrases, including a 'birthplace of silver.'

Add:

```text
ADV-01 = ETYMOLOGICAL_GEOGRAPHY_FABRICATION_CONTROL
```

Rule:

```text
SEMANTIC FIT + LITERARY MOTIVE != HISTORICAL TOPONYM
```

This does not weaken phonemic-construction research; it gives it an adversarial control.

## 4. XI.5 — Caucasus name transferred for prestige

Strabo says Alexander-flattering writers transferred the name Caucasus from the mountains above Colchis/Euxine to mountains near India because the older Caucasus carried ends-of-the-earth, Prometheus, and Argonautic prestige.

Add:

```text
NAME-07 = PRESTIGE_TOPONYM_TRANSFER
```

```text
PRESTIGIOUS OLD GEOGRAPHIC NAME
-> NEW DISTANT GEOGRAPHY
-> HEROIC/POLITICAL AMPLIFICATION
```

## 5. XI.2 — the two Iberias are explicitly compared

Strabo says the Caucasian Iberians may perhaps have the same name as the western Iberians because both countries were associated with gold mines. Whether this explanation is historically correct is secondary here: it shows an ancient geographer seeking a functional/material explanation for a distant duplicate ethnogeographic name rather than requiring common ancestry.

Add candidate:

```text
NAME-CAND-07 = DUAL_IBERIA_FUNCTIONAL_ETIOLOGY
```

## 6. XI.2 — Dioscurias: multilingual microgroups under a macro-classifier

Strabo says about seventy tribes come together at Dioscurias and all speak different languages; exaggerated reports said three hundred. Yet he also says the majority are Sarmatian and, at the broadest level, all are Caucasii.

```text
many local languages / tribes
-> one trade node
-> broader external macro-classifier
```

Add:

```text
OUT-06 = MULTILINGUAL_MACRO_CLASSIFIER
```

## 7. XI.2 — sceptuchoi as delegated-authority control

Strabo says certain Caucasian peoples are governed by sceptuchoi, while the sceptuchoi themselves are subject to kings or tyrants.

```text
KING / TYRANT
-> SCEPTUCHOS
-> PEOPLE / DOMAIN
```

This strengthens AUTH-01 with an explicit political hierarchy.

## 8. XIII.1.52 — title survives regime change at Scepsis

Strabo gives a sequence from royal families to oligarchy, then Milesian co-citizenship and democracy; nevertheless descendants of the royal house continued to be called kings and retained prerogatives.

Add:

```text
AUTH-06 = TITLE_PERSISTENCE_AFTER_REGIME_CHANGE
```

## 9. XII.1 — Cataonian distinction disappears while classification survives

Strabo says the ancients distinguished Cataonians from Cappadocians, but in his own time he could detect no difference in language or usages.

```text
OLDER TRIBAL CLASSIFIER
-> LANGUAGE/CUSTOM CONVERGENCE
-> DISTINCTION BECOMES INVISIBLE
```

Add:

```text
ID-01 = CLASSIFIER_FOSSILIZATION_AFTER_CONVERGENCE
```

## 10. XVI.4 + I.2 — Aramaean / Arimaean comparative lane

Strabo/Posidonius compares Syrians, Aramaeans/Arammaeans, Greek Arimaeans/Arimi, Armenians, Arabians and Erembians. The historical linguistic claims should not be accepted wholesale merely because Strabo reports them, but the passage is highly valuable as an ancient example of reasoning through language resemblance, ethnonym resemblance and geography/contact together.

## 11. Methodological synthesis

Strabo gives at least seven distinct mechanisms that should not be collapsed:

```text
A. FOREIGN NAME ADAPTATION
B. TEXTUAL VARIANT
C. COMMENTATOR FABRICATION
D. PRESTIGE NAME TRANSFER
E. MACRO-CLASSIFICATION
F. TITLE PERSISTENCE
G. CLASSIFIER FOSSILIZATION
```

## Immediate next queue

- Build a full Strabo foreign-name adaptation table from Books I, XI, XIII and XVI.
- Compare Helli/Selli with NEL/THEL as a controlled textual-variant experiment.
- Build a 'fabricated to save Homer' negative-control set from Strabo/Demetrius of Scepsis.
- Extend the dual-Iberia study using Strabo's explicit gold-mines explanation.
- Build a sceptuchos hierarchy matrix against camillus, flamen, heniochos, estate-holder and satrap/governor cases.
- Search Strabo for titles that survive constitutional change or become hereditary honorifics.
- Search Strabo for local-language distinctions erased by later convergence.
