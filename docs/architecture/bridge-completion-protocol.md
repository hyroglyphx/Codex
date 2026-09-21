# Bridge Completion Protocol — Translation / Transposition Graph

Status: **ACTIVE ARCHITECTURE**  
Updated: **2026-09-20**

## Purpose

Connect the remaining corpus without forcing every relation into genealogy or direct borrowing.

A valid connection is a **typed edge** with:

```text
source
→ bridge mechanism
→ target
→ evidence class
→ preserved information
→ altered information
→ loss
→ introduced material
→ return path
```

The default rule is:

> Prefer a documented translation, bilingual/trilingual parallel, or historically attested transposition before using a long speculative jump.

## Bridge alphabet

### B1 — DIRECT_TRANSLATION
A target text is produced as a translation of a source-language textual tradition.

Examples:
- Hebrew → Septuagint Greek
- Hebrew/Aramaic textual tradition → Targumic Aramaic
- biblical source traditions → Syriac/Peshitta
- Hebrew/Greek biblical traditions → Latin/Vulgate

### B2 — PARALLEL_WITNESS
Two or more languages encode the same inscriptional/institutional proposition.

Examples:
- Letoon: Lycian | Greek | Aramaic
- Behistun: Old Persian | Elamite | Babylonian
- Rosetta: hieroglyphic | Demotic | Greek
- Karatepe/Cinekoy: Phoenician | Luwian
- Pyrgi: Phoenician | Etruscan

### B3 — RECENSION_RECOMPOSITION
Inherited material is reorganized, expanded, condensed, or synthesized into a new literary state.

Examples:
- Sumerian Gilgamesh stories → Akkadian epic traditions
- Old Babylonian → Standard Babylonian Gilgamesh
- Atrahasis flood tradition → later Akkadian flood reuse

### B4 — READOUT_TRANSPOSITION
Carrier persists while language-specific reading changes.

Examples:
- Sumerograms in Akkadian/Hittite contexts
- Akkadograms in Hittite
- inherited sign conventions with local lexical readout

### B5 — MODE_SCRIPT_TRANSPOSITION
Language or information survives a change in script or representational mode.

Examples:
- Luwian cuneiform ↔ Hieroglyphic Luwian
- Mycenaean/Arcadocypriot syllabic Greek → alphabetic Greek
- Egyptian hieroglyphic/Demotic → Coptic alphabetic evidence

### B6 — LEXICAL_CALQUE_BORROWING
A word, title, formula, or construction crosses a contact boundary by borrowing or semantic calque.

This bridge must record whether the carrier, meaning, or both move.

### B7 — FUNCTION_OPERATOR_TRANSPOSITION
The lexical/narrative carrier changes while a constrained operation survives.

Examples:
- BOUNDARY → PRESERVE → RETURN
- CHAOS/UNDIFFERENTIATED → SEPARATE → ORDER
- FOREIGN CARRIER → LOCAL ADAPTATION → INSTITUTIONAL INCORPORATION

This is a structural connection, not automatically a claim of direct textual descent.

### B8 — INSTITUTIONAL_LITURGICAL_CUSTODY
A language or form is preserved because an institution continues to use it after ordinary speech changes.

Examples:
- scribal Sumerian in later Mesopotamia
- liturgical/scriptural Hebrew, Greek, Syriac, Latin, Sanskrit
- ritual Hattic/Hurrian material embedded in Hittite archives

### B9 — SUBSTRATE_RESIDUE
A displaced or lost language survives through phonology, morphology, place names, lexical islands, or specialized vocabulary.

### B10 — DIALECT_GENEALOGICAL_TRANSPOSITION
Known inherited material is followed through regular diachronic transformation.

This is the correct bridge for secure family relations such as:
- Hurrian ↔ Urartian
- Etruscan ↔ Lemnian ↔ Raetic
- Mycenaean → later Greek
- Old Indo-Iranian branches

### B11 — STRUCTURAL_CONTROL
No historical transport is asserted. The comparison exists to measure convergence, universality, or false positives.

Examples:
- Sumerian E.GAL versus Egyptian pr-ꜥꜣ "great house"
- distant agglutinative controls
- Vedic operator parallels where transmission is not established

## Evidence classes

- **C0 DIRECT** — direct translation, bilingual/trilingual witness, or securely linked textual relation.
- **C1 HISTORICAL** — established historical contact, genealogy, borrowing, recension, or custody.
- **C2 CONTROLLED** — reproducible transposition with chronology/contact constraints but no direct source-target witness.
- **C3 MATRIX** — shared cultural/contact field; direct dependence unresolved.
- **C4 STRUCTURAL** — operator/formal correspondence only.
- **C5 CANDIDATE** — useful hypothesis awaiting tests.

## Minimum bridge rule

To connect node A to node Z:

1. find the shortest path whose edges are independently admissible;
2. prefer C0/C1 edges;
3. preserve each intermediate language and witness;
4. never replace a missing historical edge with operator similarity;
5. allow a C4 structural edge only if it is explicitly labeled as such;
6. record competing paths when more than one is plausible.

A chain may therefore be strong even when one remote relationship is not direct:

```text
A --C0--> B --C1--> C --C3--> D
```

The weakness belongs to the relevant edge, not to the whole graph indiscriminately.

## Scriptural spine calibration

The biblical witness family is the project's best translation calibration set because it permits repeated comparison of related propositions across languages.

For passage P:

```text
P_H = Hebrew
P_G = Greek
P_A = Aramaic
P_S = Syriac
P_L = Latin
```

Track:

```text
preserved
expanded
compressed
omitted
reframed
transliterated
calqued
syntactically relocated
legally/theologically refunctionalized
```

This empirical deformation grammar becomes a reference for older or less directly documented transpositions.

## Completion criterion

A major corpus node is considered **CONNECTED** when it has at least one path to the evidence spine satisfying:

- explicit bridge type at every edge,
- chronology,
- geography/contact context,
- source pointer or declared structural-only status,
- preserved/altered/lost/introduced fields,
- confidence/evidence class,
- return path.

Nodes may remain connected through C4 structural controls without being historically linked.

## Research principle

```text
translation preserves proposition imperfectly
transposition preserves selected invariants imperfectly
genealogy preserves inherited structure through change
custody preserves carriers across social discontinuity
loss itself is evidence
```

The graph must record all five.
