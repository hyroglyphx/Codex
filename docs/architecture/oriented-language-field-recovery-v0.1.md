# Oriented Language Field Recovery Bridge v0.1

Status: ADOPTED_LEGACY_ARCHITECTURE  
Date: 2026-09-23  
Recovered source: The Oriented Language Field Volumes I–XVII  
Scope: Linguistic Core / Experiment Harness / Representation Interaction / Structural Continuation / Learning

## Purpose

Recover the parts of the Oriented Language Field (OLF) architecture that were not yet represented in the current Codex branch.

This bridge imports the tested structural machinery, not every historical UI or curriculum detail.

## 1. Carrier chain

OLF models language as a chain of typed carrier views:

```
L = (P, A, C, G, O, Y, M)
```

where:

- P phoneme/articulatory state;
- A acoustic signal;
- C cymatic/apparatus-conditioned visualization;
- G glyph/sign;
- O orientation/layout;
- Y syntax/role order;
- M meaning/context.

No coordinate defines another coordinate.

The cymatic lane remains experimental and apparatus-conditioned; it cannot supply lexical meaning.

## 2. Multi-view analysis object

```
R = (
  witness,
  acoustic_view,
  cymatic_view,
  glyph_view,
  syntax_view,
  transforms,
  nuisance_variables,
  uncertainty,
  decision,
  failure_state
)
```

A missing view is UNKNOWN, not inferred agreement.

## 3. Variance decomposition

Observed variation should be decomposed into:

```
candidate signal
+ carrier/context
+ speaker/apparatus/scribe/reader
+ residual
```

The strongest plausible nuisance variable must be held out before promotion.

## 4. Metric family

Recover the OLF metrics as optional experiment outputs:

```
W = within-class dispersion
B = between-class separation
Q = B/(W+epsilon) invariance ratio
L_nuisance = held-out nuisance leakage
C_view = cross-view concordance
O_sens = orientation sensitivity
Y_role = role-recovery accuracy
T_return = round-trip retention
```

No metric becomes a universal score.

## 5. Nuisance gate and late fusion

Views are calibrated independently before fusion.

Forbidden:

```
raw acoustic + glyph + syntax + image vectors
-> one opaque similarity embedding
```

Preferred:

```
view-specific quality gate
-> nuisance estimate
-> calibrated evidence
-> late fusion
```

## 6. Transport-loss vector

Promote the OLF transport-loss vector:

```
Lambda = (
  phonetic,
  morphological,
  semantic,
  pragmatic,
  orientation,
  provenance
)
```

No scalar average may hide a catastrophic loss in a dimension required by the claim.

This complements ASL-W4.3's non-compensatory relation vector.

## 7. Decision grammar

Add reusable experiment outcomes:

```
PASS
FAIL
INCONCLUSIVE
REPAIR
QUARANTINE
```

These are experiment decisions, not historical truth labels.

They coexist with:

```
OBSERVED -> CANDIDATE -> TESTED -> CORROBORATED -> CANONICAL
FAILED / CONTRADICTED / SUPERSEDED / OMEGA
```

## 8. Corpus quality states

Recover:

```
SEED
REVIEWED
GOLD
REPAIR
INCONCLUSIVE
QUARANTINE
```

A GOLD lexical record requires source lock and independent adjudication.

Multiple valid dialect/variety forms may remain parallel rather than being normalized into one answer.

## 9. Human review as typed witness

A reviewer judgment is evidence about:
- speaker;
- variety;
- register;
- session;
- context.

It is not automatically the single correct form for a whole language.

Review conflicts remain explicit.

## 10. OLF-72 / 64+8 kernel

Retain as a curriculum/benchmark architecture, not ancestry evidence.

The older design contains:
- 64 practical concept roles;
- 8 operator/reflection roles.

A separate 72-form seed matrix aligned twelve roles across six working languages.

Use only after exact source, sense, register, and review state are attached.

## 11. Transport holonomy

For a closed transport path Gamma returning to witness space:

```
H_Gamma(W) = Delta(W, Gamma(W))
```

Use a vector-valued return defect:

```
H_Gamma = (
  H_phon,
  H_morph,
  H_sem,
  H_prag,
  H_orient,
  H_prov
)
```

This gives Structural Continuation a quantitative return audit.

## 12. Path divergence

Two paths sharing nominal endpoints may preserve different information.

```
P(Gamma1,Gamma2 | W)
=
Delta(Gamma1(W), Gamma2(W))
```

Endpoint equality does not imply path equality.

## 13. Semantic curvature / noncommutativity

For transforms A and B:

```
K(A,B | W)
=
Delta(B(A(W)), A(B(W)))
```

Non-zero K means operation order contributes measurable information/loss at the declared resolution.

This bridges directly to the current representation-interaction residual.

## 14. Admissible geodesics

The shortest transform path need not be the most faithful.

Define a claim-specific path cost:

```
Gamma*_c = argmin_Gamma C_c(Gamma)
```

subject to:
- provenance;
- evidence;
- reversibility;
- carrier requirements;
- mandatory relation dimensions.

## 15. Ariadne Trace Condition

A reversible claim must retain enough ordered path information to reconstruct the required return.

```
reach(target)
AND
recover(exit)
```

A result that reaches a target but cannot reconstruct the route is incomplete for reversible tasks.

## 16. Identity / proof / carrier holonomy

Recover the triad:

```
H* = H_C + H_I + H_P
```

conceptually as three separate audits:
- carrier return;
- declared identity return;
- proof/evidence return.

Do not collapse them into one scalar.

## 17. Prior admissibility gate

Before holonomy testing, an operator must be:

```
TYPED
-> OBSERVABLE
-> ADMISSIBLE
-> CLOSABLE
-> BOUNDARY-COMPATIBLE
```

This is the OLF XVII "prior-gate" correction.

It fits the current Experiment Analysis Harness:

```
TYPE
-> OBSERVE
-> ADMIT
-> OPERATE
-> CLOSE
-> TRANSPORT
-> RETURN
-> CERTIFY
```

## 18. Integration map

- ASL-W4.3 supplies relation-specific historical gates.
- Linguard supplies form/segmentation/semantic admissibility.
- Experiment Analysis Harness supplies preregistration, competitors, holdout, and result/interpretation separation.
- Representation Interaction supplies composition residuals.
- OLF supplies nuisance control, loss vectors, round-trip metrics, path divergence, holonomy, and noncommutativity.
- Structural Continuation supplies the cross-domain abstraction.

## Governing rule

> A transport is not characterized only by its endpoints. Its carrier views, nuisance variables, ordered transforms, loss vector, return defect, and failure state are part of the result.


## 19. Distributed holonomy / Volume XVI

Volume XVI extends witness transport to a changing system whose members, capabilities, route graph, information, legitimacy, residue, memory, and mission may all change together.

Canonical distributed state:

```
E_t=(Carrier,Capability,Graph,Info,Legitimacy,Residue,Memory,Mission)
```

Key additions:
- distributed continuity = required relations remain recoverable after change;
- carrier can be an active coordination operator;
- handoff has role, tacit-memory, coordination, authority, and observer defects;
- route topology can change after passage;
- return is generally non-inverse;
- mission completion is not world restoration;
- a certificate is not a remedy;
- role labels may depend on observer, jurisdiction, time, and relation.

Controlling supplement:
`docs/architecture/distributed-holonomy-capability-ecology-v0.1.md`.
