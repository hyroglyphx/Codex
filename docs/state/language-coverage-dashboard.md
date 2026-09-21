# Language Coverage Dashboard

Status: **Living registry**  
Source of truth: `registries/language-coverage-registry.yaml`

## Coverage meaning

This dashboard measures how deeply each language/tradition is integrated into **our research system**.

- **D0 — absent:** not yet incorporated.
- **D1 — registered:** named, scoped, and assigned a possible role.
- **D2 — structured:** relation type / operator / control role is defined; some examples exist.
- **D3 — active study:** dedicated analysis, explicit transformations, controls, or historical nexus anchors exist.
- **D4 — dense/cross-linked:** multiple studies intersect; the language participates in several independent operators, controls, or benchmarks.
- **D5 — instrumented end-to-end:** a complete witness can move through shared record → inference → product surface → return path.

Do not infer scholarly certainty from this score.

## Current inventory

The Comparative Atlas currently defines a **40-row operator matrix**. Some rows deliberately group closely connected traditions (for example Egyptian/Coptic, Aramaic/Syriac, Phoenician/Punic), so the matrix represents **more than forty individual language varieties**.

Beyond that core matrix, the living registry now includes adjacent languages and subcorpora that are incorporated but not yet equally populated.

### Density by major path

| Path | Density | Current character |
|---|---:|---|
| Mesopotamia → Syria → Levant | **D4** | Densest historical-language lane; carrier/readout, Semitic calibration, operator panels, bilingual/contact controls |
| Hurrian/Urartian + Hattic/Hittite | **D3** | Strong adversarial/control architecture; fewer filled witness sets |
| Anatolian branch + script-mode | **D3** | Hittite/Luwian strong; Lycian useful; Lydian/Carian/Phrygian/Palaic/Sidetic thinner |
| Aegean/Cyprus | **D3** | Mycenaean→alphabetic Greek logic strong; Arcadocypriot structured; Eteocypriot bounded |
| Greek/IE case + root depth | **D4** | Case syncretism and root/stem comparison now cross-link Greek, Anatolian, Sanskrit, Old Iranian, Latin, Armenian, Albanian |
| Iranian/Achaemenid | **D3** | Behistun/Susa multilingual control + Indo-Iranian lane |
| Western Mediterranean | **D3** | Pyrgi, Etruscan/Lemnian and numeral work are active; Iberian/Basque/Celtic lighter |
| Nile/Northeast Africa | **D3** | Egyptian/Coptic dense; Demotic active; Berber and Meroitic controlled adjacent lanes |
| Arabia | **D2** | Arabic/MSA structured; Old Arabic/ONA/ASA newly incorporated and under-populated |
| Distant controls | **D2** | Kartvelian, Uralic, Tamil, Baltic and Balkan nodes mainly serve adversarial calibration |

## Highest-density languages/traditions now

### D5
- **Akkadian** — only current language with a demonstrated complete reader/product fixture in GlyphWalk in addition to deep comparative use.

### D4
- **Sumerian**
- **Ugaritic**
- **Hebrew**
- **Aramaic/Syriac**
- **Egyptian/Coptic**
- **Hittite**
- **Classical Greek**
- **Sanskrit**
- **Phoenician/Punic**

These form the present high-density backbone.

## Strong D3 active-study band

- Eblaite
- Arabic
- Sumerian Emesal
- Hurrian
- Elamite
- Luwian
- Lycian
- Mycenaean Greek
- Latin
- Avestan/Old Iranian
- Old Persian
- Armenian
- Albanian
- Etruscan
- Berber
- Turoyo
- Demotic Egyptian

## Structured / control band (D2)

- Soqotri / Modern South Arabian
- Ge'ez / Tigrinya
- Urartian
- Hattic
- Lydian
- Carian
- Phrygian
- Lithuanian
- Lemnian
- Iberian
- Basque
- Proto-Kartvelian / Georgian
- Proto-Uralic / Finnic
- Tamil
- Meroitic
- Amorite
- Canaanite
- Maltese
- Arcadocypriot
- Eteocypriot
- Mitanni Indo-Aryan embedded register

## Registered / newly incorporated band (D1)

- Old Arabic
- Sabaic / Ancient South Arabian
- Safaitic
- Hismaic
- Dadanitic
- Taymanitic
- Palaic
- Sidetic
- Libyco-Berber
- Celtic
- Thracian
- Dacian
- Paeonian

## Cross-cutting study density

| Study | Density | Main language lanes |
|---|---:|---|
| Numeral-seven carrier | **D4** | Egyptian/Coptic, Etruscan, Hurrian, Sumerian, Armenian, Berber, Uralic/Kartvelian controls |
| Case-Operator Ecology | **D4** | Mycenaean/Classical Greek, Hittite/Luwian, Latin, Sanskrit, Old Iranian |
| Script-state transposition | **D4** | Sumerian/Akkadian, Hittite, Luwian, Mycenaean/Greek, Egyptian/Coptic, Phoenician |
| Rosetta redundancy | **D3** | Tell Fekheriye, Letoon, Behistun/Susa, Karatepe/Cinekoy, Pyrgi |
| Numeric transposition/sign value | **D3** | Greek, Hebrew, Aramaic, Arabic, Phoenician, Mesopotamian name-number practice |
| Boundary-language discipline | **D2** | Eteocypriot, Meroitic, Iberian, Linear Elamite/Elamite work |

## Promotion rule

Coverage is increased only after adding one or more of:

1. exact witnesses,
2. native decompositions,
3. typed transformations,
4. historical nexus anchors,
5. negative/adversarial controls,
6. held-out or blind tests,
7. shared HistoricalRecord entries,
8. GlyphWalk/Atlas renderings,
9. return-path validation.

Merely mentioning a language does **not** raise its density.

## Immediate coverage gaps

The clearest weak seams are:

- **Old North Arabian / Ancient South Arabian:** incorporated but not yet witness-populated.
- **Palaic / Sidetic / Lydian / Carian / Phrygian:** present as Anatolian controls, but uneven in operator-level treatment.
- **Meroitic / Eteocypriot / Iberian:** useful boundary nodes; need exact-sign/witness datasets rather than broader semantic speculation.
- **Urartian:** structurally positioned but still much thinner than Hurrian.
- **Kartvelian / Uralic / Tamil:** important external controls, but mostly invoked at the family/control level.
- **Balkan minor languages:** registered but not yet meaningfully instrumented.

## Update discipline

Every meaningful language-study advance should update this registry in the same change set:

```text
new witness / new transformation / new control / new benchmark
                 ↓
       update HistoricalRecord(s)
                 ↓
   update language coverage level if earned
                 ↓
       update path-density summary
```

This keeps the map synchronized with actual research rather than accumulated mentions.
