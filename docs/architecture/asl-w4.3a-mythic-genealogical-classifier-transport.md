# ASL-W4.3a — Mythic Genealogy / Classifier Transport Supplement

Status: ADOPTED_PROJECT_SUPPLEMENT  
Date: 2026-09-23  
Parent: ASL-W4.3  
Scope: Ancient Script Lattice / Nexus / Myth-Logic Kernel / TCIM / Structural Continuation

## Purpose

Add transformation classes exposed by the Phoroneus and Pelasgian witness sets without duplicating already-incorporated Pelasgian/Tyrsenian, Danaan-renaming, or Aegean substrate material.

The new focus is not ancestry recovery from myth. It is recovery of how geography, polity, social order, ethnonyms, and institutional memory are compressed into genealogical and authorial classifiers.

## Governing distinction

```
genealogy can encode geography/political partition
without being literal population genealogy

ethnography can encode authorial classification
without being emic self-identification
```

## New operators

### PHOR-01 — CIVIC_AGGREGATION

Observed Phoroneus role bundle:
- primordial ruler;
- fire/forge culture hero;
- law giver;
- gatherer of previously dispersed households into community.

Structural path:

```
DISPERSED HOUSEHOLDS
-> GATHER
-> COMMUNITY
-> LAW
-> TECHNOLOGY/FIRE
-> POLITICAL ORDER
```

Use as an operator comparison, not a transmission claim.

### PHOR-02 — SPEECH_FRAGMENTATION_TO_LOCAL_ORDER

A Phoroneus-related tradition places confusion/differentiation of human speech before localized civic order.

Structural path:

```
COMMON ORDER
-> SPEECH DIFFERENTIATION
-> SOCIAL/POLITICAL DIFFERENTIATION
-> LOCAL REAGGREGATION
-> LAW/KINGSHIP
```

Use as a controlled comparison lane for traditions coupling linguistic differentiation with political differentiation. Direct textual dependence is not implied.

### PHOR-03 — GEO_GENEALOGICAL_COMPRESSION

Phoroneus is genealogically generated from river/land personifications in some traditions.

Canonical transform:

```
GEOGRAPHIC FEATURE(S)
-> PERSONIFICATION
-> KINSHIP
-> FOUNDER/RULER
-> TERRITORIAL IDENTITY
```

This operator records geography compressed into genealogy.

### PHOR-04 — RELATIONAL_ROLE_PERMUTATION

Across mythographic witnesses, stable entity identity may coexist with changing kinship edges.

```
NODE IDENTITY relatively stable
!=
KINSHIP GRAPH fixed
```

Track each relation with source, date, witness, and confidence. Do not reconcile contradictory kinship edges into one synthetic genealogy.

### PHOR-05 — POLITICAL_PARTITION_TO_TERRITORIAL_LINEAGE

One Phoroneus genealogy places Pelasgus in the partition of a prior Argive order and links him with a territorial branch/Larissa.

Canonical transform:

```
PRIOR POLITICAL UNITY
-> SUCCESSION / PARTITION
-> GENEALOGICAL BRANCH
-> TERRITORIALIZATION
```

This is a mythic-state transform; it does not establish literal population descent.

## Pelasgian classifier controls

### PEL-01 — AUTHORIAL_CLASSIFIER_LAW

```
ETHNONYM != EMIC SELF-IDENTIFICATION
```

An externally supplied ethnonym is first evidence for a witness's classification system and only secondarily evidence for the classified population.

Required classifier provenance:

```
classifier_author
classifier_date
classifier_audience
classifier_purpose
emic_or_etic
referent_location
referent_period
source_provenance
```

### PEL-02 — FOLK_ETYMOLOGY_FALSE_POSITIVE

Use ancient/scholarly Pelasgos ~ pelargos and related etymologizing as an adversarial control.

Failure path:

```
PHONETIC RESEMBLANCE
-> SEMANTIC STORY
-> MIGRATION/HISTORY NARRATIVE
```

without sufficient independent phonological, morphological, chronological, and provenance support.

Register in the False-Equivalence Control Suite.

### PEL-03 — COMPOSITE_ETHNONYM

Retain ancient compound/fused classifier such as Tyrsenoi-Pelasgoi as an OBSERVED authorial classification relation.

Allowed inference:

```
ancient witness jointly classifies labels
```

Not automatically allowed:
- same population;
- same language;
- common ancestry;
- migration direction.

### PEL-04 — RETROACTIVE_SPATIAL_UNIFICATION

A literary witness may gather multiple inherited loci under one ruler, ethnonym, or polity.

```
SEPARATE PLACE MEMORIES
-> NARRATIVE AGGREGATION
-> RETROSPECTIVE TERRITORIAL UNITY
```

Therefore:

```
place-memory preservation != demonstrated historical polity
```

## New transform family

### MYTHIC_GENEALOGICAL_COMPRESSION

General form:

```
GEOGRAPHY
-> PERSON
-> KINSHIP
-> PEOPLE
-> TERRITORY
```

Possible payloads:
- river;
- land;
- city;
- political partition;
- cult;
- ethnonym;
- office;
- territorial memory.

The transform is reversible only to a candidate historical state unless independent evidence constrains the inverse.

## Classifier transport family

General form:

```
POPULATION / PLACE / PRACTICE
-> AUTHORIAL CLASSIFIER
-> LITERARY RECLASSIFICATION
-> LATER ETHNIC/HISTORICAL OBJECT
```

Track classifier mutation separately from population continuity.

## New negative controls

Add to permanent control suite:

- Pelasgos/pelargos folk-etymology: sound resemblance must not generate history.
- Pelasgian authorial classifier: recurring label must not be treated as stable emic ethnos without witness support.
- retrospective territorial unification: literary aggregation must not be treated as demonstrated political geography.
- kinship permutation: contradiction among genealogies must remain visible rather than be harmonized.

## Integration with ASL-W4.3 relation vector

For mythic-genealogical claims, use the existing relation vector:

```
R(A,B)=<F,P,M,S,G,T,X,C,V>
```

but add non-score metadata:

```
CLASSIFIER_PROVENANCE
KINSHIP_EDGE_PROVENANCE
NARRATIVE_PHASE
PLACE_ADDRESS
POLITICAL_ROLE
EMIC_ETIC_STATE
```

These fields are not compensatory score dimensions.

## Promotion gate

A mythic relation may reach TESTED as a transformation-pattern claim when:
- the literary witness is source-locked;
- the operator is explicitly typed;
- competing readings are preserved;
- chronology of the witnesses is tracked;
- historical reconstruction is kept separate from narrative structure;
- at least one adversarial/control comparison is run.

A transformation-pattern result does not itself promote a historical ancestry or migration claim.

## Immediate experiments

- MG-01 Phoroneus civic aggregation bundle.
- MG-02 Phoroneus geography -> genealogy compression.
- MG-03 Phoroneus kinship-edge variance across witnesses.
- MG-04 Phoroneus -> Pelasgus partition/territorialization.
- CL-01 Pelasgian authorial-classifier provenance matrix.
- CL-02 Pelasgos/pelargos folk-etymology negative control.
- CL-03 Tyrsenoi-Pelasgoi composite-classifier analysis.
- CL-04 Pelasgian retrospective spatial-unification comparison.

## Governing rule

> Mythic genealogy is evidence for a historical culture's model of relation before it is evidence for literal descent.

> Ethnonym recurrence is evidence for classifier continuity before it is evidence for population continuity.


## Pre-Greek substrate firewall

### PEL-05 — SUBSTRATE_CLASSIFIER_FIREWALL

```
PRE_GREEK_SUBSTRATE
!=
PELASGIAN_AUTHORIAL_CLASSIFIER
!=
POPULATION_IDENTITY
```

An ancient ethnonym cannot supply the missing linguistic reconstruction of a substrate.

Substrate features must be tested through lexical, phonological, morphological, toponymic, chronological, and geographic evidence before they are connected to an ethnonym.

### PEL-06 — TOPONYMIC_MORPHOLOGY_SEPARATION

Toponymic patterns such as proposed `-ssa/-nda` and `-ssos/-nthos` lanes may be studied as morphological/geographic evidence without converting them directly into population identity, migration direction, or a single reconstructed "Pelasgian language."

Required independent layers:

```
TOPONYMIC_PATTERN
LINGUISTIC_SUBSTRATE_HYPOTHESIS
AUTHORIAL_ETHNONYM
ARCHAEOLOGICAL_POPULATION_MODEL
```

Controlling supplement:
`docs/architecture/pre-greek-substrate-pelasgian-separation-control-v0.1.md`.

## Distributed role metadata

Where a classifier activates permissions, liabilities, or social role, add:

```
OBSERVER
JURISDICTION
PHASE
RELATION
PERMISSIONS
DUTIES
```

A recurring label can therefore preserve a classifier while changing its operative role under another jurisdiction.


## Strabo founder-geography extension — 2026-09-24

Strabo supplies a source-locked expansion of the genealogy/classifier family in which eponymic persons become political, ethnic, territorial, and colonial classifiers.

### MG-05 — EPONYMIC_CLASSIFIER_CASCADE

```text
PERSON
-> POLITICAL / SETTLEMENT ACT
-> PEOPLE OR TERRITORY CLASSIFIER
-> OPTIONAL COLONIAL EXPORT
```

Canonical Strabonian controls:
- Dorus -> Dorians;
- Achaeus -> Achaeans -> Achaea;
- Ion -> governance/social partition -> Ionians -> Ionia -> Asian Ionian colony;
- Aetolus -> Aetolia + metropolitan unification;
- Lycus -> Lycians, with earlier labels retained as controls.

### MG-06 — TERRITORY_CLASSIFIER_SUCCESSION

```text
SAME LAND
-> SUCCESSIVE POPULATION-LINKED NAMES
```

Canonical control:

```text
Aegialeia
-> Ionia
-> Achaea
```

### MG-07 — LOCAL_TO_PANETHNIC_SCALE_EXPANSION

```text
LOCAL CLASSIFIER
-> REGIONAL CLASSIFIER
-> PANETHNIC CLASSIFIER
```

Canonical inquiry:

```text
local Hellas/Hellenes
-> broader Hellenes
-> Panhellenes
```

The chronology and mechanism of expansion remain source-sensitive.

### MG-08 — SUCCESSIVE_EPONYMIC_OVERWRITE

The same geography may accumulate competing eponymic names across different narrative or political phases.

Canonical Thessalian stack:

```text
Pyrrhaea <- Pyrrha
Haemonia <- Haemon
Hellas <- Hellen
Thessaly <- Thessalus
Nessonis <- Nesson
```

### MG-09 — POLITICAL_ETHNONYM_IMPOSITION

```text
AUTHORITY
-> RENAMING RULE
-> NEW COLLECTIVE CLASSIFIER
```

Canonical ancient narrative control: Strabo's Euripidean citation that people previously called Pelasgians were ordered to be called Danaans.

### MG-10 — INHERITED_COMPOSITE_ETHNONYM

```text
PREDECESSOR EPONYM
-> SUCCESSOR RULE
-> MIXED / RECOMPOSED SUBJECTS
-> INHERITED COLLECTIVE NAME
```

Canonical control: Latinus -> Aeneas as successor ruler -> subjects called Latini.

### Additional firewall

```text
GENEALOGICAL BRANCH
!=
FIXED LINGUISTIC BRANCH
```

Strabo's own dialect discussion permits isolation, contact, mixture, and later divergence within or across inherited tribal classifications.

Primary study:
`studies/strabo-founder-genealogy-geography-v0.1.md`
