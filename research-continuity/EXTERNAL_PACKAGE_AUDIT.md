# Legacy package mining decisions

Inspected the three ZIP archives in the connected private Website-Works repository on 2026-10-19. No package was executed or deployed.

## Anamnesis Chat
Two files: WordPress PHP plugin and a placeholder JavaScript frontend. The PHP endpoint forwards user-provided messages to a chat-completions service. It does not provide persistent archival ingestion, historical retrieval, or research provenance. The route is configured with an unrestricted permission callback and the plugin defines the same shortcode twice. **Do not import unchanged.** Retain only the idea of a future authenticated WordPress ingestion interface.

## Codex Core Package
README plus Python script that prints a startup line. No substantive research engine. **Archive as historical stub.**

## GHAT Harmonic Interpreter
A WordPress shortcode accepts a symbolic term, removes a small set of English stopwords and suffixes, and emits a truncated MD5 digest. This is a string fingerprint, not evidence of semantic or harmonic identity. HTML output includes the submitted term without explicit output escaping. **Do not import unchanged.** A source-byte digest and versioned canonicalization may help future deduplication, but hashes alone do not establish conceptual equivalence.

## Reuse priority
1. Existing Codex Relay and Reuptake event log remain the canonical continuity backbone.
2. RCK will provide source manifest, retrieval coverage, and candidate duplicate detection.
3. Any public-facing WordPress interface must require appropriate authentication, authorization, rate limits, input validation, and output escaping.
4. Keep private research transcripts out of the public repository.

This is a source review, not a runtime/security certification.
