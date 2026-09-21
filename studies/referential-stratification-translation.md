# Referential Stratification in Ancient Translation

Status: ACTIVE CROSS-CORPUS METHOD
Updated: 2026-09-21

## Core observation

Ancient texts regularly alternate among a named person, that person's office/household, their immediate contingent, the broader people, and the polity/land.

A translation can therefore change the surface noun while preserving the historical address.

## Referential strata

R0 — NAMED_INDIVIDUAL
- Tigranes
- Cyrus
- Agamemnon
- Jacob/Israel as person

R1 — REPRESENTATIVE_OFFICE
- prince, king, commander, patriarch, house-head
- the named person acting as authorized representative

R2 — HOUSE_RETINUE_CONTINGENT
- "Tigranes and his men"
- king + companions/bodyguard
- named leader + military following

R3 — ETHNIC_TRIBAL_COLLECTIVE
- Armenians
- Medes
- Hyrcanians
- Persians
- Achaeans / Trojans
- Israel as people

R4 — POLITY_TERRITORY
- Armenia
- Media
- Hyrcania
- Persia
- Israel/Judah/Edom as territorial-political address

R5 — DYNASTIC_INSTITUTIONAL_BODY
- house of X
- royal house
- imperial administration
- covenant community
- army/state acting under ruler

The same lexeme may occupy more than one R-level depending on syntax and context.

## Xenophon micro-anchor

Cyropaedia Book IV gives a compact control:

```text
Medes + Hyrcanians + Tigranes
        ↓
Tigranes + his men
        ↓
Medes + Armenians
```

This is not three different Armenian entities. It demonstrates a discourse shift:

```text
R0/R1 named representative
→ R2 contingent
→ R3 people
```

Translation consequence:
A target version rendering "Tigranes" with an Armenian collective, or an Armenian collective with a leader/house expression, should not automatically be scored as semantic error. First test whether the referential address is preserved.

## Transform operators

RS1 — LEADER_TO_CONTINGENT
R0/R1 → R2

RS2 — LEADER_TO_PEOPLE
R0/R1 → R3

RS3 — PEOPLE_TO_LAND
R3 → R4

RS4 — LAND_TO_PEOPLE
R4 → R3

RS5 — HOUSE_TO_DYNASTY
R2/R5 → R5

RS6 — RULER_TO_POLITY
R0/R1 → R4/R5

RS7 — EPONYM_TO_DESCENDANTS
R0 → R3

RS8 — DESCENDANTS_TO_POLITY
R3 → R4

RS9 — CONTINGENT_TO_ETHNOS_GENERALIZATION
R2 → R3

RS10 — ETHNOS_TO_REPRESENTATIVE_COMPRESSION
R3 → R0/R1

## Translation record

For every aligned expression store:

```text
Q = (
  surface_form,
  language,
  grammatical_number,
  referential_stratum,
  human_group_scope,
  political_scope,
  territorial_scope,
  agency,
  representative_link,
  confidence
)
```

Then compare source and target by referential address before lexical surface.

## Biblical calibration

The Hebrew Bible provides particularly strong stratification controls.

### Jacob → Israel
A named individual receives the name Israel; the same name later denotes his descendants and eventually a collective political/territorial body.

```text
Jacob/Israel person R0
→ children/house of Israel R2/R3
→ Israel people R3
→ Israel polity/land R4
```

### Esau → Edom
Genesis explicitly links Esau and Edom, while later "Edom" denotes descendants and territory.

```text
Esau R0
→ Edom eponymic identity
→ Edomites R3
→ Edom R4
```

### Judah
Track separately:
- Judah son of Jacob R0
- tribe of Judah R3
- land/kingdom of Judah R4
- house/dynasty R5

These are ideal controls for Septuagint/Targum/Peshitta/Vulgate alignment because the same underlying referential lift is visible before translation.

## Homeric calibration

Greek epic constantly alternates between leaders and collectives.

Examples to test:
- Agamemnon / son of Atreus / sons of Atreus
- Argives / Achaeans / Danaans
- Achilles / Myrmidons
- Priam / Trojans
- Hector / Trojan contingent

Do not flatten ethnonym variation into simple synonymy. Track:
- leader,
- army,
- coalition,
- people,
- place.

## Mesopotamian calibration

Gilgamesh provides an important negative and positive control.

Do not assume:
```text
Gilgamesh = Uruk
```

Instead test passages where:
- king acts for city,
- city population responds,
- city name stands for civic body,
- ruler's household/retinue performs collective action.

This prevents overextension of the Xenophon pattern.

For flood traditions, keep:
```text
name identity
role identity
household/family group
surviving-humanity function
```
separate.

## Achaemenid / Xenophon application

For each:
- Cyrus ↔ Persians
- Cyaxares ↔ Medes
- Tigranes ↔ Armenians
- Gobryas ↔ household/territory/Assyrian affiliation
- Gadatas ↔ contingent/territory
- Hyrcanian envoys/officers ↔ Hyrcanians

identify whether a passage changes R-level without changing political address.

This is especially important when comparing Xenophon with:
- Old Persian inscriptions,
- Babylonian records,
- Elamite records,
- Imperial Aramaic,
- Hebrew/Aramaic biblical texts.

A documentary source may name a country where Xenophon names its ruler; that can be a valid R4 ↔ R0/R1 transform rather than contradiction.

## Translation scoring

Do not score:
```text
person != people
```
as automatic mismatch.

Score independently:

- lexical match
- referential-stratum match
- representative-link match
- agency match
- political-scope match
- geography match

Possible result:
```text
lexical mismatch
+ stratum shift
+ same representative address
= admissible metonymic translation
```

## STRAT-01 benchmark

Align high-value cases across:
1. Xenophon Greek
2. Old Persian / Babylonian / Elamite controls
3. Hebrew MT
4. Septuagint Greek
5. Aramaic Targum
6. Syriac Peshitta
7. Latin Vulgate
8. Homeric Greek
9. Hittite/Hurrian translated corpora where applicable

Initial cases:
- Tigranes / Armenians
- Cyaxares / Medes
- Cyrus / Persians
- Jacob / Israel
- Esau / Edom
- Judah / tribe / kingdom
- Agamemnon / Atreidae / Achaeans
- Achilles / Myrmidons
- ruler / city in Gilgamesh
- flood hero / household / surviving humanity

For every translation difference, ask whether the target changed:
```text
R-level
without changing
referential address.
```

That distinction should be resolved before declaring semantic expansion, omission, contradiction, or mistranslation.
