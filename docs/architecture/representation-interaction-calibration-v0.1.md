# Representation and Interaction Calibration Layer v0.1

Status: ACTIVE_EXPERIMENTAL
Date: 2026-09-22

## Purpose
Extend the Codex reconciliation spine with two complementary historical controls surfaced in the 2026-09-22 analysis:

1. Mesopotamian mathematical witnesses: unfamiliar carrier/notation with recoverable formal operation.
2. Bar-Hebraeus dietary disputation: individually characterized inputs whose conjunction is claimed to produce a non-additive effect.

Together they separate two questions that recur across Codex:
- What survives a change of representation?
- What changes only when states are composed?

## A. Representation Continuation

Core form:

```
R_c(O) -> carrier-specific representation of object/relation O
Decode(R_c(O)) -> candidate invariant I
```

A successful representation-blind recovery preserves I while carrier, notation, basis, or cultural classifier changes.

### Mesopotamian positive controls

MESO-MATH-01 — sexagesimal sqrt(2)
- carrier: Old Babylonian mathematical tablet tradition
- native representation: sexagesimal positional value
- target invariant: square/diagonal numerical relation
- test: remove modern decimal gloss and recover the represented numerical relation from declared sexagesimal rules.

MESO-MATH-02 — square/diagonal reconstruction
- test geometric relation independently from notation familiarity.

MESO-MATH-03 — Plimpton 322 structural control
- recover table structure under competing mathematical interpretations without allowing the modern label "Pythagorean" to perform the classification.

MESO-MATH-04 — representation-blind recovery
- parser receives normalized sign/value/position/operation data but no culture or era label.

MESO-MATH-05 — modern-notation removal
- compare performance with and without modern mathematical restatement.

MESO-MATH-06 — carrier -> operation -> invariant reconstruction
- require explicit return path from native carrier to recovered relation.

Governing rule:

```
NOTATIONAL ALIENNESS != OPERATIONAL ALIENNESS
```

## B. Interaction Continuation

A separate operator is required when composition changes behavior.

For states A and B and measured/claimed effect H:

```
Delta_int(A,B) = H(A compose B) - F(H(A),H(B))
```

where F is the preregistered additive/independent baseline.

A nonzero interaction residual means the compound cannot be modeled from isolated effects under that baseline.

### Bar-Hebraeus control

BH-DIET-01 — fish/milk disputation
- surface: humorous/sophistic physician story
- objects: fish, milk, combined consumption
- conflict: individual wholesomeness vs claimed compound unwholesomeness
- operational question: what causal model permits H(A)=acceptable and H(B)=acceptable while H(A compose B)=unacceptable?
- historical classifiers must remain separate: medical/dietetic, logical/sophistic, communal custom, religious-law comparison.

BH-DIET-02 — preparation transform
- burnt/cooked food stories test whether preparation changes the state before ingestion.

BH-DIET-03 — timing/appetite transform
- distinguish food identity from temporal/contextual admissibility.

BH-DIET-04 — intervention collateral effect
- laxative/medicine stories test target effect vs damage to healthy state.

BH-DIET-05 — classifier migration
- trace a dietary rule across medical, communal, philosophical, ascetic, and religious contexts without treating classifier continuity as proof of common origin.

## C. Integration with Structural Continuation

Extend the conceptual state to:

```
X = (carrier, surface, operator, state, path, composition, interaction_residual, invariant, provenance)
```

Structural Continuation now distinguishes:
- representation transformation: same target relation under changed encoding;
- state transformation: same object after an operator/path;
- composition transformation: multiple states enter a joint system;
- classifier transformation: cultural explanation changes;
- provenance transformation: witness is copied/translated/reframed.

This prevents a recurrent category error: an invariant under representation change need not remain invariant under composition.

## D. Integration with Dual-Use / Protective Gloss

The label-blind parser gains positive controls before being applied to Dee:
- recover known mathematics from unfamiliar Mesopotamian representation;
- recover interaction structure from humorous/nontechnical prose;
- then apply the same operation-first parser to Dee.

DEE-09 therefore becomes a calibrated test rather than a free-standing interpretive exercise.

## E. Organon questions

For every candidate:
1. What is the carrier?
2. What classifier is attached to it?
3. What operation is actually specified or recoverable?
4. Is this a representation change, state change, or composition?
5. What survives?
6. What new residual appears only after composition?
7. Can a label-blind parser recover the same structure?
8. What control or holdout could falsify the recovery?

## Promotion
Promote only when the operator and invariant/residual are reproducible from declared inputs and survive relevant controls. Preserve historical classifier and provenance as coordinates rather than allowing either to substitute for operational evidence.
