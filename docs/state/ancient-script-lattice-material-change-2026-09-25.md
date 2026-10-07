# Ancient Script Lattice — Material Change 2026-09-25

## Scope

Two new witnesses materially affect OBJ-006 and OBJ-001.

## OBJ-006 — Tell Fekherye / KAI 309

The artifact geometry is now explicitly part of provenance:

- Assyrian-dialect Akkadian: 38 lines, statue front.
- Aramaic: 23 lines, statue back.
- Opening portions correspond closely.
- Second half diverges more substantially.

A project-library witness states that the text is most likely based on an
Aramaic prototype and cites Greenfield & Shaffer (1983). Existing project
calibration already preserved a competing "double bilingualism" model, with
possible local changes of translation direction by section. Other contemporary
review literature has also argued Assyrian priority.

Therefore the lattice must not replace one global arrow with another.

Canonical update:

```
DIRECTIONALITY = SECTION-LEVEL VARIABLE
```

and every derived relation must record:

```
face + language + exact line range + edition/reconstruction + local directionality model
```

The prior symmetric OBJ-006 label "Akkadian ↔ Aramaic transport/control anchor"
is too coarse. The object remains an anchor, but the relation family is:

```
PARALLEL BILINGUAL
+ LOCAL DIRECTIONALITY
+ INTERNAL DIVERGENCE
```

Word-by-word phonological correspondences must be re-audited. Translation
equivalence does not become etymological equivalence.

## OBJ-001 — Byblos title tradition

Yehimilk / KAI 4 is inserted as an independently identified Phoenician waypoint
in the tenth-century BCE Byblos sequence.

The comparison lane should therefore be waypointed:

```
Amarna-era Akkadian bēltu ša Gubla
-> Yehimilk KAI 4 Phoenician bʿlt gbl
-> later Byblian Phoenician title witnesses
```

This narrows a previous long chronological jump. Exact KAI 4 orthography and
sign forms must be compared before promoting phonological continuity.

## Non-evidential update

Later GlyphWalk exports are duplicate/near-duplicate renderings of already
indexed inscription/transliteration material. They do not constitute
independent witnesses and do not change exact-sign relations.

## New controls

```
TRN-17 = SECTION_LEVEL_BILINGUAL_DIRECTIONALITY
PROV-01 = FACE_LANGUAGE_LINE_RANGE_PROVENANCE
CHRON-01 = DATED_INTERMEDIATE_WAYPOINT
CTRL-03 = DUPLICATE_EXPORT_NOT_INDEPENDENT_WITNESS
```
