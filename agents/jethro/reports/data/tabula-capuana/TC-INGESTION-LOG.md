# TC ingestion log

Append-only. Each entry: date, actor, what was done, witness state.

## 2026-10-05 — Jethro (scaffolding)

- Verified frozen artifacts: report 07 (`agents/jethro/reports/07-tabula-capuana-preregistration.md`)
  and manifest (`agents/jethro/reports/data/tabula-capuana/tc_preregistration_manifest.json`).
  Note: manifest lives under `agents/jethro/reports/data/`, not `data/` as one
  background note had it — corrected here.
- Workspace sweep: no van der Meer 2014/15 or Cristofani 1995 transcription on
  disk. Only `~/workspace/user/files/Tabula_Capuana_-_Wikipedia.pdf`, which
  report 07 §1 bars as authority. **Ingestion NOT started — Gate 0 open.**
- Scaffolding built (no corpus content): `INGESTION-CHECKLIST.md`,
  `tc_d1_normalize.py` (report 04 §2.1 rules; VERIFIED: reproduces all 1,277
  LL D0→D1 pairs exactly — mapped chars stay uppercase S/T, `^` dropped;
  non-listed specials like θ pass through unchanged, matching the frozen
  candidate spellings), `tc_token_schema.md`, `tc_test_harness.py` (4
  manifest-driven skeletons, NO_CORPUS guards), this log.
- Bleed controls restated: XI chain sealed; nothing outside the four tests is
  confirmatory.

## 2026-10-05 — user directive: HOLD

- User: "Hold. Move on." TC-1 lane HELD. No procurement, no ingestion.
- Scaffolding remains in place for whenever the lane reopens.
- Bleed controls continue to hold: XI sealed, no cross-lane leakage.

## 2026-10-13 — Jethro (TC-1 execution, Idea activation)

- Gate 0 CLOSED: W0_TC obtained — van der Meer 2014/15, "Some comment on the
  Tabula Capuana" (Studi Etruschi 77, pp. 149–175), Appendix I (pp. 165–173),
  full text via the author's Academia.edu posting. Wikipedia transcription NOT
  used as authority (report 07 §1). Cristofani 1995 not consulted for readings.
- Gates 1–3 complete: D0 diplomatic capture (321 tokens, §§1–10, lines 1–62);
  structural flags (section dividers, damage); D1 via `tc_d1_normalize.py`
  UNCHANGED (verified: D1 == lowercase(D0) across all 321 tokens; frozen
  mapping chars absent). D0/D1 1:1 row-aligned inventory written
  (`tc_token_inventory.tsv`, 642 rows). No red-ink rulings marked in this
  witness (incised terracotta); schema flags supported but empty.
- Gate 4: D1 inventory reconciled against the appendix line inventory
  (lines 1–62 continuous; §5 line 29 empty). Frozen parameters re-read from
  the manifest. Lane harness stubs NOT modified (frozen scaffolding); the
  four tests were implemented once, in the execution script, against the
  D1 inventory.
- Gate 5: seeds declared at execution (TC-MARCH forward 20261013, reverse
  20261014; 10,000 iterations). Verdicts: TC-RI FAILURE (1/5); TC-TUL
  INDETERMINATE (tul(e) 0 standalone occurrences); TC-NUNΘ NO FROZEN
  VERDICT (rule gap: T1 PASS, T2 FAIL, T3 FAIL); TC-MARCH FAILURE
  (p_fwd 1.00, p_rev 0.27). Line-26 nuthe-ri check logged exploratory-only
  (no such form at line 26; nearest damaged form at line 25).
- Bleed controls hold: no Column XI text; no Magliano text; vacil H_A/H_B
  discriminators not executed; nothing outside the four tests confirmatory.
- Deliverables: ingested corpus document + token inventory table +
  verdict report (user-facing files).
