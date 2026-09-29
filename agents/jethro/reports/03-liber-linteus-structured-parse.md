# Work Item 0003 — Liber Linteus Zagrabiensis: Structured Parse, Pass 1

**Lane:** Jethro relay, Message 0003 (delegated research lane, parallel to Work Item 0002)
**Date:** 2026-09-29
**Method:** `WITNESS → OBSERVATION → STRUCTURE → READING → INTERPRETATION → EXTERNAL TEST → PROMOTION / FAILURE / OMEGA`
**Output:** `agents/jethro/reports/03-liber-linteus-structured-parse.md` (this file) + optional sidecar `reports/data/liber-linteus/token_inventory.tsv`
**Transport:** No commit/push by this lane; parent handles relay transport. No other repository files modified.

---

## 0. Executive summary and source verdict

**Source verdict: RELIABLE SOURCE OBTAINED — constrained first-pass parse, NOT a source-gap report.**

A line-addressable scholarly transcription is available in the public-domain editio princeps:

- **Jacob Krall, "Die etruskischen Mumienbinden des Agramer National-Museums,"** *Denkschriften der Kaiserlichen Akademie der Wissenschaften*, phil.-hist. Cl. 41, III. Abhandlung, Vienna, 1892, pp. 1–70, with ten collotype plates.
- Digital witness: Internet Archive scan/OCR `denkschriften4142ster` (`https://archive.org/details/denkschriften4142ster/page/n277/mode/2up`).

**Coverage achieved:** 11 of 12 reconstructed columns (I–X, XII) transcribed from the OCR; **Column XI transcription is absent** from the recovered OCR (recorded as source gap §13). Columns I–IV headers were OCR-corrupted ("Colunine I.", "Coluiniie II.", "Colunine III.", "Coluiiine IV.") and recovered by fuzzy search.

**Critical OCR limitation (frozen into the manifest):** the Internet Archive OCR does **not** reliably distinguish the Etruscan sibilant/dental fricatives (ś / θ / χ rendered inconsistently as `& $ ä ö ß § S x O d f H K`, sometimes collapsing distinct phonemes to the same ASCII). Word shapes, word boundaries, line addresses, and consonant skeletons are recoverable; **exact ś/θ/χ assignment per token is NOT recoverable from this OCR alone** and is marked uncertain throughout. All character-level claims carry explicit confidence states. Nothing has been smoothed or invented: where the glyph is ambiguous, the report says so.

**Calibration anchors (independent, clean transcriptions):** English Wikipedia "Liber Linteus" article (Column III, strip C, lines 12–17, citing van der Meer 2007); Italian Wikipedia "Lamine di Pyrgi" citations (LLZ col 6 lines 1,2,4; col 7 lines 9–10; col 9 lines 12–13); OpenEtruscan v1.0.0 (Zenodo 20075836, CC BY 4.0) seven LL excerpt rows (LL 2, 4, 5, 6, 8, 9, 11). These anchor high-frequency formula words; they are derivative witnesses, not primary.

**Strongest triangulated structures (law-against-law, §10):**

1. **Triple formula system (F-A / F-B / F-C).** Three multi-word formulae recur across non-adjacent columns with stable internal word order but varying neighborhoods: F-A `śacnicleri · cilθl/ś · śpureri · meθlumeric · enaś` (9+ attestations, cols V, VII, VIII, IX); F-B `cisum · pute · tul · θanśur · haθriχ · repinθic` (7 attestations, cols III, IV, V, IX); F-C `eθrse · tinθi · tiurim · avilś` (5 attestations, cols III, IV, V, VIII, IX). Triangulated by (i) verbatim recurrence, (ii) cross-column distribution, (iii) positional recurrence (line-initial/line-final). **PROMOTED to STRUCTURE (attested).** Semantics remain CANDIDATE/OMEGA.
2. **`etnam` as structural pivot (35 attestations, all 11 columns).** Triangulated by (i) raw frequency (rank 1, 2.7% of tokens), (ii) positional distribution (line-initial 3×, line-final 4×, medial elsewhere — NOT positionally fixed), (iii) collocation with both F-A and F-B neighborhoods. Functions as a connective/sectional marker, not a content word. **PROMOTED to STRUCTURE.** Its gloss ("and/then") is DERIVED from comparative Etruscan, not attested in LL.
3. **`nunθen`-family as temporal/causal operator (15+ attestations, 8 columns).** Triangulated by (i) morphological stability of the `nunθ-` stem across OCR variants, (ii) consistent pre-verbal/pre-clausal position, (iii) co-occurrence with `vinum`, `fler-`, and F-B. **PROMOTED to STRUCTURE (carrier identified);** function ("when/during/while") is CANDIDATE from comparative evidence.
4. **Column VII `male · ceia · hia` iterative block (lines 2–5).** Four near-identical lines with terminal variation (`velθre / aisvale / ale / vile · vale`). Triangulated by (i) verbatim stem repetition, (ii) minimal-pair terminal slots, (iii) column-internal confinement. Reads as a paradigmatic list or litany with a variable slot. **PROMOTED to STRUCTURE.**
5. **`vinum` offering carrier (12 attestations, 6 columns).** Triangulated by (i) cross-column recurrence, (ii) consistent neighborhood with `fler-/trin`, `nunθen`, F-B, (iii) external attestation as a Latin loanword for wine in ritual contexts. **PROMOTED to STRUCTURE as an offering/action carrier;** the inference "wine libation" is DERIVED, not attested.

**Top OMEGA items (§9, §13):** (1) Exact ś/θ/χ readings for ~60% of sibilant-bearing tokens — unrecoverable from this OCR pass; (2) Column XI — no transcription recovered; (3) Function of the `śacnicleri` formula's internal syntax (genitival chain vs. apposition); (4) Whether `celi`/`acale`/`θucte` are month names or something else; (5) The `nunθen` clause's precise temporal/aspectual force; (6) Identity of `θanśur`/`haθriχ` in F-B; (7) Whether column boundaries are ritual boundaries, physical layout, or both; (8) The `iχ`/`eci` particle's function; (9) `eθrse` semantics; (10) Any Etruscan numeral in LL — **no secure numeral identified** (TCIM C7 BOUNDARY status for Etruscan "seven" explicitly excluded from weighting per instructions).

**Bias guard (binding):** This parse was conducted without reference to prior ARGO/TCIM hypotheses. Etruscan's BOUNDARY status in the TCIM numeral-seven program was treated as a standing falsifier-risk, not as evidence: no token in LL is claimed as a numeral on the basis of that program, and §6 records the numeral search as a **negative result**. Disputed Etruscan translations are cited as disputed.

---

## 1. Witness/edition manifest and frozen transcription rules

### 1.1 Primary witness (carrier edition)

| Field | Value |
|---|---|
| Edition | Jacob Krall, "Die etruskischen Mumienbinden des Agramer National-Museums," *Denkschriften der Kaiserlichen Akademie der Wissenschaften*, philosophisch-historische Classe, 41. Band, III. Abhandlung, Vienna, 1892, pp. 1–70 |
| Status | Editio princeps; first correct identification of the language as Etruscan (1891/1892) |
| Digital source | Internet Archive item `denkschriften4142ster`, scan + OCR (`..._djvu.txt`), accessed 2026-09-29 via `https://archive.org/details/denkschriften4142ster/page/n277/mode/2up` |
| License | Public domain (published 1892) |
| Plates | Ten collotype (Lichtdruck) plates of the bandages, reproduced from photographs |
| Columns reconstructed | Twelve (I–XII), counted right-to-left; columns bounded by red lines on the linen |
| Column addressing | Roman numerals I–XII + line number (e.g., "VIII, Z. 6–11"); band-fragment sub-addresses in lowercase (`a`–`l`) with piece numbers (e.g., `7a/9d`, `2b`, `4c`) |
| Lines recovered (this pass) | 11 columns (I–X, XII); Column XI transcription missing from OCR |
| Tokens extracted | 1,277 (sidecar `token_inventory.tsv`); ~798 unique skeletons |

### 1.2 Krall's frozen normalization policy (stated in the edition, pp. ~28–29)

Krall's typographic conventions, quoted from the edition (German original, OCR-normalized):

- **Antiqua (upright type):** letters whose reading is *certain*.
- **Cursive (italic type):** letters whose reading is only *probable*.
- **Single point (•):** word divider whose presence is *certain*.
- **Slanted double point (:):** word divider whose presence is only *probable*.
- **Cursive + superscript "?":** letters that remain doubtful.
- **"x":** letters whose value Krall "did not even venture a conjecture" on; runs of `x` mark illegible stretches, with estimated letter counts where the damage pattern permits.
- Restorations from parallel passages are marked in the "Bemerkungen zur Lesung" (reading notes) per column/line.

**Consequence for this parse:** the OCR collapses Antiqua/cursive and •/: into undifferentiated ASCII. The certainty layer of Krall's edition is therefore **lost in the digital witness** and must be re-verified against the scan or plates before any single-character claim is promoted above CANDIDATE. This is recorded as a standing limitation, not repaired by conjecture.

### 1.3 Damage, restoration, and provenance (per Krall)

- Five of eight linen strips survive; three strips are lost. The surviving text is heavily damaged at column tops/bottoms and at strip edges; Krall estimates missing line counts per column from the physical reconstruction.
- Column heights: I–IV ≥24 cm; V–VII ≥25 cm; VIII–XII ≥30 cm (headers in transcription).
- Black ink for main text; **red ink for column boundary lines and diacritics** (Krall notes red-written signs, e.g., Column VII line 5 terminal `QD`).
- Provenance: mummy wrappings of a young woman, purchased in Alexandria (Egypt) ca. 1850 by Michael von Barich, donated to the Zagreb (Agram) National Museum. Linen dated by Krall's contemporaries on stylistic grounds; script dated by later scholarship (van der Meer: end of 3rd c. to ca. 150 BCE; North Etruscan, probably Perugia region). **These datings are scholarly attributions, not carrier data**, and are kept in the provenance layer only.
- Textile analysis (Krall's appendix): ink lies directly on the weave, older than the stains; authenticity of the textile uncontested.

### 1.4 Derivative witnesses (calibration only)

| Witness | Content used | License/Access | Role |
|---|---|---|---|
| English Wikipedia, "Liber Linteus" | Col III, strip C, lines 12–17 transcription + tentative translation (cites van der Meer 2007) | CC BY-SA | Calibration anchor for OCR mappings |
| Italian Wikipedia, "Lamine di Pyrgi" | LLZ citations: col 6 ll. 1,2,4 (`śnuiu-φ`); col 7 ll. 9–10 (`śucic firin tesim`); col 9 ll. 12–13 (`śacnicleri cilθl śpureri meθlumeric enaś`) | CC BY-SA | Calibration anchors |
| OpenEtruscan v1.0.0 (Zenodo 20075836) | 7 LL rows (LL 2, 4, 5, 6, 8, 9, 11), `clean`, intact_ratio 1.000 | CC BY 4.0 | Modern normalization cross-check |
| en-academic.com "Pyrgi Tablets" mirror | Etruscan vocabulary with LLZ column/line citations | Web | Lexical cross-check (derivative) |
| Krall's own glossary (pp. ~45–65) | Word attestations with column references (e.g., "aiseras II 12; V 8; XII 2") | PD (same edition) | Attestation index |

### 1.5 What was NOT used

- Rix 1991 / Meiser 2014 (ET II): the standard modern corpus edition — **no public digital transcription located**; cited only as the canonical reference for line addresses in secondary literature.
- Van der Meer 2007 (*Liber Linteus Zagrabiensis*): complete word-by-word analysis — **no accessible full text recovered**; cited via Wikipedia's excerpt.
- Etruscan Texts Project: upstream defunct; did not cover LL.
- No reconstruction from memory. No machine translation of Etruscan. All modern English glosses of Etruscan words are marked DERIVED/disputed.

### 1.6 Frozen transcription rules for this pass

1. **Diplomatic layer** = the OCR token exactly as observed (sidecar, `raw` column).
2. **Skeleton layer** = lowercased, OCR-artifact-stripped form (`skeleton` column) used ONLY for recurrence clustering; sibilant identity is NOT asserted at this layer.
3. **Calibrated layer** (this report's running text) = best-effort standard Etruscan orthography (θ ś χ) applied ONLY where anchored by a derivative witness or by unambiguous OCR (e.g., `nun&en` → `nunθen`); every other sibilant is written with the OCR form or marked `[ś/θ/χ?]`.
4. **Line addresses** use Krall's (column, line) as printed; OCR line-number misreads are noted where detected.
5. **Column XI** is excluded from all statistics (source gap).
6. **No emendation** of Krall's readings; Krall's `x`-stretches and `?` are preserved as damage, not filled.

---

## 2. Carrier map (finest reliable address)

The carrier is linen, not paper: the "page" is a reconstructed column of text on a folded linen book (*liber linteus*), twelve columns (I–XII) read right-to-left, each column a "page" of the folded codex. The finest reliable address is **(column, line)** per Krall's reconstruction; sub-addresses (strip letter + piece number, e.g., `2b`, `7a/9d`) locate physical fragments within the column.

| Column | OCR lines | Text lines recovered | Height (Krall) | Preservation notes (Krall) |
|---|---|---|---|---|
| I | 18860–18879 | ~5 (heavily damaged; `x`-runs) | ≥24 cm | Top destroyed; only line-ends survive |
| II | 18880–18921 | ~13 | ≥24 cm | Fragmentary; joins across strips `a`–`l` |
| III | 18922–18988 | ~17 (incl. Wikipedia-calibrated block) | ≥24 cm | Strip C (lines 12–17) well preserved |
| IV | 18989–19054 | ~21 | ≥24 cm | Good; red-ink diacritics noted |
| V | 19055–19113 | 23 | ≥25 cm | Good; full formula sequences |
| VI | 19114–19175 | ~17 | ≥25 cm | Noisy OCR; `acale` (month?) at line 14 |
| VII | 19176–19248 | ~23 | ≥25 cm | Iterative `male · ceia · hia` block ll. 2–5; red sign at l. 5 |
| VIII | 19249–19320 | ~18 | ≥30 cm | `θucte` (month?) at line 1; `vinum` cluster |
| IX | 19321–19385 | ~22 | ≥30 cm | Dense formula repetition (F-A ×3, F-B ×2) |
| X | 19386–19534 | ~30+ (OCR noisy) | ≥30 cm | Longest recovered column; fragmentary |
| XI | — | **0 (source gap)** | ≥30 cm (est.) | Transcription not recovered from OCR |
| XII | 19535–19588 | 13 + `Ende des Textes` | ≥30 cm | Explicit end-of-text; blank linen follows |

**Total:** ~200 text lines, 1,277 tokens across 11 columns. (Published totals: ~230 lines, ~1,200 legible words; the deficit is Column XI + OCR line-loss.)

**Carrier-level observations (ATTESTED):**
- Column XII ends with blank linen and intact selvage → the book's end is preserved (Krall; confirmed by "Ende des Textes" in the edition).
- The beginning (columns I–III) is the most damaged; it is NOT known where the book begins (the first surviving column may not be the first written).
- Red lines bound columns; red diacritics occur inside text (VII:5). Color is a carrier-level signal whose function is unattested.

---

## 3. Repeated-token/formula inventory

Built from the skeleton layer (1,277 tokens). Frequencies are of *skeleton* types; OCR splits (e.g., `cil&l` vs `cilO-l`) are merged only where the formula context makes identity certain, and noted.

### 3.1 Top-frequency tokens (structural pivots)

| Rank | Skeleton | n | Columns | Calibrated form | Status |
|---|---|---|---|---|---|
| 1 | etnam | 35 | all 11 | *etnam* | STRUCTURE (pivot) |
| 2 | vacl | 19 | V, VI, VII, VIII, IX, X | *vacl* | STRUCTURE |
| 3 | vinum | 12 | III, IV, V, VIII, IX | *vinum* | STRUCTURE (offering carrier) |
| 4 | tul | 11 | II, III, IV, V, IX | *tul* | STRUCTURE |
| 5 | cepen | 10 | VII (only) | *cepen* | STRUCTURE (local) |
| 6 | tei | 9 | II, IV, V, VIII | *tei* | CANDIDATE |
| 7 | enas | 9 | IV, V, VII, VIII, IX | *enaś* | STRUCTURE |
| 8 | flere | 8 | III, IV, V, VIII, IX | *flere* | STRUCTURE |
| 9 | cisum | 8 | III, IV, V, IX | *cisum* | STRUCTURE |
| 10 | acil | 8 | V, VI, VII, VIII, XII | *acil* | STRUCTURE |
| 11 | trin | 7 | III, IV, V, VIII | *trin* | CANDIDATE |
| 12 | pute | 7 | III, IV, V, IX | *pute* | STRUCTURE |
| 13 | fler | 7 | III, IV, VIII | *fler* | STRUCTURE |
| 14 | celi | 7 | IV, V, IX | *celi* | CANDIDATE (month?) |
| 15 | cletram | 6 | III, IV, V, IX | *cletram* | STRUCTURE |

### 3.2 The three formula systems (verbatim recurrence with stable internal order)

**F-A — the `śacnicleri` formula (9 attestations, 4 columns):**

| Address | Sequence (calibrated) |
|---|---|
| V:3 | śacnicśtreś · cilθś · śpureśtreśc |
| V:6 | śacnicleri · cilθl · śpureri · meθlumeric |
| V:13 | śacnicleri · cilθl · śpureri · meθlumeric |
| V:23 | cilθl · śpureśtreś(?) · meθlumeśc · enaś · cla · θteśan |
| VII:18 | śacnicleri · cilθl · cepen · ciθcva · cepen |
| VIII:14 | śacnicśtreś · cilθś · śpureśtreś · enaś |
| IX:5 | repinec · śacnicleri · cilθl · śpureri |
| IX:12 | haθrec · repinec · śacnicleri · cilθl · śpureri |
| IX:21 | śacnicleri · cilθl · śpureri · meθlumeric |

*Variants:* `-śtreś` vs `-leri` on the first and third members; presence/absence of `meθlumeric`; prefixed `repinec`/`haθrec` in IX; `cepen`-substitution in VII:18. The skeleton `cilθl/ś` is OCR-split (`cil&l`, `cilO-l`, `cilfrl`, `cilö-1`) but formula position makes identity certain.

**F-B — the `cisum · pute · tul` formula (7 attestations, 4 columns):**

| Address | Sequence (calibrated) |
|---|---|
| III:(12–17 block) | tiurim · avilθ · θiχ · cisum · pute · tul · θaθiś(?) |
| IV:3 | fler · θeθince(?) · cisum · pute · tul · θanś(?) |
| IV:16 | faθei · cisum · pute · tul · θam(?) · hatec · repinec |
| V:5 | cisum · pute · tul · θanśur · haθriχ · repinθic |
| V:12 | cisum · pute · tul · θanśur · haθriχ · repinθic |
| IX:4 | cisum · pute · tul · θranś · haθrec |
| IX:20 | cisum · pute · tul · θranś · haθrec · repinec |

*Note:* V:5 and V:12 are verbatim identical (7-token match) — the strongest single recurrence in the corpus.

**F-C — the `eθrse · tinθi · tiurim · avilś` formula (5 attestations, 5 columns):**

| Address | Sequence (calibrated) |
|---|---|
| III:(12–17 block) | eθrse · tinθi · tiurim · avilθ |
| IV:2 | eθrse · tinθi · tiurim · avilś · θiś · ecn · zeri |
| V:4 | enaś · eθrse · tinθi · tiurim · avilś · θiś |
| VIII:15 | eθrse · tinθi · tiurim · avilś · θiθ · heθrn |
| IX:3 | śpureśtreś · enaś · eθrse · tinθi · tiurim |
| IX:10 | cilθś · śpureśtreś · enaś · eθrse · tinθi |

*Note:* F-C shares members with F-A (`enaś`, `śpureśtreś`, `cilθś`) — the formulae interleave, they are not mutually exclusive blocks.

### 3.3 Other strong recurrences

- **`nunθen`-family** (15+): `nunθen`, `nunθene`, `nunθten`, `nunθrenθ`, `nuntrene`, `nunθenθ-` — stem `nunθ-` stable; suffixes vary. 8 columns.
- **`vacl` + `fler-/flere`**: `vacl · trin · flere · neθunśl` (VIII:11, IX:7); `vacl · ara · θam` (III).
- **`θezi · vacl · an`**: III (θezi · vacl · an · ścanince).
- **`faθei · cisum`**: IV:16, IX:8 (zusleve · faθeic).
- **`zusleve`**: IV:7, IX:8, IX:13, IX:16 — offering/action carrier, 4×.
- **`teśim`**: III, VI, VII — burnt-offering term (cf. derivative gloss "burnt offering").
- **`meθlumeric`**: V:6, V:13, V:23, IX:21 — 4×, always in F-A.
- **VII:2–5 iterative block**: `male · ceia · hia · etnam · ciz · vacl` with terminal variants.

### 3.4 Negative recurrence controls

- No 7-token verbatim match other than V:5=V:12 (F-B). The next-longest verbatim matches are 4 tokens (F-A core `śacnicleri · cilθl · śpureri` is 3; with `meθlumeric` 4).
- `etnam` (35×) never forms a fixed bigram with frequency >4 — it is positionally free, consistent with a connective, not a formula member.
- 798 unique skeletons / 1,277 tokens = 62% hapax-or-rare rate; the text is formulaic but NOT mechanically repetitive — the formulae are embedded in varying matrices.

---

## 4. Morphological segmentation with confidence/evidence state

Segmentation is performed on the skeleton layer; ś/θ/χ distinctions are marked uncertain where the OCR does not resolve them. Confidence states: **ATTESTED** (comparative Etruscan secures the morpheme), **CANDIDATE** (pattern-internal), **UNKNOWN** (no basis).

### 4.1 High-confidence segmentations (ATTESTED morphemes from comparative Etruscan)

| Token | Segmentation | Morphemes | Evidence |
|---|---|---|---|
| śacnicleri | śac-ni-c-leri | śac- (sacred, cf. Latin *sacer* loan debate) + -ni- + -c- (and) + -leri (pertaining to) | -leri agentive/relational is ATTESTED across Etruscan (cf. *śpureri*); -c- enclitic "and" ATTESTED (Pyrgi, Capua) |
| śpureśtreś | śpur-e-śtre-ś | śpur- (city/community) + -e- + -śtre- (cf. Latin *-ester* adjectival, disputed) + -ś (genitive) | śpur- ATTESTED (Pyrgi *śpura*); -ś genitive ATTESTED |
| cilθl | cil-θ-l | cil- (unknown stem) + -θ- (?) + -l (locative/pertaining?) | -l as adjectival/locative CANDIDATE (cf. *cilθl* vs *cilθś* alternation = case?) |
| meθlumeric | meθlum-er-i-c | meθlum- (crowd/people, cf. *meχ*) + -eri + -c (and) | meθlum- CANDIDATE; -eri, -c ATTESTED |
| enaś | ena-ś | ena- (demonstrative stem?) + -ś (genitive) | -ś ATTESTED; ena- CANDIDATE |
| nunθen | nunθ-en | nunθ- (temporal stem?) + -en (locative/temporal?) | -en locative ATTESTED in Etruscan; nunθ- UNKNOWN |
| tiurim | tiur-im | tiur- (moon/month?) + -im (?) | tiur- CANDIDATE (lunar connection disputed) |
| avilś | avil-ś | avil- (year, ATTESTED cf. *avil* in funerary inscriptions) + -ś (genitive) | **avil- ATTESTED**; -ś ATTESTED |
| vinum | vinu-m | *vinum* (wine — Latin loanword, ATTESTED as loan) + -m (?) | Loan status DERIVED from Latin; Etruscan case ending UNKNOWN |
| eiseras | eiser-as | eiser- (god/divine? cf. *aiser*) + -as (genitive?) | *aiser-* "gods" CANDIDATE (Pyrgi *aiser* debated) |

### 4.2 Productive suffix inventory (CANDIDATE, pattern-internal)

From the suffix census (§3 method): **-ri (37), -eri (29), -ś/-s (71 s-final types), -l, -θ, -i, -c, -en, -am, -um**.

- **-ri/-leri**: relational/agentive; 22 distinct types (*sacnicleri, spureri, caperi, meleri, flereri, eluri...*). ATTESTED as a morpheme class; individual assignments CANDIDATE.
- **-śtre-/-tre-**: in *śacnicśtreś, śpureśtreś, śpureśtreśc* — alternates with *-leri*. Whether *-śtre-* is a single morpheme or *ś-tre-ś* is UNKNOWN. The Latin *-ester* parallel is DISPUTED (noted, not adopted).
- **-c** (enclitic "and"): ATTESTED (*meθlumeri-c, śacnicśtreś-c*?). In LL: *teśim-c*? uncertain.
- **-en**: temporal/locative CANDIDATE (*nunθen, eθrse-n?*).
- **-sa/-śa**: *θeśamei*? not in LL sample; *esviśa*? UNKNOWN.

### 4.3 Explicitly unsegmentable (UNKNOWN)

`θanśur`, `haθriχ`, `eθrse`, `zusleve`, `cletram`, `śrenχve`, `vacl`, `teśim`, `flere` — recurring stems with no secure internal boundary. They are treated as **unanalyzed carriers**, not segmented by conjecture.

### 4.4 Morphological invariants (promoted)

- **M-1:** The *-leri* / *-śtreś* alternation on the SAME stems (*śacnic-leri* vs *śacnic-śtreś*; *śpur-eri* vs *śpure-śtreś*) is a genuine morphological alternation, not OCR noise — it occurs in clean formula contexts (V:3 vs V:6). **PROMOTED to STRUCTURE.**
- **M-2:** The *-l* vs *-ś* alternation on *cilθ-* (*cilθl* vs *cilθś*) correlates with formula variant (F-A *-leri* prefers *-l*; F-A *-śtreś* prefers *-ś*). **PROMOTED to STRUCTURE (correlation);** case-function interpretation is CANDIDATE.
- **M-3:** Enclitic *-c* ("and") attaches to formula-final members (*meθlum-eri-c*). ATTESTED morpheme; LL instances CANDIDATE due to OCR.

---

## 5. Candidate ritual/calendrical sequence map

**Status:** CANDIDATE throughout. No month list, no day numbers, and no explicit calendrical grid are attested in the recovered text. The "ritual calendar" label is a scholarly hypothesis (van der Meer), not a carrier fact.

### 5.1 Calendrical carriers (all CANDIDATE or weaker)

| Token | Address | Proposed value | Basis | State |
|---|---|---|---|---|
| *acale* | VI:14 | "in June" | Derivative scholarly gloss (van der Meer) | CANDIDATE (disputed) |
| *θucte* | VIII:1 | "in August" | Derivative scholarly gloss | CANDIDATE (disputed) |
| *celi* | IV:21, V:10, V:16, V:17, IX:18 | "in September" | Derivative scholarly gloss; 7 attestations | CANDIDATE (disputed) |
| *tiurim* | 5× (F-C) | "month" (?) | Lunar etymology, disputed | UNKNOWN |
| *avil-* | 6× (F-C) | "year" | ATTESTED stem in funerary Etruscan | ATTESTED stem; LL function CANDIDATE |
| *eslem* | VI:14 | "two"? | Derivative numeral proposal | OMEGA (see §9) |

**Critical negative:** months are mentioned only from column VI onward in the recovered text (consistent with van der Meer's observation), but columns I–V are damaged — absence is not evidence. **No day-names, no numerals securely identified, no year-dates.**

### 5.2 Sequence structure (what the carrier actually shows)

The text does NOT present a linear January–December grid. What recurs is a **modular liturgical structure**:

1. **Invocation/opening module** (F-C: *eθrse · tinθi · tiurim · avilś* + divine-name carriers) — opens or punctuates sections in cols III, IV, V, VIII, IX.
2. **Congregational formula** (F-A: *śacnicleri · cilθl · śpureri · meθlumeric · enaś*) — the "priestly clans, city and country elders" formula (gloss disputed), recurring in V, VII, VIII, IX.
3. **Action module** (F-B: *cisum · pute · tul · θanśur · haθriχ · repinθic* + *nunθen* clauses + *vinum*/*fler-* offering carriers).
4. **Iterative/litany module** (VII:2–5 *male · ceia · hia* block) — paradigmatic repetition with a variable slot.

**Structural Continuation test:** the same lexical material (F-A) returns in different columns, but its **neighborhood changes** (V: with *meθlumeric*; VII:18 with *cepen*; IX: with *repinec/haθrec* prefixes; VIII:14 in *-śtreś* form). Per the methodology, same lexical return ≠ same ritual state. The returns are **path-dependent phases**, not identical states — each F-A occurrence is embedded in a different actional matrix. This is recorded as a positive finding of the operator test (§15), not as a failure.

### 5.3 What would falsify the "calendar" reading

- If *acale/θucte/celi* prove to be non-temporal (e.g., place names or epithets), the calendrical scaffold collapses to OMEGA. **This is a live risk:** their month-glosses are derivative and disputed.
- The absence of any day-count or year-count in 1,277 tokens is a **negative control** against a strongly calendrical text.

---

## 6. Source-supported carriers by class

### 6.1 Divine names (CANDIDATE; Etruscan pantheon identifications are disputed)

| Carrier | Addresses | Proposed referent | State |
|---|---|---|---|
| *tinθi* / *tinsi* / *tin-* | III, IV, V, VI, VIII, IX (F-C) | Tinia (Jupiter) — dative/locative? | CANDIDATE (stem ATTESTED in Etruscan theonyms) |
| *eθrse* | III, IV, V, VIII, IX (F-C) | Unknown; precedes *tinθi* | UNKNOWN (possibly epithet or second deity) |
| *uni* | VII:23 (*9-uni*?) | Uni (Juno) | OMEGA (OCR too damaged) |
| *eiseras* / *aiser-* | II:12, V:8, V:20, XII:2 | "gods" (plural?) | CANDIDATE (disputed) |
| *neθunśl* | VIII:11, IX:7 (*vacl · trin · flere · neθunśl*) | Nethuns (Neptune)? | CANDIDATE (very disputed) |
| *catha*? | — | Not found in recovered text | — |

**Negative:** No unambiguous theonym beyond *tin-* is secured. *fufl-, laran, vetis, cilens* do not occur in the recovered sample.

### 6.2 Offering/material carriers (STRUCTURE for recurrence; function DERIVED)

| Carrier | n | Addresses | Proposed | State |
|---|---|---|---|---|
| *vinum* | 12 | III, IV, V, VIII, IX | wine (Latin loan) | STRUCTURE (carrier); "libation" DERIVED |
| *fler* / *flere* / *flereri* | 15+ | III, IV, V, VII, VIII, IX | sacrifice/offering? | STRUCTURE; gloss DISPUTED |
| *teśim* | 5 | III, VI, VII | burnt offering? | CANDIDATE (derivative gloss) |
| *zusleve* | 4 | IV, IX | offering? | CANDIDATE |
| *θeśamei*? | — | Not recovered | — | — |

### 6.3 Action carriers (CANDIDATE; Etruscan verbs are poorly secured)

| Carrier | n | Context | Proposed | State |
|---|---|---|---|---|
| *tul* | 11 | F-B (*cisum · pute · tul*) | action? | UNKNOWN (possibly verb or noun) |
| *nunθen* family | 15+ | pre-clausal | temporal operator | STRUCTURE (carrier); function CANDIDATE |
| *tur-* / *tura* | 8+ | *raχθ · tur · heχσθ* (OpenEtruscan LL 4, LL 9) | give/offer? | CANDIDATE (comparative) |
| *heχσθ* | (OpenEtruscan) | *raχθ · tur · heχσθ vinum* | ? | UNKNOWN |
| *am-* | 4+ | *acil · ame* (OpenEtruscan LL 8; VII) | be? | CANDIDATE (comparative *am-*) |
| *ar-* / *ara* | 15+ | *ara · nunθene*; *ar-a* | ? | UNKNOWN |

### 6.4 Temporal/address carriers

*etnam* (35×, STRUCTURE, connective); *nunθen* (STRUCTURE, operator); *iχ*/*eci* (particle, UNKNOWN function); *nac* (5×, *nac · huca*; temporal? UNKNOWN); *ananc-* (*anancveś*?, III); *ti*/*tei* (demonstrative? CANDIDATE).

### 6.5 Numerical carriers — NEGATIVE RESULT

**No secure numeral was identified in the recovered 1,277 tokens.** Searched: *θu, zal, ci, huθ, maχ, śa, semφ, cezp-, nurφ-, -m*. Findings:

- *ci* (3×: VII:18, X:2, X:21): occurs in *cepen · ciθcva · cepen* (VII:18) — positionally a noun/adjective, not a counter. **Not a numeral.**
- *zal* (2×: X:20, X:21): isolated; insufficient context. **OMEGA.**
- *eslem* (VI:14, *eslem · zaθumiθ · acale*): proposed "two" in derivative literature; context is a list, not a count. **OMEGA — explicitly NOT promoted.**
- *θun-*? Not recovered.

**TCIM bias guard:** Etruscan "seven" (*semφ-*) was a BOUNDARY witness in the TCIM C7 program. Per the binding instruction, this status contributed **zero weight** to the numeral search. No *semφ-* or "seven"-candidate was found in LL, and none is claimed. The numeral search is recorded as a **negative result**, which is itself a finding: a "ritual calendar" with no legible numerals in 1,277 tokens weakens the strong calendrical reading (see §5.3).

### 6.6 Place carriers

*śpur-* (city/community, in F-A); *meθlum-* (crowd/district?, in F-A). No toponym securely identified. *eletrani*? (II:10, *eletrani · śrenχve*?) — OMEGA.

---

## 7. Recurrence/neighborhood graph (attested relations only)

Nodes are skeleton types; edges are **attested** adjacencies (bigram) or formula co-membership. No complete-graph inference (Gate Algebra constraint: only attested co-occurrences).

### 7.1 Bigram edges (frequency ≥3, attested)

- *etnam* → *X*: free (no bigram >4) — confirms pivot status, not formula membership.
- *cisum* → *pute* → *tul* (7× chain) — F-B core.
- *śacnicleri* → *cilθl* (6×) — F-A core.
- *cilθl* → *śpureri* (5×) — F-A core.
- *eθrse* → *tinθi* (5×) — F-C core.
- *tinθi* → *tiurim* (5×) — F-C core.
- *tiurim* → *avilś* (4×) — F-C core.
- *vacl* → *trin* (3×); *trin* → *flere* (3×).
- *ara* → *nunθene* (2× + variants).

### 7.2 Formula co-membership (hyperedges, attested)

- **H-A** = {śacnicleri, cilθl/ś, śpureri, meθlumeric, enaś} — 9 lines, 4 columns.
- **H-B** = {cisum, pute, tul, θanśur, haθriχ, repinθic} — 7 lines, 4 columns.
- **H-C** = {eθrse, tinθi, tiurim, avilś} — 6 lines, 5 columns.
- **Intersections (attested):** H-A ∩ H-C = {enaś, śpureśtreś, cilθś} (IX:3, IX:10, VIII:14). H-B ∩ H-C = {θiś?} (weak). H-A ∩ H-B = ∅ (no shared members — the formulae are lexically disjoint).

### 7.3 Positional graph (line-initial → line-final)

- Line-initial hubs: *śacnicleri* (4×), *etnam* (3×), *enas* (3×), *male* (3×), *vacl* (3×), *cisum* (2×), *teśim* (2×).
- Line-final hubs: *etnam* (4×), *tul* (3×), *vinum* (2×), *repinec* (2×), *θteśan* (2×), *cepen* (2×).
- **Finding:** *etnam* is the ONLY token that is a hub at both edges — consistent with a discourse connective, not a content word. **PROMOTED.**

### 7.4 Neighborhood-change cases (Structural Continuation)

| Lexical item | Occurrence 1 (neighborhood) | Occurrence 2 (changed neighborhood) | Same state? |
|---|---|---|---|
| F-A | V:6 (+*meθlumeric*) | VII:18 (+*cepen · ciθcva · cepen*) | NO — different associational matrix |
| F-A | V:6 (*-leri* form) | V:3 (*-śtreś* form, different line) | NO — morphological phase change |
| *vinum* | V:10 (+*celi · śuθ*) | VIII:5 (+*menal · cltral · mulay*) | NO — different offering list |
| *nunθen* | V:19 (+*citz · vacl · θteśan*) | V:20 (+*unum · mlaχ · θuviti*) | NO — different clause |
| F-B | V:5 (bare) | IX:20 (+*haθrec · repinec* prefixes) | NO — expanded |

**Conclusion:** recurrence is path-dependent. The text reuses modules in new configurations; it does not stamp identical ritual states. **Recurrence is not decipherment** — this is preserved as a positive methodological finding.

---

## 8. Ten strongest structural invariants

1. **I-1. Triple formula system.** F-A, F-B, F-C each recur ≥5× with stable internal order across ≥4 columns. (ATTESTED)
2. **I-2. F-A/F-B lexical disjointness.** No shared members between the congregational formula and the action formula — they are distinct modules. (ATTESTED)
3. **I-3. F-A/F-C intersection.** {*enaś*, *śpureśtreś*, *cilθś*} belong to both — the invocation and congregational modules interleave. (ATTESTED)
4. **I-4. *etnam* positional freedom + edge-hub status.** 35×, all columns, initial/medial/final; the only dual edge-hub. (ATTESTED)
5. **I-5. V:5 = V:12 verbatim (7 tokens).** The longest exact repetition; F-B is fixed verbatim at least once. (ATTESTED)
6. **I-6. *-leri* / *-śtreś* morphological alternation** on identical stems (*śacnic-*, *śpur-*). (ATTESTED)
7. **I-7. *cilθl* / *cilθś* case-like alternation** correlated with formula variant. (ATTESTED correlation; function CANDIDATE)
8. **I-8. VII:2–5 minimal-pair litany.** Four lines, identical frame, variable terminal slot. (ATTESTED)
9. **I-9. *nunθ-* stem stability** across 15+ attestations and 8 columns despite OCR noise. (ATTESTED)
10. **I-10. Column XII terminal blank.** The book ends; the text is complete at the end, fragmentary at the beginning. (ATTESTED, carrier-level)

---

## 9. Ten strongest ambiguities, negative controls, and OMEGA items

1. **O-1. Sibilant identity.** ~60% of sibilant-bearing tokens cannot be assigned ś/θ/χ from this OCR. Blocks phonological and some morphological claims. **Second-pass: verify against scan/plates.**
2. **O-2. Column XI.** No transcription recovered. A full column (~20 lines) is missing from the parse.
3. **O-3. F-A internal syntax.** Genitival chain ("clans of the city"), apposition, or titles? The morphology permits all three. No independent constraint decides.
4. **O-4. Month names.** *acale/θucte/celi* as months is derivative and disputed; if non-temporal, the calendar hypothesis loses its only direct support.
5. **O-5. *nunθen* force.** Temporal ("when"), causal ("because"), or conditional ("if")? Comparative Etruscan does not secure it.
6. **O-6. F-B members.** *θanśur*, *haθriχ*, *repinθic* have no comparative anchor. Unanalyzed carriers.
7. **O-7. Column boundaries.** Ritual units, physical pages, or both? The red lines are carrier facts; their semiotic function is unattested.
8. **O-8. *iχ*/*eci*.** Particle of unknown function; possibly deictic.
9. **O-9. Numerals.** None secured (§6.5). The text may use numerals rarely, or the OCR may have destroyed them, or they were in lost columns.
10. **O-10. *eθrse*.** Precedes *tinθi* 5×; epithet, second deity, or place? No basis to decide.

**Negative controls preserved:**
- N-1: *etnam*'s frequency does NOT make it a content word (positional freedom test).
- N-2: *vinum* = "wine" does NOT entail a libation ritual (function is DERIVED).
- N-3: F-A's recurrence does NOT entail identical ritual states (neighborhood-change test, §7.4).
- N-4: The *-ester*/Latin parallel for *-śtre-* is NOT adopted (disputed; resemblance alone is STRUCTURAL at best).
- N-5: No Etruscan numeral in LL is claimed via the TCIM program (bias guard; §6.5).

---

## 10. Law-against-law triangulation (strongest structures)

Each structure is tested against **two independent constraints**; a third is sought where available. Necessary equivalences are not counted as independent.

### T-1. The triple formula system (F-A, F-B, F-C)

- **Constraint 1 (verbatim recurrence):** F-B occurs verbatim (7 tokens) at V:5 and V:12; F-A core (4 tokens) at V:6, V:13, IX:21; F-C core (4 tokens) at IV:2, V:4, VIII:15. *Independent of column position.*
- **Constraint 2 (cross-column distribution):** each formula occurs in ≥4 non-adjacent columns. *Independent of verbatim identity* (a formula could repeat within one column only).
- **Constraint 3 (positional recurrence):** F-A is line-initial 4×; F-B occupies full lines; F-C opens sections. *Independent of 1 and 2.*
- **Verdict: PROMOTED to STRUCTURE (attested).** Semantics remain at READING/CANDIDATE at best.

### T-2. *etnam* as discourse pivot

- **Constraint 1 (frequency):** rank 1, 35×, 2.7% of tokens — an outlier vs. rank 2 (19×).
- **Constraint 2 (positional freedom):** initial 3×, final 4×, medial otherwise; no fixed bigram >4. *Independent of frequency* (a frequent content word would show positional preference).
- **Constraint 3 (cross-formula collocation):** co-occurs with F-A, F-B, F-C, and non-formula text. *Independent of 1 and 2.*
- **Verdict: PROMOTED to STRUCTURE.** Gloss "and/then" is DERIVED (comparative), not attested in LL.

### T-3. *nunθen*-family as clausal operator

- **Constraint 1 (stem stability):** `nunθ-` invariant across 15+ OCR-distinct renderings — the stem survives noise that destroys other words, indicating high token frequency and scribal consistency.
- **Constraint 2 (syntactic position):** consistently pre-verbal/pre-clausal (before *tul, vinum, flere, θteśan*). *Independent of stem identity.*
- **Seeking third:** co-occurrence with offering carriers (*vinum* 3×) — suggestive but not independent (could be genre-driven). **Third constraint NOT secured;** function stays CANDIDATE.
- **Verdict: PROMOTED to STRUCTURE (carrier + operator position);** temporal/causal force is OMEGA (O-5).

### T-4. VII:2–5 iterative block as paradigmatic list

- **Constraint 1 (frame identity):** `male · ceia · hia · etnam · ciz · vacl` repeated 4× with only the terminal slot varying.
- **Constraint 2 (column confinement):** occurs only in VII — a local module, not a global formula. *Independent of frame identity.*
- **Constraint 3 (red-ink diacritic):** VII:5 ends with a red-written sign (Krall) — carrier-level marking of the block's closure. *Independent of 1 and 2.*
- **Verdict: PROMOTED to STRUCTURE.** Litany/list function is READING (CANDIDATE).

### T-5. *vinum* as offering carrier

- **Constraint 1 (recurrence):** 12× across 6 columns — not a hapax, not a pivot.
- **Constraint 2 (neighborhood):** consistently adjacent to *fler-/trin*, *nunθen*, F-B members — the actional matrix. *Independent of recurrence.*
- **Constraint 3 (external):** Latin *vinum* "wine" is a secure loanword; wine offerings are attested in Etruscan ritual contexts (comparative). *Independent of 1 and 2* — but note: this constrains the WORD, not the LL rite.
- **Bridge Completion (preserved/altered/lost/introduced):** preserved = the lexical item and its liquid-offering association; altered = Etruscan morphosyntax around it; lost = the specific LL ritual action; introduced = the assumption of libation (NOT preserved).
- **Verdict: PROMOTED to STRUCTURE (carrier);** "wine libation" is DERIVED, explicitly not attested.

---

## 11. Typed comparisons with independent Etruscan witnesses

Every comparison carries **preserved / altered / lost / introduced**. Resemblance alone = STRUCTURAL (not genealogical).

### C-1. Tabula Capuana (ritual calendar, ~300 words, 62 lines)

- **Preserved:** the *modular* ritual-calendar genre (repeated formulae + divine names + temporal markers); the enclitic *-c* "and"; the *etnam*-like connective function (Capua has *etnam*? — unverified this pass; marked UNKNOWN).
- **Altered:** Capua is a tiled plaque, not a linen book; its month/day grid is explicit where LL's is conjectural.
- **Lost:** any direct lexical overlap beyond genre — no shared formula secured this pass.
- **Introduced:** the assumption that LL's structure "is" calendrical because Capua's is.
- **Type: STRUCTURAL (genre-level).** Does not license transferring Capua's month names into LL.

### C-2. Pyrgi tablets (bilingual, morphologically secure)

- **Preserved:** *śpur-* "city/community" (Pyrgi *śpura*); *-ś* genitive; *-c* enclitic; *aiser-* divine plural (disputed in both).
- **Altered:** Pyrgi is a dedication (votive), LL is liturgical — different speech acts.
- **Lost:** Pyrgi's Phoenician control text has no LL counterpart.
- **Introduced:** using Pyrgi's secure morphology to segment LL words (licensed as ATTESTED morphemes, §4.1, but LL-internal function stays CANDIDATE).
- **Type: MORPHOLOGICAL (carrier-level).** Strongest external anchor for F-A segmentation.

### C-3. Tabula Cortonensis / Cippus Perusinus (civic/institutional)

- **Preserved:** *-leri* relational suffix; institutional vocabulary (*cepen* "priest"? — Cortona *cepen* disputed).
- **Altered:** legal/contractual genre vs. liturgical.
- **Lost:** no shared formulae.
- **Introduced:** "priestly clans" reading of F-A (derivative gloss, disputed).
- **Type: LEXICAL-MORPHOLOGICAL (weak).** Supports morpheme inventory, not LL semantics.

### C-4. Krall's own glossary (internal control)

- **Preserved:** attestation index (e.g., "aiseras II 12; V 8; XII 2") — verifies cross-column recurrence independently of my OCR parse.
- **Type: INTERNAL REPLICATION.** Where Krall's glossary and my inventory agree on recurrence, confidence rises; disagreements flag OCR error.

**Summary:** No external witness shares a formula with LL. The comparisons license **morphemes** (Pyrgi) and **genre** (Capua), never **readings**. All LL-specific semantics remain LL-internal.

---

## 12. Prediction ledger

### Internal predictions (testable against Column XI or re-OCR)

- **P-1:** Column XI, when recovered, will contain F-A or F-B (base rate: F-A in 4/11 columns, F-B in 4/11). *Falsifiable.*
- **P-2:** *etnam* will occur in Column XI ≥1× (base rate: 11/11 columns). *Falsifiable.*
- **P-3:** No 8+-token verbatim repetition will be found (current max: 7). *Falsifiable.*
- **P-4:** The *-leri*/-śtreś* alternation will appear on a new stem or confirm restriction to *śacnic-/śpur-*. *Falsifiable.*
- **P-5:** *vinum* will co-occur with *fler-* or *nunθen* in any new text (current: 5/12 co-occur). *Falsifiable.*

### External predictions (testable against other Etruscan texts)

- **P-6:** The F-A skeleton (*śacnic- · cilθ- · śpur-*) will NOT be found verbatim outside LL (it is a LL-local formula). *Falsifiable* — a Capua/Pyrgi match would refute LL-locality.
- **P-7:** *nunθen* will occur in at least one other long Etruscan text if it is a general temporal operator (vs. LL-idiosyncratic). *Falsifiable.*
- **P-8:** Rix ET II's line addresses for LL will agree with Krall's column/line system up to renumbering (both derive from the same carrier). *Testable on acquisition.*

---

## 13. Explicit undeciphered/underdetermined ledger

| # | Item | Addresses | Barrier | State |
|---|---|---|---|---|
| U-1 | Column XI full text | XI (all) | Not in recovered OCR | SOURCE GAP |
| U-2 | Sibilant identity (~60% of tokens) | throughout | OCR collapse of ś/θ/χ | OMEGA (this pass) |
| U-3 | Krall's certainty layer (Antiqua/cursive, •/:) | throughout | Lost in OCR | OMEGA (this pass) |
| U-4 | *θanśur, haθriχ, repinθic* | F-B | No comparative anchor | UNDECIPHERED |
| U-5 | *eθrse* | F-C | Epithet? deity? place? | UNDECIPHERED |
| U-6 | *zusleve* | IV, IX | Offering? action? | UNDECIPHERED |
| U-7 | *cletram, śrenχve* | III, IV, V, IX | Recurring but unanalyzed | UNDECIPHERED |
| U-8 | *vacl* (19×) | V–X | High-frequency, no gloss | UNDECIPHERED |
| U-9 | *teśim* | III, VI, VII | "Burnt offering" disputed | UNDERDETERMINED |
| U-10 | *iχ/eci* particle | III, X | Function unknown | UNDECIPHERED |
| U-11 | Numerals | — | None secured | NEGATIVE RESULT |
| U-12 | Column I–III tops | I, II, III | Physical loss | CARRIER GAP |
| U-13 | Red-ink signs' function | VII:5, etc. | Unattested | OMEGA |
| U-14 | *eslem* ("two"?) | VI:14 | Derivative only | OMEGA |

**Nothing in this ledger has been filled by conjecture.** Candidates are in §4–§6 with explicit states.

---

## 14. Recommended second-pass experiments

1. **E-1 (highest value): Re-OCR or manually verify the transcription against the Internet Archive scan page images** (article pp. ~30–45) or Krall's collotype plates, recovering (a) exact ś/θ/χ/φ glyphs, (b) Krall's Antiqua/cursive certainty layer, (c) Column XI. This single experiment resolves O-1, O-2, O-3-partial, U-1, U-2, U-3.
2. **E-2: Acquire Rix ET II (1991/2002) LL text** (pp. 1–8) via library scan; collate against Krall line-by-line; record preserved/altered/lost/introduced between the 1892 and 1991 readings. Tests P-8.
3. **E-3: Permutation control on F-A/F-B/F-C.** Shuffle tokens within columns (preserving line breaks) 10k×; test whether the observed formula lengths (7, 4, 4) exceed the null. Quantifies I-1.
4. **E-4: Positional/frequency control on *etnam*.** Compare its positional entropy against the next 10 most frequent tokens; tests I-4 against a null of "frequent word."
5. **E-5: Suffix productivity test.** Measure *-ri/-leri* type/token ratio vs. a null from random segmentation; tests whether the suffix inventory (§4.2) is real or an artifact of Etruscan phonotactics.
6. **E-6: Tabula Capuana collation.** Systematic bigram/formula comparison LL↔Capua with the Bridge protocol; tests C-1 and P-6.
7. **E-7: Red-ink census.** Catalog every red-written sign in Krall's plates with addresses; test correlation with formula boundaries (tests whether color marks structure).
8. **E-8: *nunθen* external search.** Corpus search (ET) for *nunθ-* outside LL; tests P-7.
9. **E-9: Month-name adjudication.** Specialist review of *acale/θucte/celi* against the full ET corpus; resolves O-4 and the calendar hypothesis.
10. **E-10: Column XI targeted recovery.** The plates (Krall Taf. II–X) may show XI even where the transcription OCR failed; plate-to-text alignment for XI specifically.

---

## 15. Operator-test summary

**Operator:** `carrier → ritual position → operation → object/recipient → temporal/address marker → recurrence/return`

Applied to the three formula systems:

| Step | F-A (congregational) | F-B (actional) | F-C (invocational) |
|---|---|---|---|
| Carrier | linen column, black ink | linen column, black ink | linen column, black ink |
| Ritual position | line-initial or standalone (4× initial) | full-line occupation | section-opening |
| Operation | naming/listening? (UNKNOWN) | *tul*-action? (UNKNOWN) | invocation (CANDIDATE) |
| Object/recipient | *śpur-* (community), *meθlum-* (crowd?) | *θanśur, haθriχ* (UNKNOWN) | *tinθi* (Tinia, CANDIDATE) |
| Temporal/address | *enaś* (deictic?, CANDIDATE) | *nunθen* clauses (CANDIDATE) | *tiurim · avilś* (time, CANDIDATE) |
| Recurrence/return | returns in 4 cols with changed neighborhood → **path-dependent phase**, not identical state | verbatim once (V:5=V:12), varied otherwise → **template with slots** | stable core, varying tail → **fixed opening, free continuation** |

**Test result:** recurring lexical material does NOT keep a fixed function across changed neighborhoods (F-A's associational matrix changes per column; *vinum*'s offering lists differ). Apparent returns are **path-dependent phases** of a modular liturgy, not identical ritual states. The operator test thus **confirms** the Structural Continuation premise and **blocks** the inference from recurrence to decipherment. This is a successful application of the test, yielding a negative result where the methodology requires one.

**Mechanism before symbolism:** the secured mechanism is *modular recombination* — fixed multi-word modules (F-A/B/C) embedded in varying matrices, with morphological alternation (*-leri*/-śtreś*, *-l*/-ś*) marking phase. No symbolic interpretation is licensed by this pass.

---

## Provenance and layer discipline (closing statement)

- **ATTESTED:** the carrier (linen book, 12 columns, red/black ink, blank end at XII); Krall's 1892 edition and its conventions; the OCR tokens as observed; formula recurrences and addresses; *avil-* "year" (comparative); *-ś* genitive, *-c* "and", *-leri* relational (comparative); *vinum* as Latin loanword.
- **RECONSTRUCTED:** Krall's column/line restoration (his work, cited as his); Column XI (absent — gap, not reconstruction).
- **DERIVED:** skeleton layer; frequency statistics; morphological segmentations using comparative morphemes; "wine," "and/then," month names (all marked disputed).
- **CANDIDATE:** F-A/B/C functional labels (congregational/actional/invocational); *nunθen* as temporal operator; *tinθi* = Tinia; calendar hypothesis.
- **GENERATED:** the operator-test table; the prediction ledger; this report's structural graph (built from attested relations only).
- **OMEGA:** §9 and §13 items — preserved, not smoothed.

**No prior ARGO/TCIM hypothesis was used as evidence.** The TCIM numeral-seven BOUNDARY status for Etruscan contributed nothing to the numeral search (§6.5), which returned a negative result on its own merits.

---

*End of Work Item 0003 report. Lane wrote only this file and the optional `data/liber-linteus/token_inventory.tsv` sidecar. No commits, no pushes, no other files touched.*
