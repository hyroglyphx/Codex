# Xenophon, Cyropaedia — Linguistic Transport Study

Status: **ACTIVE SOURCE STUDY**  
Updated: **2026-09-21**

## Research role

Treat the *Cyropaedia* as a **Greek historiographic/readout layer** over Iranian, Median, Armenian, Anatolian, and Babylonian material.

It is not a documentary 6th-century Persian source. Its value lies in:
- Greek transcriptions of Iranian names,
- Greek exonyms for peoples and regions,
- translations or approximations of Persian offices,
- court and military terminology,
- ethnographic recoding,
- preservation of oral/traditional material,
- comparison against Old Persian, Babylonian, Elamite, Aramaic, Hebrew, Armenian, and later Iranian witnesses.

## New bridge classes

### B15 — EXONYM_ONOMASTIC_TRANSPOSITION
A foreign personal name, ethnonym, title, or place-name is rendered into Greek phonology/orthography.

### B16 — HISTORIOGRAPHIC_RETROJECTION
A later observer describes an earlier period using later institutions, categories, oral traditions, or ideological framing.

These two classes must remain separate.

## High-value name orbits

### Cyrus
```text
Old Persian Kuruš
→ Greek Kûros / Latin Cyrus
→ Elamite Ku-raš
→ Babylonian Ku(r)-raš
→ Aramaic kwrš
→ Hebrew Kōreš
→ Egyptian kwrš
→ later Armenian Kiwros via Greek
```

### Cambyses
```text
Old Persian Kambūjiya
↔ Elamite Kanbuziya
↔ Akkadian Kambuziya
↔ Aramaic Knbwzy
↔ Greek Kambysēs
```

### Astyages
```text
Old Iranian *Ṛšti-vaiga-
↔ Babylonian Ištumegu
↔ Greek Astyagēs / Astuigas
```

The Greek form is partly remodeled by Greek phonological/folk-etymological pressure.

### Cyaxares
```text
Old Iranian *Huvaxštra
↔ Akkadian Uakšatar / Umakištar etc.
↔ Elamite variants
↔ Greek Kyaxarēs
```

Xenophon's post-Astyages "Cyaxares" is not independently established as a historical Median king; keep name equivalence separate from person-identification.

### Tanaoxares / Bardiya orbit
```text
Old Persian Bardiya
↔ Greek Smerdis (Herodotus)
↔ Tanaoxares (Xenophon)
↔ Tanyoxarkes (Ctesias)
```

This is a prime identity-resolution test.

### Gobryas
```text
Old Persian Gaub(a)ruva
↔ Akkadian Gubaru / Ugbaru
↔ Aramaic gwbrw
↔ Greek Gobryas
```

Xenophon's "Assyrian" Gobryas may preserve an echo of a historically attested Gubaru/Gobryas associated with the capture/governance of Babylon, but narrative details must be separated from the name orbit.

### Hystaspes
```text
Old Persian Vištāspa
↔ Elamite Mi-is-da-áš-ba
↔ Akkadian Uš-ta-as-pa
↔ Greek Hystaspēs
↔ Armenian Vštasp
↔ Middle/New Persian Wištāsp/Goštāsp forms
```

### Tigranes
Xenophon uses **Tigranes** for an Armenian crown prince (Cyrop. 3.1.7). This is useful for the early Greek representation of an Iranian-rooted Armenian dynastic name and for the Armenia–Iran onomastic lane.

## Greek mythic recoding

Cyrop. 1.2.1 derives the Persian **Persidae** from Greek **Perseus**.

This is not historical etymology. It is a valuable example of:
- Greek interpretatio,
- mythic naturalization,
- cultural parentage,
- exonymic/etiological back-projection.

## Administrative translation

### Satrap
Greek **satrapēs / satrapeia** should be compared with Iranian **xšaça-pā-van-** "protector of empire/sovereignty."

Important distinction:
- the Iranian title is securely attested,
- the Greek abstraction "satrapy" does not map perfectly onto one Old Persian territorial noun,
- Old Persian **dahyu-** is used for lands/countries/provinces.

Cyrop. 8.6.7 supplies Xenophon's satrapal assignment list, but that list differs substantially from Old Persian country lists.

### Chiliarch / decimal command
Cyrop. 2.1.23 gives commanders of 10, 5, 50, 100, 1000, etc.
Greek **chiliarchos** can be compared with Old Persian **hazārapati-** and later Armenian **hazarapet** / Middle Persian **hazārbed** traditions.

### Greek generic titles
Greek **basileus** can flatten several Iranian titulary distinctions. Record the exact Greek word and compare it with attested Iranian royal titulature rather than assuming one-to-one equivalence.

### Court vocabulary
Track:
- satraps,
- chiliarch-like ranks,
- sceptre/mace-bearers,
- eunuchs,
- royal companions/peers,
- bodyguards,
- heralds,
- cavalry and decimal units.

Each item should be tagged:
`translation | Greek functional approximation | Iranian loan | literary invention | unresolved`.

## Ethnonym and geography map

The *Cyropaedia* names:
- Persians,
- Medes,
- Hyrcanians,
- Armenians,
- Chaldaeans,
- Cadusians,
- Sacians/Saka,
- Assyrians,
- Babylonians,
- Bactrians,
- Lydians,
- Carians,
- Cappadocians,
- Phrygians,
- Phoenicians,
- Cilicians,
- Paphlagonians,
- Arabs,
- Indians,
- Asiatic Greeks,
- Cyprus,
- Egypt.

These are useful for an **exonym/political-geography layer**.

Special caution:
Xenophon's "Assyrian" enemy-state language and his simultaneous use of Babylonia/Babylon should be analyzed as Greek political labeling, not automatically equated with Neo-Assyrian ethnic or linguistic identity.

## "Even to this day" markers

Xenophon repeatedly uses formulations equivalent to "even now/even to this day."

These should be tagged as:
```text
4th-century observation
projected onto 6th-century narrative
```

Examples include:
- Persian/Median dress,
- kissing custom,
- court and military institutions,
- satrapal practice,
- procession and royal protocol.

This is useful for distinguishing **observed late-Achaemenid practice** from **narrative retrojection**.

## Priority passages

- **1.2.1** — Cyrus, Cambyses, Mandane, Astyages; Persidae/Perseus mythic etiology.
- **1.5.2-5** — Cyaxares as successor to Astyages.
- **2.1.23** — decimal military organization.
- **3.1.7ff.** — Armenia; Tigranes.
- **4.6.1ff.** — Gobryas.
- **6.1.1ff.** — Cadusians, Hyrcanians, Sacians, Gobryas, Hystaspes, Gadatas.
- **7.2** — Chaldaeans, Sardis, Croesus.
- **8.3** — royal procession/court display.
- **8.6.7ff.** — satrap appointments and imperial administration.
- **8.7.11** — Tanaoxares and succession.

## Cross-source triangulation matrix

For every Cyropaedia name/title/place:

```text
Greek Xenophon
↔ Herodotus/Ctesias
↔ Old Persian inscription
↔ Babylonian chronicle/document
↔ Elamite form
↔ Aramaic form
↔ Hebrew/biblical form
↔ Armenian/later Iranian reflex
```

Assign:
- identity confidence,
- phonological transformation,
- script transformation,
- chronological gap,
- whether the same person/entity is certain,
- whether only the name-form correspondence is secure.

## New benchmark — CYR-XEN-01

Build 50 high-value Cyropaedia entities.

For each:
1. Greek form,
2. Greek morphology,
3. entity type,
4. Xenophon passage,
5. alternative ancient forms,
6. likely source language,
7. transformation path,
8. documentary controls,
9. historical-person confidence,
10. linguistic-form confidence,
11. exonym/endonym status,
12. later reflexes,
13. notes on Greek semantic or mythic recoding.

The goal is not to "correct Xenophon" but to turn the *Cyropaedia* into a measured Greek transposition layer.


## Leader-to-contingent compression: Tigranes → Armenians

Tigranes does not vanish immediately after the Armenian episode. He remains individually visible:
- Book V: he speaks in Cyrus' coalition council.
- Book VII: he is named among Cyrus' honored companions.
- Book VIII: he wins the Armenian horse race.

However, once his personal reconciliation/mediation role has been established, Xenophon often refers simply to **the Armenians** as a military or political contingent.

Model this as:
```text
Tigranes (named representative / prince)
        ↓
Tigranes + Armenian contingent
        ↓
Armenians (collective political-military address)
```

This is a form of **leader-to-contingent metonymic compression**, not evidence by itself that Tigranes has left the narrative or died.

Research consequence:
- do not use absence of the personal name to infer absence of the represented group;
- do not use later collective reference to prove that every Armenian action is personally directed by Tigranes;
- track person, contingent, ethnonym, and political role as separate but linkable state variables.
