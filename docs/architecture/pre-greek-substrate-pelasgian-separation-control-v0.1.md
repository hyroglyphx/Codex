# Pre-Greek Substrate / Pelasgian Classifier Separation Control v0.1

Status: SOURCE_ASSISTED_CONTROL  
Date: 2026-09-23  
Scope: ASL-W4.3a / Aegean substrate / classifier transport / historical linguistics

## Purpose

Prevent three distinct objects from being silently collapsed:

```
PRE_GREEK_SUBSTRATE
!=
PELASGIAN_AUTHORIAL_CLASSIFIER
!=
POPULATION_IDENTITY
```

This control is conservative by design. It does not choose among competing substrate theories.

## 1. Substrate is not ethnonym

A linguistic substrate is inferred from recurring lexical, phonological, morphological, or toponymic behavior.

An ethnonym/classifier is a historical witness's category for people, places, or traditions.

Therefore:

```
substrate_feature
-> linguistic_stratum_candidate
```

does not license:

```
linguistic_stratum_candidate
-> "Pelasgian language"
```

without independent evidence.

## 2. Pelasgian is not a reconstruction shortcut

The source snapshot records modern scholarly criticism of attempts to reconstruct a single Indo-European "Pelasgian" language from the ethnonym and mixed evidence.

Operational rule:

```
PELASGIAN_LABEL
cannot substitute for
PRE_GREEK_CORPUS
```

The corpus itself must supply the phonology/morphology.

## 3. Toponymic morphology is its own evidence lane

Suffix distributions such as:

```
-ssa / -nda
-ssos / -nthos
```

may be studied as toponymic/morphological evidence.

They do not automatically identify:
- one population;
- one ethnonym;
- one migration;
- one language family.

Required path:

```
TOPONYM
-> MORPHOLOGICAL_PATTERN
-> GEOGRAPHIC_DISTRIBUTION
-> CHRONOLOGY
-> COMPARATIVE_LANGUAGE_HYPOTHESIS
```

Only then can a population-history model be tested separately.

## 4. Folk-etymology control

Pelasgos ~ pelargos is retained as a negative control because resemblance can generate an attractive migration narrative without independently establishing the historical path.

This strengthens PEL-02.

## 5. Layer stack

For every Aegean substrate claim, store:

```
LEXICAL_FORM
TOPONYMIC_FORM
MORPHOLOGICAL_PATTERN
SCRIPT/LANGUAGE_STATE
AUTHORIAL_ETHNONYM
ARCHAEOLOGICAL_POPULATION_MODEL
GEOGRAPHY
CHRONOLOGY
PROVENANCE
```

No layer inherits confidence automatically from another.

## 6. Cross-application

### Pelasgian classifier research

Treat ancient "Pelasgian" recurrence first as classifier-history evidence.

Then ask separately whether any linguistic substrate feature can be connected to the classified group.

### Linear A / Eteocretan / Minoan

Aegean substrate comparison remains structural until exact sign/readout and language evidence support stronger linkage.

### Lemnian / Tyrsenian

Secure or candidate linguistic relations must not be absorbed into a generic "Pelasgian substrate" label.

### Anatolian comparison

Toponymic/morphological parallels may be tested as a dedicated edge family without converting the whole pre-Greek substrate into one Anatolian language.

## Governing rule

> Do not use an ancient ethnonym to fill a missing linguistic reconstruction. Let substrate features, classifier history, and population models meet only through explicit typed edges.
