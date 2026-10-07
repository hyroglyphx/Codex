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

## 12. Second pass — explicit foreign morphology: Thracian -bria

Strabo gives a direct ancient morpheme gloss:

```text
Menebria = city of Menas
Selybria = city of Selys
Poltyobria = city of Poltys
bria = 'city' in the Thracian language
```

This is unusually valuable because it is not merely a guessed resemblance; Strabo explicitly segments the foreign place-name.

Add:

```text
MORPH-01 = EXPLICIT_FOREIGN_TOPONYM_SEGMENTATION
```

Rule:

```text
PERSON/FOUNDER NAME + LOCAL MORPHEME
-> TOPONYM
```

This becomes a calibration control for testing other ancient place-name suffixes and for distinguishing inherited morphology from later Greek folk parsing.

## 13. Greek macro-name versus native partition

Strabo says Greeks call the Iapygian region Messapia, while local populations distinguish Salentini and Calabri; he also says natives apply Apulia to a broader territory.

Thus:

```text
GREEK MACRO-EXONYM
!=
LOCAL INTERNAL PARTITION
```

Add:

```text
OUT-07 = EXONYM_ENDONYM_SCALE_MISMATCH
```

This is a direct ancient control for the identity-tensor rule that one external geographic name can flatten several local classifiers.

## 14. Serial ethnonym rebinding in Lycia

Strabo preserves a sequence in which populations are variously called Solymi, Milyae, Termilae and later Lycians, while also noting that Homer can distinguish groups that later accounts identify.

```text
SOLYMI / MILYAE
-> TERMILAE
-> LYCIANS
```

The source tradition ties some of these changes to settlement, founder figures and political incorporation.

Add:

```text
NAME-08 = SERIAL_ETHNONYM_REBINDING
```

Important control:

```text
same-population tradition
!=
proof that every historical label denoted exactly the same social set at every date
```

## 15. Cibyra — language preserved outside the homeland

Strabo says the Cibyratae used four languages:

```text
Pisidian
Solymian
Greek
Lydian
```

and immediately adds that there was no longer even a trace of the Lydian language in Lydia.

This gives a major historical-language operator:

```text
LANG-01 = PERIPHERAL_LANGUAGE_RETENTION
```

```text
language disappears in homeland
while surviving in diaspora / mixed frontier community
```

This is a strong warning against using later homeland silence as proof that an older language or carrier never existed.

## 16. Mysian as a contact-language mixture

Strabo reports an older explanation that Mysian speech was in some way a mixture of Lydian and Phrygian, connected to migration and resettlement around Olympus and the Caicus.

Add:

```text
LANG-02 = CONTACT_LANGUAGE_MIXTURE
```

This is an ancient explicit model of migration/contact producing a mixed linguistic state.

## 17. Administrative repartition can erase both names and dialects

In Bithynia/Asia Minor, Strabo remarks that after successive Phrygian, Mysian, Lydian, Persian, Macedonian and Roman dominations, many peoples had already lost both their dialects and their names because the country had been repartitioned differently.

Add:

```text
ID-02 = ADMINISTRATIVE_REPARTITION_ERASURE
```

```text
new jurisdictional map
-> old classifier loss
+ possible dialect loss
```

This directly links political geography to identity-language erosion.

## 18. Zancle -> Messene -> Mamertine classifier capture

Strabo gives a layered sequence at Messana:

```text
Zancle
-> Messene
-> Mamertini dominate
-> people commonly called Mamertini
-> local wine also called Mamertine rather than Messenian
```

This is more than simple renaming. A dominant political group captures the outward classifier of the city and even its commodity.

Add:

```text
NAME-09 = POLITICAL_CLASSIFIER_CAPTURE
```

```text
ruling group
-> urban demonym
-> regional product label
```

## 19. Agylla -> Caere: phonemic omen becomes city-name

Strabo preserves an etiological story in which Lydian/Tyrrhenian attackers ask the city's name; someone on the wall says Greek `chaire` as a greeting, the attackers take it as an omen, and after capturing the city rename it accordingly.

Add:

```text
NAME-10 = NARRATIVE_PHONEMIC_RENAMING
```

This is a powerful ancient control for the project's phonemic-construction lane:

```text
heard utterance
-> semantic reinterpretation
-> political event
-> new proper name
```

Whether the story is historical etymology or etiological myth, it directly demonstrates that ancient authors considered phonemic reinterpretation capable of generating names.

## 20. Relocation plus renaming: Astypalaea -> Cos

Strabo says the Coans moved their settlement because of civil strife and simultaneously changed the city-name from Astypalaea to Cos, matching the island-name.

```text
sedition
-> relocation
-> macro-toponym adopted as city-name
```

Add:

```text
NAME-11 = RELOCATION_MACROTOPONYM_ADOPTION
```

## 21. Dynastic rebuilding and patronal renaming

Strabo repeatedly gives the pattern:

```text
Cius -> Prusias
Myrleia -> Apameia
Antigonia -> Nicaea
Antigonia -> Alexandria (elsewhere in successor-city tradition)
```

after destruction, refoundation, dynastic transfer or royal patronage.

Add:

```text
NAME-12 = SOVEREIGN_PATRONAL_RENAMING
```

This is distinct from ordinary phonetic transmission. Same site or community can acquire a wholly new name because sovereignty changes.

## 22. Geographic scale shift: Asia

Strabo explicitly notes that Roman usage called a province `Asia` by the same name as the entire continent.

Add:

```text
OUT-08 = TOPONYM_SCALE_SHIFT
```

```text
continent-name
-> administrative province-name
```

This is another control against assuming that a familiar geographic label had a constant scale across periods.

## 23. Language change by isolation and contact

Strabo's opening discussion of Greek dialects attributes divergence both to isolation and to mixing. He says rugged, low-contact populations can change speech/custom independently, while other regions develop mixed speech under contact.

Add:

```text
LANG-03 = ISOLATION_CONTACT_DIALECT_DIVERGENCE
```

This is a useful ancient conceptual control for the ECVR contact lattice.

## 24. Turdetanian language loss under Romanization

Strabo says the Turdetanians near the Baetis had adopted Roman life so thoroughly that they no longer remembered their own language, and many had become Latins.

Add:

```text
ID-03 = LANGUAGE_LOSS_WITH_STATUS_RECLASSIFICATION
```

```text
political/cultural assimilation
-> ancestral language loss
-> new civic/status classifier
```

## 25. Boundary inscription as identity operator

Strabo reports the Isthmian boundary pillar:

```text
This is Peloponnesus, not Ionia
This is not Peloponnesus, but Ionia
```

depending on which side the reader faced.

Add:

```text
OUT-09 = BIDIRECTIONAL_BOUNDARY_INSCRIPTION
```

This is perhaps the cleanest literal example yet of identity being defined by side-of-boundary and observer orientation.

## Second-pass synthesis

Strabo now gives us direct controls for:

```text
foreign morpheme segmentation
exonym/endonym scale mismatch
serial ethnonym rebinding
peripheral language retention
mixed contact languages
administrative erasure of names/dialects
political classifier capture
phonemic renaming
relocation-linked renaming
dynastic patronal renaming
toponym scale shift
isolation/contact dialect divergence
language-loss status reclassification
bidirectional boundary identity
```
