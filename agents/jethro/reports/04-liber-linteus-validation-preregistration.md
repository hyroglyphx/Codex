# Liber Linteus Validation Preregistration (report 04)

**Lane:** Jethro independent research, Codex relay sequence 5.
**Status of report 03:** frozen L4 discovery artifact at commit `52525c5`. Nothing in this
report rewrites its claims in place; corrections are recorded here as challenges/corrections.
**This pass is validation/preregistration, not a new decipherment pass.**
**Column XI was not inspected, recovered, or sought in any form during this pass.**

## 0. Scope and non-goals

This report implements the steward audit corrections from inbox Message 0004:

1. Downgrade the operator-test conclusion to what the evidence secures.
2. Freeze the D0/D1/D2 data layers and the transformation ledger (machine-readable).
3. Gate inferential statistics on frozen D2; descriptive counts stay layer-labeled.
4. Protect Column XI as a prospective holdout with a frozen prediction manifest.
5. Restate recurrence ≠ decipherment as a standing rule.
6. Specify the executable reference pipeline W0 → … → ResultPacket.
7. Inherit the GA-07 statistical corrections from Work Item 0002.
8. Correct the 1_r scope: D-1R-v0.1 tests the event-counter interpretation only.

Non-goals: no new transcription, no Column XI recovery, no semantic decipherment claims,
no alteration of report 02 or report 03, no canonical registry changes.

## 1. Operator-test downgrade — challenge/correction C-1

**Challenge to report 03 §15:** the sentence-equivalent "the operator test thus **confirms**
the Structural Continuation premise" overclaims. The evidence secures repeated lexical modules
(F-A, F-B, F-C) occurring in changed neighborhoods. It does **not** secure identical ritual
function across those neighborhoods, nor does it secure distinct ritual *phases* in any
semantic sense — "phase" in report 03 is a structural description of the recurrence pattern,
not an independently attested ritual state.

**Replacement wording (binding on future L4 claims):**

> **STRUCTURALLY CONSISTENT WITH path-dependent return; ritual-state continuation remains
> CANDIDATE/OMEGA pending independent semantic evidence.**

What the current evidence does secure:

- Module identity under the D1 skeleton layer (verbatim and near-verbatim multi-token
  recurrence with fixed internal order — ATTESTED as recurrence).
- Neighborhood variance: the associational matrix around F-A differs per column
  (DERIVED from D1 counts).
- The *negative* finding stands and is the methodologically load-bearing one: recurrence
  does not license functional identity.

What it does not secure:

- That two F-A occurrences realize the same ritual act, the same officiant role, or the
  same liturgical phase in any semantic sense (all CANDIDATE at best, mostly OMEGA).
- Any mapping from the operator's six slots (carrier → ritual position → operation →
  object/recipient → temporal/address marker → recurrence/return) to historical ritual
  reality. The operator table is a GENERATED analytic scaffold, and its slot-fillers for
  "operation" and "object/recipient" are UNKNOWN/CANDIDATE throughout report 03.

**Standing rule:** no future report may promote a structural-consistency finding to a
continuation claim without an independent semantic bridge (bilingual, comparative ritual
text, or archaeological correlate) recorded under the Bridge Completion Protocol.

## 2. Frozen data layers and deterministic ID schemes

### 2.1 Layer definitions

- **W0 (witness):** the physical carrier (linen book, 12 columns, red/black ink) and the
  scholarly edition as published artifact. For this pass, W0 = Krall 1892 editio princeps
  as scanned (Internet Archive), edition-level facts only.
- **D0 (raw):** OCR/diplomatic extraction exactly as observed — the `raw` column of
  `token_inventory.tsv`, 1,277 rows. No correction, no normalization.
- **D1 (skeleton):** the normalized layer used for recurrence clustering — the `skeleton`
  column: ASCII case-fold plus the OCR-special mapping (`&`→`T`; `ä/ö/ü/ß/§/$/Ä`→`S`;
  `^` dropped). This mapping is a *convention*, and its interpretive guesses
  (e.g. `&`→`T` presuming a dental) are recorded per-row in the ledger, never silently.
- **D2 (scholarly tokenization):** reconstructed tokenization and calibrated orthography.
  D2 exists this pass **only** as (i) the type-level calibration rows in
  `d2_transformation_ledger.tsv` (the §4.1 segmentations, §4.3 unanalyzed carriers, M-1/M-2/M-3
  promotions, suffix census), and (ii) explicit OMEGA rows where D2 is not determinable.
  There is no token-complete D2. Any claim of a token-complete D2 before E-1 plate
  verification is GENERATED until the ledger says otherwise.

### 2.2 Deterministic ID schemes (frozen)

- **Address ID:** `LL.{COL}:{LINE}`, e.g. `LL.VII:5`. Missing line address in OCR →
  `LL.{COL}:?` (deterministic given the missing value), e.g. `LL.III:?`.
- **Token ID:** `{LAYER}.LL.{COL}:{LINE}#{NNN}`, e.g. `D0.LL.VII:5#003`,
  `D1.LL.VII:5#003`. `NNN` is the 1-based index of the token in `token_inventory.tsv`
  file order *within* its (col, line) group, zero-padded to 3 digits. D0 and D1 share the
  index because they are 1:1 row-aligned by construction.
- **D2 type-level targets:** `D2.TYPE.{name}` for calibration rules applying to a token
  type (source_token_ids lists every matching D1 token ID).
- **OMEGA targets:** `OMEGA.{name}` (e.g. `OMEGA.sibilant_identity`,
  `OMEGA.column_XI_holdout`).

D0/D1/D2 rows join deterministically on these IDs. Any future re-OCR must either preserve
this scheme or ship an explicit ID-remap table; silent re-indexing is prohibited.

### 2.3 Transformation ledger format (frozen)

`d2_transformation_ledger.tsv` columns:

`source_token_ids | target_token_id | operation | preserved | altered | lost | introduced |
witness | address | confidence | rationale`

Operation vocabulary (closed): `verbatim`, `skeleton_normalize`, `scholarly_segmentation`,
`unanalyzed_carrier`, `unresolved_calibration`, `structural_promotion`, `pattern_census`,
`information_loss`, `holdout`, `negative_result`.

**Rule (binding):** never silently merge OCR fragments because a formula makes the intended
reading plausible. Every merge, split, glyph normalization, line reassignment, or emendation
is a ledger row with `preserved/altered/lost/introduced` filled and a confidence no higher
than the evidence supports. Where a D2 decision cannot be made machine-readable from
available evidence, it is an OMEGA row — not an invented row.

**Ledger census this pass:** 1,305 rows — 1,277 D0→D1 (1,008 verbatim, 269
skeleton_normalize) + 28 D1→D2/OMEGA rows (9 scholarly_segmentation, 9 unanalyzed_carrier,
3 structural_promotion, 1 pattern_census, 3 unresolved_calibration, 1 information_loss,
1 holdout, 1 negative_result). Confidence distribution: 1,101 high / 152 medium / 33 low /
7 UNKNOWN / 6 OMEGA / 2 STRUCTURE / 2 CANDIDATE / 1 SOURCE GAP / 1 NEGATIVE.

## 3. Statistical gating rule

- **Descriptive counts** from D0/D1 (frequencies, co-occurrence windows, verbatim n-gram
  censuses) may remain, **labeled with their input layer** in every table and caption.
- **No inferential recurrence/morphology statistics on prose-calibrated D2** until D2 is
  frozen machine-readably (token-complete ledger, E-1 verified). Report 03's E-3/E-4/E-5
  are therefore **declared but not yet runnable**; their declarations are frozen below.
- **Any E-3/E-4/E-5 inferential test must declare** its input layer, the frozen
  transformation provenance (ledger file + commit), the statistic, the null model, the
  random seed, and the iteration count — before execution.

### Frozen test declarations

| Test | Input layer | Statistic | Null | Seed | Iterations | Status |
|---|---|---|---|---|---|---|
| E-3 formula permutation | D1 | max formula length (7,4,4) | token shuffle within columns, line breaks kept | 20260929 | 10,000 | DECLARED |
| E-4 etnam positional control | D1 | positional entropy vs next-10 frequent tokens | permutation of token positions | 20260930 | 10,000 | DECLARED |
| E-5 suffix productivity | D1 | -ri/-leri type/token ratio | random segmentation null | 20261001 | 10,000 | DECLARED |

Seeds are calendar-derived fixed integers (YYYYMMDD), frozen here. If a future run needs
more iterations, the seed and count change only by new preregistration, not by silent edit.

## 4. Column XI holdout protocol

1. Predictions P-1…P-8 (report 03 §12) are frozen at commit `52525c5`.
2. `prediction_manifest.json` (8 predictions; exact text; discovery/training data with
   layer + commit + addresses/base rates; operational success/failure/indeterminate
   criteria; source commit `52525c5`) **must be committed before any Column XI recovery
   or inspection.**
3. Predictions are not alterable after XI exposure. Post-exposure analysis may add *new*
   predictions; it may not edit the frozen eight.
4. XI is the holdout test set for P-1…P-5 (internal). P-6…P-8 (external) test against
   other Etruscan witnesses.
5. **Absence of XI content is a SOURCE GAP, not a failure** — except where the prediction's
   precondition is structural (XI exists as a column), in which case absence of the
   predicted carrier is the recorded outcome. The manifest states the indeterminate
   conditions per prediction.

## 5. Recurrence ≠ decipherment — standing rule

Formula recurrence under a chosen transcription layer may establish **module identity and
ordering**. Semantic function requires an **independent bridge** (comparative linguistic,
textual-external, or archaeological). Functional labels (congregational/actional/invocational
for F-A/F-B/F-C; "temporal operator" for *nunθen*; "libation" for *vinum*) are **not
promotable on recurrence or null-test success alone** — a significant E-3/E-4/E-5 result
strengthens the structural claim only. This rule binds all future LL passes.

## 6. Executable reference pipeline spec

```
W0 witness
 -> D0 raw                      (OCR/diplomatic extraction; ledger operation: verbatim/diplomatic_capture)
 -> D1 skeleton                 (normalization convention; ledger: skeleton_normalize rows)
 -> D2 scholarly tokenization   (calibration rules + OMEGA rows; ledger: scholarly_segmentation, ...)
 -> features                    (n-gram censuses, positional entropy, suffix type/token — descriptive, layer-labeled)
 -> frozen predictions          (prediction_manifest.json at source commit)
 -> null tests                  (declared tests with frozen seeds/iterations; input layer + ledger provenance declared)
 -> ResultPacket                (resultpacket_schema.json)
```

Each transformation exposes `preserved / altered / lost / introduced` and provenance
(witness, address, commit, ledger row IDs) per the Bridge Completion Protocol. The
ResultPacket schema requires: `packet_id`, `produced_at`, `source_commit`, the pipeline
stage list, `test_declarations` (input_kind descriptive|inferential, input layer, ledger
commit, seed, iterations, statistic, null), `test_results` (outcome, statistic_value,
p_value, interpretation, layer_state), and `ledger_ref`. SOURCE_GAP / OMEGA / NEGATIVE
are first-class `outcome` values, not error states.

## 7. GA-07 statistical corrections (inherited from Work Item 0002)

### 7.1 Exact algorithm for the 2×7 test — frozen

Report 02 §6 S1 specifies "two-sided Fisher exact" on a 2×7 table without an algorithm.
**Frozen decision:** the S1 p-value is computed by **Monte Carlo exact approximation of
the Fisher–Freeman–Halton test**, `B = 1,000,000` replicates, **seed `20260929`**,
two-sided (probability-ordering of tables).

**Feasibility justification:** with ≥30 frozen edges over a 2×7 table, full FFH enumeration
via the network algorithm cannot be guaranteed tractable before the data exist; the Monte
Carlo exact variant is always executable, declared, seeded, and reproducible. At
B=1,000,000 the Monte Carlo standard error on p̂ is at most 0.0005 (worst case p=0.5,
far smaller near the α=0.05 boundary), so accept/reject decisions at α=0.05 are stable.
The FFH full-enumeration p-value is the reference estimand the approximation converges to;
if a future implementation computes it exactly and disagrees at the decision boundary,
that discrepancy is itself a recorded result, not a silent substitution.

### 7.2 Permutation null seeds — frozen

N-A (label permutation): 10,000 permutations, **seed `20261002`**. N-B (type shuffle):
10,000 permutations, **seed `20261003`**. N-C stays conditional per report 02 §6
(OMEGA-for-this-null if infeasible under sparsity).

### 7.3 The 30/8/4/4 gates are heuristic, not power-demonstrated

Report 02 §7's minimum-data bar (≥30 edges total / ≥8 closure-incident / ≥4 per
sub-partition, plus B1/B3/B4/B5) is a **disclosed heuristic gate**, not demonstrated
statistical power. Before execution, run a **prospective power simulation**:

- Simulate typed edge tables under M0 (homogeneous) and under M1 with closure-enrichment
  odds ratios {2, 3, 5} at exactly the gate counts.
- Estimate power of S1+S2 (Holm-adjusted, α=0.05) by Monte Carlo (≥10,000 replicates,
  seed frozen in the execution preregistration).
- **Decision rule:** if power < 0.8 at OR=3, the gates are inadequate and execution is
  blocked pending a **new preregistration** — report 02 is never edited in place.

### 7.4 Naming: GA-07A / GA-07B

**GA-07** is preserved as the parent `count_sensitivity` benchmark. The combinatorial/count
sensitivity (50→1225, 51→1275, delta-50 arithmetic) stays **GA-07A** pending
steward/canonical naming approval. The typed historical-boundary experiment preregistered
in report 02 becomes the child experiment, provisionally **GA-07B**. The child does not
silently replace the parent benchmark.

## 8. 1_r scope correction

D-1R-v0.1 (report 02 §9) stays frozen. It tests the **event-counter interpretation** of 1_r
only. All L4 analysis must use provisional labels:

- **`1_r.event`** — the D-1R-v0.1 interpretation: one RETURN TO WITNESS cycle appending
  exactly one return_path-bearing OrganonEvent; falsifiable by the (i)/(ii)/(iii) criteria.
- **`1_r.phase`** — the distinct phase-return interpretation:
  `X = (x, k, m) → R(X) = (x, k+1, m')`, with `π(RX) = π(X)` and `RX ≠ X`
  (return preserves projection, changes state).

**Failure of D-1R-v0.1 must not be treated as falsifying `1_r.phase`.** Evidence aimed at
one definition cannot retire the other. The phase formulation stays GENERATED/OMEGA until
independently operationalized and preregistered — which has not happened in this pass.

## 9. Descriptive vs inferential; first-class outcomes

Every future quantitative claim carries its input layer (D0/D1/D2) and, for inferential
tests, its frozen seed, iteration count, and ledger provenance. The following are
first-class results, recorded in the ResultPacket `outcome` field and never recast as
missing data:

- **SOURCE_GAP** — witness or carrier unavailable (Column XI; Krall certainty layer).
- **OMEGA** — underdetermined by available evidence (ś/θ/χ identity for ~60% of tokens;
  red-ink function; *eslem* numeral candidacy).
- **NEGATIVE** — the test ran and the effect was absent (zero secure numerals in
  1,277 tokens; INSUFFICIENT DATA at the GA-05 bar). A negative result is a finding.

## 10. Judgment calls disclosed

1. **Monte Carlo exact over FFH full enumeration** for S1 (§7.1): chosen for guaranteed
   executability pre-data; the approximation is declared and seeded rather than leaving
   "Fisher exact" underspecified. If the steward requires full enumeration, that is a new
   preregistration.
2. **Calendar-derived seeds** (20260929–20261003): arbitrary but fixed and memorable;
   no seed was tuned to data (no data have been run).
3. **Type-level (not token-level) D2 rows**: a token-complete D2 would require inventing
   1,277 calibration decisions; the ledger instead freezes exactly what report 03 decided
   and marks the rest OMEGA. This makes D2's incompleteness machine-readable rather than
   prose-implied.
4. **`&`→`T` and `{ä,ö,ü,ß,§,$,Ä}`→`S` mappings flagged medium-confidence**: the D1
   skeleton convention bakes in glyph guesses; the ledger records them as `altered` with
   the underlying glyph marked `lost`, so no downstream test can mistake D1 for observation.
5. **P-4 partial-success criterion**: confirming the restriction to śacnic-/śpur- is
   scored as informative-but-weaker rather than binary, because a restriction confirmation
   still constrains the morphology.
6. **OR=3, power 0.8 as the gate-adequacy bar** (§7.3): conventional, disclosed, and
   revisable only by new preregistration.

## 11. What this pass leaves OMEGA (explicit)

- Token-complete D2 (pending E-1 plate verification).
- Exact sibilant/dental-fricative identity for the collapsed tokens.
- Any semantic content of the formulae beyond carrier recurrence.
- Ritual-state continuation in any sense stronger than structural consistency (§1).
- The `1_r.phase` formulation (GENERATED/OMEGA; unoperationalized).
- GA-07B's power at the current gates (pending the §7.3 simulation).

---

*End of validation preregistration. Four deliverables: this report;
`data/liber-linteus/d2_transformation_ledger.tsv` (1,305 rows);
`data/liber-linteus/prediction_manifest.json` (8 frozen predictions);
`data/liber-linteus/resultpacket_schema.json` (ResultPacket schema).
Column XI was not inspected in any form. Report 03 and commit 52525c5 remain frozen.*
