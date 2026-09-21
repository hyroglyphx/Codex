# Crosswise Resolution & Covariance Benchmark

Status: ACTIVE / BENCHMARK
Updated: 2026-09-21

## Purpose

Turn the new Arity–Compression and Synchronous-State modules into an actual crosswise test.

The core question is not whether two forms look alike. It is whether multiple representation systems expose compatible transformations of the same hidden or partially hidden linguistic state.

```text
REPRESENTATION A
      ↘
       LATENT / SHARED STATE
      ↗
REPRESENTATION B
```

The project therefore tests:

```text
surface resemblance
-> structural correspondence
-> transformation covariance
-> cycle consistency
-> bounded reconstruction
```

The strongest relation is not sameness of surface form but stability of the transformation law.

---

## 1. First crosswise result: script medium and encoding logic are separable

### Egyptian

Early Egyptian writing gives a single script environment in which one sign may function as:

- logogram,
- uniliteral phonogram,
- biliteral phonogram,
- triliteral phonogram,
- classifier/determinative,
- or part of a phonetic-complement construction.

The Oriental Institute / ISAC summary of early Egyptian writing reports:

- a near-complete set of uniliteral consonantal signs by ca. 3100–3000 BCE;
- a large set of biliteral values before the Third Dynasty, ca. 2750 BCE;
- increasing use of phonetic and semantic complementation as writing expanded its functional range.

This is not a simple historical ladder from picture -> one consonant -> two -> three.
The roles coexist.

### Mesopotamian cuneiform

Proto-cuneiform begins as a highly context-dependent administrative system.
CDLI describes a later shift toward partial phonetic coding, with the more systematic use of phonetic writing becoming apparent by the mid-third millennium.

ORACC sign-list resources show the mature cuneiform system as a mixture of:

- word signs / logograms,
- syllable signs / phonograms,
- polyvalent signs with multiple word and syllable values.

The script was adapted to Akkadian in the middle of the third millennium BCE.

### Ugarit: decisive control

Ugarit is the clean control because the same material technology—wedge-shaped writing on clay—hosts a radically different encoding strategy.

At Late Bronze Age Ugarit:

```text
Akkadian
-> logo-syllabic cuneiform

Ugaritic
-> alphabetic cuneiform / abjad
```

The Ugaritic alphabet has 30 cuneiform signs, mostly representing consonantal phonemes.

Therefore:

```text
MATERIAL MEDIUM != ENCODING GRANULARITY
```

A change in representational resolution does not require a change from clay to ink, or from wedges to linear characters.

This makes Ugarit a high-value TRANSVERSE control.

---

## 2. Spectral order versus historical order

The current evidence supports a representational spectrum:

```text
whole-sign semantic/logographic carrier
-> syllabic / multi-phoneme carrier
-> consonant-explicit carrier
```

but does not establish a universal historical sequence for spoken language.

Required distinction:

```text
SPECTRAL PRECEDENCE
= one representation is more compressed than another

HISTORICAL PRECEDENCE
= one state is demonstrably earlier in time
```

The first may generate a hypothesis for the second.
It cannot substitute for chronology.

---

## 3. Expressivity–Resolution Coupling

Egypt and Mesopotamia independently show a useful historical tendency:

```text
restricted/context-heavy use
-> wider communicative burden
-> increased phonetic specification
```

CDLI explicitly describes phonetic coding as allowing cuneiform to represent information previously transmitted orally and to support new text types.

The early Egyptian record likewise shows writing representing more aspects of language as its functional range widened, accompanied by increasing phonetic and semantic complementation.

Candidate general operator:

```text
EXPRESSIVITY DEMAND
-> REPRESENTATIONAL DECOMPRESSION
-> HIGHER PHONETIC EXPLICITNESS
```

Status: STRUCTURAL / COMPARATIVE.
This is not a claim that all writing systems follow one evolutionary path.

---

## 4. Root arity is independent of sign arity

Egyptian provides a strong control against equating sign count and root length.

James P. Allen notes that early Egyptian includes roots of two and four-to-six radicals, while almost two-thirds of verbal roots in the Pyramid Text corpus are triconsonantal. Egyptian also preserves productive-looking expansions such as reduplication.

Therefore:

```text
one sign may encode three consonants
while
one language may contain roots of several arities
```

The two dimensions must remain independent.

---

## 5. Semitic biradical -> triradical hypothesis: keep live, do not universalize

The hypothesis that many Semitic triradicals preserve older biconsonantal kernels has a substantial history in Semitic scholarship, but a universal biradical Proto-Semitic lexicon is not established.

Current project posture:

```text
C1C2 -> C1C2X
C1C2 -> C1C2C2
C1C2 -> XC1C2
```

are admissible candidate transformations only when supported by:

- recurrent morphology,
- regular sound correspondence,
- semantic clustering,
- attested alternation,
- historical distribution,
- or another independent constraint.

No third radical is stripped merely because doing so creates a resemblance.

Current H-S-S benchmark:

```text
Akkadian Ḫ-S-S
Ugaritic Ḫ-S-S
-> test whether a deeper Ḫ-S kernel is historically licensed
```

Status remains CANDIDATE until morphology and comparison support it.

---

## 6. Indo-European / Vedic control: root enlargement is a real independent mechanism

Indo-European research provides an independent control for shorter/longer root relations.

Historical Sprachforschung 131 includes a dedicated root-extension section. Alexander Lubotsky specifically analyzes Sanskrit:

```text
hi-   "impel, hurl"
hiṣ-  "injure, harm"
hīḍ-  "make/be angry"
```

in relation to Indo-European root enlargements in -s- and -d-.

The importance for Nexus is methodological:

```text
compact root + consonantal extension
```

is a historically recognized linguistic mechanism outside Semitic.

It does not prove that Semitic triradicalism arose the same way.
It gives an independent mechanism-control.

---

## 7. Ancient crosswalks: use the ancients' own synchronization tables

The strongest crosswise evidence comes from corpora where ancient scribes themselves provide a mapping.

### Ebla

ORACC/DCCLT notes that mid-third-millennium Ebla preserves the earliest known cuneiform sign list with reading glosses.

This is an ancient calibration object:

```text
SIGN
-> DECLARED READING
```

### Ugarit

The Ugaritic abecedary KTU 5.14 is especially important.
The Mnamon database notes that individual Ugaritic consonants are paired with Akkadian syllabic signs intended to render their pronunciation.

This is effectively an ancient cross-script phonetic crosswalk:

```text
UGARITIC CONSONANT
<-> AKKADIAN SYLLABIC APPROXIMATION
```

### High-confidence calibration family

Use as primary Nexus calibration anchors:

- Ebla sign/readout lists,
- Ugaritic consonant/Akkadian-syllable crosswalks,
- Sumerian/Akkadian lexical lists,
- Rosetta hieroglyphic/Demotic/Greek,
- Behistun Old Persian/Elamite/Babylonian,
- Tell Fekheriye Akkadian/Aramaic,
- Karatepe/Cinekoy Phoenician/Luwian,
- Letoon Lycian/Greek/Aramaic.

These witnesses allow the system to learn transformation behavior from historically anchored cross-representations before projecting into uncertain corpora.

---

## 8. Concordant Redundancy: a major crosswise operator

Egyptian phonetic complements repeat consonantal information already contained inside biliteral or triliteral signs.
Determinatives constrain semantic class.

Cuneiform likewise can pair logographic writing with phonetic complementation or reading aids.

This creates:

```text
DENSE CARRIER
+ REDUNDANT PHONETIC SIGNAL
+ SEMANTIC CLASSIFIER
-> DISAMBIGUATED READOUT
```

The Books of Jeu present a structurally comparable—but historically distinct—multimodal procedure:

```text
NAME
+ SEAL
+ CIPHER
+ SEQUENCE
-> RECOGNIZED / ADMISSIBLE STATE
```

The comparison is operator-level only.

Generalized operator:

```text
CONCORDANT REDUNDANCY
= multiple partially independent channels constrain one admissible interpretation/state
```

This is an error-correction analogy, not a claim of ancient information theory.

---

## 9. Classifier / guardian boundary analogy

A second crosswise relation appears at the boundary of interpretation.

### Linguistic system

```text
carrier + determinative/classifier
-> admissible semantic class
```

### Ritual ascent system

```text
identity + name/seal/cipher
-> admissible threshold passage
```

Shared structural operator:

```text
PAYLOAD
+ TYPE / CREDENTIAL
-> BOUNDARY VALIDATION
```

Relation type: STRUCTURAL CONTROL.
No historical dependence is implied.

---

## 10. Crosswise Covariance Test

For two representations A and B of a target state:

```text
A --T_A--> A'
B --T_B--> B'
```

test whether the known A<->B relation predicts A'<->B'.

Equivalently, for three mapped representations:

```text
A -> B -> C
A ------> C
```

compare:

```text
T_BC(T_AB(A))
with
T_AC(A)
```

A model gains strength when the two routes converge.

This is CYCLE / PATH CONSISTENCY.

---

## 11. Prospective Divergence Gradient

For a candidate relation between A and B:

```text
D_AB(t) = distance( T_AB(A(t)), B(t) )
```

track the rate:

```text
dD_AB/dt
```

Interpretation:

- low divergence across phonology + morphology + semantics + chronology:
  stronger shared historical structure;
- low divergence only in surface phonology:
  resemblance remains weak;
- rapid semantic or morphological divergence:
  candidate edge is retyped or sent to SURGERY.

This formalizes the earlier project principle that the strongest correspondence is a shared change-law, not a static match.

---

## 12. Root-kernel experiment

For every proposed biconsonantal kernel K = C1C2:

1. collect all roots preserving C1...C2 in declared positions;
2. separate real morphology from arbitrary consonant deletion;
3. group by chronology and language;
4. score semantic clustering;
5. identify the apparent extension consonant and position;
6. compare with random consonant-pair controls matched for frequency;
7. test whether earlier witnesses show lower arity more often;
8. measure semantic divergence through later branches;
9. preserve failures.

Primary hypotheses:

### H1
True historical kernels should show more semantic coherence than frequency-matched random two-consonant windows.

### H2
Extension consonants should show non-random positional or functional behavior.

### H3
If root enlargement is historical, older independent witnesses should improve—not degrade—the reconstruction.

### H4
A genuine kernel should survive cross-language transformation better than a chance surface substring.

---

## 13. New high-value index

Every token in the arity experiment should carry:

```text
WITNESS
LANGUAGE
SCRIPT
SIGN_ROLE
GRAPHIC_ARITY
PHONETIC_LOAD
ROOT_ARITY
MORPHOLOGICAL_SEGMENTATION
SEMANTIC_VECTOR
CLASSIFIER
DATE
PLACE
CONTACT
CROSSWALK_WITNESS
RELATION_TYPE
EVIDENCE_CLASS
NEGATIVE_CONTROL
RESIDUE
```

Derived measures:

```text
COMPRESSION = information carried per visible sign
ROOT_VISIBILITY = explicit radicals / reconstructed radicals
REDUNDANCY = repeated constraints across channels
COVARIANCE = stability of mapped change
DIVERGENCE = rate at which mapped states separate
```

---

## 14. Immediate benchmark sequence

### Benchmark A — Egyptian internal spectrum
Construct matched examples of:

```text
logogram
uniliteral
biliteral
triliteral
phonetic complement
determinative
```

and score compression / redundancy / root visibility.

### Benchmark B — Ugarit dual-script control
Compare the same administrative or lexical domain where possible across:

```text
Ugaritic alphabetic cuneiform
vs
Akkadian logo-syllabic cuneiform
```

The material medium is approximately held constant while encoding logic changes.

### Benchmark C — Ancient crosswalk calibration
Train admissible transformation weights first on Ebla, Ugaritic/Akkadian, Rosetta, Behistun, Tell Fekheriye, Karatepe/Cinekoy, and Letoon.

### Benchmark D — Root enlargement
Run Egyptian, Semitic, and Indo-European root-arity tests independently, then compare the transformation signatures.

### Benchmark E — Multimodal concordance
Compare Egyptian phonetic/classifier redundancy with Books of Jeu name/seal/cipher redundancy only at the operator level:

```text
multiple channels -> constrained state
```

---

## 15. Current result

The first crosswise pass supports three claims at different evidence levels.

### Strong
Writing systems can distribute the same linguistic burden across radically different carrier granularities.

### Strong
Phonetic explicitness and semantic/classifier redundancy can coexist; "more phonetic" does not simply mean "less symbolic."

### Candidate
The representational spectrum from dense whole-sign carriers toward more decomposed phonetic carriers may provide a useful model for investigating historical root-arity expansion, but script decomposition cannot by itself establish spoken-language chronology.

The project should therefore search for:

```text
HOMOGENY OF CHANGE
rather than
IDENTITY OF FORM
```

and promote a historical relation only when crosswise transformation remains stable under independent witnesses and negative controls.

---

## Sources / calibration references

- Andréas Stauder, "The Earliest Egyptian Writing," ISAC/Oriental Institute:
  https://isac.uchicago.edu/sites/default/files/uploads/shared/docs/oimp32.pdf
- James P. Allen, *The Ancient Egyptian Language*, Cambridge University Press:
  https://www.cambridge.org/core/books/ancient-egyptian-language/ancient-egyptian/1F2D538F620D2D16C6A0FE02EC99F0CE
- CDLI, "The Origins of Writing as a Problem of Historical Epistemology":
  https://cdli.earth/articles/cdlj/2006-1
- ORACC, Introduction to Cuneiform Sign Lists:
  https://oracc.museum.upenn.edu/dcclt/signlists/signlists/
- ORACC/DCCLT sign-list bibliography, including the Ebla reading-gloss tradition:
  https://oracc.museum.upenn.edu/dcclt/signlists/bibliography/
- Philip Boyes, "Writing and Social Diversity in Late Bronze Age Ugarit":
  https://www.repository.cam.ac.uk/handle/1810/336736
- William M. Schniedewind and Joel H. Hunt, *A Primer on Ugaritic*, Cambridge University Press:
  https://www.cambridge.org/core/books/primer-on-ugaritic/grammatical-precis/EE93864F48F81761AFE2D98345AFB57D
- Mnamon, Ugaritic writing system and KTU 5.14:
  https://mnamon.sns.it/index.php?id=30&lang=en&page=Scrittura
- Alexander Lubotsky, "Sanskrit roots hi-, hiṣ-, hīḍ- and the Indo-European root enlargements -s- and -d-," *Historische Sprachforschung* 131:
  https://www.jstor.org/stable/27032365
- Erin M. Evans, *Books of Jeu and the Pistis Sophia*, University of Edinburgh:
  https://era.ed.ac.uk/handle/1842/9438
- Schmidt / MacDermot, *The Books of Jeu and the Untitled Text in the Bruce Codex*, Brill:
  https://brill.com/display/title/7045


---

## 16. Rosetta Nexus / Parallax Levels

The calibration family is now formalized in:

`registries/rosetta-nexus-calibration.yaml`

The useful analogy to the Parallax cave model is not a ladder of certainty but a ladder of **representation distance**.

```text
PX0  same occurrence, multiple roles
PX1  same object, script/register shift
PX2  same object, cross-language
PX3  co-located object set, parallel/near-parallel
PX4  same text/event, distributed objects
PX5  explicit scribal crosswalk
PX6  archival / recensional relay
PX7  structural control only
```

A PX level never substitutes for evidence class.

The crosswise engine therefore records two independent coordinates:

```text
PARALLAX DISTANCE
x
ALIGNMENT GRANULARITY
```

Alignment granularity ranges from:

```text
sign
-> phoneme/syllable
-> lexeme/name
-> phrase/formula
-> clause/sentence
-> proposition
-> section
-> document/event
```

This lets a Rosetta-like witness be used at several scales at once.

### Required Rosetta Nexus variables

Every calibration witness should now record:

```text
NEXUS_ID
OBJECT_ID
CARRIER_CLASS
MATERIAL_SUBSTRATE
OBJECT_COUNT
COLOCATION
SPATIAL_LAYOUT
LANGUAGES
SCRIPTS
REGISTERS
PARALLAX_LEVEL
ALIGNMENT_GRANULARITY
CROSSWALK_EXPLICITNESS
PARALLELISM_TYPE
SAME_REFERENT
SAME_PROPOSITION
SAME_LEXICALIZATION
TRANSLATION_DIRECTION_KNOWN
ANCHOR_TYPES
OMISSION_EXPANSION_REORDERING
DAMAGE_PROFILE
TRANSFORM_VECTOR
COVARIANCE
CYCLE_CONSISTENCY
DIVERGENCE_RATE
RESIDUE
EVIDENCE_CLASS
CALIBRATION_WEIGHT
ONTOLOGY_CLAIM_CEILING
```

### Why this matters

A monument or tablet can be treated as a multi-angle observation of one institutional, linguistic, or semantic state.

The correct operation is not to flatten the versions into one "translation."

It is:

```text
VIEW_1
VIEW_2
VIEW_3
   ↓
ALIGN BY ANCHOR AND GRANULARITY
   ↓
MEASURE PRESERVATION / DIVERGENCE
   ↓
RECONSTRUCT THE CONSTRAINED SHARED STATE
```

This is the historical-linguistic analogue of using several projections to constrain a hidden geometry.

### Primary Rosetta Nexus set

- Memphis / Rosetta
- Behistun
- Tell Fekheriye
- Karatepe / Cinekoy
- Letoon
- Pyrgi
- Ebla sign and lexical lists
- Ugarit KTU 5.14
- Sumerian–Akkadian lexical traditions
- Egyptian–Hittite treaty tradition

The set deliberately mixes stelae, rock inscriptions, statues, tablet corpora, gold tablets, and distributed diplomatic copies so that material carrier and encoding behavior can be separated.
