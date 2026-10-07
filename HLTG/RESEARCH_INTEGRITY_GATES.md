# Research Integrity Gates v0.1

This document turns the Codex/HLTG research method into repository invariants.

## Epistemic separation

The following layers are distinct and MUST NOT be silently collapsed:

```
raw witness != observation != reading != interpretation != historical claim
```

Promotion is ordered:

```
ADMISSIBILITY -> SCORING -> INFERENCE -> PROMOTION
```

A record may remain UNSCORABLE when prerequisite feature space is missing. Null, contradictory, bounded, rejected, and failed-prediction results are preserved.

## Provenance gates

1. Recovered, Reconstructed, Generated, and Missing states remain explicit.
2. A generated reconstruction may not be relabeled as recovered historical fact without source-addressed evidence.
3. Witness identity, observation, reading, interpretation, and historical claim must remain separately addressable.
4. Translation equivalence does not by itself establish etymology or historical transmission.
5. Surface glyph, grapheme, and phonetic value remain distinct.
6. Sign arity, phonological load, root arity, morphology, and semantic compression remain distinct.
7. Spectral/structural order is not chronological order unless chronology is independently demonstrated.

## Validation gates

1. Prefer explicit ancient crosswalks over retrospective resemblance for calibration.
2. Cross-witness recurrence outranks repetition internal to one witness.
3. Genealogical, witness, scholarly, temporal, and transmission/contact dependence must be modeled before evidence is counted as independent.
4. Holdout regeneration and prospective prediction outrank retrospective fit.
5. Frozen weights/features may not be changed retroactively to rescue a favored relation; changes require a new version.
6. Failed frozen predictions remain evidence.
7. Missing or damaged witness material is not semantic omission.
8. Alignment support and historical-relation support are separate quantities.

## Repository checks

CI MUST at minimum:
- parse every HLTG YAML file;
- reject duplicate mapping keys;
- reject unresolved merge-conflict markers;
- require the core HLTG directories and methodological contract files;
- keep the validation script dependency-light and deterministic.

Future gates should add schema validation, cross-file referential integrity, provenance-chain validation, promotion-rule enforcement, blind/holdout leakage detection, benchmark regression, and Muse/Jethro packet conformance.
