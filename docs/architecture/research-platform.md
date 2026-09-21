# Reconciled Research Platform Architecture

Status: **Recovered + Reconstructed integration checkpoint**  
Checkpoint date: **2026-09-20**  
Branch: `research/reconcile-state-2026-09-20`

## Canonical flow

```text
Confluence
   ↓
Relay Kernel
   ↓
Nexus
   ↓
Thought Sieve / Council
   ↓
Adversary
   ↓
Organon
   ↓
Builder
   ↘
 ResultPacket ──→ Relay Kernel ──→ accepted state / exception queue
```

### Separation of concerns

- **Confluence** reconstructs emergence: it gathers the live research streams without declaring them equivalent.
- **Relay Kernel** preserves change: append-only events, state transitions, validation, routing, logging, testing, merge/version provenance, and return paths.
- **Nexus** identifies lawful cross-domain bridges.
- **Thought Sieve / Council** applies explicit perspective transforms and records which parser produced which interpretation.
- **Adversary** runs counterexamples, negative controls, contradiction checks, ablations, and failure preservation.
- **Organon** chooses the next admissible operation or experiment.
- **Builder** implements artifacts, software, documents, simulations, tests, and public surfaces.
- **ResultPacket** returns implementation outcomes to the kernel for acceptance, repair, quarantine, supersession, or further testing.

**Correction preserved:** kernel ≠ domain ≠ interface.  
A storage/event kernel is not itself a mathematical theory, symbolic domain, website, or user interface.

## Six relay primitives

1. **State** — current normalized project condition.
2. **Event** — immutable transition record.
3. **Object** — research entity being transformed or tested.
4. **Claim** — proposition with evidence, counterevidence, maturity, and authority.
5. **WorkPacket** — bounded operation sent to an agent/tool/builder.
6. **ResultPacket** — returned outcome with provenance, losses, changes, and next-state implications.

## Authority ladder

- **L0 Source** — original witness, data, artifact, inscription, code output, or directly observed evidence.
- **L1 User** — explicit research instruction, declaration, naming, correction, or scope rule.
- **L2 Canonical** — accepted project definition, schema, invariant, protocol, or frozen baseline.
- **L3 Validated** — derivation or result that survived an explicit test within its declared scope.
- **L4 Hypothesis** — exploratory inference, proposed bridge, reconstruction, or generated association.

No additional authority level is canonical in this checkpoint.

## Promotion states

Main path:

```text
OBSERVED → CANDIDATE → TESTED → CORROBORATED → CANONICAL
```

Permanent or non-promoting states:

```text
FAILED | CONTRADICTED | SUPERSEDED | Ω-UNRESOLVED
```

Corrections are append-only: never rewrite the event that was wrong. Append a challenge, test, supersession, or replacement event that points back to it.

## Governing loops

### IER loop

```text
Object
→ Partition
→ Representation
→ Admissible Operations
→ Invariant Extraction
→ Attractor Detection
→ Compression
→ Regeneration
```

### ARGO / return loop

```text
Witness
→ Carrier
→ Transformation
→ Relation
→ Evidence
→ Feedback
→ Return
```

Return is necessary but not sufficient: require carrier return, identity continuity, proof/evidence closure, and ethical/admissibility checks where the domain needs them.

### Governance loop

```text
PROMOTE ↔ HOLD ↔ REPAIR ↔ QUARANTINE ↔ ROLLBACK
```

Governance is a rollback loop, not a one-way approval ladder.

## Implementation rule

Every major research object should be expressible simultaneously as:

1. an **IER object**,
2. one or more **OrganonEvents**,
3. a set of **claims with authority + maturity**,
4. a **return path** explaining how the result can be traced to its carrier/source,
5. an **adversarial test plan**, and
6. a **Builder target** when implementation is appropriate.
