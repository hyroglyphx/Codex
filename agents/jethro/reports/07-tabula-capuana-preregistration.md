# Tabula Capuana independent-replication preregistration (report 07)

**Lane:** user-directed. **Status:** FROZEN — no TC text ingested before this commit.
**Experiment identity:** `LL_discovery → TC_independent_replication`. This is a separate
experiment from the Column XI holdout chain
(`52525c5 → 8d9b933 → Pass 2 → XI still sealed`). The two must not bleed together.

## 0. Pre-freeze knowledge statement

The TC hypotheses below were generated from LL discovery (reports 03/05, E-4/E-5
aftermath) and published scholarship (van der Meer 2007, 2014/15; Steinbauer/Rix on
*vacil*), as specified by the scope authority. The Wikipedia Tabula Capuana transcription
was read during leads review; the frozen candidate forms, operational criteria, and
decision thresholds below were NOT tuned against it. Thresholds are preregistered
conventions, not power-demonstrated — same standing as report 04's heuristic gates.

## 1. Corpus plan (post-freeze ingestion only)

- **W0_TC:** van der Meer 2014/15, "Some comments on the Tabula Capuana" (Studi Etruschi
  77), primary; Cristofani 1995 as secondary where legibility differs. The Wikipedia
  transcription is a convenience copy, never the authority.
- **D1_TC:** the frozen D1 normalization rules from report 04 §2.1, applied unchanged —
  cross-text comparability requires identical normalization.
- **Token schema extension:** red-ink rulings/diacritics (LL) and scribed section lines
  (TC) are recorded as structural flags on token records, not stripped. Missingness is
  documented per section, never treated as IID (see §5).

## 2. Frozen confirmatory tests

### TC-RI — morphological replication of the -ri operator

- **H_RI:** *-ri* is a productive verbal/necessitive operator in the Etruscan
  ritual-calendar register, shared across LL and TC — not a frozen lexical accident.
  (Replaces the saturated E-5 type/token question.)
- **Frozen TC candidate set:** {*pepri, picasri, muluri, sacri, nunθeri*} — no additions
  after freeze.
- **Operator signature** (per candidate, evaluated on the combined LL+TC D1 corpus):
  (i) the stem recurs with ≥2 distinct endings across the combined corpus, one of them
  *-ri*; (ii) the *-ri* form occurs in ≥2 distinct formula environments (distinct ±2-token
  neighbor-type multisets, or distinct sections).
- **Decision:** SUCCESS if ≥4/5 candidates meet (i)∧(ii); FAILURE if ≤2/5; else
  INDETERMINATE. Per-candidate table required
  (candidate | stem | endings observed | environments | signature met).
- **Direction discipline:** LL generated H_RI; TC adjudicates. LL's own *-ri* forms are
  not re-tuned to fit.

### TC-TUL — calendrical-position test

- **H_TUL:** *tul(e)* is calendrical/phase-addressing rather than a tightly bound formula
  component; its positional freedom should exceed that of strongly formula-bound ritual
  vocabulary. (Motivated by the E-4 anomaly: LL *tul* entropy 1.241, highest of all
  frequent items — the test itself runs on TC.)
- **Operational definition:** E-4's 3-bin positional entropy, reused unchanged. TC bins =
  token's section tercile by line (first/middle/final third of the section's lines).
- **Frozen reference set** (formula-bound TC vocabulary, from the article's explicitly
  noted repetitions): {*vacil, mulu, saca, leθamsul, savcnes*}.
- **Primary:** entropy_TC(*tul(e)*) vs reference entropies. **Secondary (descriptive):**
  calendrical-context rate = fraction of *tul(e)* occurrences within ±2 tokens of
  {*apirase, anpile, acalve, iśvei, ilucu, tule*} vs the same rate for the reference set.
- **Decision:** SUCCESS if *tul* entropy > max(reference entropies); FAILURE if ≤
  median(reference); else INDETERMINATE. Secondary reported descriptively, does not flip
  the verdict.

### TC-NUNΘ — operator-family replication

- **H_NUN:** TC *nunθeri* and LL *nunθen* instantiate one operator family — shared stem
  *nunθ-* with grammatical-operator alteration (*-en* vs *-ri*) — not two unrelated
  tokens. Tests whether LL recurrence tracks a lexical stem with changing operators
  rather than a fixed ritual token.
- **T1 (morphological):** distinct endings on the *nunθ-* stem across LL+TC ≥ 2. Sanity
  gate.
- **T2 (positional):** modal 3-bin line position (E-4 scheme) of LL *nunθen* vs TC
  *nunθeri* — same modal bin required.
- **T3 (neighborhood):** ≥1 shared neighbor type within ±1 token across the two forms'
  occurrences.
- **Decision:** SUCCESS if T1∧T2∧T3; INDETERMINATE if T1∧(T2⊕T3); FAILURE if ¬T1. No
  naked string-similarity claims — typed comparison only.

### TC-MARCH — frozen cross-text formula test

- **Frozen parallel (published, van der Meer):** LL 3.15–17
  (*vacl. an. ścanince. saucsaθ. persin / cletram. śrenχve. iχ. ścanince. ciz. vacl /
  ara*) ↔ TC §1.1–7 (*…vacil…/ ai savcnes …*) — the *sauc-*/*vacl* co-occurrence in
  March-context sections of both texts. Frozen BEFORE any global match search.
- **W_LL** = D1 token multiset of LL 3.15–17; **W_TC** = D1 token multiset of TC §1.1–7.
  **S(A,B)** = |A∩B| / min(|A|,|B|) on multisets (frozen).
- **Forward:** rank S(W_LL, TC_§i) over i=1..10; record rank of §1. **Reverse:** rank
  S(W_TC, LL_col_j) over j∈{I..X,XII}; record rank of III.
- **Nulls:** 10,000 label permutations (sections / columns); p = fraction with rank ≤
  observed. Seeds to be declared at execution; 10,000 iterations fixed here.
- **Decision:** SUCCESS (promote to cross-text formula) if both p < 0.05; FAILURE
  (background ritual-register similarity) if either p ≥ 0.20; else INDETERMINATE.

## 3. The vacil competing-analysis branch

- **H_A:** *vacil/vacl* = libation/offering. **H_B:** *vacil* = discourse/temporal "then"
  (Steinbauer/Rix). **Both live; neither resolved in this round.**
- **Preregistered discriminators (future round, not executed now):** H_A predicts *vacil*
  co-occurs with liquid/offering vocabulary {*vinum, faś, zusle, fler*} above chance;
  H_B predicts *vacil* at phrase/section boundaries preceding varied content.
- **Governance correction:** report 03's "vinum as offering carrier (libation DERIVED)"
  is re-labeled **DERIVED|H_A**. Every inference involving *vinum* → offering/libation
  remains conditional on H_A and must carry the label. Nothing becomes semantic ground
  truth by silent default.

## 4. Bleed controls

1. TC text ingestion begins only after this freeze is committed. The four tests above
   are the complete confirmatory set.
2. TC results cannot modify P-1…P-8, reports 02–06, the D2 ledger, or the XI holdout
   state. Column XI stays sealed under report 06's standing rule.
3. Any TC finding outside the four tests is exploratory (GENERATED), never confirmatory.
4. The XI chain and the TC chain are different experiments; shared vocabulary is
   reported with its experiment label.

## 5. Physical structure — standing rules for both corpora

- **Missingness is not IID.** LL: ~60% preservation plus a longitudinal missing strip;
  TC: badly damaged from §6 on. All null models use block-structured permutation
  (within-section / within-column, as E-3 did). Token-level IID shuffles are
  prohibited — a formula detector must not mistake manuscript layout for linguistic
  recurrence.
- **Red rulings/diacritics are structural features,** recorded as flags, never stripped
  during normalization — otherwise genuine segmentation information is erased.

---

*Frozen 2026-09-29. Machine-readable counterpart:
`data/tabula-capuana/tc_preregistration_manifest.json`. Ingestion of the TC corpus is
authorized only after this commit.*
