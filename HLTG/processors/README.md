# Processor Pipeline

Canonical flow:

`INGEST -> TYPE -> ADDRESS -> DEPENDENCY-GROUP -> TEXT-LAYERS -> FEATURE EXTRACTION -> CANDIDATE EDGES -> CRYPTO-SCRIBE -> RIIR -> NULLS -> HOLDOUT -> REVIEW`

## Artifact processors

Processors should be modular and may operate before language identification:

- sign frequency and positional distribution
- repeated sequence / formula detection
- document topology detection
- reading-direction/chirality states
- numeral + unit + operator + address parsing
- onomastic/name candidate detection
- phonotactic profiles
- morphological recurrence/clustering
- bilingual/bigraphic alignment
- lexical/semantic candidate neighborhoods
- chronology/geography/contact admissibility
- source-dependency grouping
- holdout regeneration

## Search ladder

Cross-script/historical searches must expose the level used:

`EXACT_SIGN -> ALLOGRAPH -> NORMALIZED_SIGN -> PHONOLOGY -> RELAXED_HISTORICAL_FORM -> DIACHRONIC_FORM`

A hit at a relaxed level must never be presented as an exact match.

## Independence

Independent evidence routes are graph objects. Multiple editions, translations, or publications derived from the same physical witness share a dependency group unless independent observation is demonstrated.

## Ingestion

External corpora may be imported as source snapshots or adapters. Preserve upstream IDs, licensing, version/date, transformations applied, and original text alongside normalized forms. External proposed decipherments enter as hypotheses, not facts.
