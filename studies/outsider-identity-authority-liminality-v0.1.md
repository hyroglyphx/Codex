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


## 13. First source-lock results — 2026-09-24

### OUT-EXP-01 — Ebir-nari / Abar-Nahara

Observed Mesopotamian carrier variation is itself informative:

```text
e-ber ID2
e-bir ID2
e-bir-ma ID2
Eber-nari / ebēr nāri
```

ORACC normalizes these as "Across the River" / Syria west of the Euphrates. In Achaemenid administration, the older Assyrian geographical expression becomes a formal provincial concept. Imperial Aramaic `Abar-Nahara` preserves the same observer-relative geography.

Promotion:

```text
OUTSIDER_RELATIONAL_CLASSIFIER = SOURCE_LOCKED_POSITIVE_CONTROL
```

Important consequence: a relational phrase can harden into a territorial-administrative identity without first being an ethnic self-name.

### OUT-EXP-02 — `Ivri` speaker-context pattern

The first pass shows a strong outsider/intergroup concentration, while not making `Ivri` exclusively foreign speech.

Observed contexts include:

- Abram called `ha-Ivri` in a multi-polity war narrative;
- Joseph described as a "Hebrew man" inside an Egyptian household;
- Joseph himself speaks of the "land of the Hebrews" to Egyptian royal officials;
- Pharaoh's daughter identifies the foundling as a "Hebrew child";
- Moses is instructed to tell Pharaoh that the "God of the Hebrews" appeared;
- Philistines speak of the "camp of the Hebrews";
- Jonah answers foreign sailors `Ivri anokhi`.

Working result:

```text
Ivri has high salience at intergroup boundaries
!=
Ivri is only an outsider exonym
```

This is now an identity-tensor calibration case for `REFERENCE_FRAME` and `BOUNDARY_RELATION`.

### OUT-EXP-03 — ancient explicit classifier-blurring control

Dionysius of Halicarnassus explicitly states that distant peoples were often grouped under broad names because remoteness obscured exact distinctions. He gives:

- Trojans / Phrygians as a frequently conflated pair;
- Latins, Umbrians, Ausonians and others called Tyrrhenians by Greeks;
- Rome itself sometimes treated as Tyrrhenian.

This is direct ancient testimony for:

```text
DISTANCE
-> LOWER ETHNOGRAPHIC RESOLUTION
-> MACRO-CLASSIFIER
```

Add:

```text
OUT-03 = DISTANCE_RESOLUTION_COMPRESSION
```

### AUTH-EXP-01 — Eumaeus / Philoetius

Homeric source lock strengthens the domain-holder reading.

Eumaeus:

- "cared for [Odysseus'] substance above all the slaves";
- independently constructed the large swine enclosure during Odysseus' absence;
- controlled twelve sties, breeding stock, boars, guard dogs and multiple subordinate herdsmen;
- dispatched animals to the palace;
- is repeatedly called "leader of men."

Philoetius:

- was appointed by Odysseus over the cattle while still young;
- describes the herd as multiplying under his care;
- remains "in charge of cattle";
- is also called "leader of men."

Promotion:

```text
DOMAIN_TITLE_VS_LABOR_TASK = HOMERIC_POSITIVE_CONTROL
```

The lexical herd-title remains real, but the narrative function includes delegated management of the absent king's productive assets.

### CAP-EXP-01 — technical-capacity extraction

Source-locked positive pair:

1. II Kings 24 explicitly groups commanders, warriors, artisans/craftsmen and smiths in the deportation to Babylon, while saying only the poorest remained.
2. Neo-Assyrian SAA 15 280 orders carpenters and potters to be collected so they can direct deportees working at Dur-Sharrukin.

Plato, Republic 421d-e supplies the independent craft-capacity mechanism:

```text
lack of tools / requirements
-> worse products
-> worse next-generation craftsmen
```

Together these support testing:

```text
SPECIALIST RELOCATION
<-> CAPACITY TRANSFER
```

without projecting the mechanism onto every deportation.

### ORIG-EXP-01 — sacred-carrier route into Rome

Dionysius provides a source-indexed chain more precise than generic "Trojan ancestry":

```text
Samothrace
-> Dardanus carries Palladia/images of Great Gods into Asia
-> Dardania
-> Ilium/Troy
-> Aeneas removes sacred objects during the fall
-> Italy
-> Roman/Vestal custody tradition
```

This is a continuity claim about sacred objects and rites in addition to human genealogy.

Diodorus independently gives:

```text
Samothrace
-> Dardanus/Cybele/Corybas
-> Asia/Phrygia
```

and also has the Argonauts invoke and later repay vows to the Great Gods of Samothrace.

Therefore the recurrent origin network has at least three carrier types:

```text
people
sacred objects
ritual knowledge
```

which must be tracked separately.

### CAM/CABIR source control

Varro explicitly glosses `camilla` as `administra` and says Casmilus at Samothrace is a divine minister to the Great Gods.

Thus the strongest current claim remains:

```text
Casmilus/Cadmilus <-> ritual minister field
Camillus/camilla <-> Roman ritual attendant field
```

Ancient comparison: observed.
Deep etymological identity: unresolved.

### CAR-EXP-01 — BR carrier observation

ORACC provides a useful non-hypothetical carrier-control:

```text
e-ber
e-bir
e-bir-ma
```

for the same "Across the River" geographic address.

This directly licenses vowel/readout flexibility within the carrier orbit.

It does not by itself license arbitrary consonant metathesis; that remains transform-specific.


## 14. Numa 7 office-translation cluster — Camillus / Hermes / pilamenai / flamines

Plutarch, *Numa* 7 preserves two different translation mechanisms in the same paragraph.

### A. Office-name through ritual regalia

Plutarch says the Roman `flamines` were associated with close-fitting `piloi` (caps) and a longer form he reports as `pilamenai`, adding that Greek words were more intermixed with Latin in that earlier period.

Ancient competing explanations preserve the same semantic neighborhood:

- Plutarch: cap / `pilos` / `pilamenai` -> flamen;
- Varro: head bound with woolen `filum` -> flamen;
- Dionysius: renders Roman flamines by Greek `stephanephoroi`, "crown-wearers," while explaining their cap/fillet.

The historical etymologies compete, but the ancient semantic invariant is strong:

```text
RITUAL HEADGEAR / BINDING
-> VISIBLE OFFICE MARKER
-> PRIESTLY TITLE
```

Add:

```text
AUTH-03 = REGALIA_TO_OFFICE_CLASSIFIER
```

This is structurally parallel to sceptre-holder and other offices named through an entrusted or visible instrument.

### B. Camillus as functional translation of Hermes

In the same *Numa* passage, Plutarch says a freeborn boy with both parents living who serves the priest of Jupiter is called `Camillus`, and that some Greeks likewise called Hermes `Camillus` "from the service/attendance" (`apo tes diakonias`).

Macrobius preserves the Etruscan formulation more sharply:

```text
Camillus = Mercury
meaning praeminister deorum
```

and immediately says Roman `camilli/camillae` are attendants of flamines/flaminicae.

Servius likewise glosses:

```text
Mercury in Etruscan = Camillus
~ minister deorum
```

This is not merely phonetic equivalence. It is explicit office/function translation:

```text
DIVINE ROLE: Hermes/Mercury
-> messenger / minister / authorized intermediary
-> Camillus

HUMAN ROLE:
god
-> flamen
-> camillus
```

Add:

```text
TRN-01 = FUNCTIONAL_OFFICE_TRANSLATION
```

### C. Recursive delegated-authority ladder

The same vocabulary yields a nested model:

```text
DEITY
-> FLAMEN: dedicated priest / cult representative
-> CAMILLUS: attendant / praeminister of the priest

DIVINE ANALOG:
GODS
-> HERMES/MERCURY = CAMILLUS / PRAEMINISTER
```

Thus `Camillus` can mark a role of authorized mediation at both divine and human scales.

### D. Romulus/Quirinus classifier shift

Plutarch introduces this vocabulary while saying Numa adds a priest of Romulus, the `Flamen Quirinalis`.

This supplies a compact identity transform:

```text
ROMULUS named founder/person
-> QUIRINUS cult/divine classifier
-> FLAMEN QUIRINALIS dedicated office
-> CAMILLUS attendant
```

The passage therefore directly links person, divine classifier, office and subordinate minister without requiring those categories to be identical.

### Control

Do not require Plutarch's `pilamenai -> flamines` etymology to be historically correct for the passage to be useful. The source securely witnesses an ancient explanatory model in which:

```text
foreign-language mapping
+ ritual regalia
+ office
+ function
```

can generate alternative names for the same institutional address.
