# Diachronic Translation Lattice

Status: ACTIVE CROSS-CORPUS METHOD
Updated: 2026-09-21

## Principle

Do not compare a source text to one translation.

Compare a **translation lattice** across:
- source-language manuscript states,
- ancient translations,
- medieval translations,
- early modern translations,
- modern scholarly translations,
- multiple target languages.

A translation is both:
1. evidence about the source as understood by a reader in a particular historical setting;
2. evidence about the target culture that received and reformulated it.

## Core state

Represent a translation witness as:

```text
T = (W, Ls, Lt, Ds, Dt, V, G, R, E)
```

where:
- W = work/passage,
- Ls = source language,
- Lt = target language,
- Ds = source date/state,
- Dt = translation date,
- V = source Vorlage/manuscript state if known,
- G = translation genealogy/intermediary,
- R = register/style,
- E = editorial/ideological environment.

## Delta decomposition

For an observed difference, do not assign one cause automatically.

```text
Δ = ΔV + ΔL + ΔT + ΔI + ΔE
```

- ΔV — different source Vorlage / textual state
- ΔL — target-language accommodation
- ΔT — translator choice
- ΔI — target-culture intertextual/ideological overlay
- ΔE — editor, apparatus, or later modernization

## Translation genealogy correction

Translations are not automatically independent witnesses.

Example:
```text
Hebrew
→ Greek
→ Latin
→ vernacular
```

A vernacular translation made from Latin is not independent evidence for the Hebrew reading.

Count lineages, not editions.

For every translation, record:
- direct from source?
- mediated through another language?
- revised against source?
- dependent on a prior translation?
- paraphrase/adaptation?

## Convergence test

If several **independent** translations converge on the same interpretation:
- check whether the source grammar supports it;
- check whether they share a lost/variant Vorlage;
- check whether the semantic range naturally invites that rendering.

Independent convergence can raise confidence in an interpretation.

But if dependent translations share the same phrase, that may merely reflect inheritance from an intermediary translation.

## Divergence test

If translations differ sharply:
- source ambiguity?
- different manuscript/Vorlage?
- language-specific grammar?
- theological/political reinterpretation?
- stylistic domestication?
- translator misunderstanding?

Divergence is evidence to classify, not noise to discard.

## Translation overlay control — Cyropaedia

Cyropaedia 3.1.21:
source sense:
```text
we violate nothing of what Astyages agreed
```

Dakyns/Stawell:
```text
"every jot and tittle"
```

The biblical phrase is target-culture overlay, not source-language intertext.

Therefore compare:
- literal modern English,
- Dakyns/Stawell,
- Loeb,
- French,
- German,
- Latin if available,
- other historical translations.

If only Dakyns introduces "jot and tittle," classify it as translator-specific.
If several unrelated translations independently introduce scriptural exactness imagery, investigate why.

## Technical vocabulary control

For terms such as:
- goēteia / goēteuein,
- anchinoia,
- archē / archōn,
- satrapēs,
- basileus,

record:
1. Greek lemma,
2. literal semantic range,
3. translator rendering,
4. historical target-language connotations,
5. later technical associations.

This prevents modern occult, biblical, philosophical, or political vocabulary from being retrojected into the ancient source.

## Cross-language temporal array

For a passage P build:

```text
P_Greek_source_states
↔ ancient_Latin
↔ Syriac/Armenian/Arabic where extant
↔ medieval/renaissance_Latin
↔ early_modern_vernaculars
↔ 19th-c_translations
↔ modern_critical_translations
```

The goal is not to choose a single "best wording."

The goal is to observe how semantic possibilities move through time.

## Reverse triangulation

Later translations can sometimes help expose:
- an earlier reading now absent,
- an ambiguity already perceived in antiquity,
- an older technical sense,
- a cultural association that has since disappeared.

But later translation evidence cannot by itself override an extant source-language reading.

## Ancient translation priority

Ancient translations can be especially valuable because they are historically closer to lost source states.

Examples:
- Septuagint
- Targums
- Peshitta
- Vulgate
- Hittite/Hurrian translations
- Greek/Latin adaptations
- Ethiopic preservation chains

Always separate chronological proximity from textual independence.

## Cross-corpus use

### Cyropaedia
Track Greek → Latin → early modern → modern translations.
Use for Persian names, offices, customs, and philosophical vocabulary.

### Gilgamesh
Track Sumerian → Akkadian → Hittite/Hurrian and modern translations of each source state.
Do not compare modern English renderings as though they were ancient witnesses.

### Homer
Track Greek manuscript states → Latin adaptations/translations → later vernaculars.
Separate meter accommodation from semantic translation.

### Biblical corpus
Use Hebrew/Aramaic source plurality + LXX/Targum/Peshitta/Vulgate as the principal calibration environment.

### Philosophumena
Compare Greek critical text with older Latin/English/French/German translations.
Flag technical terms where target-language theological or occult vocabulary exceeds the Greek.

## Benchmark — TRLAT-01

For one passage:
1. freeze source-language critical text;
2. list known manuscript variants;
3. assemble translations by date and language;
4. build dependency genealogy;
5. align clause by clause;
6. tag each difference as:
   - SOURCE_VARIANT
   - LANGUAGE_ACCOMMODATION
   - TRANSLATOR_CHOICE
   - TARGET_INTERTEXT
   - EDITORIAL_GLOSS
   - UNRESOLVED
7. count only independent translation lineages;
8. identify semantic invariants and historically introduced overlays.

## Promotion rule

A translation-derived claim is strongest when:
- supported by source-language grammar,
- attested in an early independent translation,
- repeated independently across languages,
- compatible with manuscript history.

A phrase appearing only in one late translation remains evidence about that translator unless additional evidence connects it to the ancient source.
