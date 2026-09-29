# Pre-registration: GA-05/GA-07 Marduk Typed-Boundary Experiment

**Lane:** Jethro (independent) · **Date:** 2026-09-29 · **Status:** L4 preregistration (NOT an execution report)
**Relay work item:** 0002 (inbox Message 0002, steward sequence 3)
**Governing constraints:** do_not_merge · do_not_modify_canonical_state · preserve_negative_results ·
separate_arithmetic_identity_from_independent_evidence · do_not_infer_missing_marduk_edges ·
preregister_before_boundary_test · insufficient_data_is_valid_result

This document registers the experiment proposed in report 01 §8 before any boundary inspection.
No edge has been inspected for this test. No GA-05/GA-07 canonical status is altered.
S_49⊕1_g is not promoted.

## 1. Scope and non-goals

**In scope:** a falsifiable comparison of two models of the Marduk closure boundary —
M0 (homogeneous adjunction) vs M1 (typed terminal/gate) — using only source-grounded typed edges
in a frozen sparse historical graph H_M ⊆ G(B_M).

**Out of scope / prohibited:**
- Populating missing H_M edges from inference, analogy, or operator similarity
  (hard constraint; also the bridge minimum rule: never replace a missing historical edge with
  operator similarity).
- Counting possibility-space arithmetic (C(50,2)=1225, C(51,2)=1275, delta 50) as evidence.
  Those numbers describe G(B_M), the possibility space; this test uses only H_M, the sparse
  historical subgraph. GGA governing rule: "No numerical coincidence is promoted merely because
  it exists in G(B)."
- Promoting S_49⊕1_g, 1_c, or 1_r on any outcome of this test.
- Altering GA-05 (DEFINED, NOT POPULATED) or GA-07 (UNRUN) registry status.

## 2. Minimum source-grounded data to instantiate H_M

### 2.1 Node set (must be complete before the test runs)

- **N1–N50:** all fifty literary-sequence name records as MDK-Nxx, one record per transmitted
  name, per `registries/marduk-fifty-names-ingestion-v0.1.yaml` schema: id,
  sequence_or_line_address, name_form, witness, reading_status, function_or_destiny, operator,
  provenance, confidence. Scope: Enuma Elish VI 121–166 through VII 1–144.
- **N51:** record MDK-N51 (Ea, VII 140–142, terminal_record, operator NAME_AS) — already seeded.
- **R0 (rubric record):** a separate record for the closure rubric (VII 143–149: "Fifty" rubric,
  transmission instruction, Marduk as Enlil of the gods). This record does not yet exist; the
  registry lists closure under controls, not records. It must be created as a first-class node
  of a distinct node kind (`kind: rubric`, not `kind: name`) before the test runs.

Current node completeness: 7 of 51 name records seeded; 0 rubric records. **Bar not met.**

### 2.2 Edge admission (frozen)

An edge enters H_M only if all hold:
- (a) its type belongs to the frozen ontology (§3), no other types admissible;
- (b) it carries a witness pointer with line address (Enuma Elish tablet/line, ORACC manuscript,
  or a parallel-witness program source such as PW-GODLIST / PW-ANANUM / PW-MANUSCRIPTS);
- (c) it carries an evidence class in {C0 DIRECT, C1 HISTORICAL, C2 CONTROLLED, C3 MATRIX}
  (bridge protocol classes); C4 STRUCTURAL edges are excluded from the primary test and admitted
  only in a labeled secondary sensitivity analysis;
- (d) broken or missing records remain OMEGA — no edge may be drawn to or from an
  un-ingested name, and no edge may be inferred from the absence of a record.

Edges already annotatable from seeded records (e.g. MDK-N03 IDENTIFY_ASPECT, MDK-N51 NAME_AS)
are record-level annotations, not frozen edges: they enter H_M only after (b) and (c) are
attached.

### 2.3 What H_M is

H_M ⊆ G(B_M) with B_M = {N1…N51, R0}. Undirected for the primary test (typed unordered
relations); directed variants are a declared secondary analysis only if direction is
witness-grounded per edge.

## 3. Frozen edge ontology

Closed list — frozen before any boundary inspection; no type may be added or redefined after
the boundary result is seen.

| ID | Edge type | Source |
|---|---|---|
| E1 | NAME_AS | GGA / identity laboratory |
| E2 | EPITHET_OF | GGA / identity laboratory |
| E3 | IDENTIFY_ASPECT | GGA / identity laboratory |
| E4 | TRANSFER_FUNCTION | GGA / identity laboratory |
| E5 | INHERIT_TITLE | GGA / identity laboratory |
| E6 | SYNCRETIZE | GGA / identity laboratory |
| E7 | SUBSUME | GGA / identity laboratory |
| E8 | DISTINGUISH | GGA / identity laboratory |
| E9 | PROMOTE_STATUS | GGA / identity laboratory |
| E10 | LOCATE_CULT | GGA / identity laboratory |
| E11 | SEQUENCE_PARALLEL | GGA ("explicit sequence/parallel relations") |
| E12 | UNKNOWN_IDENTITY_RELATION | identity laboratory (typed placeholder; counted as its own category, never silently resolved) |

For analysis, types collapse into pre-registered super-categories (sparse-data necessity;
mapping frozen here, not after seeing counts):

- **C-IDENT** = {E1, E2, E3} — identity/aspect relations
- **C-TRANSFER** = {E4, E5} — function/title movement
- **C-SYNCRETIC** = {E6, E7} — merger/subsumption
- **C-STATUS** = {E8, E9} — distinction/promotion
- **C-CULT** = {E10} — cult localization
- **C-SEQ** = {E11} — sequence/parallel
- **C-UNK** = {E12} — unknown, typed

Bridge B-types (B1–B11) may annotate an edge's evidence class but do not create new H_M edge
types. Witness-protocol transformation operators (COPY, REDACT, …) describe manuscript relations,
not name-graph edges, and are out of scope for H_M.

## 4. Partition specification

Three edge partitions, defined before inspection:

- **P-INT (field-internal):** both endpoints in {N1…N50}.
- **P-T51 (name-51-incident):** at least one endpoint is N51 (Ea). Includes N51–Ni edges and,
  if attested, N51–R0 edges (classified here, not under the rubric, to keep the name/rubric
  distinction clean).
- **P-RUB (rubric-incident):** at least one endpoint is R0, excluding N51–R0 edges (which sit in
  P-T51). Edges between R0 and Ni (i ≤ 50) capture the rubric's relational role — e.g. the
  "Fifty" naming act itself.

**Name-51 vs rubric separation (mandatory):** N51 is an onomastic record (a name with a
destiny/function: "control the sum of Ea's rites; administer Ea's decrees"). R0 is a
paraliterary record (a closure rubric and transmission instruction). They are different node
kinds. Collapsing them would repeat exactly the harmonization the registry forbids ("Do not
silently force the literary Fifty rubric to equal the transmitted record count"). The primary
test pools P-T51 ∪ P-RUB as **P-CLO (closure-incident)**; the three-way split is reported
descriptively and tested separately where sub-partition data bars are met.

## 5. Models

**M0 — homogeneous adjunction.** N51 is ordinary with respect to edge-type distribution; the
closure is a literary/rubrical fact with no typed relational signature. The 51st node contributes
incidence, not type-distinction. Prediction: the type distribution over P-CLO is
indistinguishable from P-INT up to sampling noise.

**M1 — typed terminal/gate.** Terminal/closure incidence carries a distinguishable edge
signature: P-CLO is systematically enriched in transfer/status/closure-instruction types
(C-TRANSFER, C-STATUS, and rubric-anchored C-SEQ) relative to P-INT. Prediction: significant
divergence of the P-CLO type distribution from P-INT, with the enrichment direction as stated.

**What each outcome licenses:**
- Reject M0-homogeneity (both primary tests significant, §6) → the field⊕distinguished-terminal
  *type* is promoted to TESTED for the Marduk case. It does not promote S_49⊕1_g (different
  field, different n), 1_c, or 1_r.
- Fail to reject → negative result, preserved: M1 remains GENERATED/OMEGA. Failure to reject is
  not proof of M0 (sparse-data caveat recorded).
- Data bar unmet → INSUFFICIENT DATA: a valid terminal outcome, not a failure.

## 6. Statistics and null models

All statistics use typed edge labels only. No arithmetic-coincidence counting: the
possibility-space counts (1225, 1275, delta 50) do not enter any statistic.

### S1 — primary: Fisher exact test of partition × type independence

Contingency table: rows {P-INT, P-CLO}, columns {C-IDENT, C-TRANSFER, C-SYNCRETIC, C-STATUS,
C-CULT, C-SEQ, C-UNK}. Two-sided Fisher exact (chi-square is not pre-registered: cell counts
will be small). Alpha 0.05.

### S2 — secondary, directional: closure enrichment

2×2 table: rows {P-INT, P-CLO}, columns {C-TRANSFER ∪ C-STATUS, all other types}. One-sided
Fisher exact (enrichment at closure, the M1 direction). Alpha 0.05, Holm-adjusted with S1.

### Null models (permutation; GGA geometry-laboratory discipline)

- **N-A (label permutation):** fix the typed edge multiset and node set; permute the "terminal
  name" designation over the 51 name records (rubric fixed — rubric-hood is not exchangeable
  with name-hood). Statistic: total-variation distance between the P-CLO type distribution and
  the P-INT type distribution. 10,000 permutations; p = fraction ≥ observed. Tests whether N51's
  incident-type signature is extreme among all name records.
- **N-B (type shuffle):** fix graph structure and partition; shuffle edge-type labels among
  edges preserving the global type multiset; recompute the S1 statistic; p likewise. Tests
  whether type concentration at the boundary exceeds chance given type frequencies.
- **N-C (degree-preserving rewire):** conditional on ≥40 frozen edges; rewire preserving degree
  sequence, reassign types from the global multiset. Pre-registered as likely infeasible under
  sparsity; if infeasible, record OMEGA-for-this-null rather than substituting an easier null.

**Law-against-law check:** S1/S2 are decidable under both M0 and M1 (each model makes a
distinct distributional prediction); N-A/N-B supply the independent constraint (exchangeability
nulls, not arithmetic); the frozen ontology supplies the third (type categories fixed before
inspection, so post-hoc re-typing cannot manufacture significance).

## 7. Minimum-data bar and sufficiency gates

The test may run only if all hold; otherwise return INSUFFICIENT DATA:

- **B1 node completeness:** all 51 name records + 1 rubric record exist per schema §2.1 with
  line addresses. (Now: 7/51, 0 rubric → FAIL.)
- **B2 edge volume:** ≥30 frozen edges total; ≥8 edges in P-CLO; ≥4 in P-T51 and ≥4 in P-RUB
  for the three-way sub-analysis (if a sub-partition falls short, that sub-analysis alone
  returns INSUFFICIENT DATA while the pooled test may still run).
- **B3 per-edge provenance:** every edge satisfies §2.2(b)–(c). Zero inferred edges (§2.2(d)).
- **B4 type coverage:** ≥3 distinct super-categories present in each of P-INT and P-CLO;
  otherwise the signature comparison is degenerate.
- **B5 rubric independence:** R0's record must not be derived from N51's record (no double
  counting of the Ea material as both name and rubric).

**Current assessment:** bar not met (B1, B2, B3 fail). The pre-registered outcome for the
present Codex state is **INSUFFICIENT DATA**. The experiment is valid; execution is blocked
pending ingestion completion. This agrees with the steward's sequence-3 finding and is recorded
as a result, not a postponement.

## 8. GA-07 relationship

GA-07 (`MDK-50-51 / count_sensitivity`) currently holds an arithmetic baseline only:
literary 50 → 1225 pairs, transmitted 51 → 1275, delta 50 edges. That baseline is a property of
the possibility space G(B_M) and does **not** constitute a run.

**Definition (frozen):** the completed GA-07 run is exactly the execution of this
preregistration's test (§§2–7) against a frozen H_M meeting the data bar, with the M0/M1
decision recorded per §5. Until then GA-07 remains **UNRUN / NOT RECOVERED AS RUN**.

Prediction ledger stub (GGA schema):

- prediction_id: GA-07-PRED-001
- training_witnesses: Marduk ingestion seed records MDK-N01…MDK-N51 (partial)
- declared_operator: typed-boundary comparison per this preregistration
- predicted_relation: P-CLO type distribution diverges from P-INT (M1) — registered as the
  directional alternative, not as an expectation
- target_holdout: frozen H_M edge set (not yet existent)
- success_metric: S1 + S2 significant at Holm-adjusted 0.05 with N-A/N-B confirmation
- timestamp/commit: 2026-09-29 / relay sequence 3
- result: NOT RUN — INSUFFICIENT DATA (pre-registered)

## 9. Operational definition of 1_r (frozen; NOT tested)

**D-1R-v0.1:** A recursive-return increment (1_r) is a single completed RETURN TO WITNESS cycle
in the Organon workflow that appends exactly one OrganonEvent bearing a non-empty `return_path`
field to the append-only provenance spine.

Operationalization (frozen with the definition):
- (a) **Cycle delimitation:** a cycle is the event sequence in the provenance log from one
  RETURN TO WITNESS marker to the next. Delimitation must be mechanical from log markers; any
  researcher-discretionary segmentation fails criterion (i) below.
- (b) **Count:** within each cycle, count appended OrganonEvents with non-empty `return_path`.
- (c) **Test statistic:** fraction of cycles with count exactly 1, over ≥10 observed cycles.
- (d) **Falsification criteria** (any one retires 1_r as a Codex typing):
  - (i) cycles cannot be delimited without discretionary choices → 1_r is GENERATED-ornamental;
  - (ii) observed fraction < 0.8 with ≥10 cycles → the "increment" does not hold;
  - (iii) `return_path` empty/absent in >50% of events → the field is not a counter.

**Status:** GENERATED/OMEGA. **Not tested in this report** — the definition is frozen here so a
future test cannot move the goalposts. Recorded (untested) prediction: the definition fails on
(ii) and probably (iii), because the Codex appends variable numbers of events per correction
and `return_path` is a path field, not a counter (cf. report 01 §9.4). A prediction is not a result.

## 10. Negative-result and status ledger

Preserved regardless of outcome:

| Item | Status after this preregistration |
|---|---|
| GA-05 H_M | DEFINED, NOT POPULATED (unchanged) |
| GA-07 | UNRUN — arithmetic baseline only (unchanged) |
| M0 homogeneous adjunction | null model, retained |
| M1 typed terminal/gate | GENERATED/OMEGA (unchanged by preregistration alone) |
| S_49⊕1_g | GENERATED/OMEGA (not promotable by this test) |
| 1_c fixed center | GENERATED/OMEGA (unchanged) |
| 1_r return increment | GENERATED/OMEGA; definition D-1R-v0.1 frozen, untested |
| Boundary test execution | INSUFFICIENT DATA (valid outcome) |

## 11. Judgment calls disclosed

1. **Rubric as a separate node (R0, kind: rubric).** The registry lists closure under controls,
   not records; I require its promotion to a record. Justification: the partition the test needs
   (name-51 vs rubric) cannot be computed otherwise, and the registry's own anti-harmonization
   rule demands the distinction be representable.
2. **Super-category collapse (7 categories).** With sparse historical edges, 12 raw types would
   leave the contingency table degenerate. The mapping is frozen here, before inspection, to
   block post-hoc re-typing.
3. **Data-bar numbers (30/8/4/4 edges, 3 categories).** Power-motivated judgments for Fisher
   exact on a 2×7 table, not derived from Codex text. If the steward's ingestion yields a
   different sparsity regime, the bar may be revised only by a new preregistration, not
   mid-analysis.
4. **C4 exclusion from primary.** Structural-only edges would confound a historical-signature
   test; they enter only the labeled secondary analysis (bridge minimum rule: C4 allowed only
   if explicitly labeled as such).
5. **N-A permutes terminal-name designation over name records only.** Rubric-hood is not
   exchangeable with name-hood; permuting it would test a meaningless null.
6. **Directional secondary (S2).** Pre-registered to avoid HARKing: the TRANSFER/STATUS
   enrichment direction comes from MDK-N51's own recorded function ("control the sum of Ea's
   rites; administer Ea's decrees"), stated before any edge is inspected.
7. **N51–R0 edges classified under P-T51.** Keeps every rubric-incident edge in P-RUB free of
   name-51 influence, so the rubric's independent signature is measurable.

---

*Preregistration only. No boundary inspected, no edge inferred, no status altered, no promotion
performed. The valid outcome for the present Codex state is INSUFFICIENT DATA — recorded here
in advance so it cannot later be mistaken for a failed test.*
