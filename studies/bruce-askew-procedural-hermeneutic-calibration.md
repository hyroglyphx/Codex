# Bruce–Askew Codices — Procedural, Hermeneutic, and Witness-Identity Calibration

Status: ACTIVE / SOURCE-CONSULTED RECURSIVE CALIBRATION
Updated: 2026-09-22

## Purpose

Use the Bruce Codex and Askew Codex as calibration witnesses for:
- procedural state transitions,
- seals/names/ciphers as locally scoped credentials,
- diagram + utterance + ritual sequence synchronization,
- internal hermeneutic crosswalks,
- codex-order and title provenance,
- referenced-work identity,
- and the difference between ritual prescription and historically demonstrated performance.

This study is deliberately structural.
It does **not** claim that the codices encode modern signal-processing, information-theory, or computer-science concepts.

---

## 1. Physical codex, textual work, and modern title are separate

### Bruce Codex

The Bruce Codex (Bodleian Bruce 96) is a physical manuscript collection with:
- the texts conventionally called the *Books of Jeu*,
- an Untitled Text,
- fragments,
- multiple hands,
- damaged/missing leaves,
- and a modern editorial ordering reconstructed after the leaves had lost their original sequence.

The title "Books of Jeu" is not written as the title of the whole surviving Bruce text.
The surviving first work ends with a title closer to "The Book of the Great Logos corresponding to Mysteries."

Source controls:
- Schmidt/MacDermot, *The Books of Jeu and the Untitled Text in the Bruce Codex*
- NASSCAL, "Books of Jeu"
- Digital/Bibliographic Bruce 96 descriptions

### Askew Codex

The Askew Codex (British Library Add MS 5114) preserves the work conventionally called *Pistis Sophia*:
- 23 quires,
- 178 folios in the catalogue description,
- missing leaves,
- two scribes,
- multiple textual divisions/books.

The modern umbrella title does not by itself prove that every internal textual unit originally circulated as one work under that title.

British Library:
https://searcharchives.bl.uk/

### Governing distinction

```text
PHYSICAL CODEX
!=
TEXTUAL WORK
!=
INTERNAL TITLE
!=
MODERN SCHOLARLY TITLE
```

This is the manuscript analogue of:

```text
NAME
!=
IDENTITY
!=
ROLE
```

---

## 2. Referenced work != surviving witness

The Askew Codex refers to "two Books of Jeu" and gives them an Enochic revelatory provenance.

Modern scholarship has often identified those referenced books with the texts in the Bruce Codex.

That identification must not be encoded as a certainty.

Hugo Lundhaug explicitly cautions that the Askew reference does not prove that the extant Bruce texts are those exact books; among other differences, Enoch does not appear in the surviving Bruce works in the way the Askew narrative suggests.

At the same time:
- Steve Johnston identifies literary proximity between Askew Book Four and the Bruce *Books of Jeu* and asks whether they may be complementary parts of a larger plan;
- Erin Evans argues that the *Books of Jeu* and *Pistis Sophia* reflect a coherent religious group/system.

Sources:
- Lundhaug, "Fictional books in Coptic apocrypha" (2023)
  https://journals.sagepub.com/doi/10.1177/09518207231152828
- Johnston, "Proximité littéraire entre les codices Askew et Bruce" (2015)
  https://poj.peeters-leuven.be/content.php?id=3132120&url=article
- Evans, *Books of Jeu and the Pistis Sophia: system, practice, and development of a religious group*
  https://era.ed.ac.uk/items/98432d44-2e2e-4134-8362-5a7f03fcba10

### New rule

```text
REFERENCED WORK IDENTITY
!=
EXTANT MANUSCRIPT IDENTITY
```

A title/name correspondence is a relation hypothesis, not a manuscript-equation operator.

---

## 3. Bruce Codex as a procedural credential system

The *Books of Jeu* describe:
- treasuries and ranks,
- diagrams,
- seals,
- names,
- ciphers,
- watchers,
- veils/gates,
- ritual offerings,
- baptisms,
- and ordered passage through regions.

NASSCAL summarizes the revelations as configurations of aeons/treasuries with seals, ciphers and formulas required for passage.

The Schmidt/MacDermot content summary further specifies procedures in which:
- a seal is given,
- a cipher is held,
- a name/formula is spoken,
- watchers/ranks/veils withdraw,
- the practitioner/soul passes to the next region.

Sources:
- https://www.nasscal.com/e-clavis-christian-apocrypha/books-of-jeu/
- https://www.gnosis.org/library/bookss.htm

### Typed state machine

Represent one procedural step as:

```text
X_n
= (
  REGION,
  RANK,
  AUTHORIZATION_STATE,
  SEAL,
  NAME,
  CIPHER,
  UTTERANCE,
  EMBODIED_ACTION,
  GATEKEEPER,
  NEXT_STATE
)
```

Transition:

```text
PREPARE
→ APPLY / POSSESS CREDENTIAL
→ UTTER FORMULA
→ RECOGNITION / WITHDRAWAL
→ CROSS THRESHOLD
→ UPDATE STATE ADDRESS
```

This is a modern structural representation of the text's procedure.

---

## 4. Credential scope is local

A crucial lesson is that a seal/name is not simply a universal magic token.

The texts repeatedly associate credentials with:
- a rank,
- treasury,
- aeon,
- watcher,
- veil,
- or specific transition.

Therefore add:

```text
CREDENTIAL_SCOPE
```

and require:

```text
credential
+ correct jurisdiction
+ correct sequence position
```

before calling two tokens equivalent.

### New rule

```text
SAME TOKEN FORM
!=
SAME AUTHORIZATION FUNCTION
```

if the jurisdiction/state address differs.

---

## 5. Procedural order is non-interchangeable

The Bruce procedures are ordinal.

The structural model should therefore treat the operators as potentially noncommuting:

```text
C_j ∘ C_i(X)
!=
C_i ∘ C_j(X)
```

unless the source demonstrates interchangeability.

This does **not** mean the ancient text formulated noncommutative algebra.

It means our modern parser should preserve the order in which:
- baptism,
- sealing,
- naming,
- invocation,
- passage,
- and recognition

are prescribed.

### Project consequence

```text
RITUAL TOKEN SET
!=
RITUAL PROCEDURE
```

The same ingredients in a different order are not automatically the same operation.

---

## 6. Askew Codex as an internal hermeneutic-crosswalk system

In Books 1–3 of *Pistis Sophia*, Jesus narrates the sufferings/repentances of Pistis Sophia.

Disciples repeatedly answer by giving a scriptural "solution" or interpretation, especially from:
- Psalms,
- Odes of Solomon,
- prophetic material.

A recent study of the canon/library of *Pistis Sophia* catalogues this recurring interpretive procedure.

Source:
- Dylan Burns, "Canon of the Pistis Sophia Books 1–3," *Journal of Theological Studies* 73 (2022)
  https://academic.oup.com/jts/article/73/2/649/6815670

Example internal architecture:

```text
NARRATED REPENTANCE / PRAISE
→ DISCIPLE INTERPRETATION
→ SCRIPTURAL CITATION
→ DECLARED "SOLUTION"
```

This is a real crosswalk **inside the composition**.

But it is not the same kind of evidence as Rosetta.

### New crosswalk class

```text
HERMENEUTIC_CROSSWALK
```

Definition:
an author/text explicitly maps one discourse state to another authoritative text as its interpretation or "solution."

### Dependency warning

```text
authorial self-exegesis
!=
independent external witness
```

Ten scriptural "solutions" in one compositional system do not become ten independent historical confirmations.

---

## 7. Three witnesses — textualized witness architecture

*Pistis Sophia* also presents Philip, Thomas and Matthew as designated writers/witnesses for Jesus' discourses and interprets the "two or three witnesses" formula through them.

This is valuable for the Nexus because it separates:

```text
NARRATIVE WITNESS ROLE
```

from:

```text
MANUSCRIPT INDEPENDENCE
```

A text can *represent* multiple witnesses while surviving in one manuscript tradition.

Therefore:

```text
represented witness count
!=
effective independent witness count
```

This directly reinforces the dependency correction already used in:
- numeral genealogies,
- manuscript families,
- multilingual lexical copies.

---

## 8. Askew seals and bonds — reversible state authorization

Later portions of *Pistis Sophia* describe:
- seals/bonds attached to the soul,
- mysteries that undo bonds/seals,
- seals presented to rulers/regions,
- passage through ordered cosmic domains,
- baptisms and purification.

Primary translation examples:
- chapters 112, 115, 128, 131–132 in the Askew tradition.

This adds a reversible credential operator:

```text
BIND / SEAL
→ STATE CONSTRAINT

MYSTERY / COUNTER-SEAL
→ UNBIND
→ RELEASE
→ PASSAGE
```

Structurally this resembles the reversible embodied operator already found in:

```text
GIRD → capacity up
LOOSEN → capacity down
```

but the historical systems are different and are not genealogically equated.

---

## 9. Bruce–Askew operational overlap

The two corpora share a strong family resemblance at the level of:
- post-resurrection teaching,
- mysteries,
- ascent/passages,
- ordered cosmic regions,
- seals/names,
- baptismal/ritual elements,
- light cosmology.

That overlap is historically relevant.

But current project state should distinguish:

```text
SYSTEMIC / LITERARY PROXIMITY
```

from:

```text
IDENTICAL BOOK IDENTITY
```

and from:

```text
DIRECT TEXTUAL DEPENDENCE
```

### Current evidence typing

```text
shared milieu/system hypothesis        = supported scholarly model
literary proximity                     = supported
Bruce texts = Askew-referenced Jeu     = candidate / disputed
direct one-way textual dependence      = unresolved
```

---

## 10. Prescriptive text != performed ritual

The Bruce texts contain detailed ritual instructions.

Evans argues that the Bruce/Askew corpus reflects a coherent religious community and ritual system.

Still, the Nexus must preserve:

```text
PRESCRIPTIVE RITUAL TEXT
!=
DIRECT ARCHAEOLOGICAL ATTESTATION OF PERFORMANCE
```

Add:

```text
PRACTICE_STATUS
= prescribed | narrated | inferred | externally_attested
```

This prevents procedural detail from being automatically converted into social-history fact.

---

## 11. Manuscript order is an evidentiary variable

The Bruce Codex is particularly important because its leaf order was lost and later reconstructed editorially.

Therefore add:

```text
ORDER_PROVENANCE
```

with values such as:

```text
originally_numbered
quire_reconstructable
editorially_reconstructed
uncertain
modern_binding_order
```

This matters for every sequence analysis.

### Recursive consequence for Byblos

A sequence graph is only as secure as:
- sign segmentation,
- inscription orientation,
- line ordering,
- fragment joining,
- and object reconstruction.

The Bruce Codex demonstrates why **editorial sequence must itself have provenance**.

---

## 12. Graphic token != linguistic grapheme

The Bruce diagrams/seals are meaningful graphic forms, but their function is not simply phonetic writing.

That creates an important warning for Byblos and other undeciphered corpora:

```text
visible recurring sign
!=
phonetic grapheme by default
```

Before assigning phonetic values, test whether a sign could function as:
- grapheme,
- divider,
- emblem,
- seal,
- diagrammatic operator,
- numeral,
- classifier,
- or mixed-role token.

This is not a claim that Byblos contains ritual seals.

It is a **sign-role null** learned from a different documented corpus.

---

## 13. Internal vs external cycle rank

The Ugarit work currently rewards independent cycle closure.

The Askew material shows why cycle type must now be split.

Define:

```text
CR_external
= cycle closure through independently transmitted representations

CR_internal
= cycle closure created within one compositional/hermeneutic system
```

Both are informative.

But:

```text
CR_external
>
CR_internal
```

for claims about historical independence.

Askew's Psalm/Ode "solutions" are powerful evidence for **how the author/community mapped meaning**, not independent proof of the narrated cosmic event.

---

## 14. New operational crosswalk depth

Create a separate procedural scale rather than forcing ritual systems into the linguistic X0–X5 scale:

```text
OX0 = token or symbol only
OX1 = token + named role
OX2 = token + state/jurisdiction
OX3 = token + ordered procedure
OX4 = procedure + recognition/verification event
OX5 = procedure + verified state transition/result
```

The *Books of Jeu* repeatedly reach OX3–OX5 at the literary-prescription level.

This scale records **what the text says the token does**.
It does not prove external performance.

---

## 15. New Nexus variables

```text
CODEX_ID
TEXTUAL_WORK_ID
INTERNAL_TITLE
MODERN_TITLE
TITLE_PROVENANCE
REFERENCED_WORK_ID
EXTANT_WORK_IDENTIFICATION_CONFIDENCE
SCRIBE_ID
QUIRE_ID
ORDER_PROVENANCE
PRACTICE_STATUS
HERMENEUTIC_CROSSWALK
CREDENTIAL_SCOPE
CREDENTIAL_JURISDICTION
CREDENTIAL_SEQUENCE
RECOGNITION_AGENT
FAILURE_MODE
OX_DEPTH
CR_EXTERNAL
CR_INTERNAL
SIGN_FUNCTION_CLASS
```

---

## 16. Recursive lessons for the current queue

### Byblos

Do not assume every recurrent graph node is phonetic.

Before the blind holdout, freeze a sign-role alternative model:

```text
phonetic
vs
boundary
vs
graphic/administrative
vs
mixed
```

without assigning values.

### Ugarit

Keep external multilingual cycle rank separate from:
- internal scribal repetitions,
- copies of the same school text.

This strengthens the current dependency correction.

### Aphek

Treat:
- object-level trilingual lexical crosswalk
separately from:
- site-level multilingual environment.

### Karatepe / Cinekoy

Distinguish:
- direct bilingual semantic equivalence,
- dynastic/onomastic identity,
- regional historical continuity.

The Bruce–Askew lesson is the same:
**a shared name/title does not settle object identity or transmission route.**

---

## Governing compression

```text
TOKEN
→ ROLE
→ JURISDICTION
→ ORDER
→ RECOGNITION
→ STATE TRANSITION
```

and:

```text
REFERENCE
→ IDENTIFICATION HYPOTHESIS
→ WITNESS
→ PROVENANCE
→ DEPENDENCY
→ CLAIM CEILING
```

The first is the procedural lesson.

The second is the manuscript-critical lesson.

Together they strengthen the Nexus without converting symbolic architecture into unbounded historical claims.
