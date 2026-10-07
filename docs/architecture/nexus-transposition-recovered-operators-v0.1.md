# Nexus Transposition Recovered Operators v0.1

Status: ADOPTED_LEGACY_RECOVERY  
Date: 2026-09-23  
Recovered source: Nexus Transposition Engine corpus  
Scope: Linguistic Core / ASL / TCIM / Nexus / Structural Continuation / Elamite Carrier Pivot

## Purpose

Recover high-value operators from the Nexus Transposition Engine that were not explicit in the current Codex branch.

These operators refine the distinction:

```
carrier
!= reading
!= language
!= semantic address
```

## 1. Carrier orbit

A carrier orbit is the set of states reachable under a frozen transformation grammar:

```
O(K) = {
  K,
  tau_1(K),
  ...,
  tau_n(K)
}
```

Only declared transformations belong to the orbit.

Vowel alternation, assimilation, metathesis, exonymy, logographic readout, script change, and borrowing remain different operator classes.

## 2. Carrier–operator coupling

Experimental hypothesis:

```
K <-> O
```

A candidate relation is stronger when both directions survive independent testing:

```
P(O | K) > P(O)
and
P(K | O) > P(K)
```

This must use frozen corpora and dependency-aware nulls.

It is a discovery architecture, not an ancestry rule.

## 3. PHASESHIFT

Different languages can lexicalize different positions inside one process.

Example abstract process:

```
SOURCE
-> CROSSING
-> EMERGENCE
-> NEW_STATE
```

A ford, crossing, crosser, arrival, emergence, offspring, successor, hearing, understanding, accepting, and obeying may occupy different process positions.

PHASESHIFT records:

```
PROCESS_ID
PHASE_POSITION
LEXICAL_WITNESS
ROLE
```

It permits functional/process comparison without collapsing distinct glosses.

## 4. PARALLEL_READOUT

One carrier may support multiple language-specific readouts:

```
C --L1--> R1
C --L2--> R2
```

or several carriers may reach one semantic address.

Canonical consequences:

```
VISIBLE_CARRIER
!=
SPOKEN_LANGUAGE
```

and:

```
PHONETIC_DISCONTINUITY
does not imply
INFORMATION_DISCONTINUITY
```

Primary controls:
- Sumerograms in Akkadian;
- Sumerian/Akkadian heterograms in Hittite;
- bilingual lexical lists;
- multilingual royal monuments.

## 5. Semantic Back-Projection

A transmitted form may enter a new phonological neighborhood and acquire a later interpretation from the receiving language.

```
old carrier
-> sound/readout change
-> new neighborhood
-> semantic attraction
-> reinterpretation
```

Store the later interpretation as a real reception/history state, but do not back-project it into the earlier etymology without evidence.

## 6. Honorific transposition

Written order may differ from phonological or syntactic order when semantic rank controls placement.

Therefore position decomposes into:

```
phonological_position
graphical_position
syntactic_position
semantic_rank
```

No one position coordinate substitutes for the others.

## 7. Same language / different carrier

Use script change as a positive calibration family:

- Greek: Linear B -> alphabetic Greek;
- Egyptian: hieroglyphic/hieratic/demotic -> Coptic;
- Luwian: cuneiform <-> hieroglyphic;
- Aramaic: imperial script traditions -> later Syriac developments;
- Elamite: Linear Elamite -> cuneiform Elamite.

This binds directly to CARRIER_PIVOT.

## 8. Same carrier / different language

Use:
- Sumerogram in Akkadian;
- heterogram in Hittite;
- bilingual lexical lists;
- multilingual monuments.

This is the complementary calibration to section 7.

Together:

```
same_language_different_carrier
AND
same_carrier_different_language
```

provide a two-sided test that carrier and language are independent coordinates.

## 9. Empirical admissibility envelope

Transformation cost should be learned from controlled historical behavior.

```
C(X,Y)
=
min_path sum c(tau_i)
```

Low cost:
repeatedly demonstrated historical transformation.

Medium cost:
phonetically or structurally natural but less directly witnessed.

High cost:
stacked, rare, or corpus-specific transformations.

These costs may guide search but cannot override mandatory historical dimensions.

## 10. Blind discovery

Freeze the transform alphabet before evaluating culturally salient names.

Then:
1. generate admissible neighbors without meaning labels;
2. retrieve lexical occupants;
3. score operator distribution;
4. compare controls;
5. reveal target hypotheses last.

This reduces attractive-example selection.

## 11. Cross-application

### Elamite

Carrier-pivot tests should be paired with the complementary same-carrier/different-language controls, not studied alone.

### QBL / center-interface

Use PHASESHIFT when senses occupy different positions of an encounter process:

```
FRONT
-> ENCOUNTER
-> APPROACH
-> RECEIVE
```

Do not treat process adjacency as cognacy evidence by itself.

### Aramaic / textual relay

PARALLEL_READOUT and Semantic Back-Projection distinguish:
- inherited form;
- translated function;
- later interpretive attraction.

### Egyptian

Honorific transposition becomes a permanent position-control against assuming visible order is spoken order.

### Numeric and symbolic transports

A carrier orbit must be frozen before numeric projection. Numerical recurrence cannot enlarge the underlying linguistic orbit.

## Governing rule

> Compare transformations inside a declared orbit, distinguish process phase from lexical identity, and keep carrier, readout, language, semantic address, and position as independent coordinates.
