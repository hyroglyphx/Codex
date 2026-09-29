# Liber Linteus Column XI Holdout Validation — Attempt Record (report 06)

**Lane:** Jethro independent research, Codex relay. **Steward directive:** inbox Message 0006.
**Outcome: `SOURCE_GAP` / `HOLDOUT_UNSCORABLE`.** No scoring performed; predictions P-1…P-8
remain FROZEN-UNTESTED.

## 0. Position in the evidential chain

Message 0006 required: `report 03 freeze (52525c5) → report 04 freeze (8d9b933) →
pass 2 D1 null results (66a7729) → Column XI holdout exposure → scored predictions →
ResultPacket`. The chain executed through pass 2 and the pre-exposure gate, then terminated
at acquisition with SOURCE_GAP. Per Message 0006 ("If XI cannot be recovered at sufficient
fidelity, return SOURCE_GAP / HOLDOUT_UNSCORABLE. Do not substitute another column"), this
is a first-class outcome, not a failure to report.

## 1. Pre-exposure gate (executed by parent agent before any acquisition work)

Recorded in `data/liber-linteus/xi_holdout_run_manifest.json`:

1. Freeze commit verified: `8d9b933a29d553e5078f91e9e11b450a33b31014` contains the frozen
   `prediction_manifest.json` and report 04.
2. P-1…P-8 unchanged since freeze: blob SHAs of `prediction_manifest.json`
   (`fc458513…`), `resultpacket_schema.json` (`e2933839…`),
   `d2_transformation_ledger.tsv` (`004485fb…`), and report 04 (`16dad2eb…`) are
   identical at the freeze commit and at tip `66a7729`. No PREREGISTRATION INTEGRITY
   FAILURE.
3. Pass 2 closed: `resultpacket_pass2.json` committed in
   `66a77296305dd1d94eb345db0422895c3ba065b4`.
4. `XI_EXPOSURE_NOT_YET_BEGUN` recorded before acquisition began.

## 2. Acquisition attempt

A blinded acquisition agent (forbidden from reading `prediction_manifest.json`; exact
prediction texts never visible) searched 15 candidates for a Column XI witness at
diplomatic fidelity. Full trail in `data/liber-linteus/xi_w0_provenance.json`. In brief:

- **Krall 1892 scans** (Internet Archive, HathiTrust, Reinach/MOM): the edition that
  supplied pass 1 — fetch timeouts and HTTP 403; pass-1's OCR of the same scan lacked
  Column XI entirely. Not bypassed, not retried against instruction.
- **Modern scholarly editions** (Rix 1985, Rix ET II 1991, van der Meer 2007, Belfiore
  2010): the Column XI text exists in these — print-only, no accessible online copy.
- **Mirnik & Rendić-Miočević 1986/87** (open access): pre-dates the modern column
  reconstruction; not a usable XI source.
- **Copeland/Maravot amateur transcription**: exists but organized by idiosyncratic
  "Scripts," author states working images were very poor — judged insufficient fidelity,
  not used.
- **ETP, OpenEtruscan, AMZ, Wikimedia Commons, legacy etext mirrors**: no usable XI
  witness. Wikipedia/secondary: isolated lexical citations only, not transcription.

**Core finding:** the modern scholarly Column XI text exists but is locked in print
editions with no legitimate accessible online copy. No D0/D1 layers were produced —
writing empty files would misrepresent the outcome; writing inferred text would violate
the holdout. No column substitution, no reconstruction from memory.

## 3. Blinding and contamination

- `prediction_manifest.json` was never opened by the acquisition agent
  (`prediction_manifest_accessed: false` in the contamination ledger).
- Four incidental exposures are honestly recorded in
  `data/liber-linteus/xi_contamination_ledger.json` — isolated lexical items from search
  snippets and Wikipedia (`veive` [XI]; `Satrs` at 11.f4; `Velθa` in 7/10/11;
  `Veive-/Vetis` in 10/11). Assessed as non-acquisition: no line-addressable
  transcription, no scoring performed against them, no prediction criterion triggered.

## 4. Standing of the holdout

- The holdout remains **open and unscored**. P-1…P-5 (XI-designated) and P-6…P-8
  (external) are all FROZEN-UNTESTED.
- Unblocking requires consulting a print edition (Rix ET II or van der Meer 2007)
  through a library or other legitimate channel — a human procurement step, out of
  scope for this agent.
- Any future acquisition must repeat the pre-exposure gate (re-verify frozen hashes —
  the four incidental exposures are now on record in the contamination ledger) and the
  same blinding protocol before scoring.

## 5. Judgment calls disclosed

1. Treating fetch timeouts as terminal for those candidates (per the agent's
   instructions, not retried) — a faster or credentialed route might succeed; recorded
   rather than assumed.
2. Rejecting the amateur transcription on fidelity grounds rather than attempting to
   salvage it — a salvage attempt would have risked contaminating the blind with
   low-quality text shaped by unknown editorial choices.
3. Writing no D0/D1 files rather than empty placeholders — the absence is itself the
   machine-readable outcome (`d0_d1_produced: false`).

---

*End of attempt record. Sidecars: `xi_w0_provenance.json` (search trail),
`xi_contamination_ledger.json` (4 incidental exposures), `xi_holdout_run_manifest.json`
(gate + exposure records). Column XI was not acquired in usable form. The frozen
predictions are untouched.*
