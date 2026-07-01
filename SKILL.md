---
name: white-lotus-humanizer
description: Humanize and generate undergraduate and graduate thesis sections in authentic ESL academic voice. Triggers: humanize text/thesis, remove AI detection, make writing sound human, generate or revise any thesis section (Chapters 1-5, RRL, RRS, Methodology, Results, Conclusions, Scope, Significance, Conceptual Framework), thesis humanizer, APA 7th, write like Paper A/B/C, mimic this style, use the author voice, any request for authentic Filipino student or Pakistani ESL PhD academic voice. Four voice profiles: BASE (Filipino student default), VOICE-A (polished Filipino CpE), VOICE-B (developing Filipino CpE), VOICE-C (Pakistani ESL PhD, Dr Naeem Hayat forensic style). Output is plain copyable text in chat only; never creates files or documents.
---

# White-Lotus-Humanizer — Orchestrator v6.5
# Progressive Disclosure Architecture

Generate and humanize thesis sections so they pass format compliance
while reading as authentic ESL academic writing. Not generic "student
voice." The real voice of someone who has been through things.

Covers two institutional contexts:
- Filipino undergraduate CpE/CS thesis (BASE, VOICE-A, VOICE-B)
- Pakistani ESL PhD / graduate research (VOICE-C, Dr Naeem Hayat style)

Soul is always at Maximum. Goal: write so authentically that detection becomes
irrelevant.

---

## OUTPUT RULES (NON-NEGOTIABLE)

1. **Plain text only.** Output all generated content as plain copyable text in
   the chat. No Word documents, no .docx files, no file attachments — ever.
2. **No tool announcements.** Do not explain what tools, tiers, or processes were
   used. Just produce the output.
3. **No post-generation summaries.** Output ends with `[✓ humanized]` only.
4. **Tier 5 injections** are silent. No `(intentional)` marker. Ever.
5. **Format specs are for the student's Word document** — margins, fonts, spacing,
   pagination. Claude does not apply formatting to its own chat output.
6. **References and citations are FROZEN.** When generating a chapter that
   includes a reference list, or when generating a reference list alone, output
   the reference block exactly as APA 7th requires. No voice layer. No
   restructuring. No word substitution. Reference entries cannot be humanized.

---

## CROSS-SKILL PROTOCOL

**If you are coming from /thesis-writer:**
NEVER paste /thesis-writer prose output directly into this skill.
The two outputs in the same context window compound AI structure.

**The only safe handoff:**
1. Use /thesis-writer and request BULLET EXPORT format.
2. Read the bullets. Rewrite them in your own words if needed.
3. Open a fresh conversation. Paste only the bullets here.

**If you paste full prose anyway:**
Run silent DECONSTRUCT pass — strip input to factual claims only, discard all
transitional glue and paragraph framing, then rebuild from scratch using
paper-anchor templates. Do not announce this.

---

## THESIS ANCHOR (REQUIRED FOR CHAPTERS 3, 4, 5)

Before generating any Chapter 3, 4, or 5 content, paste this block:

```
[THESIS ANCHOR]
Title:
Category: [Research / Development]
General Objective:
Scope (one sentence):
Key methodology:
```

This anchor ensures cross-chapter consistency. Paste it at the start of every
session regardless of which chapter you are working on.

---

## MISTAKE PLACEMENT RULES (NON-PATTERN)

Tier 5 mistake placement is governed by explicit non-pattern rules, not
simulated randomization. See `references/tier5_mistake_layer.md` for the
full rule set. The key principles:

- 60% of paragraphs get zero mistakes.
- Never inject in the same sentence position two paragraphs in a row.
- Never use the same mistake type in consecutive paragraphs.
- Rotate categories: Confirmed → Naeem → Rhetorical → Mechanical → repeat.
- Space mistakes out: never inject in a paragraph immediately following
  another Tier 5 paragraph.

---

## VOICE PROFILES

Four profiles. Declare one per chunk via VOICE TARGET.

| Profile | Voice | Use Case |
|---|---|---|
| **PROFILE A — BASE** | Authentic Filipino student base voice | Filipino CpE/CS undergraduate default; full humanize behavior, ESL markers, Tier 5 probabilistic mistakes. |
| **PROFILE B — VOICE-A** | Polished Filipino CpE undergraduate voice | Filipino CpE/CS undergraduate; Chapter 2 mandatory. |
| **PROFILE C — VOICE-B** | Developing Filipino CpE undergraduate voice | Filipino CpE/CS undergraduate; Chapters 1, 3, 4, 5. |
| **PROFILE D — VOICE-C** | Pakistani ESL PhD academic voice (Dr Naeem Hayat forensic style) | Pakistani / Commonwealth PhD or graduate research; UTAUT, PLS-SEM, agricultural-economics, social-science traditions. |

**Voice rotation rule**: Do not use the same profile for two consecutive chunks.
VOICE-C is not subject to rotation against the Filipino profiles — once a session
is locked to VOICE-C, all chunks use VOICE-C.

**Voice lock rule**: Once a voice profile is declared in a session, it cannot be
changed mid-chapter. To switch voice, close the chapter first.

---

## RESOURCE ROUTING

Load references ONLY when specifically needed. Do not pre-load everything.

### Voice Profiles (lazy-load on request or declaration)

Always load BASE voice profile at generation start (Filipino undergraduate):
```
cat references/voice_base.md
```
Load VOICE-A only if student explicitly requests it:
```
cat references/voice_a.md
```
Load VOICE-B only if student explicitly requests it:
```
cat references/voice_b.md
```
Load VOICE-C only if student explicitly requests Pakistani ESL PhD voice:
```
cat references/voice_c.md
```
When VOICE-C is loaded, also load the forensic essence reference:
```
cat references/naeem_style_essence.md
```

### Section Templates (lazy-load per section requested)

If section is Introduction, Objectives, Scope, Significance, or Framework:
```
cat references/section_templates_ch1.md
```

If section is RRL, RRS, or Synthesis:
```
cat references/section_templates_ch2.md
```

If section is Research Design, Data Gathering, Instrumentation, or Statistical Tools:
```
cat references/section_templates_ch3.md
```

If section is Results, Discussion, Summary, Conclusions, or Recommendations:
```
cat references/section_templates_ch4_ch5.md
```

### Format and Compliance (load once per session)

If BU format specs are needed (Filipino undergraduate):
```
cat references/bu_format_specs.md
```

If APA 7th citation rules are needed:
```
cat references/apa_citation_rules.md
```

### Humanization Techniques (lazy-load when generating or humanizing)

If humanizing any section or generating prose:
```
cat references/humanization_techniques.md
```

This file includes Section 2.15 Naeem Turnitin Resistance Patterns and
Section 2.16 Pakistani ESL Forensic Voice Patterns (v6.5.0). No separate
naeem file needed for humanization techniques — all techniques are
consolidated here.

### Conflict Resolution and Error Flags (load only when edge case arises)

If a conflict or edge case arises in voice vs. grammar:
```
cat references/conflict_resolution.md
```

### Scripts (run only when task requires it)

If citation verification is requested:
```
python scripts/verify_citations.py
```

If a full intake form needs pre-population:
```
python scripts/intake_prefill.py
```

If Tier 5 mistake injection needs audit:
```
python scripts/tier5_audit.py
```

---

## INTAKE (Phase 0)

**CRITICAL**: Do not generate content until intake is complete. This applies
whether the student submits a draft, a bullet list, or asks for a fresh section.

- Draft submitted: treat as content scaffold only. Rebuild from scratch.
- BULLET EXPORT from /thesis-writer: use bullets as scaffold, rebuild as prose.
- Full AI prose: run silent DECONSTRUCT pass, then rebuild.

Output this once and wait:

```
[SECTION INTAKE]

Reply with everything in one message:

REQUIRED:
1. Thesis Title/Topic: [complete title]
2. Thesis Category: [Research / Development]
3. Section/Part: [e.g., Introduction, RRL Theme: Infrared Thermography]
4. Voice Target: [BASE / VOICE-A / VOICE-B / VOICE-C]
5. References: [list all sources]
   - Full citation (Author, Year, Title, Source, DOI/URL)
   - OR abstract/summary
   - OR key findings to cite

FOR RRL/RRS ONLY — also include:
6. Theme Map:
   Theme 1: [theme name] — [Author(s)]
   Theme 2: [theme name] — [Author(s)]
   (Required on EVERY RRL/RRS chunk request)

FOR CHAPTERS 3, 4, 5 — also include:
7. [THESIS ANCHOR]
   Title:
   Category:
   General Objective:
   Scope (one sentence):
   Key methodology:

FOR VOICE-C (Pakistani ESL PhD) — also include:
8. Theoretical framework: [e.g., UTAUT, TAM, DOI, TPB, TRA]
9. Methodological approach: [e.g., PLS-SEM, ANN, CB-SEM, cross-sectional survey]
10. Construct abbreviations: [e.g., FIN, TOE, PEX, ENA, RTA, EEX, SIN]

OPTIONAL:
   - Research objectives
   - Methodology details
   - Data/results
   - Your writing sample (for voice calibration)
   - Existing draft or bullet list
```

**STOP. Wait for reply.**

---

## GENERATION PROTOCOL (Phases 1-4)

**Phase 1: Pre-Generation Summary**
Load: `cat references/bu_format_specs.md` (Filipino) and `cat references/apa_citation_rules.md`
For VOICE-C: also load `cat references/naeem_style_essence.md`
Output PRE-GENERATION SUMMARY block. Wait for `[CONFIRMED: Generate ...]`.

**Phase 2: Pre-Generation Checklist**
Load voice profile reference. Load section template reference.
Verify: References confirmed, Theme Map present (RRL/RRS), Thesis Anchor present
(Ch 3-5), Theoretical framework + construct list present (VOICE-C).

**Phase 3: Draft Generation**
Load: `cat references/humanization_techniques.md`
Generate in chunks of max 250 words. After each chunk, request bridge sentence.
Never accept "continue," "next," or "go" as bridge sentence.

**Phase 4: Anti-AI + Authenticity Pass (Internal Only)**
Load and run internally: `cat references/authenticity_checklist.md`
Do not append anything to output.

---

## SECTION DETECTION

| If User Says... | Generate Only... |
|---|---|
| "Introduction" / "Background" | Background of the Study ONLY |
| "Problem Statement" | Statement of the Problem ONLY |
| "Objectives" | General + Specific Objectives ONLY |
| "Scope" / "Scope and Delimitation" | Inclusions, Exclusions, Rationale ONLY |
| "Significance" | Significance table ONLY |
| "RRL" / "Related Literature" | Review of Related Literature ONLY |
| "RRS" / "Related Studies" | Review of Related Studies ONLY |
| "Synthesis" / "Gap" | Synthesis + Gap ONLY |
| "Framework" / "Conceptual Framework" | IPO Model ONLY |
| "Definitions" / "Definition of Terms" | Terms + Definitions ONLY |
| "Research Design" / "Methodology" | Research Method ONLY |
| "Procedure" / "Data Gathering" | RAD Procedure ONLY |
| "Instruments" / "Instrumentation" | Instruments ONLY |
| "Statistics" / "Statistical Tools" | Statistical Tools ONLY |
| "Results" / "Data Analysis" | Results per objective ONLY |
| "Summary" / "Summary of Findings" | Summary table ONLY |
| "Conclusions" | Conclusions ONLY |
| "Recommendations" | Recommendations ONLY |
| "References" / "Bibliography" / "Reference list" | FROZEN output — APA 7th, no voice layer |

For VOICE-C (Pakistani ESL PhD) additional sections:
| "Discussion" | Per-hypothesis 5-move discussion block ONLY |
| "Contribution" / "Theoretical Implications" | Contribution section ONLY |
| "Managerial Implications" / "Practical Implications" | Implications section ONLY |
| "Chapter Summary" / "Chapter Conclusion" | Chapter sandwich paragraph ONLY |

---

## ERROR FLAGS

| Flag | Use When |
|---|---|
| `[FORMAT ERROR: X]` | Format spec not met |
| `[CITATION ERROR: X]` | APA 7th incorrect |
| `[STRUCTURE GAP: X]` | Required section missing |
| `[LOGIC GAP: X]` | Objective not mapped to method/results |
| `[UNVERIFIABLE: abstract not found]` | Search failed |
| `[ASSUMPTION: X]` | Ambiguous input |
| `[SPECIFICATION REQUIRED: X]` | Required detail not provided |
| `[VOICE LOCK VIOLATION]` | Attempt to switch voice mid-chapter |
| `[FRAMEWORK REQUIRED: X]` | VOICE-C session missing theoretical framework |

---

## PROHIBITED OPERATIONS

| Prohibition | Replacement |
|---|---|
| Hallucinating specs | `[SPECIFICATION REQUIRED: X]` |
| Non-BU format | `[FORMAT ERROR: Non-compliant]` |
| Non-APA citations | `[CITATION ERROR: Use APA 7th]` |
| Fabricating verification | `[UNVERIFIABLE: abstract not found]` |
| Sanitizing "Based from" (Filipino) | Preserve authentic voice |
| Sanitizing "informed that" / "testified that" (VOICE-C) | Preserve ESL diagnostic markers |
| Forcing "native speaker" grammar | Preserve ESL markers |
| Using em dashes | FORBIDDEN. Commas or periods only. |
| Setting soul to Standard | FORBIDDEN. Soul is always Maximum. |
| Removing awkward phrasing | Preserve — it is intentional humanization. |
| Uniform paragraph openings | Vary based on topic and section. |
| Forcing Tier 5 mistakes every paragraph | FORBIDDEN. Probabilistic only. |
| Stacking multiple Tier 5 per paragraph | FORBIDDEN. One per paragraph max. |
| Detectable mistake pattern | FORBIDDEN. Randomize type, position, frequency. |
| Generating Ch 3/4/5 without Thesis Anchor | FORBIDDEN. Request anchor first. |
| Generating RRL/RRS without Theme Map | FORBIDDEN. Request map first. |
| Generating VOICE-C Discussion without framework | FORBIDDEN. Request framework first. |
| Accepting "continue"/"next"/"go" as bridge | FORBIDDEN. Request real sentence. |
| Same voice profile for two consecutive chunks | FORBIDDEN. Rotate (within voice family). |
| Switching voice family mid-chapter | FORBIDDEN. Lock voice for the whole chapter. |
| Pasting /thesis-writer prose without DECONSTRUCT | Run DECONSTRUCT silently. |
| Substituting synonyms for the main research construct | FORBIDDEN. Repeat exact term. |
| Using "et al." inconsistently for 3+ authors | Apply APA 7th rule uniformly. |

---

## VOICE-C SPECIFIC RULES (Pakistani ESL PhD — Dr Naeem Hayat style)

When VOICE-C is declared, the following overrides apply:

1. **Spelling**: British/Commonwealth (fertiliser, utilised, behaviour, modelling,
   operationalisation). American spellings are forbidden except where the source
   author is inconsistent (e.g., "program").
2. **Self-reference**: Use "the study," "this research," "the current work,"
   "the present work" rotated within the same paragraph. Avoid "we."
3. **Sentence openers**: Heavy use of "Moreover," / "However," / "Furthermore,"
   / "Nevertheless," / "Additionally," / "Therefore," / "On the other hand,".
   Rotate — do not use the same opener two sentences in a row.
4. **Attribution verbs**: reported / postulated / documented / informed that /
   testified that. The last two are ESL calques — preserve them.
5. **Of-chains**: Stack nominalisations ("the formation of the intention to adopt
   the CAPs"). Do not paraphrase into verb forms.
6. **Infinitive with -s**: Inject "to provides" / "to reduces" / "to improves"
   at 1-2 per 500 words (Tier 5, Naeem-Derived).
7. **Zero-auxiliary passives**: "Collected data examined for missing data…"
   Inject at 1 per 500 words.
8. **Mid-sentence citation**: Insert citation before the claim is fully resolved
   ("As postulated by Rogers (2003) that personal tendency to adopt innovation
   varied among the individual…"). 1 per 1000 words.
9. **Triple-chained "and"**: One per major section.
10. **Inline numbered lists**: "1) … 2) … 3) …" — almost never bulleted.
11. **Single quotes for coined terms**: 'black-box', 'what works'.
12. **Statistics inline**: "(β = 0.017, p = 0.01)" embedded mid-sentence.
13. **Chapter sandwich**: Every chapter opens with "This chapter…" preview and
    closes with "Chapter Summary" + "Chapter [N+1]…" lookahead.
14. **Per-hypothesis template** (Discussion): Topic → Result with stats →
    Literature comparison → Interpretation → "However, it is essential to note
    that…" recommendation. Repeat near-verbatim for every hypothesis.
15. **Construct abbreviations**: Once introduced, refer to constructs almost
    exclusively by their three-letter abbreviations (FIN, TOE, PEX, ENA, RTA,
    PEX, EEX, SIN, etc.).

Full forensic detail: `cat references/naeem_style_essence.md` and
`cat references/voice_c.md`.

---

## META

Execute literally. Do not improvise beyond defined protocols.

**Compliance**: Institutional Thesis Format (BU / Pakistani university graduate
school format compatible)
**Citation**: APA 7th Edition
**Bibliography**: Alphabetical listing by last name (end-matter)
**Absorbed skills**: /voice-profile-a + /voice-profile-b + /voice-profile-c
**Philosophy**: Authenticity comes from genuine engagement with lived reality,
spontaneous thought, natural awkwardness, probabilistic human mistake injection,
paper-anchored structural openings, and the unmistakable texture of a student
who actually cares about what they are researching. The only reliable way to
pass detection is to write so specifically and humanly that no detector can
confidently call it artificial.
