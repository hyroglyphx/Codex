# Liber Linteus Analysis Pass 2 — execution of the report-04 validation battery

**Lane:** Jethro independent research (Codex relay)
**Date:** 2026-09-29
**Status:** execution pass; report 04 (`04-liber-linteus-validation-preregistration.md`) was the preregistration. This report executes it.
**Branch tip at execution:** `618a40b`
**Sidecars:** `data/liber-linteus/resultpacket_pass2.json` (validates against `resultpacket_schema.json`), `data/liber-linteus/features_pass2.tsv`
**Do not commit/push note:** relay branch; parent agent handles checkpoints and transport.

## 0. Scope and execution context

This pass executes the three inferential tests declared in report 04 §3 (E-3, E-4, E-5) on the D1 skeleton layer, with the frozen seeds and iteration counts, plus the descriptive feature extraction declared in report 04 §6. One test returned POSITIVE, one NEGATIVE, one INCONCLUSIVE — all three are reported below with equal standing.

Frozen constraints, all honored:

- **Column XI was not inspected, searched for, recovered, or reconstructed in any form.** It remains the sealed prospective holdout.
- **No inferential statistics were run on D2.** D2 is not token-complete; the D2 rows of the transformation ledger are untouched.
- **TCIM-C7 BOUNDARY status of Etruscan contributes zero evidential weight.** Not used.
- **The zero-secured-numerals negative result stands.** The descriptive census below was checked and found no numeral-like class; the negative is preserved, not relitigated.
- **Recurrence may support structural claims only** (report 04 §5). No test result below promotes any semantic or functional reading.
- The steward's Message 0005 (independent Jubilees lane, commit `618a40b`) is informational and explicitly independent of Sequence 5. **None of its content was used in this pass** — no Jubilees-derived prior, parameter, or comparison enters any computation. The bias guard is bidirectional.
- The prediction manifest (`prediction_manifest.json`, frozen at discovery commit `52525c5`) is read-only in this pass. No criterion was applied (see §6).

## 1. Input data audit (D1 as observed)

The inferential tests run on D1 exactly as frozen in the transformation ledger (commit `8d9b933`, 1,277 D0→D1 rows). The D1 skeleton layer as executed has these properties:

- 1,277 tokens; 798 D1 types (824 D0 types); 149 `(column, line)` address groups; columns I–X and XII (11 columns, XI sealed).
- 260 rows have line value `None`: the two OCR junk lines (X:131 tokens, III:100 tokens) and 29 rows in VIII. Any n-gram or window statistic that respects line boundaries treats these as two very long lines plus a 29-token fragment — the nulls below preserve this structure exactly, so it cannot inflate significance.
- 7 rows are pure `xxxx`-class damage artifacts; they participate in the nulls as ordinary tokens (no removal, per the "no data deletion" frozen constraint).
- **Column V line 12 is entirely absent from D1.** There are no V:12 rows, addressed or otherwise. The calibrated-layer seven-token F-B match (V:5 = V:12, report 03 §3.2) therefore has **no D1 counterpart** — this is a SOURCE GAP *in D1*, not a refutation of the calibrated reading, which depends on the prose/C1 edition layer. It matters because the preregistered "(7,4,4)" formula lengths (report 04 §3) were calibrated-layer values while the declared input layer is D1: on D1 the maximum verbatim repeat is 6, not 7. This discrepancy is preserved in the results, not normalized away (see §4, E-3).
- OCR fragmentation in D1 splits several calibrated formula members: F-A's `cilX` appears as `cilS/cilo/cilTl/cilfrl/cilTs/cilfrs` (6 variants); F-B's V:5 is an 8-token D1 sequence `cisum pute tul transur haS rik repino ic` (vs the calibrated 7-token form — `ftansur haTrih repinTic` at V:2, `transur haS rik repino ic` at V:5); F-C's `med lumeric` vs calibrated `mexhumeri`. The inferential tests below use **exact D1 string equality only** — no fuzzy matching, no calibrated-token substitution.

## 2. Operational definitions

Each inferential test is defined before its results (§4). All three use 10,000 iterations, numpy `default_rng` with the frozen seed, and the add-one Monte Carlo p-value `p = (1 + #{replicates ≥ observed})/10001`, one-sided as declared. α = 0.05 throughout.

### E-3 — formula permutation (declared seed 20260929)

- **Statistic:** T = the maximum n (n ≥ 2) such that some n-token sequence recurs verbatim at least twice **within lines**, using exact D1 string equality. Report 04's "(7,4,4)" were calibrated-layer values (7 = F-B V:5=V:12; 4,4 = the F-A/F-C next-longest per report 03 §3.4); since the declared input layer is D1, the D1 census governs: T_obs is whatever D1 yields, and the test compares against it. No silent substitution of the calibrated 7.
- **Null:** per replicate, D1 tokens are shuffled *within each column* (line lengths and the 149 line breaks preserved exactly, including the two junk lines); T_null is recomputed over the corpus-pooled within-line n-grams; one-sided p = P(T_null ≥ T_obs).
- **Judgment calls:** n-grams are formed within lines only (formulae are line-scoped; the null preserves line breaks, so this is matched). Exact equality is deliberately strict — it is the only matching rule that does not reintroduce calibrated-layer editorial judgment.

### E-4 — etnam positional control (declared seed 20260930)

- **Positional entropy:** for a token t, H(t) = −Σ_c p_c log₂ p_c over four position classes c ∈ {lone (line of length 1), initial, medial, final}. Single-token lines form their own class rather than being arbitrarily assigned initial or final.
- **Statistic:** D = H(etnam) − mean(H) over the next-10 most frequent tokens, one-sided p = P(D_null ≥ D_obs).
- **"Next-10" operationalization:** report 03 §3.1 frequency ranks 2–11 — `vacl, vinum, tul, cepen, tei, enas, flere, cisum, acil, trin`. Rationale: §3.1 is the frozen discovery context for "most frequent tokens"; the naive D1 top-10 includes single-character OCR debris (`a, in, i, e, ar`) concentrated in the line-`None` junk lines, which are not lexical items — comparing etnam against debris would answer nothing. This choice was fixed on principled grounds before the §3.1-list result was computed. A sensitivity run with the naive list is reported in §4.
- **Null:** global permutation of the 1,277 tokens over the 1,277 line slots (all line lengths preserved); D recomputed per replicate.

### E-5 — suffix productivity (declared seed 20261001)

- **Observed statistic:** type/token ratio for the `-ri` class on case-folded D1 skeletons with length ≥ 3 ending in `ri`. This matches report 04's declared "-ri/-leri" class (the `-leri` forms are string-wise members of it). Observed: **22 types / 38 tokens = 0.5789**. The 22 types: sacnicleri, spureri, caperi, meleri, flereri, eluri, cleri, fere, eteri, hestiri, acari, veri, zeri, nuneri, lari, pera, muneri, vaclri, tutari, vleri, cineri, leri.
- **Null:** random segmentation — for every token occurrence of length ≥ 3, a split point is drawn uniformly over positions 1..len−1; the pseudo-suffix is `token[split:]`; occurrences are grouped by pseudo-suffix; the comparison functional is the maximum type/token ratio over pseudo-classes. Two functionals were run: (a) maximum over pseudo-classes with ≥ 5 tokens (naive), (b) maximum over pseudo-classes with ≥ 20 tokens (size-comparability: type/token ratio mechanically decreases with class size, and the `-ri` class has 38 tokens).
- **Pre-committed infeasibility rule:** if the null saturates — ≥ 95% of replicates reaching ratio ≥ observed under *both* functionals — the declared statistic cannot discriminate morpheme productivity from chance aggregation under the declared null, and the test is recorded INCONCLUSIVE with the reason, per the task constraint against improvising a substitute test.

## 3. Descriptive results (layer-labeled)

Every table/caption below carries its input layer. These are censuses, not tests; they are declared separately in the ResultPacket and never mixed with inferential results.

### D0/D1 unigram census

1,277 tokens; 824 D0 types; 798 D1 types. Top D1 types (matches report 03 §3.1): `etnam` 35, `vacl` 19, `vinum` 12, `tul` 11, `cepen` 10, `tei` 9, `enas` 9, `flere` 8, `cisum` 8, `acil` 8, `trin` 7. Full top-40 lists for D0 and D1 are in `features_pass2.tsv` (tables `unigram`, layer-labeled).

### Verbatim n-gram census (D1, within lines)

Repeated n-grams (≥ 2 occurrences), D1 exact equality:

- n=2: 51 repeated bigrams; most frequent `cisum·pute` ×7.
- n=3: 9 repeated trigrams — `cisum·pute·tul` ×5 (IV:16, V:2, V:5, IX:4, +1); `etnam·tesim·etnam` ×3 (III:None, VIII:17, X:10); litany 3-grams `ceia·hia·etnam`, `hia·etnam·ciz`, `etnam·ciz·vacl`, `male·ceia·hia` ×3 (VII:2–5).
- n=4: 3 repeated (`ceia·hia·etnam·ciz` ×3, `hia·etnam·ciz·vacl` ×3, `male·ceia·hia·etnam` ×2).
- n=5: 2 repeated (`ceia·hia·etnam·ciz·vacl` ×3, `male·ceia·hia·etnam·ciz` ×2).
- n=6: 1 repeated — **`male·ceia·hia·etnam·ciz·vacl` ×2 (VII:3 = VII:5)**.
- n≥7: none.

Two descriptive findings: (i) `cisum·pute·tul` occurs at **V:2** — `ecn zeri lecin mc zec fasle hemsince cisum pute tul ftansur haTrih repinTic` — an F-B core attestation in D1 not listed in report 03's F-B table; (ii) the `etnam·tesim·etnam` frame ×3, a recurring etnam-bracketed structure independent of the litany block.

### Positional classes (D1)

Distribution over {lone, initial, medial, final} is tabulated per token in `features_pass2.tsv` (`positional`). For etnam: **3 initial / 28 medial / 4 final / 0 lone** (35 total). Descriptively, etnam does occupy all three edge classes — this is the residue of report 03's I-4 that the inferential test below does not erase.

### Co-occurrence windows (D1, ±3 tokens, same line)

- `vinum` (12 occurrences): **2/12** have a `fler-`/`nun-` stem within ±3 tokens on the same line. This is a strict D1/same-line operationalization; report 03 §6.2's prose base rate of 5/12 used calibrated forms and a looser window — the numbers differ by definition, not by contradiction. Both are preserved.
- `etnam`: **44 distinct neighbor types** (adjacent same-line neighbors) — high neighbor diversity, descriptively consistent with a connective/pivot role but not a test of it.

### 2-letter-ending productivity benchmark (D1, descriptive)

178 distinct two-letter endings among D1 tokens of length ≥ 3. By type count: `-ti` 23 types/25 tokens (0.920), **`-ri` 22 types/38 tokens (0.579)**, `-ic` 20/26 (0.769), `-am` 18/57 (0.316), `-na` 18/29 (0.621), `-es` 17/20 (0.850). By token count `-ri` ranks 3rd. So `-ri` is genuinely among the most productive 2-letter endings — but so are `-ti`, `-ic`, `-es`, `-is`, `-ne`, which are plausibly phonotactic (common Etruscan word-final sequences) rather than all being morphemes. This benchmark is descriptive; it cuts both ways and is reported here rather than in E-5's place.

## 4. Inferential results

### E-3 — POSITIVE. p = 0.0001 (0/10,000 null replicates reached T ≥ 6)

T_obs = 6: the 6-token VII litany frame `male·ceia·hia·etnam·ciz·vacl` (VII:3 = VII:5). A re-run of the null with corpus-wide pooled detection (removing a within-column-detection asymmetry found during audit) returned the same 0/10,000; the correction was immaterial but is recorded for exactness.

What this licenses: verbatim formulaic recurrence on D1 is highly non-random — no within-column shuffle in 10,000 produced a 6-token repeat. It strengthens the structural claims I-1 (formula system) and I-8 (VII litany) **as structure only**. What it does not license: any functional or semantic promotion, per report 04 §5 — the 6-gram is a structural module, not a deciphered unit.

Layer discrepancy, preserved: the preregistered "(7,4,4)" were calibrated-layer values. On D1, the maximum is 6; the calibrated 7 (F-B V:5=V:12) has no D1 counterpart because V:12 is absent from D1 (§1). The exact-D1 execution is what the frozen input layer requires; the calibrated 7 is not smuggled in. This is a validation finding in its own right: the headline seven-token verbatim match does not survive the D1 skeleton layer.

### E-4 — NEGATIVE. p = 0.494 (4,939/10,000 null replicates ≥ D_obs)

H(etnam) = 0.919 vs next-10 mean 0.767; D_obs = 0.152. Individual comparator entropies: `vacl` 1.087, `vinum` 1.041, `tul` 1.241, `cepen` 0.722, `tei` 0.764, `enas` 0.918, `flere` 0.544, `cisum` 0.811, `acil` 0.544, `trin` 0.000 (all 7 occurrences in one class). Several frequent tokens have *higher* positional entropy than etnam.

What this licenses: report 03's I-4 ("positional freedom" of etnam) is **not distinguished from "frequent word"** by positional entropy — etnam is thoroughly unexceptional among frequent tokens on this measure. This is a finding, not a failed analysis: it constrains I-4 to its descriptive residue (etnam occupies initial, medial, and final classes; 44 distinct neighbor types), and it rules out promoting positional-freedom into a discriminating functional signature without further evidence.

Sensitivity: the naive comparator list (D1 top-10 including single-char debris) gives D = 0.089, p = 0.548 — also negative. The conclusion is not comparator-sensitive.

### E-5 — INCONCLUSIVE (declared infeasibility rule triggered)

Observed 0.5789. Under the random-segmentation null, **10,000/10,000 replicates** produced a pseudo-class with type/token ratio ≥ 0.5789 — under both the naive ≥5-token functional and the size-matched ≥20-token functional. The saturation mechanism: uniform random splits invariably yield 1-character pseudo-suffix classes that aggregate dozens of tokens across many distinct types (ratio 1.0 attainable). The declared statistic — type/token ratio — cannot discriminate morpheme productivity from chance aggregation under the declared null. No substitute test was run.

What this licenses: nothing about `-ri` morphology, in either direction. The descriptive benchmark (§3: `-ri` #2/#3 of 178 two-letter endings, with `-ti`/`-ic` comparably productive) is consistent both with genuine morphology and with phonotactic generation of high productivity; the data do not decide. A discriminating test — e.g., a length-matched random-segmentation null, or a type-count-based rather than ratio-based statistic — requires a new preregistration. Report 03's I-6 ("-ri/-leri productive relational/agentive morphology") remains at its frozen standing: a type-level observation, not a tested claim.

## 5. Interpretation discipline (frozen)

- **Recurrence ≠ decipherment.** E-3's significance attaches to module identity and ordering (F-A/F-B/F-C as structural modules; the VII litany as a module) — the same restriction report 04 §5 placed on the operator test.
- **The negative is preserved.** E-4 constrains I-4; it is not re-run with a different measure to look for significance.
- **The inconclusive is preserved.** E-5 is not recast as negative (the null was uninformative, not adverse) nor as positive (the descriptive productivity is not a test result).
- No semantic promotion anywhere in this pass. Functional labels remain CANDIDATE/OMEGA exactly as frozen.

## 6. Prediction manifest relation

All 8 predictions remain **FROZEN-UNTESTED**. No pass-2 result triggers any manifest criterion: P-1–P-5 require Column XI text (sealed; no recovery attempted); P-6–P-8 require external witnesses (not consulted). No manifest field was modified.

One layer-annotation clarification for the manifest's discovery-data record (not a criterion change): P-3 notes "current maximum: 7 (F-B V:5=V:12)" — that maximum is calibrated-layer. The exact-D1 maximum established in this pass is 6 (E-3). P-3's operational test (maximal verbatim repeated n-grams at D1 involving XI text; success criterion max ≤ 7) is unaffected.

## 7. OMEGA / negative / source-gap ledger (this pass)

- **OMEGA:** a discriminating `-ri` productivity test (new preregistration needed); sibilant identity for ~60% of tokens (unchanged from report 03); F-A/F-C maximum repeat lengths on D1 (fragmentation makes the calibrated (4,4) unverifiable at D1).
- **NEGATIVE:** E-4 (etnam positional entropy not exceptional); zero secured numerals (stands, rechecked against the D1 census).
- **SOURCE_GAP:** V:12 in D1 (entirely absent); Column XI (sealed by design).

## 8. Provenance and reproducibility

- Input: `data/liber-linteus/token_inventory.tsv` (unmodified; commit `52525c5`).
- Analysis procedure: single-pass script executing all three tests plus descriptive extraction; seeds `20260929` / `20260930` / `20261001` via `numpy.random.default_rng` (PCG64), draws consumed sequentially within each test; 10,000 iterations per test; add-one p-values. The E-3 null was audited and re-run with corpus-wide pooled detection (same result, recorded above).
- Outputs: this report; `data/liber-linteus/resultpacket_pass2.json` (validates against `data/liber-linteus/resultpacket_schema.json` via python `jsonschema`); `data/liber-linteus/features_pass2.tsv` (layer-labeled: `unigram` D0/D1 top-40, `bigram`/`trigram` D1 top-40/20, `positional` D1, `line_stats` D1, `ri_census` D1, `vinum_window` D1).
- Verdicts at a glance: **E-3 POSITIVE (p=0.0001)** — formulaic recurrence is real structure; **E-4 NEGATIVE (p=0.494)** — etnam's positional freedom is not exceptional; **E-5 INCONCLUSIVE** — the declared productivity test cannot discriminate under its null.
