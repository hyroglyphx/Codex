# Δ-001B — End-to-End Artifact Loop

This benchmark complements Δ-001A.  
Δ-001A tests research-state reconstruction.  
Δ-001B tests whether one evidence record survives the full product loop.

## Pipeline

```text
Witness
→ Nexus Corpus
→ HistoricalRecord
→ Inference Engine
→ GlyphWalk
→ Transposition Atlas
→ ResultPacket
→ Relay Kernel
→ corrected / promoted corpus state
```

## Required assertions

### Source fidelity
- Complete readable source remains available.
- Unreadable/damaged material is marked, never silently dropped.
- Source image/text/transliteration remain linked.

### Layer separation
- carrier, normalized value, reading, language, meaning, and relation type remain separately addressable.
- no surface normalization overwrites the exact witness.

### Inference discipline
- transformations are typed.
- admissibility basis is recorded.
- confidence is dimensional rather than a single undifferentiated score.
- genealogy/contact dependence is not counted as independent support.

### Adversarial behavior
- at least one negative control is attached.
- at least one withheld element is predicted before reveal.
- failures are retained in the returned result.

### Product consistency
- GlyphWalk and Atlas render the same record IDs.
- differences are view/granularity differences, not competing facts.
- both surfaces can navigate back to the same witness/provenance.

### Return closure
- the final ResultPacket lists preserved / altered / lost / introduced information.
- any correction produces a new event rather than rewriting history.
- provenance can be reconstructed from result to original witness.

## First implementation fixture

Use the supplied Marduk-apla-iddina / Middle Babylonian GlyphWalk example as the first UI fixture because it already demonstrates:
- complete-text-first presentation,
- transliteration,
- literal translation,
- smoother reading,
- contextual notes,
- confidence,
- uncertainty/method notes.

The fixture is for architecture testing; historical or philological claims should be independently source-linked before canonical promotion.
