# Homeric Textual and Linguistic Transmission Study

Status: **ACTIVE D4 STUDY**  
Updated: **2026-09-21**

## Why Homer is unusually valuable

The Iliad and Odyssey preserve several different transmission processes at once:

1. inherited Bronze-Age / Mycenaean linguistic and cultural residues,
2. oral-formulaic recomposition,
3. a mixed epic poetic language dominated by Ionic with Aeolic and older elements,
4. early Greek textual multiformity,
5. Hellenistic editorial comparison,
6. medieval manuscript transmission,
7. early Latin translation/adaptation,
8. later epitome, commentary, paraphrase, and cross-cultural reception.

The corpus therefore lets us study:

```text
ORAL MULTIFORM
→ POETIC KOINE
→ WRITTEN VARIANT
→ EDITORIAL RECENSION
→ MANUSCRIPT VULGATE
→ TRANSLATION / ADAPTATION
```

without treating these processes as equivalent.

## A. Greek-before-Homer control: Mycenaean / Linear B

Linear B is not an early "version" of Homer. It is an earlier Greek linguistic control.

High-value correspondences include:

- Mycenaean `wanax` → Homeric `anax`
- Mycenaean `gwasileus` → Homeric `basileus`
- `potnia` and other court/religious vocabulary
- older formulaic and lexical material preserved in epic diction

The semantic shift of titles must be measured, not assumed to be static.

## B. Homeric Greek as a composite language

Homeric epic is principally Ionic but includes:
- Aeolic forms,
- Arcado-Cypriot / Mycenaean-looking archaisms,
- artificial poetic forms,
- later Attic surface influence.

Therefore Homeric Greek should be modeled as:

```text
H = Ionic_base
  + inherited_formulae
  + Aeolic_options
  + older_archaisms
  + metrical_selection
  + later_surface_adjustment
```

It is not a vernacular dialect spoken by one historical community.

## C. Early Greek papyri: multiform Homer

Ptolemaic Homeric papyri preserve:
- plus verses absent from the later vulgate,
- minus verses,
- alternative formulaic phrasing,
- differing line sequences/readings.

The textual tradition becomes substantially more stable by roughly 150 BCE.

### New bridge
`B17 — ORAL_FORMULAIC_MULTIFORM`

Use when a traditional poem exists in multiple formulaically valid realizations without a single source-target translation relation.

## D. Alexandrian editorial states

Priority editors/scholars:
- Zenodotus
- Aristophanes of Byzantium
- Aristarchus

The Alexandrian tradition collated multiple Homeric texts and marked or discussed variant readings.

Their editions do not survive directly. Their work is partly reconstructible through:
- Didymus,
- Aristonicus,
- Nicanor,
- Herodian,
- Homeric scholia,
- later manuscripts.

Model:

```text
variant manuscripts
→ Alexandrian collation
→ critical judgement/signs
→ later scholia
→ medieval codex
```

Do not confuse a scholar's preferred reading with the only ancient reading.

## E. Venetus A / medieval Greek control

Venetus A (late 10th c. CE) is the oldest complete surviving Iliad.

Its value is doubled because its scholia preserve ancient scholarship and competing readings reaching back to the Alexandrian tradition.

This is a high-value **archival custody** object:

```text
ancient variants
→ lost commentaries
→ scholia compilation
→ medieval codex
```

## F. Ancient quotations as independent witnesses

Quotations in:
- Plato
- Aristotle
- Plutarch
- other Greek authors and scholiasts

can preserve readings absent from the main manuscript tradition.

These should enter as `PARALLEL_WITNESS` records, not as secondary paraphrase automatically.

## G. Greek Epic Cycle: parallel narrative versions

Not translations, but alternative/adjacent Trojan-War traditions:

- Cypria
- Aethiopis
- Little Iliad
- Iliou Persis
- Nostoi
- Telegony

These preserve competing story states.

Useful conflict examples include:
- different locations for Chryseis' capture,
- different Paris travel itineraries,
- Astyanax killed by Odysseus in one tradition but Neoptolemus in another,
- different Aeneas outcomes.

This is ideal for:

```text
same mythic event
→ different narrative realization
→ invariant action
→ altered agent / cause / sequence
```

## H. Earliest major translation: Livius Andronicus' Odusia

Late 3rd century BCE.

This is the earliest major Latin translation/adaptation of Homer and the first Latin literary epic.

Important transpositions:
- Greek hexameter → Latin Saturnian meter,
- Muse → Roman/Italic Camena,
- `polytropos` → Latin `versutus`,
- Odysseus → Roman Ulysses tradition,
- Greek cultural vocabulary → Roman equivalents.

The opening line is an exceptionally strong controlled translation object:

```text
Greek:
andra moi ennepe, Mousa, polytropon

Latin:
virum mihi, Camena, insece versutum
```

This permits word-level, meter-level, deity-equivalence, and semantic-choice comparison.

## I. Ilias Latina

First-century CE Latin epitome of the Iliad.

It is not a literal translation.

Use it to measure:
- compression,
- scene selection,
- omitted speeches/similes,
- Roman taste,
- plot preservation under aggressive reduction.

Bridge type:
`RECENSION_RECOMPOSITION / EPITOME`.

## J. Dares / Dictys / Latin-West Trojan tradition

Dares Phrygius and Dictys Cretensis are not translations of Homer.

They belong to:
```text
Trojan narrative
→ prose recomposition
→ Latin medieval custody
```

Together with the Ilias Latina, they carried the matter of Troy in the Latin West when full Homeric Greek texts were largely unavailable there.

## K. Syriac / Arabic / Armenian / Georgian halo

No secure ancient full Syriac or Arabic translation equivalent to the Odusia survives.

Later evidence includes:
- Homeric quotations used in Greek grammatical/rhetorical education,
- Syriac engagement with such material,
- reported Syriac translations/adaptations connected with Theophilus of Edessa,
- Arabic quotations and Homeric knowledge,
- Armenian and Georgian reception.

These form later custody/export lanes, not early primary textual witnesses.

## L. Hittite / Anatolian external controls

Not translations of Homer, but major Bronze-Age external anchors:

- Hittite `Ahhiyawa` ↔ Greek Achaean field
- Hittite/Luwian `Wilusa` ↔ Ilios/Ilion
- western Anatolian conflict records near Troy

These should be compared to Homeric ethnonyms/geography while keeping documentary and poetic witnesses separate.

Anatolia also offers a plausible historical corridor through which Mesopotamian/Hittite literary material could have interacted with early Greek traditions.

## M. Near-Eastern epic comparison

Use:
- Gilgamesh
- Atrahasis
- Hittite literary translations/adaptations of Mesopotamian material
- Homeric epic

as a T3/T4 operator matrix.

Do not encode:
`Gilgamesh → Homer`
as direct translation.

Do encode specific constrained correspondences where evidence supports them:
- companion loss / heroic mortality,
- divine council,
- voyage / boundary crossing,
- fame versus death,
- lament,
- ritual burial,
- return.

## N. Homeric cross-comparison stack

Preferred comparison order:

```text
Linear B / Mycenaean
→ Homeric mixed poetic diction
→ Ptolemaic papyri
→ Alexandrian variants/scholia
→ Venetus A + medieval manuscripts
→ Livius Andronicus Odusia
→ Ilias Latina
→ Epic Cycle / parallel Greek traditions
→ later Syriac/Arabic/Armenian/Georgian reception
→ Near-Eastern structural controls
```

## Benchmark — HOM-01

Choose 100 high-information Homeric lines or formulae.

For each record:
1. Iliad/Odyssey reference,
2. medieval vulgate text,
3. papyrus variant(s),
4. Alexandrian reported variant,
5. scholion,
6. dialect tags,
7. Mycenaean/Linear-B comparison if any,
8. Epic-Cycle parallel if any,
9. Latin Odusia/Ilias-Latina equivalent if extant,
10. semantic operator,
11. meter,
12. preserved/altered/lost/introduced fields,
13. evidence class.

## Benchmark — HOM-02: Odusia Translation Laboratory

Start with surviving Andronicus fragments.

For each:
```text
Homeric Greek
→ literal parse
→ Latin Andronicus
→ literal Latin parse
→ semantic changes
→ cultural substitution
→ metrical change
→ archaizing choice
```

This becomes one of the earliest high-resolution Greek→Latin translation controls in the entire Nexus.
