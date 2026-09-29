# Independent Test: 24 / 25 / 49 / 50 / 1225 and the S_49⊕1_g Construction

**Lane:** Jethro (independent) · **Date:** 2026-09-29 · **Status:** L4 Hypothesis / GENERATED test report
**Method:** Attempt falsification first. Classify every finding:
PROVEN (arithmetic) / RECOVERED (prior Codex structure) / STRUCTURAL (correspondence, no transmission
claim) / HISTORICAL (witness-grounded) / GENERATED (new hypothesis) / FAILED (negative result).
Disagreements preserved, not harmonized.

## 1. Arithmetic audit — PROVEN

| # | Identity | Verified |
|---|----------|----------|
| A1 | 49 = 24 + 1 + 24 | ✓ |
| A2 | 50 = 49 + 1 | ✓ (trivial successor) |
| A3 | 1225 = 25 × 49 | ✓ |
| A4 | 1225 = 49 × 50 / 2 | ✓ |
| A5 | 1225 = C(50,2) | ✓ |
| A6 | C(50,2) − C(49,2) = 1225 − 1176 = 49 | ✓ |
| A7 | 1225 = T_49 (49th triangular number) | ✓ |
| A8 | 1225 = 35² | ✓ |

**Necessary-equivalence clusters (do NOT constitute independent evidence):**

- **Cluster α:** A3 = A4 = A5 = A7. Proof: 25 = 50/2, so 25×49 = 49×50/2 identically; C(50,2) = 50×49/2
  by definition; T_n = C(n+1,2) so T_49 = C(50,2) identically. **One arithmetic fact in four
  notations.** Presenting "25(49)", "49(50)/2", and "C(50,2)" as converging lines of evidence is
  triple-counting. Per SCGD §10 (arithmetic identity ≠ semantic identity), none of them promotes
  anything by itself.
- **Cluster β:** A8 (35²) is the same integer again — a fifth notation, not a fifth fact. (Noted
  because square-representations are a classic source of spurious "independent" coincidences.)
- A1 stands alone but is weak (see F3). A2 is trivial. A6 is true but generic (see F2).

## 2. Falsification attempts

### F1 — "1225 appears in three forms" as converging evidence
**Attempt:** Treat A3, A4, A5 as independent witnesses to structure.
**Result: FAILED** (the claim, not the arithmetic). Cluster α shows they are necessarily equivalent.
*Classification: FAILED negative result against the independence claim; arithmetic itself PROVEN.*

### F2 — C(50,2)−C(49,2)=49 as distinctive graph-theoretic support
**Attempt:** Check whether the identity discriminates the 49/50 structure from any other n/(n+1).
**Result: FAILED.** C(n+1,2) − C(n,2) = n holds for **all** n (the (n+1)-th vertex of K_{n+1} has
degree n). It would equally "support" 30⊕1, 99⊕1, 6⊕1. Zero discriminating power for 49/50
specifically. The statement "adjoining one element to a 49-element complete relational field
introduces exactly 49 new unordered relations" is true and contentless as evidence.
*Classification: FAILED as supporting evidence; PROVEN as arithmetic.*
**Codex alignment:** GGA already states the homogeneous version ("the additional 51st node
contributes exactly 50 additional unordered edges") and separately rules "do not treat K50 or K51
as historically meaningful by default." The same restraint applies here, a fortiori.

### F3 — 49 = 24+1+24 as a distinguished decomposition
**Attempt:** Check whether the palindromic split is canonical.
**Result: FAILED as distinguished.** 49 admits 49 decompositions a+1+(48−a); 24+1+24 is one
arbitrary symmetric choice. The mathematically distinguished properties of 49 are 7² and (in this
context) T_49-adjacency — not the palindrome. If 24 carries independent meaning (24 = 4!, hours,
elders — none recovered in the Codex), that meaning must be evidenced separately; the arithmetic
does not supply it.
*Classification: FAILED as structural evidence; PROVEN as arithmetic.*

### F4 — Is there a 49 in the Codex?
**Attempt:** Repo-wide grep for 49-structures, fifty-gates/Binah traditions, 7×7.
**Result: FAILED — no 49-structure recovered.** The Codex's distinguished-terminal structure is
**50⊕1 = 51** (Marduk: 51 transmitted names vs "Fifty" rubric; 51st typed `terminal_control`;
discrepancy explicitly preserved, not normalized — RECOVERED, registries/marduk-fifty-names-
ingestion-v0.1.yaml). The S_49⊕1_g hypothesis therefore has **no Codex-internal 49-anchor**.
Its *type* (complete field ⊕ distinguished terminal element) is recovered; its *instantiation*
(49/50) is not.
*Classification: FAILED (absence is data); the 50⊕1 type is RECOVERED.*

### F5 — Does GGA support a *typed* 1_g, or only homogeneous node addition?
**Attempt:** Check whether the Codex distinguishes gate-element adjunction from homogeneous growth.
**Result: SPLIT.**
- GGA formalism: homogeneous only. Node addition is counted ("exactly 50 additional unordered
  edges"), never typed. Under GGA as written, 1_g *is* "merely a 50th homogeneous state."
  The typed construction S_49⊕1_g is **not derivable** from GGA alone.
- Marduk registry: typed. The 51st name is `terminal_control`, the closure is a separate typed
  object ("Fifty rubric, transmission instruction"), and the discrepancy is preserved by rule.
  This is field⊕distinguished-terminal *as typed practice* — but at 50⊕1, and in registry
  convention, not in gate-algebra formalism.
*Classification: STRUCTURAL correspondence (type-level) between the proposed S_49⊕1_g and the
Marduk 50⊕1 registry practice; GENERATED as a gate-algebra extension (would require a typed
adjunction operator GGA does not currently define).*

### F6 — Can 1_g "relate one completed carrier field to another"?
**Attempt:** Find Codex machinery for inter-field continuation.
**Result: PARTIALLY RECOVERED.** Components exist but are not composed into the claimed role:
- Continuation operator Γ(X) = (P,T,A,L,I,R) with return state R (SCGD) — RECOVERED.
- `return_path` as a required field on every bridge edge and every OrganonEvent — RECOVERED.
- Organon workflow terminates in RETURN TO WITNESS — RECOVERED (recursive return as practice).
- What is **missing**: any definition of a *completed carrier field* as a formal object, any typing
  of edges incident to a gate element vs field-internal edges, and any composition rule for
  field→gate→field transit. The "relating" function of 1_g is therefore GENERATED hypothesis,
  compatible with Codex machinery but not derived from it.
*Classification: machinery RECOVERED; the specific 1_g role GENERATED.*

## 3. Typed-ontology mapping (state / carrier / gate / quotient / involution / delegation / carrier rebinding / recursive return)

| Proposed type | Codex status | Source |
|---|---|---|
| state | RECOVERED — CodexState; Γ return state R | witness-protocol §State model; SCGD |
| carrier | RECOVERED — "witness-bearing carrier" | witness-protocol |
| gate | RECOVERED — G(B), GateOrbit, 231/462 | GGA; SCGD |
| quotient | RECOVERED — G(B) = D(B)/⟨σ⟩, explicit | GGA core object |
| involution | RECOVERED — σ(x,y)=(y,x), σ²=id | GGA core object |
| delegation (c_n,I)→(c_{n+1},I′) | GENERATED notation; content RECOVERED | see §4 |
| carrier rebinding | RECOVERED — NAME-02/NAME-03/TRN-02 + negative controls | older-name-carrier-rebinding-v0.1.yaml |
| recursive return | RECOVERED — return_path; RETURN TO WITNESS | bridge-protocol; Organon workflow |

7 of 8 proposed distinctions exist in the Codex as independently typed concepts. **Delegation is the
genuine novelty** — and its novelty is notational, not substantive (see §4).

## 4. Delegation abstraction (c_n,I)→(c_{n+1},I′)

**Content audit — RECOVERED, distributed across three Codex structures:**
- Bridge protocol: every edge records *preserved / altered / loss / introduced material / return
  path* — exactly the I→I′ ledger with carrier change. B7 FUNCTION_OPERATOR_TRANSPOSITION is
  carrier-change-with-invariant-preserved; B4 READOUT_TRANSPOSITION is its dual (carrier persists,
  reading changes).
- OrganonEvent canonical fields: `preserved[], altered[], lost[], introduced[]` — the same ledger
  as event grammar.
- Carrier-rebinding operators (NAME-03: preexisting name rebound to mythic role; TRN-02: entity
  gains new identity under changed jurisdiction) are worked examples of delegation with I tracked.
- Witness Protocol stress case 6 (Enoch/Seth/Hermes): "knowledge moving across pillars, tablets,
  inscriptions, books, languages, and generations" as *models for carrier-change and custody* —
  delegation avant la lettre, with historical dependence separately typed.

**What is GENERATED:** the compact notation itself, and any *algebra* of delegation (composition
(c_n,I)→(c_{n+1},I′)→(c_{n+2},I″), identity delegation, delegation failure modes). The Codex
records delegations; it does not compute with them. Proposing a delegation calculus is legitimate
GENERATED work — it must then survive the promotion rule (frozen map, measurable invariant,
adversarial null).

**Falsification note:** The abstraction adds no new empirical content over the bridge+OrganonEvent
machinery. Its value, if any, is compressive/formal, not evidential. Claiming otherwise would
violate the Codex's own model-compression ≠ discovery separation.

## 5. Comparison with existing K50/K51, Marduk, continuation-gate, bridge, carrier-rebinding work

- **K50/K51 (GGA):** C(50,2)=1225 and C(51,2)=1275 already computed in-Codex (RECOVERED). The
  "1225" in the proposed structure is therefore not a discovery — it is the Codex's own K50
  number, recontextualized. Any argument that treats 1225 as novel support must clear this.
- **Marduk 50/51:** The Codex's live numerical tension is 50-vs-51, not 49-vs-50. The proposed
  structure is adjacent (off by one at both ends: 49+1=50 vs 50+1=51). This adjacency is
  STRUCTURAL correspondence at best; at worst it is numerology sliding along the number line.
  Preserved as disagreement, not resolved.
- **Continuation-gate (SCGD):** Provides Γ, typed equality classes (kept separate by rule), and
  the hard separations that block promotion of the arithmetic. It is the instrument of
  falsification here, not the object of confirmation.
- **Bridge protocol:** Recovers the delegation content (see §4). B11 STRUCTURAL_CONTROL is the
  correct classification for the S_49⊕1_g ↔ Marduk-50⊕1 comparison: structural, no transmission
  claimed.
- **Carrier rebinding:** Recovered operators cover carrier-persistence and role-change; the
  delegation direction (carrier-change, information-tracked) is covered by B4/B7 + event fields.

## 6. Classification ledger

| Claim | Class |
|---|---|
| A1–A8 arithmetic | PROVEN |
| "Three forms of 1225" as independent evidence | FAILED |
| C(50,2)−C(49,2)=49 as distinctive support | FAILED (generic identity) |
| 49=24+1+24 as distinguished decomposition | FAILED (arbitrary) |
| 49-structure in the Codex | FAILED (absent; live negative) |
| field⊕distinguished-terminal as a Codex type | RECOVERED (at 50⊕1, Marduk registry) |
| S_49⊕1_g at 49/50 instantiation | GENERATED |
| 1_g as inter-field gate (relating completed fields) | GENERATED (machinery compatible, role underived) |
| 7/8 typed-ontology distinctions | RECOVERED |
| Delegation notation (c_n,I)→(c_{n+1},I′) | GENERATED; content RECOVERED |
| Delegation composition calculus | GENERATED, undefined (open work) |
| S_49⊕1_g ↔ Marduk 50⊕1 comparison | STRUCTURAL (B11-class; no transmission claim) |
| Any HISTORICAL grounding for 49/50/1225 as such | none found — no HISTORICAL class assigned |

## 7. Disagreements preserved (not harmonized)

1. The Codex says, in effect: numbers don't promote themselves (GGA governing rule; SCGD §10).
   The proposed structure's persuasive force currently comes *entirely* from arithmetic. This is a
   direct conflict with Codex promotion discipline, and I do not resolve it in favor of the
   hypothesis. The hypothesis must earn promotion through a typed, falsifiable test or remain
   GENERATED.
2. Off-by-one adjacency: Codex 50⊕1 vs proposed 49⊕1. I do not slide the hypothesis to 50⊕1 to
   borrow the Marduk registry's grounding, and I do not dismiss the adjacency as coincidence.
   Both readings are recorded; the typed edge-signature experiment (§8) is the adjudicator.
3. GGA's homogeneous node-addition vs the registry's typed terminal_control: these two Codex
   treatments of "one more element" are in tension with each other. The typed S_49⊕1_g proposal
   sides with the registry practice against the GGA formalism. Flagged for the steward.

## 8. Recommended next experiment

**Typed edge-signature test on the Marduk closure boundary (uses only existing Codex machinery):**

1. Populate (or locate, if GA-05 has) the sparse historical subgraph H_M with typed edges from the
   ingested name records.
2. Partition H_M edges into field-internal (among names 1–50) vs closure-incident (involving name
   51 / the Fifty rubric).
3. Test: do closure-incident edges carry a different typed signature (e.g. TRANSFER_FUNCTION,
   PROMOTE_STATUS, closure/instruction roles) than field-internal edges (NAME_AS, EPITHET_OF,
   IDENTIFY_ASPECT)?
4. Falsifier: if the 51st node's incident edges are type-indistinguishable from field edges, the
   typed-gate reading fails for the Codex's own best case — and S_49⊕1_g loses its structural
   precedent. If they differ systematically, the field⊕gate type is promoted to TESTED and a
   formal typed-adjunction operator for GGA becomes warranted GENERATED work.

This test decides something regardless of outcome, uses no arithmetic coincidence, and respects
the "do not normalize the discrepancy away" rule by making the discrepancy the object of study.

## 9. The four ones — 1_c / 1_g / 1_b / 1_r (added per relay context.md)

`context.md` refines the typings: internal fixed center (1_c), external gate/adjoined element
(1_g), carrier rebinding/delegation event (1_b), recursive return increment (1_r), with the
instruction not to assume equivalence. Each tested separately.

### 9.1 — 1_c (internal fixed center)
The "1" in 49 = 24+1+24, read as a distinguished center.
**Falsification:** Repo-wide grep for center/hub/anchor concepts in the three architecture docs
returned **nothing**. The only "anchor" hits are Marduk-registry philological anchors
(`transliteration_anchor`) and one registry note: birth name MDK-N01 "retained as identity
anchor" — a distinguished element with an anchoring role, but positional (first), not central,
and registry practice, not typed algebra. The Sefer Yetzirah wheel imagery geometrically implies
a hub, but the Codex formalism never takes it up — a clean negative: the intuition was available
and not formalized.
*Classification: GENERATED/OMEGA. No Codex anchor for a typed fixed center. The Marduk
identity-anchor is at most a STRUCTURAL hint (distinguished element, wrong position, wrong
formal status).*
Consequence: F3's failure sharpens — without 1_c, the palindromic decomposition 24+1+24 has no
typed reading at all; it is arithmetic only.

### 9.2 — 1_g (external gate/adjoined element)
As §2/F5: the *type* field⊕distinguished-terminal is RECOVERED via Marduk 50⊕1 registry practice
(51st name typed `terminal_control`, closure rubric separately typed, discrepancy preserved by
rule). GGA's formalism treats adjunction homogeneously ("exactly 50 additional unordered edges").
The 49/50 instantiation and the inter-field-relater role are GENERATED.
*Classification: type RECOVERED (at 50⊕1); instantiation GENERATED; relater-role GENERATED.*

### 9.3 — 1_b (carrier rebinding/delegation event)
The "1" read not as an element but as **one event** — a countable rebinding/delegation unit.
**Support found:** OrganonEvent is first-class (event_id, immutable, typed
preserved[]/altered[]/lost[]/introduced[] fields); rebinding operators NAME-02/NAME-03/TRN-02 are
typed; the event log counts events (append-only).
**Falsification of singularity:** Nothing in the Codex constrains rebinding events to be unique
per transition — events are plural by design (corrections *append* challenge/test/supersede
events). The "1" in 1_b (one event per delegation) is therefore unsupported as a *distinguished
singleton*; what the Codex supports is events-as-countable-units, of which there may be many.
*Classification: event-as-unit RECOVERED; singleton-1_b GENERATED (and in mild tension with the
append-only event model).*

### 9.4 — 1_r (recursive return increment)
The "+1" read as the increment contributed by each recursive return.
**Falsification:** `return_path` is a *field*, not a counter (bridge protocol, OrganonEvent).
"RETURN TO WITNESS" is a workflow step, not an increment. Γ's R is a state, not a count. The
totient dynamics in SCGD run *down* to 1 (…→8→4→2→1) — return-to-unity, the opposite direction
of an incrementing 1_r. The only increment-like structure found: the append-only event log grows
by ≥1 per correction event — but that is generic to any append-only log (same non-discrimination
problem as F2).
*Classification: GENERATED/OMEGA. No Codex anchor for return-as-increment.*
**Definition challenge (falsifiable):** 1_r survives only if given an operational definition such
that a Codex search could falsify it (e.g., "each completed Organon cycle appends exactly one
return_path event" — testable against the event log; my prediction: it fails, returns append
variable numbers of events). Without such a definition, 1_r is ornamental.

### 9.5 — Four-ones summary
| Typing | Codex verdict |
|---|---|
| 1_c fixed center | GENERATED/OMEGA — no anchor; Marduk identity-anchor at best a hint |
| 1_g gate element | type RECOVERED (50⊕1); 49/50 instantiation GENERATED |
| 1_b delegation event | event-as-unit RECOVERED; singleton claim GENERATED, mild tension |
| 1_r return increment | GENERATED/OMEGA — no anchor; definition challenge issued |

The four roles are **not equivalent** (per instruction): 1_g has the strongest Codex standing,
1_b partial, 1_c and 1_r none. Collapsing them into "the one" would violate the relay's own
non-equivalence instruction and the Codex's typed-separation discipline.

## 10. Law-against-law triangulation (explicit)

Three independent lenses, intersected:

**Lens 1 — GGA (elements vs gates, involution, quotient).** Yields: 1225 is GGA's own K50 number
(RECOVERED, not novel); adjunction homogeneous in formalism; quotient D(B)/⟨σ⟩ and involution σ
recovered as distinct types; no 49-anchor; no 1_c/1_r.

**Lens 2 — Bridge B7 (carrier changes, operation survives; preserved/altered/lost/introduced).**
Yields: delegation content recovered; rebinding events first-class but plural (1_b singleton
unsupported); return_path as field not counter (against 1_r).

**Lens 3 — SCGD (route/accumulation/lift/basin/attractor/return; same return ≠ same path).**
Yields: the falsification instruments themselves (hard separations §10); Γ compatible with a
1_g-relater role but does not derive it; totient return-to-1 runs counter to 1_r.

**Intersection:** All three lenses agree on (a) the field⊕distinguished-terminal *type* exists in
Codex practice (Lens 1 counts it, the Marduk registry types it, Lens 3's separations govern it);
(b) the arithmetic is non-evidential (each lens enforces or assumes this independently); (c) the
49/50 instantiation and the 1_c/1_r typings have no anchor in any lens. No lens rescues what
another lens rejects. The verdict is over-determined, which is the point of the exercise.

## 11. Direct answers to inbox.md

- **Strongest surviving invariant.** Two, both triangulated: (i) *Methodological* — the
  one-identity rule (25·49 = 49·50/2 = C(50,2) is a single algebraic identity) was derived
  independently by both lanes before contact; it is now a shared, tested invariant of the relay.
  (ii) *Substantive* — the field⊕distinguished-terminal type, RECOVERED via the Marduk 50⊕1
  registry practice (terminal_control, preserved discrepancy).
- **Strongest objection / negative result.** The arithmetic is non-discriminating (§2/F1–F3):
  one fact in four notations, one generic identity, one arbitrary decomposition. Compounded by
  the absence of any 49-anchor in the Codex (§2/F4) and the absence of 1_c/1_r anchors (§9.1,
  §9.4).
- **External gate typing (1_g): supported, rejected, or OMEGA?** *Supported as a type; OMEGA as
  an instantiation.* The Codex precedent (Marduk 51st as terminal_control) supports the formal
  possibility of a typed gate element distinct from a homogeneous nth state. Whether S_49⊕1_g —
  at 49/50, with 1_g relating completed carrier fields — holds, remains OMEGA pending the
  edge-signature experiment (§8). Not rejected: the structural precedent is real.
- **Next falsification experiment.** (i) Typed edge-signature test on the Marduk closure boundary
  (§8) — decisive either way, no arithmetic involved. (ii) 1_r definition challenge (§9.4):
  operationalize "return increment" against the event log; predicted failure, which would retire
  1_r to GENERATED-ornamental.

---

*Report extended 2026-09-29 ~11:25 CDT to answer relay inbox.md within the steward's structure.
§§1–8 unchanged from the independent pre-relay draft. No canonical state modified.*
