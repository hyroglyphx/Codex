# Generative Gate Algebra v0.1

Status: active experimental architecture
Updated: 2026-09-22

## Purpose

Generalize the Sefer Yetzirah 231-Gates construction, the Marduk name/function graph, prior modular/totient coherence-gate work, TCIM, Nexus, and Invariant Forge into one falsifiable relational framework.

## Historical anchor vs research extension

### Attested anchor
Sefer Yetzirah places 22 foundation letters in a wheel with 231 gates and describes forward/backward motion. The standard 231 count is the unordered-pair space C(22,2); oriented traversal yields 462 directed moves.

The 22-letter system also carries the traditional 3 Mothers / 7 Doubles / 12 Simples partition.

### Research extension
The graph-theoretic, modular, totient, Faulhaber-Fibonacci, Marduk, and cross-corpus constructions below are Codex research models. They are not attributed to the ancient texts unless independently attested.

## Core object

Let B be a finite typed basis and O a set of admissible operators.

Potential unordered gate space:
G(B) = {{x,y}: x,y in B, x != y}

|G(B)| = C(|B|,2)

Directed traversal space:
D(B) = {(x,y): x,y in B, x != y}

|D(B)| = |B|(|B|-1)

Reversal involution:
sigma(x,y) = (y,x)
sigma^2 = identity

G(B) = D(B) / <sigma>

## Evidence-state decomposition

Every potential gate receives one or more states:

- POTENTIAL: combinatorially available only
- ATTESTED: explicit witness supports the relation
- DERIVED: follows from declared operators/rules
- PREDICTED: registered before checking an independent witness
- CORROBORATED: independent witness satisfies a prediction
- CONTRADICTED: independent evidence conflicts
- REJECTED: fails declared test
- OMEGA: unresolved

No numerical coincidence is promoted merely because it exists in G(B).

## SY-231 benchmark

Basis:
B_SY = 22 Hebrew foundation letters

Potential gates:
C(22,2) = 231

Directed traversals:
22*21 = 462

### 3/7/12 edge partition

Given classes M=3, D=7, S=12:

M-M = C(3,2) = 3
M-D = 3*7 = 21
M-S = 3*12 = 36
D-D = C(7,2) = 21
D-S = 7*12 = 84
S-S = C(12,2) = 66

Total = 231

This partition is a mathematical consequence of the class sizes. Any semantic interpretation of the six sectors requires separate evidence.

## Modular operator laboratory

For indexed state x in Z/22Z, test:
T_k(x) = kx mod 22

Record:
- gcd(k,22)
- orbit structure
- image size
- fixed points
- collisions
- reversal behavior

Do not assume these operators are historically encoded in Sefer Yetzirah. They are comparative mathematical probes.

## Coherence Gate filter

Prior experimental pipeline:

word/object w
-> numerical map N = G(w)
-> residue r = N mod m
-> Euler-totient chain N0=N, N1=phi(N0), ... -> 1
-> record crossings of declared downstream nodes
-> compare against independently generated residue family
-> flag intersections

The earlier working downstream set {18,6,2,1}, modulus 60 crest rule {0,27,54}, and Faulhaber-Fibonacci overlay are retained as EXPERIMENTAL PARAMETERS, not historical facts.

A coherence gate is therefore:
C = gate satisfying >=2 independently specified filters

Promotion requires pre-registration and null testing.

## Marduk Gate Space

Let B_M be the ingested Marduk name records.

Naive possibility spaces:
if |B_M|=50: C(50,2)=1225
if |B_M|=51: C(51,2)=1275

The additional 51st node contributes exactly 50 additional unordered edges.

Do not treat K50 or K51 as historically meaningful by default.

Define H_M as the sparse historical subgraph:
H_M subseteq G(B_M)

Edges enter H_M only through typed relations such as:
- NAME_AS
- EPITHET_OF
- IDENTIFY_ASPECT
- TRANSFER_FUNCTION
- INHERIT_TITLE
- SYNCRETIZE
- SUBSUME
- DISTINGUISH
- PROMOTE_STATUS
- LOCATE_CULT
- explicit sequence/parallel relations

## Functional-basis recovery

Do not pre-impose a symbolic alphabet on the Fifty Names.

After line-addressable ingestion, construct feature vectors from attested explanations/destinies:
N_i = (f_1, f_2, ..., f_k)

Then test whether a smaller basis F compresses the corpus.

Candidate methods:
- incidence matrix name x function
- hierarchical clustering
- nonnegative matrix factorization / Boolean factorization
- minimum-description-length comparison
- community detection on the bipartite name-function graph
- stability under witness removal

A recovered basis is promoted only if it is stable, compressive, and interpretable from source-grounded features.

## Identity closure

Given recovered functional basis F and historically admissible operator set O:

MardukIdentity = Closure(F,O | witnesses, phase, scope)

This is a research definition for testing whether the composite identity can be reconstructed from typed transformations. It is not an ancient formula.

## Cross-corpus comparison

Compare systems by invariants, not surface resemblance.

For each corpus record:
- basis size
- gate-space size
- directed/undirected behavior
- partition structure
- admissible operators
- attested-edge density
- orbit structure
- reversal/involution
- closure properties
- information loss
- role of number
- role of sequence
- role of names/functions
- provenance depth

Similarity is structural analogy unless a historical transmission edge is independently evidenced.

## Geometry laboratory

Candidate embeddings:
- circle
- sphere
- torus
- hyperbolic disk
- force-directed graph
- spectral embedding

Test:
1. freeze historical edge labels
2. embed using a declared rule
3. measure clustering/geodesic preservation
4. permute labels / degree-preserving randomize
5. repeat
6. compare observed metric to null distribution

A surface is explanatory only if it beats appropriate nulls and the result survives perturbation.

## Prediction ledger

Every strong candidate must be registered before the validating witness is inspected:

prediction_id
training_witnesses
declared_operator
predicted_relation
target_holdout
success_metric
timestamp/commit
result

This extends the Byblos train/validation/holdout discipline to Gate Algebra.

## Organon workflow

BOUND
-> DEFINE BASIS
-> ENUMERATE POTENTIAL GATES
-> TYPE OPERATORS
-> INGEST ATTESTED EDGES
-> DERIVE CANDIDATES
-> REGISTER PREDICTIONS
-> TEST HOLDOUTS
-> RUN NULL MODELS
-> EXTRACT INVARIANTS
-> PROMOTE / REJECT / OMEGA
-> RETURN TO WITNESS

## Immediate benchmarks

GA-01 SY-231 enumeration and 3/7/12 partition
GA-02 directed reversal/orbit model
GA-03 modular Z22 operator scan
GA-04 coherence-gate replication using frozen prior parameters
GA-05 MDK sparse historical graph
GA-06 MDK functional-basis recovery
GA-07 K50 vs K51 sensitivity
GA-08 cross-corpus invariant comparison
GA-09 geometry/null-model challenge
GA-10 prospective prediction ledger

## Governing rule

The elements define the vocabulary.
The potential gates define the possibility-space.
Witnesses activate historical gates.
Operators derive candidates.
Independent tests decide what survives.
