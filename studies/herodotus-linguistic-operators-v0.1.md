# Herodotus — Linguistic Operators v0.1

**Date:** 2026-09-25  
**Status:** SOURCE-LOCKED FIRST PASS

## Macro result

Herodotus repeatedly treats language, ethnonym, script, cult-name and political identity as separable variables.

His corpus directly contains:

```text
language shift
mixed language
multilingual trade
professional interpreters
bilingual/biliterate elites
foreign-language lexical glosses
endonym/exonym divergence
migration-linked renaming
script/sound adaptation
divine-name translation
dialect differentiation inside one ethnonym
```

Thus Herodotus is not merely a source of isolated word comparisons. He is a source for the **mechanisms of ancient language contact**.

## 1. Pelasgian -> Hellenic: explicit language shift

Herodotus 1.57 says that if the surviving Pelasgian-speaking communities are a valid guide, the Attic people, being Pelasgian, **changed their language when they became Hellenes**.

Herodotus 1.58 then says the Hellenic group grew from a small beginning by the accession especially of Pelasgians and many other non-Greek peoples while retaining the Hellenic language.

```text
PEOPLE CONTINUITY
+ POLITICAL/ETHNIC INCORPORATION
-> LANGUAGE SHIFT
```

and simultaneously:

```text
ONE LANGUAGE COMMUNITY
+ MULTIPLE ABSORBED POPULATIONS
-> EXPANDED ETHNONYM
```

Add:

```text
LANG-03 = ETHNIC_INCORPORATION_WITH_LANGUAGE_SHIFT
ID-04 = LANGUAGE_COMMUNITY_EXPANDS_BY_POPULATION_ACCESSION
```

This is among the highest-value Herodotean passages for the project's identity tensor.

## 2. Ionian is a macro-name, not a purity label

Herodotus 1.142 says the Ionian cities themselves speak four distinct dialect groups.

Herodotus 1.146 explicitly rejects the idea that the twelve-city Ionians are more truly Ionian or better-born, listing Abantes, Minyans, Cadmeans, Dryopians, Phocians, Molossians, Pelasgian Arcadians, Dorians and others as components.

Therefore:

```text
ETHNONYM UNITY
!=
GENEALOGICAL HOMOGENEITY
!=
DIALECT UNIFORMITY
```

Add:

```text
ID-05 = COMPOSITE_ETHNONYM_WITH_DIALECT_DIVERSITY
```

## 3. Scythia is Herodotus' densest language-contact laboratory

### Endonym vs Greek exonym

Herodotus 4.6:

```text
Skolotoi = collective self-name
Scythians = Greek name
```

### Persian macro-exonym

Herodotus 7.64:

```text
Sacae = Persian name for all Scythians
```

### Mixed language

Herodotus 4.108 says the Geloni, Greek settlers among the Budini, speak a language:

```text
half Greek + half Scythian
```

while Budini themselves speak a different language.

### Contact-induced imperfect acquisition

Herodotus 4.117 says Sauromatian is Scythian 'not in its ancient purity' because the Amazon mothers did not learn Scythian correctly.

### Direct Scythian lexical glosses

Herodotus records:

```text
arima = one
spou = eye
Arimaspi = 'one-eyed'       (4.27)

oior = man
pata = kill
Oiorpata = 'man-killers'    (4.110)
```

### Divine-name crosswalk

Herodotus 4.59 maps:

```text
Hestia     <-> Tabiti
Zeus       <-> Papaeus
Earth      <-> Apia
Apollo     <-> Goetosyrus
Aphrodite  <-> Argimpasa/Artimpasa
Poseidon   <-> Thagimasadas
```

These are not simple phonetic translations; they are **functional divine-equivalence mappings**.

Add:

```text
NAME-14 = ENDONYM_EXONYM_SPLIT
LANG-04 = CONTACT_MIXED_LANGUAGE
LANG-05 = INTERGENERATIONAL_SECOND_LANGUAGE_RESHAPING
LEX-01 = HERODOTEAN_FOREIGN_GLOSS
DIV-07 = CROSS_CULT_DIVINE_EQUIVALENCE
```

## 4. Multilingual infrastructure is explicit

### Seven interpreters / seven languages

Herodotus 4.24 says Scythians trading toward the northeast conduct business:

```text
through seven interpreters
in seven languages
```

This is direct evidence for chained translation as trade infrastructure.

### Egyptian interpreters as an institution

Herodotus 2.154 says Psammetichus gave Egyptian boys to Ionian and Carian settlers to learn Greek; those boys became the ancestors of the Egyptian interpreter class.

```text
FOREIGN SETTLERS
-> LANGUAGE TRAINING
-> PROFESSIONAL INTERPRETER STRATUM
```

### Carian oracle recognition

Herodotus 8.135 says the Ptoan oracle unexpectedly spoke a foreign language; Theban scribes could not understand it, but Mys of Europus recognized it as Carian and wrote it down.

```text
SPEECH EVENT
-> UNKNOWN TO LOCAL SCRIBES
-> RECOGNIZED BY BILINGUAL HEARER
-> WRITTEN RECORD
```

Add:

```text
TRN-11 = INTERPRETER_INSTITUTIONALIZATION
TRN-12 = CHAINED_MULTILINGUAL_TRADE
REC-03 = FOREIGN_LANGUAGE_EVENT_RECOGNITION
```

## 5. Scyles proves bilingual elite identity is not hypothetical

Herodotus 4.78 says Scyles, king of Scythia, had a Greek mother who taught him:

```text
to speak Greek
+ to read Greek
```

while he remained politically a Scythian king.

He moved between Greek and Scythian clothing, cult practice and social settings.

Thus:

```text
POLITICAL IDENTITY
!=
LANGUAGE REPERTOIRE
!=
CULTURAL REGISTER
```

Add:

```text
LANG-06 = ELITE_BILINGUAL_REGISTER_SWITCHING
```

## 6. Phoenician letters: Herodotus explicitly describes script localization

Herodotus 5.58 says Phoenician settlers brought letters to Greece and that over time the Greeks changed:

```text
the SOUND of the letters
+
the FORM of the letters
```

while continuing to call them Phoenician.

This is an unusually direct ancient statement of:

```text
BORROWED SCRIPT
-> LOCAL PHONEMIC REMAPPING
+ GRAPHIC MODIFICATION
-> NEW WRITING SYSTEM
```

Add:

```text
SCR-03 = SCRIPT_SOUND_FORM_RELOCALIZATION
```

This belongs beside the Hittite/Urartian heterogram work but represents a different mechanism: alphabetic refunctionalization rather than cuneiform heterographic readout.

## 7. The Dodona 'doves' story is a language-perception model

Herodotus 2.57 rationalizes the speaking-dove tradition by saying an Egyptian woman initially spoke a foreign language that sounded like bird cries to the locals; once she learned Greek she was said to have acquired 'human speech.'

Structurally:

```text
UNINTELLIGIBLE HUMAN SPEECH
-> NONHUMAN-SOUND CLASSIFIER
-> LANGUAGE ACQUISITION
-> HUMAN-SPEECH RECLASSIFICATION
```

Add:

```text
REC-04 = INTELLIGIBILITY_CLASSIFIER_SHIFT
```

This is a major ancient example of linguistic incomprehension generating mythic ontology.

## 8. Foreign-word tests and folk-etymology packets

Herodotus repeatedly gives explicit lexical equations:

```text
bekos = Phrygian 'bread'                  (2.2)
Asmakh = 'those at the king's left hand' (2.30)
Battus = Libyan 'king'                    (4.155)
arima + spou = 'one-eye'                  (4.27)
oior + pata = 'man-killer'                (4.110)
```

These should be tested independently against inscriptions and comparative linguistics.

The important methodological point is that Herodotus preserves **claimed ancient cross-language segmentation**, even when a particular etymology later proves doubtful.

Add:

```text
LEX-02 = ANCIENT_REPORTED_SEGMENTATION
```

## 9. Names change with migration, ruler, observer and incorporation

High-yield sequences include:

```text
Briges -> Phrygians after migration Europe -> Asia        (7.73)
Meiones -> Lydians after Lydus                            (7.74)
Termilae -> Lycians after Lycus                           (1.173)
Pelasgian Cranai -> Cecropidae -> Athenians -> Ionians   (8.44)
Pindus 'Macednian' -> Dryopian -> Dorian                  (1.56)
Arians -> Medes in their own eponymic account             (7.62)
Skolotoi -> Greek 'Scythians'                             (4.6)
Scythians -> Persian 'Sacae'                              (7.64)
Syrians -> Persian 'Cappadocians'                         (7.72)
```

Herodotus therefore supplies multiple independent demonstrations that:

```text
NAME CHANGE
!=
POPULATION REPLACEMENT
```

Add:

```text
NAME-15 = MIGRATION_RULER_OBSERVER_RENAMING
```

## 10. Persian name endings: early phonotactic observation

Herodotus 1.139 remarks that Persian names characteristically end in the letter called `san` by Dorians and `sigma` by Ionians.

Whatever the precision of the universal claim, this is an ancient attempt to identify a **language-specific name-shape constraint**.

Add:

```text
PHON-02 = ETHNONYMIC_ONOMASTIC_PHONOTACTIC_PROFILE
```

## 11. Divine names are transmitted separately from divine functions

Herodotus 2.52 says Pelasgians first worshipped gods without individual names, later adopted divine names arriving from foreign lands after consulting Dodona, and Greeks then received those names from Pelasgians.

Herodotus 2.53 separately credits Homer and Hesiod with giving gods genealogies, names, honors/functions and forms.

Herodotus elsewhere gives functional equations such as:

```text
Egyptian Horus   <-> Greek Apollo
Egyptian Isis    <-> Greek Demeter
Egyptian Bubastis<-> Greek Artemis
Egyptian Amon    <-> Greek Zeus
```

Thus Herodotus himself separates several layers:

```text
DIVINE ENTITY
NAME
FUNCTION
GENEALOGY
ICONOGRAPHIC FORM
```

This aligns directly with the project's divine-role rebinding model.

## 12. Writing systems are treated as cultural variables

Herodotus 2.36 distinguishes Egyptian sacred and common scripts and contrasts Egyptian right-to-left practice with Greek left-to-right writing.

Herodotus 5.58 then describes Phoenician alphabetic import and Greek modification.

Together:

```text
SCRIPT TYPE
WRITING DIRECTION
SIGN FORM
SIGN SOUND VALUE
LANGUAGE
```

are already distinct analytic coordinates in Herodotus.

## 13. Highest-confidence Herodotean linguistic nodes

```text
A+  1.57-58  Pelasgian/Attic language shift + Hellenic incorporation
A+  5.58     Phoenician script -> Greek sound/form modification
A+  2.154    institutional Greek interpreter class in Egypt
A+  4.24     seven interpreters / seven languages
A+  4.108    Geloni half-Greek half-Scythian
A+  4.117    Sauromatian as reshaped Scythian
A+  4.6      Skolotoi vs Greek Scythians
A+  7.64     Persian Sacae as macro-exonym
A+  8.135    Carian oracle recognition
A   4.59     Scythian<->Greek divine-name/function crosswalk
A   4.78     Scyles bilingual/biliterate elite
A   1.142/146 Ionian dialect diversity + composite ethnonym
A   2.57     foreign speech -> bird/human classifier shift
B   2.2/2.30/4.27/4.110/4.155 reported foreign lexical glosses
```

## 14. Best next experiments

1. Build a complete Herodotean foreign-word glossary with passage, language, segmentation and later validation.
2. Build an endonym/exonym matrix: Skolotoi/Scythians/Sacae; Syrians/Cappadocians; Persians/Artaei/Cephenes; others.
3. Build a language-shift graph: Pelasgians->Attic Hellenes; Geloni; Sauromatae; Scyles; Egyptian interpreters.
4. Build a divine-equivalence graph: Egyptian, Scythian, Libyan and Greek deity names/functions.
5. Build a script-translation graph: Egyptian sacred/common scripts; Phoenician->Greek alphabet; Carian oracle recording.
6. Compare Herodotus' reported foreign lexical segmentations against inscriptions before using them as phonemic anchors.
7. Treat Book 4 as a priority corpus because it contains the densest concentration of explicit language-contact mechanics.

## 15. Croesus' oracle: metrical packaging across a language boundary

Herodotus 1.47 says the Pythia answered the **Lydian envoys** at Delphi `ἐν ἑξαμέτρῳ τόνῳ` — in hexameter mode/measure. The Lydians then wrote the response down and carried it back to Sardis.

The key distinction is:

```text
ORACLE LANGUAGE = Greek/Delphic
RECIPIENT NETWORK = Lydian royal court
```

which makes the episode more useful linguistically, not less.

Transmission chain:

```text
DIVINE / INSPIRED UTTERANCE
-> METRICAL GREEK FORM
-> WRITTEN RECORD
-> LYDIAN ENVOYS
-> TRANSPORT TO SARDIS
-> ROYAL INTERPRETATION
```

Hexameter therefore functions as a **portable formal carrier**: it stabilizes cadence, segmentation and recall as the oracle crosses institutional and ethnic boundaries.

This need not imply that the Pythia's spontaneous utterance was always already polished verse; ancient and later commentary allows for prophetic personnel shaping inspired speech into regular metrical form. The project should therefore distinguish:

```text
INSPIRATION EVENT
!=
METRICAL REDACTION
!= 
WRITTEN TRANSMISSION
```

Add:

```text
ORA-01 = METRICAL_AUTHORITY_CARRIER
TRN-13 = ORAL_METRICAL_WRITTEN_RELAY
```

Herodotus 1.55 gives another verse oracle to Croesus, reinforcing that this was not an isolated stylistic accident.

## 16. Herodotus 1.56 — the Hellenic/Dorian migration is an ethnonym-rebinding chain

This passage is substantially stronger than a generic origin myth. Herodotus holds one moving population-line constant while changing its geographic seat and label.

The grammatical subject of the migration sequence is the preceding `τὸ Ἑλληνικὸν ἔθνος` ('the Hellenic ethnos/people'). The chain is:

```text
under Deucalion:
HELLENIC ETHNOS -> Phthiotis

under Dorus son of Hellen:
same moving ethnos -> Histiaiotis (below Ossa and Olympus)

after expulsion by Cadmeans:
same ethnos -> Pindus -> Μακεδνὸν καλεόμενον

then:
same ethnos -> Dryopis

finally:
same ethnos -> Peloponnese -> Δωρικὸν ἐκλήθη
```

The Greek `Μακεδνὸν καλεόμενον` is neuter singular and naturally tracks the understood neuter `ἔθνος`; `Δωρικὸν ἐκλήθη` does the same at the end. Thus the text itself presents **Makednon** and **Doric** as phase-specific labels of the migrating subject, even though translators and commentators differ on how geographically to construe Pindus/Makednon.

Herodotus 8.43 independently recalls the same genealogy when he calls most Peloponnesian contingents at Salamis `Dorian and Macednian` and traces them back through Erineus, Pindus and the Dryopian region.

Add:

```text
NAME-16 = PHASE_SPECIFIC_ETHNONYM_REBINDING
GEO-02 = MIGRATION_STAGE_NAME_REINDEXING
TXT-02 = GRAMMATICAL_SUBJECT_CONTINUITY
```

### 16.1 The next chapter supplies the complementary mechanism

Herodotus 1.57 then says the Attic ethnos, originally Pelasgian, changed its language when it became Hellenic.

Placed together, 1.56-57 give two distinct transformation models:

```text
MODEL A — SAME LANGUAGE/PEOPLE-LINE, CHANGING PHASE NAME
Hellenic -> Makednon -> Dorian

MODEL B — CONTINUING PEOPLE-LINE, CHANGING LANGUAGE + MACRO-IDENTITY
Pelasgian Attic -> Hellenic Attic
```

This contiguous pairing is unusually important for the project because Herodotus explicitly refuses the modern shortcut:

```text
NAME = PEOPLE = LANGUAGE = PLACE
```

Instead he narrates each coordinate as independently mutable.

### 16.2 Thucydides preserves an independent Hellen/Phthiotis naming mechanism

Thucydides 1.3 likewise places Hellen son of Deucalion in Phthiotis and says that, as Hellen and his sons became powerful and entered alliances with other cities, the name `Hellenes` spread gradually through association. He appeals to Homer, where `Hellenes` is restricted to Achilles' Phthiotian followers rather than the whole Greek coalition.

Thus two fifth-century historians independently preserve:

```text
PHIOTHIOTIS / HELLEN
-> local or restricted Hellenic name
-> widening social-political adoption
```

Herodotus emphasizes migration/genealogy; Thucydides emphasizes alliance/network diffusion.

Add:

```text
NAME-17 = NETWORK_DIFFUSION_OF_MACRO_ETHNONYM
```

### 16.3 Deucalion now bridges the older-name-carrier study

The project already has Mycenaean `de-u-ka-ri-jo` as a Bronze Age Deukalion name-carrier. Herodotus does not prove that the Pylian bearer is the flood ancestor, but it creates a useful stratified sequence:

```text
Bronze Age personal-name carrier: de-u-ka-ri-jo
-> epic/heroic multiple Deukalion bearers
-> genealogical Deucalion as father-line of Hellen
-> Herodotean geographic/ethnic time-marker: 'in the reign of Deucalion'
```

This is a clean example of an older name being reused as a chronological and ethnogenetic anchor without requiring identity of all bearers.

### 16.4 Genealogy is functioning as compressed geography and identity metadata

The passage is almost algorithmic:

```text
Deucalion = Phthiotis stage
Dorus son of Hellen = Histiaiotis stage
Cadmean expulsion = Pindus transition
Makednon = Pindus phase-label
Dryopis = intermediate territorial phase
Dorian = Peloponnesian phase-label
```

That supports the project's standing hypothesis that mythic genealogy can encode route, political displacement, ethnonym succession and territorial memory simultaneously.

## 17. The -ōtis regional names: people-indexed geography

The repeated Thessalian names in Herodotus 1.56-57 are not random opaque toponyms. They belong to a productive regional/demonymic pattern:

```text
Phthia        -> Phthiōtēs (person) -> Phthiōtis (land/region)
Histiaia      -> Histiaiōtai        -> Histiaiōtis
Pelasgoi      -> Pelasgiōtai        -> Pelasgiōtis
Thessaloi     -> Thessaliōtai       -> Thessaliōtis
```

In historical Thessaly the four major tetrad/regional names were:

```text
Phthiotis
Histiaeotis
Pelasgiotis
Thessaliotis
```

Ancient Greek can use the feminine regional form substantivally, effectively 'the Phthiotian [land]' / 'the Histiaeotian [land]'.

This matters for Herodotus because the geography itself is **population-indexed**: a territory can bear a name derived from the people associated with it, and that name can move or be rebound.

### Histiaeotis gives an explicit migration-name example

Strabo reports that Thessalian Histiaeotis had earlier been called Doris, then received the name Histiaeotis after Histiaeans from Euboea were transferred to the mainland and settled there in numbers.

Whether every detail of that retrospective account is historical or etiological, the naming mechanism is explicit:

```text
PEOPLE NAME
-> DEMONYMIC REGIONAL FORM
-> LAND NAME
```

and:

```text
POPULATION TRANSFER
-> TOPONYM TRANSFER / REBINDING
```

Add:

```text
GEO-03 = DEMONYMIC_REGION_FORMATION
NAME-18 = POPULATION_INDEXED_TOPONYM
TRN-14 = MIGRANT_ETHNONYM_TO_REGION_REBINDING
```

### Structural implication

Herodotus 1.56-57 therefore contains not only a migration chain but a series of names whose morphology already encodes:

```text
PLACE <-> PEOPLE
```

rather than a modern fixed-territory model.

This strengthens the reading of Phthiotis / Histiaeotis / Thessaliotis as dynamic ethnogeographic labels rather than merely neutral map coordinates.

## 18. Attic Pelasgian -> Hellespont / Ionian bifurcation

Herodotus preserves a striking bifurcation around the Athenian-Pelasgian nexus.

### 18.1 Hellespontine branch

Herodotus 1.57 identifies Pelasgians at **Plakia** and **Skylake** on the Hellespont/Propontis who had formerly been co-dwellers with the Athenians. He uses them as a live linguistic control because they retained a language distinct from their neighbors and shared with another Pelasgian enclave.

Herodotus 6.137 independently says Pelasgians expelled from Attica took possession of **Lemnos and other places**. The text does not explicitly state that Plakia and Skylake were those 'other places', but the two notices naturally belong in the same diaspora problem and later commentators sometimes connect them.

Thus:

```text
ATTIC / ATHENIAN PELASGIAN CONTACT ZONE
-> expulsion / dispersal
-> LEMNOS + OTHER SITES
-> PLAKIA / SKYLAKE Hellespontine preservation branch (probable corridor; exact sequence not explicit)
```

### 18.2 Ionian branch

Herodotus 8.44 gives the Athenian identity sequence:

```text
Pelasgian Cranai
-> Cecropidae
-> Athenians
-> Ionians under Ion son of Xuthus
```

Herodotus 7.94-95 then generalizes:

```text
Aegialian Pelasgians -> Ionians
Pelasgian islanders -> later Ionian
twelve-city Ionians -> came from Athens
Aeolians -> formerly Pelasgian (Greek tradition)
Hellespontine Greek settlements -> settlers from Ionians and Dorians
```

This gives a direct Herodotean mechanism for why Pelasgian/Athenian material can appear in later Ionian and Hellespontine contexts without requiring population replacement.

### 18.3 Trojan / Aeolian parallel

Homer's Trojan catalogue includes Pelasgian allies of Troy led by Hippothous and Pylaeus from Larisa. Strabo later places the most plausible Homeric Larisa near Cyme in Aeolis and preserves a tradition that Pelasgians there survived the Trojan War and were later absorbed/displaced during Aeolian settlement.

Strabo also reports a tradition that the present Ionian coast from Mycale and neighboring islands had earlier been Pelasgian, and that Pelasgian power declined particularly during the Aeolian and Ionian migrations.

Thus the broader corridor is:

```text
THESSALIAN / AEGEAN PELASGIAN TRADITIONS
-> ATTICA / ATHENIAN CO-RESIDENCE
-> LEMNOS / Hellespontine enclaves
-> AEOLIAN / IONIAN coastal overlays
-> TROJAN-WAR Pelasgian memory in NW Anatolia
```

This is a transmission-field model, not a claim that all named Pelasgian groups were one continuously traceable biological population.

### 18.4 Plakia and Trojan Plakos: real onomastic recurrence, distinct sites

Herodotean **Plakia** east of Cyzicus is a Pelasgian town in Mysia/Propontis. Separately, Homeric **Thebe Hypoplakia / Placian Thebe**—Andromache's home—lay under Mount **Plakos** near Adramyttium on the Trojan/Mysian fringe.

The repeated `PLAK-` carrier is real and geographically regional, but the two places are distinct. Treat as:

```text
PLAK- REGIONAL ONOMASTIC RECURRENCE = explore
SAME SETTLEMENT / DIRECT COLONY = not established
```

Add:

```text
ID-06 = ATTIC_PELASGIAN_IONIAN_BIFURCATION
TRN-15 = ATTIC_TO_LEMNOS_HELLESPONT_DIASPORA_CORRIDOR
NAME-CAND-19 = PLAK_REGIONAL_ONOMASTIC_RECURRENCE
```

## 19. Croesus, Gyges, and fifth-generation Heraclid vengeance

Herodotus frames Croesus' fall as the delayed settlement of a dynastic legitimacy debt.

Sequence:

```text
Heraclid dynasty at Sardis
-> Candaules = last Heraclid king
-> Gyges (member of the royal guard) kills Candaules
-> Gyges takes wife + kingship
-> Delphi confirms Gyges as king
-> same oracle announces Heraclid vengeance in Gyges' fifth generation
-> Gyges -> Ardys -> Sadyattes -> Alyattes -> Croesus
-> Sardis falls under Croesus
```

Herodotus 1.91 makes the logic explicit: Croesus pays for the offense of the ancestor who killed his Heraclid master and took a royal station that was not rightfully his.

Important distinction:

```text
CROESUS = Mermnad
not Heraclid

but

PUNISHMENT = vengeance owed to the Heraclidae
for Gyges' seizure of their kingship
```

This is therefore not merely inherited personal guilt. It is **office-lineage debt**:

```text
UNLAWFUL TRANSFER OF SOVEREIGN OFFICE
-> DYNASTIC SUCCESSION
-> UNRESOLVED LEGITIMACY CLAIM
-> DELAYED SETTLEMENT AT GENERATION N
```

Add:

```text
AUTH-09 = DYNASTIC_OFFICE_DEBT
TIME-01 = GENERATIONAL_DELAYED_RECKONING
LEG-01 = ORACULAR_LEGITIMATION_WITH_RESERVED_VENGEANCE
```

### 19.1 Oracle paradox

Delphi both ratifies Gyges' rule and reserves future vengeance for the dispossessed Heraclidae.

Thus:

```text
CURRENT LEGAL / SACRAL RECOGNITION
!=
ERASURE OF PRIOR WRONG
```

The office may be validly occupied in the present while the transition into that office still carries an unresolved moral or dynastic liability.

### 19.2 Fifth-generation structure

Herodotus' Mermnad sequence is:

```text
1 Gyges
2 Ardys
3 Sadyattes
4 Alyattes
5 Croesus
```

so Croesus is the fifth ruler-generation of the Mermnad line from Gyges in Herodotus' narrative framing.

### 19.3 Heraclid layer

Herodotus says the prior dynasty had ruled Lydia for twenty-two generations / 505 years, from Agron to Candaules, and traced itself to Heracles through Alcaeus.

The fall of Croesus therefore closes a long temporal bracket:

```text
HERACLID ORACULAR KINGSHIP
-> HERACLID DISPOSSESSION
-> MERMNAD ORACULAR RATIFICATION
-> FIVE-GENERATION DELAY
-> HERACLID VENGEANCE FULFILLED
```

This is a powerful example of genealogy functioning as a temporal accounting system rather than merely biological pedigree.
