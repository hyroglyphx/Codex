# MDK Identity Laboratory v0.1

Status: active benchmark
Updated: 2026-09-22

## Purpose

The Marduk/Merodach corpus tests whether Codex can represent **qualified identity** without collapsing it into unrestricted equivalence.

Core distinction:

```
X identified with Marduk under function/domain F
!=
X is globally identical to Marduk
```

This extends the Codex Witness Protocol from carrier/readout transformations to identity/name/function transformations.

## Historical controls

The benchmark is grounded in three well-attested features of the Marduk corpus:

1. Old Babylonian Marduk was syncretised with Asalluhi and Tutu, while some Old Babylonian witnesses still distinguish Asalluhi and Marduk.
2. Enuma Elish VI-VII grants Marduk a climactic sequence conventionally called the Fifty Names; scholarship notes that the transmitted sequence contains fifty-one names while the literary program insists on fifty, traditionally Enlil's divine number.
3. The names are coupled to destinies/functions and participate in Marduk's elevation; the final sequence explicitly relates Marduk to Enlil's former status.

These are controls for typed historical identity, not a license to equate every associated deity globally.

## Typed identity operators

- NAME_AS(entity, name, witness, phase)
- EPITHET_OF(name, entity, domain)
- IDENTIFY_ASPECT(source_entity, target_entity, function, witness, phase)
- TRANSFER_FUNCTION(source, target, function, witness, phase)
- INHERIT_TITLE(source, target, title, witness, phase)
- SYNCRETIZE(a, b, witness, phase, scope)
- SUBSUME(source, target, scope, witness, phase)
- DISTINGUISH(a, b, witness, phase)
- PROMOTE_STATUS(entity, from_status, to_status, witness, phase)
- LOCATE_CULT(entity, place, sanctuary, witness, phase)
- UNKNOWN_IDENTITY_RELATION(a, b, witness)

All identity edges require scope and provenance.

## MDK-01 — Functional Identification

Question:
Can Codex preserve a statement of the form:

```
deity X -> Marduk-as(function F)
```

without promoting it to:

```
X == Marduk everywhere
```

Required fields:

```yaml
source_entity:
target_entity: Marduk
operator:
function:
scope:
witness:
date_or_phase:
reading:
confidence:
counter_witnesses: []
promotion_state:
```

A counter-witness distinguishing the entities remains first-class evidence.

## MDK-02 — Fifty Names / Name-Destiny Graph

Model:

```
Marduk
 -> Name_i
 -> gloss/explanation_i
 -> destiny/function_i
 -> inherited or asserted authority_i
```

The graph must preserve:

- sequence position
- manuscript witness
- name form
- philological reading
- explanation/destiny
- associated prior deity where historically supported
- numerical/list position
- variant or broken readings
- relation to other god lists/commentaries
- uncertainty

The conventional label "Fifty Names" is retained as the literary category even where the counted sequence is analyzed as fifty-one.

### Number/status control

Do not encode:

```
50 = Marduk
```

globally.

Encode the historical symbolic relation:

```
50 --associated_divine_number--> Enlil
50 --appropriated/status_signal_in(Enuma_Elish)--> Marduk
```

with witness and scholarly interpretation attached.

## MDK-03 — Spatial Instantiation

Initial path:

```
Marduk
 -> Babylon
 -> Esagila
 -> cultic/architectural address
 -> textual witness
```

Reverse traversal must also work:

```
Esagila
 -> sanctuary occupant/function
 -> Marduk
 -> names/aspects
 -> witnesses supporting each edge
```

This joins identity topology to the Esagila text-to-geometry pipeline.

## MDK-04 — Borsippa / Tutu bridge

Tutu is a critical bridge because Borsippa and Marduk's name-complex meet in a historically typed syncretic relation.

Required representation:

```
Tutu
 -> patron/cultic association: Borsippa
 -> syncretic relation: Marduk
 -> appearance in Marduk name tradition
```

The graph must retain temporal phase so that later identity does not erase earlier/local distinction.

## MDK-05 — Contradiction preservation

Permitted state:

```
Witness A: DISTINGUISH(Asalluhi, Marduk)
Witness B: SYNCRETIZE(Asalluhi, Marduk)
Witness C: NAME_AS(Marduk, Asalluhi-derived designation)
```

Codex does not resolve these by majority vote. Organon asks which transformation, date, genre, location, and function account for the difference.

## Invariant Forge question

For any identity cluster, compute:

```
I = what survives across
    name change
    cult transfer
    function transfer
    syncretism
    geographic relocation
    recension
    commentary
```

Possible output invariants:

- function
- cult center
- genealogy
- title
- ritual role
- numerical status
- cosmological role
- lexical name
- iconographic marker

No invariant is assumed in advance.

## Promotion tests

A proposed identity edge must answer:

1. Which witness asserts it?
2. What operator best describes the relation?
3. In what phase?
4. In what domain/function?
5. Does another witness distinguish the entities?
6. What prediction follows from the proposed relation?
7. Does an independent witness satisfy that prediction?

## Integration

```
Nexus
 -> Codex Witness Protocol
 -> MDK Identity Laboratory
 -> Esagila spatial graph
 -> Borsippa restoration/cult graph
 -> Organon
 -> Invariant Forge
 -> GlyphWalk / Atlas
```

This laboratory turns divine names into a rigorous test case for typed historical identity rather than a flattened synonym table.


## MDK-06 — Office / Function Separation

The recovered Sumerian control set adds a useful structural distinction:

```
LUGAL = holder / king
NAM-LUGAL = kingship / office-state
ME = function / office / responsibility / capacity
```

This is a calibration, not a direct etymological claim about Marduk.

The identity graph must therefore preserve:

```
ENTITY
!= NAME
!= OFFICE
!= FUNCTION
!= AUTHORIZED_CAPACITY
```

A transferred function or inherited title does not by itself prove global entity identity.

Required fields:

```yaml
holder:
office:
function:
authorized_capacity:
name_or_title:
source_entity:
target_entity:
witness:
phase:
scope:
counter_witnesses: []
```

Positive control:
`registries/sumerian-operator-morphology-control-v0.1.yaml`.

Test:
Can Codex move an office/function through a historical identity graph while preserving holder distinction, phase, and counter-witnesses?
