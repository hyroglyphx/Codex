# Outsider Identity, Delegated Authority, and Liminal Classifiers v0.1

**Date:** 2026-09-24  
**Status:** ACTIVE SYNTHESIS / SOURCE-LOCK QUEUE  
**Scope:** identity tensor, outsider labels, boundary geography, office/function separation, mythic speaking names, origin attribution, utility-class extraction, carrier-window comparison

## Why this supplement exists

The current Codex already separates:

- ethnonym from emic self-identification;
- person from office, people, polity, and territory;
- holder from office and function;
- name carrier from role, episode, and classifier;
- historical etymology from productive reception and folk etymology.

The current conversation adds a missing relational layer:

> an ancient identity label may describe where a population stands relative to an observer, boundary, river, imperial center, route, or jurisdiction rather than describing ancestry.

This supplement therefore extends the existing classifier and referential-stratification architecture rather than replacing it.

## 1. Observer-relative identity tensor

Use:

```text
I(x,s,t) = [
  ENDONYM,
  EXONYM,
  LANGUAGE,
  CULT,
  POLITY,
  ALLEGIANCE,
  JURISDICTION,
  LEGAL_STATUS,
  MOBILITY,
  OFFICE,
  KINSHIP_NARRATIVE,
  NETWORK,
  NARRATIVE_FUNCTION,
  REFERENCE_FRAME,
  BOUNDARY_RELATION
]
```

where:

- `x` = person/group;
- `s` = source/observer;
- `t` = historical phase.

Two sources may classify the same population differently without contradiction because they project different tensor coordinates.

Canonical rule:

```text
projection_i(I) != I
```

No single ethnonym, polity-name, language, cult, or ancestry label exhausts the identity state.

## 2. OUT-01 — OUTSIDER_RELATIONAL_CLASSIFIER

A label may be defined by the observer's geography:

```text
CENTER
-> BOUNDARY / RIVER / STRAIT
-> OTHER SIDE / BEYOND / EDGE
-> HABITUAL REGIONAL LABEL
-> POSSIBLE ETHNONYM / ADMINISTRATIVE NAME
```

Required metadata:

```text
OBSERVER
REFERENCE_CENTER
BOUNDARY_OBJECT
DIRECTION
LOCAL_ENDONYM
EXONYM
JURISDICTION
DATE
SOURCE
```

Priority source-lock cases:

- Assyrian/Babylonian/Aramaic "Beyond the River" / Ebir-nari / Abar-Nahara;
- biblical outsider-facing uses of `Ivri`;
- western Iberia as Mediterranean/Atlantic horizon geography;
- Caucasian Iberia as a separate eastern liminal/corridor comparison.

This operator does not imply common ancestry or common etymology.

## 3. OUT-02 — BOUNDARY_RELATION

Add `B` as an orthogonal identity coordinate:

```text
B = {
  this_side,
  crossing,
  other_side,
  frontier,
  corridor,
  coast,
  upland,
  island,
  outer_edge,
  imperial_beyond
}
```

A population may move between `B` states while other coordinates remain stable.

Analytical "Pale's end" is permitted as a modern model for:

```text
NAMED/CONTROLLED WORLD
-> LIMINAL NAMED ZONE
-> POORLY CLASSIFIED BEYOND
```

but it must not be retroactively presented as an ancient technical term unless source-attested.

## 4. AUTH-01 — DELEGATED_DOMAIN_HOLDER

Extend the existing Sumerian `HOLDER != OFFICE != FUNCTION` control to entrusted domains.

Canonical form:

```text
SOVEREIGN / INSTITUTION
-> DELEGATED AGENT
-> INSTRUMENT OR DOMAIN HELD IN TRUST
-> EXECUTION OF AUTHORITY
```

Candidate comparison field:

- sceptre-holder;
- reins-holder / charioteer;
- herd or estate supervisor;
- priestly minister / camillus-casmilus-cadmilus;
- governor / satrap / regional administrator.

Do not infer that every occupational noun is an office. Promotion requires source evidence for subordinates, assets, delegated command, jurisdiction, or representative authority.

## 5. AUTH-02 — DOMAIN_TITLE_VS_LABOR_TASK

Track separately:

```text
TITLE
OFFICE
MANAGED_DOMAIN
SUBORDINATES
MANUAL_TASK
OWNER
DELEGATING_AUTHORITY
```

This is intended to prevent translations such as "swineherd" from automatically flattening an estate-level supervisory role into a modern wage occupation when the source describes a larger managed domain.

## 6. CAP-01 — UTILITY_CLASS_EXTRACTION

Mass exile/deportation can target not only rulers and soldiers but also technical capacity.

Structural hypothesis:

```text
CONQUEST
-> REMOVE / RELOCATE SPECIALISTS
-> SOURCE_REGION CAPACITY LOSS
-> RECEIVING_CENTER CAPACITY GAIN
```

Decompose technical capacity as:

```text
C = [SKILL, TOOLS, MATERIAL ACCESS, APPRENTICESHIP, INSTITUTIONAL SUPPORT]
```

Possible compounding path:

```text
remove masters
-> lose production
-> lose apprenticeship
-> lose inherited technical memory
```

This is a source-lock research program, not a universal claim about every deportation.

Priority witnesses:

- Neo-Assyrian deportation and specialist relocation;
- Babylonian removal of Jerusalemite craftsmen/smiths;
- Greek philosophical remarks on craft decline under lack of means;
- palace-economy specialist titles.

## 7. NAME-01 — SPEAKING_NAME_FUNCTION

Keep three questions separate:

```text
historical_etymology?
ancient_narrative_etymology?
functional_semantic_fit?
```

A mythic or heroic name may be:

- inherited;
- translated;
- semantically reinterpreted;
- an eponym;
- a title;
- a role label;
- a speaking name describing trait, office, origin, or fate.

Canonical test:

```text
NAME_FORM
<-> SOURCE_GLOSS
<-> NARRATIVE_FUNCTION
<-> GEOGRAPHIC/INSTITUTIONAL ROLE
```

A strong narrative-semantic fit does not by itself establish the prehistory of the word.

Priority calibration nodes:

- Astyanax;
- Odysseus;
- Calypso;
- Tros/Troy;
- Latinus/Latins;
- Phoenix/Phoenicia;
- Cilix/Cilicia;
- Roma/Romulus/Romus traditions.

## 8. ORIG-01 — ORIGIN_ATTRIBUTION_NETWORK

For foundation traditions, preserve repeated upstream origin attributions even when the named human carrier varies.

Model:

```text
SOURCE_ZONE
-> MIGRATION / CULT / SACRED OBJECT / DYNASTIC CARRIER
-> INTERMEDIATE POLITY
-> FOUNDATION / REFOUNDATION
```

Record edges as:

```text
(source_author, source_date, origin_node, carrier_person_or_group, destination, function, confidence)
```

Do not require exact-person identity to compare recurrent attribution structure.

Priority corridor:

```text
Samothrace
-> Dardania / Troy
-> Aeneas / Trojan refugee traditions
-> Latium
-> Rome
```

Cross-check with:

- Cadmean/Phoenician-Boeotian routes;
- Amazon/Pontic routes;
- Colchian/Black Sea routes;
- Roman second-founder/re-foundation traditions.

## 9. CAR-01 — PERMUTATION_AWARE_CARRIER_WINDOW

The existing QBL study already says metathesis is a candidate transform only when independently licensed.

Extend that rule to carrier windows:

```text
carrier_orbit
=
base form
+ attested phonological loss
+ script accommodation
+ vocalic insertion/prosthesis
+ licensed local metathesis
```

For the BR inquiry, maintain separate layers:

```text
A. attested Semitic root/family forms
B. cross-script carrier forms (e.g. EBR/IBR/BR-type windows)
C. candidate permuted forms
D. semantic/geographic operator
E. independent contact/chronology
```

No promotion occurs from `BR` surface similarity alone.

Required rule:

```text
CARRIER_SIMILARITY
+ LICENSED_TRANSFORM
+ SEMANTIC_COMPATIBILITY
+ CHRONOLOGY
+ CONTACT/GEOGRAPHY
> surface resemblance alone
```

QBL/QALB-style order variation is a calibration warning about consonantal mobility, not automatic proof that every permutation is cognate.

## 10. CABIRI / CADMILUS / CAMILLUS cluster

Track this as a high-priority transmission problem because ancient sources themselves connect the ritual-minister field.

Keep separate:

```text
KABEIROI
CADMILUS / CASMILUS
CAMILLI
CAMILLUS personal cognomen
```

Test:

- office/function continuity;
- cultic geography;
- Samothrace-Troad-Italy transmission;
- ancient antiquarian equivalences;
- later narrative rebinding.

Do not reduce the cluster to a free-standing `CAM-` morpheme without evidence.

## 11. Identity tensor and referential strata

The new tensor is orthogonal to the existing R0-R5 referential levels.

Example:

```text
R3 = people/ethnos
```

does not tell us whether the label is:

```text
emic
etic
imperial
boundary-relative
cultic
linguistic
juridical
commercial
```

Therefore use:

```text
IDENTITY_STATE = (R_LEVEL, K_CLASSIFIER, I_TENSOR)
```

rather than replacing the existing stratification system.

## 12. Negative controls

Permanent controls:

- outsider label does not equal ancestry;
- frontier/river semantics do not establish etymology;
- similar title morphology does not prove identical office;
- functional speaking name does not prove historical word origin;
- recurring Trojan/Samothracian attribution does not prove a single literal migration event;
- carrier permutation without independently attested transform remains unresolved;
- utility-class extraction must be source-specific and cannot be projected onto every ancient decline.

## Immediate experiments

- OUT-EXP-01: source-lock Ebir-nari / Abar-Nahara as observer-relative administrative geography.
- OUT-EXP-02: classify biblical `Ivri` passages by speaker and social setting.
- OUT-EXP-03: compare western and Caucasian Iberia as reference-frame/boundary classifiers without ancestry assumptions.
- AUTH-EXP-01: Homeric Eumaeus domain-control matrix: assets, subordinates, authority, owner, task.
- AUTH-EXP-02: sceptre-holder / reins-holder / camillus delegated-authority comparison.
- CAP-EXP-01: specialist-deportation matrix across Assyrian, Babylonian, and biblical witnesses.
- NAME-EXP-01: speaking-name calibration on Astyanax, Odysseus, Calypso, Latinus, Tros.
- ORIG-EXP-01: source-indexed Troy/Samothrace -> Rome attribution graph.
- CAR-EXP-01: BR carrier-window transform table with explicit allowed/disallowed operations.

## Governing synthesis

> Ancient identity is often relational before it is essentialized.

> A label may encode who names a population, from which side of which boundary, under whose jurisdiction, and in what function.

> Names, offices, domains, peoples, and founder genealogies must remain separate coordinates even when a narrative deliberately makes them rhyme.
