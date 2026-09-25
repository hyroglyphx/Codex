# Strabo Founder-Genealogy Geography v0.1

**Date:** 2026-09-24  
**Status:** SOURCE-LOCKED FIRST PASS

## Core result

Strabo repeatedly uses genealogy as a naming machine:

```text
PERSON
-> POLITICAL / SETTLEMENT ACT
-> PEOPLE CLASSIFIER
-> COUNTRY NAME
-> COLONIAL EXPORT / SCALE EXPANSION
```

This extends the existing `MYTHIC_GENEALOGICAL_COMPRESSION` family.

## 1. Strabo 8.7.1 — Deucalion/Hellen cascade

```text
Deucalion
-> Hellen
   -> Dorus
   -> Xuthus
      -> Achaeus
      -> Ion
```

Dorus unites the Dorians around Parnassus and leaves them his name.

Achaeus moves to Lacedaemon; the population is called Achaeans. Later Achaeans displace Ionians from Aegialus and the territory is called Achaea.

Ion defeats Eumolpus' Thracians, receives political authority, divides the Athenians into tribes and occupational orders, leaves his name to the country, and the Ionian classifier is then exported through colonization into the Peloponnese and Asia.

Ion therefore gives the fullest cascade:

```text
PERSON
-> GOVERNANCE
-> SOCIAL PARTITION
-> PEOPLE
-> TERRITORY
-> COLONIAL EXPORT
```

Add:

```text
MG-05 = EPONYMIC_CLASSIFIER_CASCADE
```

## 2. Same land, successive classifiers

Strabo gives:

```text
Aegialeia / Aegialeians
-> Ionia / Ionians
-> Achaea / Achaeans
```

The land persists while the dominant classifier changes.

Add:

```text
MG-06 = TERRITORY_CLASSIFIER_SUCCESSION
```

## 3. Hellen: local -> panethnic

Strabo 8.6.6 preserves disagreement over when `Hellenes` became a common name. One ancient line restricts Homeric Hellenes to Thessaly/Phthia; later witnesses use Hellenes/Panhellenes more broadly.

Strabo 9.5 places the Deucalion/Hellen tradition in Phthia/Thessaly.

```text
LOCAL HELLEN / HELLAS
-> REGIONAL HELLENES
-> GENERAL HELLENES
-> PANHELLENES
```

Add:

```text
MG-07 = LOCAL_TO_PANETHNIC_SCALE_EXPANSION
```

## 4. Thessaly as stacked eponymic geography

Strabo 9.5 preserves overlapping names for the same broad region:

```text
Pyrrhaea <- Pyrrha
Haemonia <- Haemon
Hellas <- Hellen
Thessaly <- Thessalus
Nessonis <- Nesson
```

Nearby microtoponyms preserve the Deucalion/Pyrrha complex, including Cape Pyrrha and islands called Pyrrha and Deucalion.

Add:

```text
MG-08 = SUCCESSIVE_EPONYMIC_OVERWRITE
```

## 5. Pelasgians -> Danaans

In 8.6.9 Strabo quotes the Euripidean tradition that Danaus established a rule that people previously called Pelasgians should be called Danaans. Strabo then says the fame of Argos helped wider labels such as Argives and Danaans spread to other Greeks.

```text
POLITICAL AUTHORITY
-> NEW COLLECTIVE NAME
-> MACRO-CLASSIFIER EXPANSION
```

Add:

```text
MG-09 = POLITICAL_ETHNONYM_IMPOSITION
```

## 6. Aetolus -> Aetolia

Strabo 8.3.33, following Ephorus:

```text
Aetolus
-> Aetolia
-> cities united under one metropolis
```

This joins eponymy with political aggregation.

## 7. Lycus -> Lycians: positive case plus adversarial control

Strabo 12.8.5 gives the serial tradition:

```text
Solymi
-> Milyae
-> Termilae
-> Lycians after Lycus
```

but immediately notes that Homer distinguishes Solymi from Lycians where later tradition can identify them.

So:

```text
later genealogical renaming
!= guaranteed identity of every earlier social set
```

## 8. Latinus / Aeneas / Latini

Strabo 5.3 gives a different mechanism. Latinus supplies the royal/eponymic classifier; after Latinus dies, Aeneas becomes king and calls his subjects Latini.

```text
PREDECESSOR EPONYM
-> SUCCESSOR RULE
-> COMPOSITE SUBJECTS
-> INHERITED COLLECTIVE NAME
```

Add:

```text
MG-10 = INHERITED_COMPOSITE_ETHNONYM
```

## 9. Genealogy is not a literal language tree

Strabo 8.1 complicates the genealogy by relating tribes and dialects while also allowing isolation, contact, and mixture to change speech and customs.

Therefore:

```text
GENEALOGICAL BRANCH != FIXED LINGUISTIC BRANCH
```

## 10. Formal naming-machine model

Use:

```text
E = eponymic person
P = population
T = territory
I = institution/political order
C = colony/exported geography
```

Possible transforms:

```text
E -> P
E -> T
E -> I -> P
P -> T
P -> C
T_old -> T_new
P_local -> P_macro
```

Examples:

```text
Ion     : E -> I -> P -> T -> C
Dorus   : E -> I -> P
Achaeus : E -> P -> T
Hellen  : E -> P_local -> P_macro
Aetolus : E -> T + I
Danaus  : authority -> classifier replacement -> P_macro
```

## Governing questions

For every ethnogeographic name ask:

```text
WHO names it?
AFTER whom/what?
AT what scale?
BEFORE/AFTER which migration or political change?
DID the people move, the name move, or both?
DID the label expand from local to macro use?
```

## Immediate experiments

- Build Hellen/Hellas/Hellenes/Panhellenes scale-expansion matrix.
- Compare Strabo 8.7 with Apollodorus 1.7.3.
- Make Ion the canonical person->office->partition->people->territory->colony cascade.
- Compare Aegialeia->Ionia->Achaea with Solymi->Milyae->Termilae->Lycians.
- Test Pyrrhaea/Haemonia/Hellas/Thessaly/Nessonis as stacked geographic-memory layers.


## 12. Aspiration must be separated from the EL/ELL carrier

Greek `Ἕλλην` and `Ἑλλάς` carry rough breathing. In conventional Latin transliteration, that breathing is rendered as initial `H-`.

So analytically:

```text
Ἕλλην = aspiration[+] + ELLĒN
Ἑλλάς = aspiration[+] + ELLAS
```

The `H` is not a detachable lexical prefix. It is a phonological feature recorded by the rough-breathing tradition.

This matters because Greek dialects underwent psilosis at different times: some dialects lost initial /h/, while Attic retained it longer. Therefore:

```text
H- / zero
```

can be a dialectal/readout variable without changing the deeper lexical carrier.

Herodian is especially useful here: in his prosodic rules he treats `Ἕλλην` and `Ἑλλάς` as exceptional rough-breathing forms among epsilon-plus-lambda words, showing that their aspiration was already something ancient grammarians had to mark explicitly.

Strabo's Dodona discussion adds a separate but nearby control:

```text
Helli
vs
Selli
```

with Hellopia and the river Selleis used to adjudicate the reading.

This does **not** prove:

```text
Selli -> Helli -> Hellenes
```

but it makes a controlled `S/H/zero + EL(L)` carrier experiment legitimate.

Add exploratory lane:

```text
NAME-CAND-08 = ASPIRATION_STRIPPED_EL_ELL_CARRIER
STATUS = EXPLORE_ONLY
```

Required comparison layers:
- rough versus smooth breathing;
- dialect and date;
- Helli/Selli textual variants;
- Hellopia;
- Hellen/Hellas;
- `Ἑλένη` / `ἑλένη` torch-name field;
- external-language renderings that may preserve or omit aspiration.

Important distinction:

```text
Hellen: double lambda
Helen/helene: single lambda
```

Do not collapse the carriers solely because both are aspirated EL-forms.

## 13. Semitic ʾEL / Greek EL-ELL carrier lane

The aspiration-stripped Hellen/Hellas experiment warrants an external-language control because Northwest Semitic has an independently meaningful and highly productive `ʾL / EL` carrier.

### A. Semitic control

Across Semitic languages, cognates of `ʾil / ʾel` function as the common noun 'god' and as the divine name El.

Source-locked examples:

```text
Ugaritic: ʾil / ʾIlu
Phoenician-Canaanite: ʾl
Hebrew: ʾēl
Akkadian: ilu(m)
```

Phoenician/Canaanite personal names also use `ʾl` productively as a theophoric element.

Thus `EL` is not a retrospective symbolic extraction; it is an ancient Semitic lexical and onomastic carrier.

### B. Greek reception of Phoenician El is explicitly attested

Philo of Byblos, preserved by Eusebius, states that the Phoenicians called Kronos `El / Elus`.

This gives a direct Greek literary crosswalk:

```text
Phoenician ʾEl
-> Greek literary El / Elus
-> functional equation with Kronos
```

This is highly important for the Codex because it demonstrates that a Semitic `ʾEL` divine carrier could enter Greek discourse in an `EL-` shaped form while retaining semantic identity.

Add:

```text
TRN-06 = SEMITIC_EL_TO_GREEK_DIVINE_READOUT
```

### C. Compare with aspiration-stripped Hellen/Hellas

Greek:

```text
Ἕλλην  = H + ELLĒN
Ἑλλάς  = H + ELLAS
Ἑλένη  = H + ELENĒ
```

where the written Latin H represents rough breathing / aspiration rather than a lexical prefix.

Therefore the exploratory carrier comparison is:

```text
Semitic ʾEL
Greek EL / ELUS
Greek H-EL / H-ELL
Greek S-ELL? (Dodona Helli/Selli textual lane)
```

### D. Transform licensing

Already supported:

```text
Semitic ʾEL -> Greek EL/ELUS
H-EL -> EL under psilosis / aspiration loss in Greek dialect history
```

Not yet independently supported:

```text
EL -> ELL gemination as a cross-language convention
EL -> HELL as a specific Semitic-to-Greek historical derivation
SEL -> HELL as a regular sound law
```

Those remain experiments.

Add:

```text
NAME-CAND-09 = SEMITIC_EL_GREEK_ELL_ATTRACTION
STATUS = EXPLORE_ONLY
```

### E. Why Hellen is now a better test than an isolated resemblance

The candidate now sits inside a real contact architecture:

```text
Phoenician / West Semitic contact with Greek world
+ direct Greek knowledge of Phoenician El
+ Greek foreign-name adaptation documented by Strabo
+ aspiration as a removable coordinate
+ local Hellas/Hellenes scale expansion
+ Helli/Selli textual/onomastic ambiguity at Dodona
```

So the correct question is no longer merely:

```text
Does Hellen look like El?
```

but:

```text
Did Greek speakers encounter EL as an independently meaningful divine/onomastic carrier,
and could an inherited HELL-/EL- name be semantically attracted or reinterpreted through that field?
```

That is a testable reception/transmission question even if ultimate etymology remains unresolved.

### F. Promotion requirements

Before any historical derivation is promoted, seek:

- Phoenician/Aramaic renderings of Hellen/Hellas or related Greek ethnonyms;
- Greek bilingual renderings of Semitic `ʾl` in names/titles;
- archaic Aegean/Levantine divine-name crosswalks;
- same-referent inscriptions where aspiration or gemination varies;
- chronological overlap between Phoenician contact zones and expansion of Hellenes as a macro-classifier;
- evidence distinguishing inherited root from later semantic attraction.

