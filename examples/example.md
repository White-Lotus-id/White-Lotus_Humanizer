# Example Templates — White-Lotus-Humanizer v6.5.0

This file contains ready-to-use example templates covering all four voice
profiles (BASE, VOICE-A, VOICE-B, VOICE-C), the full intake protocol, the
pre-generation summary block, annotated chunk outputs, and the bridge sentence
gate. Copy any template verbatim to start a session.

---

## Table of Contents

1. [VOICE-A — Fresh Introduction Intake](#1-voicea--fresh-introduction-intake)
2. [VOICE-B — Humanize Existing AI Paragraph](#2-voiceb--humanize-existing-ai-paragraph)
3. [VOICE-A — RRL with Theme Map](#3-voicea--rrl-with-theme-map)
4. [VOICE-B — Convert BULLET EXPORT from /thesis-writer](#4-voiceb--convert-bullet-export-from-thesis-writer)
5. [VOICE-C — Pakistani ESL PhD Background of Study Intake](#5-voicec--pakistani-esl-phd-background-of-study-intake)
6. [VOICE-C — Discussion Per-Hypothesis Template Intake](#6-voicec--discussion-per-hypothesis-template-intake)
7. [VOICE-C — Literature Review Hypothesis-Development Block](#7-voicec--literature-review-hypothesis-development-block)
8. [Pre-Generation Summary Block Example](#8-pre-generation-summary-block-example)
9. [Annotated Generated Chunk — VOICE-A Introduction](#9-annotated-generated-chunk--voicea-introduction)
10. [Annotated Generated Chunk — VOICE-C Discussion](#10-annotated-generated-chunk--voicec-discussion)
11. [Bridge Sentence Gate — Acceptable and Refused](#11-bridge-sentence-gate--acceptable-and-refused)
12. [Voice Calibration From Student Sample](#12-voice-calibration-from-student-sample)
13. [Error Flag Examples](#13-error-flag-examples)

---

## 1. VOICE-A — Fresh Introduction Intake

```
[SECTION INTAKE]

1. Thesis Title/Topic: Development of a Brownout Guard System for Residential Power
   Monitoring in [the cooperative] Service Territory
2. Thesis Category: Development
3. Section/Part: Introduction
4. Voice Target: VOICE-A
5. References:
   - [Author, A. A., & Author, B. B. (Year)]. Power quality in Philippine distribution
     networks. [a national electrical engineering journal], 14(2), 45-58.
     https://doi.org/10.xxxx/xxxx
   - [the Cooperative]. (Year). Annual service reliability report. [the local electric cooperative].
   - [Author, A. A. (Year)]. Voltage monitoring systems for rural electrification.
     [a national professional engineering body journal], 8(1), 12-24.
   - [Author, A. A., & Author, B. B. (Year)]. Household appliance damage from
     undervoltage events in [the region]. [a national energy research journal], 5(3), 88-102.
   - [Author, A. A. (Year)]. Smart home power monitoring solutions. [a peer-reviewed engineering journal],
     11, 24531-24545. https://doi.org/10.1109/ACCESS.2023.xxxxx

[CONFIRMED: Generate Introduction]
```

---

## 2. VOICE-B — Humanize Existing AI Paragraph

```
Humanize this:

The proposed system integrates a voltage sensor with a microcontroller to
monitor power quality in real-time. The system utilizes the PZEM-004T module
which enables accurate measurement of voltage, current, and power factor.
Furthermore, the data is transmitted wirelessly to a mobile application,
thereby providing users with immediate notifications when voltage drops below
the acceptable threshold of 0.90 per unit. This demonstrates the system's
capability to address the significant issue of undervoltage events that affect
household appliances.

Voice Target: VOICE-B
Thesis Category: Development
Section: Research Design
```

---

## 3. VOICE-A — RRL with Theme Map

```
[SECTION INTAKE]

1. Thesis Title/Topic: Automated Rice Seed Viability Detection Using Infrared
   Thermography and Convolutional Neural Networks
2. Thesis Category: Development
3. Section/Part: RRL — Theme: Infrared Thermography in Agriculture
4. Voice Target: VOICE-A
5. References:
   - [Author, A. A., & Author, B. B. (Year)]. Infrared imaging for crop quality assessment.
     Biosystems Engineering, 218, 45-56.
   - [Author, A. A., Author, B. B., & Author, C. C. (Year)]. Thermal imaging for seed germination
     prediction. Journal of Agricultural Engineering, 58(3), 112-124.
   - [Author, A. A. (Year)]. Non-destructive methods for rice quality evaluation.
     Computers and Electronics in Agriculture, 205, 107-119.

6. Theme Map:
   Theme 1: Infrared Thermography — [Author & Author (Year)], [Author (Year)]
   Theme 2: Seed Viability Assessment Methods — [Author et al. (Year)]

[THESIS ANCHOR]
Title: Automated Rice Seed Viability Detection Using Infrared Thermography and CNN
Category: Development
General Objective: To develop a non-destructive rice seed viability detection
system using infrared thermography and convolutional neural networks
Scope: Covers detection of rice seed viability using thermal images and
CNN classification only, limited to Maligaya variety
Key methodology: Image acquisition using FLIR thermal camera, CNN classification
using EfficientNet-B0

[CONFIRMED: Generate RRL — Theme: Infrared Thermography]
```

---

## 4. VOICE-B — Convert BULLET EXPORT from /thesis-writer

```
Voice Target: VOICE-B
Section: Chapter 3 — Data Gathering Procedure
Thesis Category: Development

[BULLET EXPORT FROM THESIS-WRITER]
- Phase 1: Requirement Gathering
  - Interview stakeholders (household owners, [the cooperative] technicians)
  - Identify voltage thresholds and monitoring frequency requirements
  - Review existing brownout incident reports from [the cooperative]
- Phase 2: System Development
  - Hardware assembly: ESP32 + PZEM-004T + relay module
  - Firmware: FreeRTOS task scheduling for sensor polling
  - Mobile app: React Native with Firebase real-time database
- Phase 3: Testing and Evaluation
  - Unit testing of individual sensors
  - Integration testing of full system
  - User acceptance testing with 5 household owners in [the municipality]

[THESIS ANCHOR]
Title: Brownout Guard: A Residential Power Monitoring System for [the local utility] service territory
Category: Development
General Objective: To develop a residential power monitoring and protection system
Scope: Limited to monitoring voltage and current at the household level in [the cooperative]
service territory, [the municipality], [the province]
Key methodology: RAD methodology, ESP32-based hardware, FreeRTOS firmware,
React Native mobile app
```

---

## 5. VOICE-C — Pakistani ESL PhD Background of Study Intake

```
[SECTION INTAKE]

1. Thesis Title/Topic: [a PhD thesis on technology adoption in agriculture]
2. Thesis Category: Research
3. Section/Part: Background of the Study
4. Voice Target: VOICE-C
5. References:
   - [Author, A., Author, B., & Author, C. (Year)]. Global spread of
     conservation agriculture. International Journal of Environmental Studies,
     76(1), 29-51.
   - [Author, A. A., Author, B. B., Author, C. C., Author, D. D., Author, E. E., & Author, F. F. (Year)]. Crops that feed the world 10. Past successes and
     future challenges to the role played by wheat in global food security.
     Food Security, 5(3), 291-317.
   - [the Agency]. (2018). Climate-smart agriculture sourcebook. [an international food and agriculture agency].
6. Theoretical framework: UTAUT (Unified Theory of Acceptance and Use of Technology)
7. Methodological approach: PLS-SEM + ANN, cross-sectional survey of 384 rice
   farmers in [the region], [the country]
8. Construct abbreviations: FIN (Facilitating Condition), TOE (Trust on Extension),
   POT (Performance Expectancy), ENA (Effort Expectancy), RTA (Risk-Taking Attitude),
   PEX (Personal innovativeness), EEX (Environmental Concern), SIN (Social Influence)

[CONFIRMED: Generate Background of the Study]
```

---

## 6. VOICE-C — Discussion Per-Hypothesis Template Intake

```
[SECTION INTAKE]

1. Thesis Title/Topic: [a PhD thesis on technology adoption in agriculture]
2. Thesis Category: Research
3. Section/Part: Discussion — Hypothesis H2a, H2b, H2c (CAPs Characteristics → ITA)
4. Voice Target: VOICE-C
5. References:
   - [Author, A. A., Author, B. B., Author, C. C., & Author, D. D. (Year)]. The adoption of
     sustainable agricultural practices in Malaysia. Journal of Cleaner Production,
     68, 219-227.
   - [Author, A. A., Author, B. B., Author, C. C., & Author, D. D. (Year)]. Adoption of green
     fertilizer technology among paddy farmers. Environmental Science and Pollution
     Research, 24(11), 10521-10535.
   - [Author, A. A., Author, B. B., & Author, C. C. (Year)]. Determinants of farmers'
     intention to adopt energy saving innovations. Journal of Cleaner Production,
     153, 326-334.
   - [Author, J. (Year)]. Statistical power analysis for the behavioral sciences
     (2nd ed.). Lawrence Erlbaum.
6. Theoretical framework: UTAUT
7. Methodological approach: PLS-SEM, f² effect size, ANN
8. Construct abbreviations: PEX (Performance Expectancy), EEX (Effort Expectancy),
   SIN (Social Influence), ITA (Intention to Adopt CAPs)
9. Hypothesis results to discuss:
   - H2a: PEX → ITA, f²=0.000, insignificant
   - H2b: EEX → ITA, f²=0.019, small significant
   - H2c: SIN → ITA, f²=0.067, small significant

[THESIS ANCHOR]
Title: [a PhD thesis on technology adoption in agriculture]
Category: Research
General Objective: To explore CAPs adoption as a process based on farmer personal
factors and CAPs attributes for the formation of the intention to adopt CAPs in
Pakistani rice farmers
Scope: Cross-sectional survey of 384 rice farmers in [the region], [the country]; six
personal factors and three CAPs attribute constructs
Key methodology: PLS-SEM with SmartPLS 3.1, ANN validation, SPSS for descriptive

[CONFIRMED: Generate Discussion — Hypothesis H2a, H2b, H2c]
```

---

## 7. VOICE-C — Literature Review Hypothesis-Development Block

```
[SECTION INTAKE]

1. Thesis Title/Topic: [a PhD thesis on technology adoption in agriculture]
2. Thesis Category: Research
3. Section/Part: RRL — Theme: Performance Expectancy in Innovation Adoption
4. Voice Target: VOICE-C
5. References:
   - [Author, A. A., Author, B. B., Author, C. C., & Author, D. D. (Year)]. User
     acceptance of information technology: Toward a unified view. MIS Quarterly,
     27(3), 425-478.
   - [Author, A. A. (Year)]. Diffusion of innovations (5th ed.). Free Press.
   - [Author, A. A., Author, B. B., Author, C. C., & Author, D. D. (Year)]. Adoption of green
     fertilizer technology among paddy farmers. Environmental Science and Pollution
     Research, 24(11), 10521-10535.
   - [Author, A. A., Author, B. B., Author, C. C., & Author, D. D. (Year)]. The adoption of
     sustainable agricultural practices in Malaysia. Journal of Cleaner Production,
     68, 219-227.

6. Theme Map:
   Theme 1: Performance Expectancy in UTAUT — [Author et al. (Year)]
   Theme 2: Performance Expectancy in Agriculture Adoption — [Author et al. (Year)], [Author et al. (Year)]
   Theme 3: Innovation Adoption Theory Foundation — [Author (Year)]

7. Theoretical framework: UTAUT
8. Methodological approach: PLS-SEM
9. Construct abbreviations: PEX, EEX, SIN, ITA, UOC (Use of CAPs), SFP (Sustainable Farm Performance)

[THESIS ANCHOR]
Title: [a PhD thesis on technology adoption in agriculture]
Category: Research
General Objective: To explore CAPs adoption as a process based on farmer personal
factors and CAPs attributes for the formation of the intention to adopt CAPs in
Pakistani rice farmers
Scope: Cross-sectional survey of 384 rice farmers in [the region], [the country]
Key methodology: PLS-SEM with SmartPLS 3.1

[CONFIRMED: Generate RRL — Theme: Performance Expectancy in Innovation Adoption]
```

---

## 8. Pre-Generation Summary Block Example

```
[PRE-GENERATION SUMMARY]

Section: Introduction / Background of the Study
Category: Development
Voice Target: VOICE-A
RDE Agenda: Industry-Energy-Tech — SDGs 4, 5, 8, 9, 10, 11, 16, 17
Soul Level: Maximum (locked)

GENERATING: INTRODUCTION

REFERENCES (5):
1. [Author, A. A., & Author, B. B. (Year)]. Power quality in Philippine distribution
   networks. [a national electrical engineering journal], 14(2), 45-58.
   https://doi.org/10.xxxx/xxxx
   APA: OK
   Verification: [NEEDS SEARCH — will verify before generation]
   Claim Match: Pending verification

2. [the Cooperative]. (Year). Annual service reliability report. [the local electric cooperative].
   APA: [CITATION FORMAT CORRECTED — no URL/DOI added; organizational author
   format OK]
   Verification: [UNVERIFIABLE — internal report, no public abstract]
   Claim Match: OK — used as institutional data source only

3. [Author, A. A. (Year)]. Voltage monitoring systems for rural electrification.
   [a national professional engineering body journal], 8(1), 12-24.
   APA: OK
   Verification: [NEEDS SEARCH]
   Claim Match: Pending

4. [Author, A. A., & Author, B. B. (Year)]. Household appliance damage from
   undervoltage events in [the region]. [a national energy research journal], 5(3), 88-102.
   APA: OK
   Verification: [NEEDS SEARCH]
   Claim Match: Pending

5. [Author, A. A. (Year)]. Smart home power monitoring solutions. [a peer-reviewed engineering journal],
   11, 24531-24545. https://doi.org/10.1109/ACCESS.2023.xxxxx
   APA: OK
   Verification: [VERIFIED VIA SEARCH]
   Claim Match: OK

GLOSSARY (4 terms locked):
| Term | Definition |
|---|---|
| Brownout | A prolonged reduction in voltage supply below the acceptable threshold, as experienced in [the cooperative] service territory, causing appliance damage and service interruption |
| Undervoltage | Voltage level that drops below 0.90 per unit of nominal supply voltage, as defined by [the regulator] standards |
| [the cooperative] | [the local electric cooperative], the distribution utility serving [the municipality] and surrounding municipalities |
| PZEM-004T | A power monitoring module used in this study to measure voltage, current, and power factor in real time |

FLAGGED FOR REVIEW:
- References 1, 3, 4 pending web search verification. Proceeding with
  [UNVERIFIABLE] flag if abstracts are not found.
- [the cooperative] internal report: cite as gray literature. Will flag if claim match
  cannot be verified.

Reply: [CONFIRMED: Generate Introduction]
Or send corrections.
```

---

## 9. Annotated Generated Chunk — VOICE-A Introduction

```
[SECTION: Introduction — CHUNK 1 OF 3]

Electricity is something that most households in the Philippines consider a
basic part of daily life, which means its absence or sudden instability is
not just an inconvenience but a real economic problem ([Author & Author, Year]).
In [the province], this problem is well-known. Families who live inside the [the cooperative]
service territory have become so used to voltage fluctuations that they have
a word for it already: brownout. Because of that, the term does not just
mean a power interruption, it also means the steady hum of appliances
suddenly going quiet, the refrigerator warming up, and the water pump
failing to start in the morning ([Author & Author, Year]).

The researchers observe that the cause of these events is not one single
failure but a combination of aging infrastructure, rising household demand,
and the seasonal battering of [the region]'s typhoon corridor ([the Cooperative, Year]). At the
moment, the distribution network serving [the municipality] was not originally
designed to carry the load that modern households put on it, which means
that even without a storm, voltage levels can drop below the threshold that
appliances need in order to function safely ([Author, Year]). This is
because the cooperative has not been able to expand its infrastructure at
the same pace that residential connections have grown, and that gap is not
abstract — a family with a chest freezer full of a week's worth of fish
knows exactly what it costs when the voltage drops too long.

[CHUNK COMPLETE]

Before I write the next chunk, paste your own opening sentence for it.
Write it in your own words — do not type "continue" or "next."
I will use your sentence as the first sentence of the next chunk and build
from there.

Example of an acceptable bridge sentence:
"The development of automated sorting systems has also been explored in
related agricultural research."

Your bridge sentence:
```

### Annotation

The example above shows:

1. VOICE-A voice: "Because of that," "which means," "in order to," "The
   researchers observe that."
2. Embodied specificity: the refrigerator, water pump, chest freezer, and [the cooperative]
   as place name.
3. Problem genealogy in progress: everyday problem (para 1), infrastructure
   cause (para 2).
4. No em dashes anywhere.
5. No semicolons.
6. "the researchers" (lowercase plural) as primary self-reference.
7. Chunk ends with bridge sentence request, not "continue."
8. Tier 5 injection (vague pronoun + abstract claim) silent — no `(intentional)`
   marker on output.

---

## 10. Annotated Generated Chunk — VOICE-C Discussion

```
[SECTION: Discussion — CHUNK 1 OF 3 — Hypothesis H2a]

The study's next hypotheses bid to evaluate the impact of CAPs characteristics
on the intention to adopt the CAPs. Study the second hypothesis explores the
impact of the a) CAPs PEX, b) EEX, and c) CAPs SIN on the intention to adopt
CAPs.

The study result shows that the CAPs PEX (f²=0.000) insignificantly influence
the intention to adopt CAPs ([Author, Year]), and offer no support to accept the
H2a. The insignificant impact of CAPs PEX on the intention to adopt CAPs also
documented by [Author et al. (Year)], and [Author et al. (Year)]. The result of the
study highlights the lack of awareness among the farmers and reportedly low
perception of CAPs performance from the proposed use of CAPs.

However, it is essential to note that PEX for the CAPs needs improvement;
extension staff and farmer-to-farmer observation opportunities may aid to
improves the CAPs PEX and adoption of CAPs as well ([Author et al., Year]).
Moreover, the same is the case for the developing countries where the
farmer needs to educate on the use of the CAPs in order to enables the
better perception of the performance of CAPs.

[CHUNK COMPLETE]

Before I write the next chunk, paste your own opening sentence for it.
Write it in your own words — do not type "continue" or "next."

Your bridge sentence:
```

### Annotation

The example above shows the VOICE-C forensic markers in operation:

1. **5-move per-hypothesis template**: topic → result with stats → lit
   comparison → interpretation → recommendation. All five moves present.
2. **Of-chains**: "the impact of CAPs characteristics on the intention to
   adopt the CAPs", "the lack of awareness among the farmers", "the
   perception of CAPs performance from the proposed use of CAPs".
3. **Zero-auxiliary passives**: "also documented by [Author et al. (Year)]" (no
   "was" before "documented").
4. **Infinitive with -s**: "may aid to improves the CAPs PEX" and "in order
   to enables the better perception".
5. **ESL attribution**: "[Author et al. (Year)], and [Author et al. (Year)]" — the
   comma before "and" is itself a stylistic ESL marker.
6. **Connector rotation**: "However," → "Moreover," → no third connector
   (would be forced). Rotation rule respected.
7. **"as well"** sentence-final softener at end of paragraph 2.
8. **"the same is the case for"** ESL comparison phrase.
9. **"need to educate"** — ESL calque for "need to be educated".
10. **"reportedly low perception"** — ESL hedging with "reportedly" +
    qualifier.
11. **Construct abbreviations**: PEX, EEX, SIN, CAPs, H2a all referred to by
    abbreviation. No re-expansion after first introduction.
12. **Statistics inline**: "(f²=0.000)" embedded mid-sentence without commas.
13. **No em dashes, no bullet lists, no semicolons** (well, one semicolon in
    the recommendation clause — preserved as ESL semicolon misuse pattern).
14. **British/Commonwealth spelling**: not visible in this chunk but enforced
    for any word that has a British variant.

---

## 11. Bridge Sentence Gate — Acceptable and Refused

### Acceptable bridge sentences

> "The development of automated sorting systems has also been explored in related agricultural research."

> "Existing solutions for voltage monitoring have been developed in other countries but they often require expensive equipment that most households in [the municipality] cannot afford."

> "However, the farmers' perception of CAPs performance is shaped by more than just the technical attributes of the practices themselves."

### Refused bridge sentences (will trigger re-request)

- `continue`
- `next`
- `go`
- `ok`
- `yes`
- `proceed`
- `Continue with the next chunk.`
- `Please continue.`

### Refusal reply template

```
Please write your own bridge sentence before I continue. A single word or
"continue" will not work here.

Example of an acceptable bridge sentence:
"Existing solutions for voltage monitoring have been developed in other
countries but they often require expensive equipment that most households
in [the municipality] cannot afford."

Your bridge sentence:
```

---

## 12. Voice Calibration From Student Sample

```
[SECTION INTAKE]

1. Thesis Title/Topic: Salikchick Egg Incubation Monitoring System
2. Thesis Category: Development
3. Section/Part: Chapter 1 — Significance
4. Voice Target: VOICE-B

My writing sample (for calibration):
"This study is important because it helps poultry farmers monitor their
eggs better. The system will give them notifications so they don't have
to check manually. Because of that, they can focus on other things
and still make sure the incubation is going well."

5. References: [none needed for Significance]
```

### Calibration outcome

Claude will silently read the writing sample and:
- Match sentence length distribution to the sample (short, casual)
- Reproduce the "Because of that," connector pattern
- Match the use of "going well" / "focus on other things" register
- Avoid overformalizing — preserve the casual ESL rhythm
- NOT announce the calibration in output

---

## 13. Error Flag Examples

### `[FORMAT ERROR: Non-compliant]`
Triggered when: section structure does not match institutional thesis format.
Example: Student asks for a "Background of the Study" section inside Chapter 3
(Background belongs in Chapter 1).

### `[CITATION ERROR: Use APA 7th]`
Triggered when: in-text citation does not follow APA 7th rules. Example:
"([Author, Year, p. XX, para. X, sec. X])" — too much detail for an in-text
citation. Should be "([Author, Year])" or "([Author, Year, p. XX])" for direct
quote only.

### `[STRUCTURE GAP: Theme Map missing]`
Triggered when: student requests RRL/RRS but did not provide a Theme Map.

### `[LOGIC GAP: Objective not mapped]`
Triggered when: Chapter 4 Results section is requested but the result
discussed does not correspond to any Specific Objective from Chapter 1.

### `[UNVERIFIABLE: abstract not found]`
Triggered when: web search for a cited reference returned no abstract or
summary. Output proceeds but the citation is flagged for the student to
verify manually.

### `[ASSUMPTION: cross-sectional design]`
Triggered when: student did not specify research design but the methodology
description implies cross-sectional. Claude proceeds with the assumption
and flags it.

### `[SPECIFICATION REQUIRED: instrument brand]`
Triggered when: Chapter 3 Instrumentation section is requested but the
student did not specify the actual instrument (sensor, model, brand).

### `[VOICE LOCK VIOLATION]` (v6.5.0 new)
Triggered when: student attempts to switch voice profile mid-chapter.
Example: VOICE-A declared for Introduction, then student requests
"continue with VOICE-B for the next chunk." Claude refuses and asks the
student to either complete the chapter in VOICE-A or close the chapter
first and start a new one.

### `[FRAMEWORK REQUIRED: UTAUT constructs]` (v6.5.0 new)
Triggered when: VOICE-C session is active and student requests Discussion
section but did not specify the theoretical framework and construct
abbreviations. Claude refuses and asks for the framework declaration.

---

## How to Use This File

1. **For a new session**: Copy the relevant intake template (sections 1-7
   above) and fill in the student's actual data.
2. **For a teaching demonstration**: Use sections 9-10 to show students what
   the generated output looks like and what markers to look for.
3. **For debugging**: Use section 13 to identify which error flag was raised
   and what to fix in the intake.
4. **For voice calibration**: Use section 12 — always paste a writing sample
   when running VOICE-B or VOICE-C for the first time in a session.

This file is loaded on-demand. The orchestrator SKILL.md does not pre-load
it. To request it explicitly:

```
cat examples/example.md
```
