# White-Lotus-Humanizer
note: this is optimized for claude only(sonnet 5 below, with medium effort only for sonnet 5 as it gets flagged by the regulations when use maximum effort)
## Disclaimer

- This Claude skill does not guarantee a 0% similarity score in Turnitin or any other plagiarism detection system. Such a guarantee cannot be made because the skill has not been tested with Turnitin, and the developer does not have access to Turnitin for validation.
- The primary purpose of this Claude skill is to reduce AI-generated writing patterns, making the generated drafts easier to revise and paraphrase. Results will vary depending on the prompt, the provided source material, the generated content, and the detection tool being used.
- Based on the developer's personal experience, when evaluated using Grammarly's AI detector, the skill has occasionally produced outputs under 300 words (such as simple essays, thesis abstracts, or introduction sections) that were reported as 0% AI-written. This is only an anecdotal observation, not a guarantee or expected outcome. Different AI detectors, longer documents, or more complex writing tasks may produce different results.
- Recommended workflow: Upload this Claude skill together with your master thesis file (your single source of truth). Use it to generate drafts only, then carefully review, edit, and paraphrase the output before using it in any academic or professional work.
- If an AI detector still flags the generated content, manually revise and rewrite the affected sections. Never submit generated content without substantial human review and editing.
- This Claude skill intentionally prioritizes natural, human-like writing over perfectly polished grammar. As a result, some outputs may include minor grammatical imperfections, slightly awkward phrasing, or inconsistent sentence structures to better resemble authentic human writing.
- If you expect flawless grammar, publication-ready writing, or guaranteed AI detector performance, this Claude skill is not intended for that purpose. It is a drafting assistant, not a replacement for careful human writing and editing.
- You are solely responsible for ensuring the final document meets your institution's requirements for originality, citations, formatting, academic integrity, and factual accuracy.

## Collaboration

I welcome collaboration from the community to improve this Claude skill. Contributors are welcome to help with prompt engineering, workflow optimization, evaluation methods, writing quality, natural language generation, documentation, and testing.

My long-term vision is to continue researching and improving this project. If the writing pipeline becomes sufficiently mature and well-validated, I plan to build a writing assistance system focused on producing more original, natural, and well-edited academic drafts that better satisfy plagiarism and AI-writing evaluation standards while maintaining academic integrity.

**Undergraduate & Graduate Thesis Humanizer**
Version 6.5.0 — Progressive Disclosure Architecture

Generates and humanizes thesis sections with authentic ESL academic voice
across **four voice profiles**, institutional format compliance, and APA 7th
edition citations.

- **BASE / VOICE-A / VOICE-B** — Filipino undergraduate CpE/CS thesis voice
- **VOICE-C** — Pakistani ESL PhD / graduate research voice (the author
  forensic reconstruction, confirmed 0% Turnitin AI-detection)

---

## What This Skill Does

- Generates any thesis section from scratch (Chapters 1-5, Bibliography,
  plus graduate-level Discussion, Contribution, Managerial Implications,
  Chapter Summary)
- Humanizes existing AI-written text so it reads as authentic ESL academic
  writing
- Converts /thesis-writer BULLET EXPORT into full prose
- Enforces institutional thesis format compliance ([the University] / [a Commonwealth] university
  graduate school format compatible)
- Enforces APA 7th edition citations
- Verifies citations via web search before generation
- Four voice profiles across two voice families:
  - Filipino undergraduate: BASE, VOICE-A, VOICE-B
  - Pakistani ESL PhD: VOICE-C (the author forensic style)
- Chunks output and gates on student-written bridge sentences to prevent
  AI-looking continuity
- Injects probabilistic human mistakes (Tier 5) to avoid detection,
  including Pakistani ESL markers (zero-auxiliary passives, infinitive-with-s,
  dropped articles) when VOICE-C is active

---

## Repository Structure

```
White-Lotus-Humanizer-v6.5.0/
├── SKILL.md                        Orchestrator — lightweight, always loaded
├── README.md                       This file
├── LICENSE                         MIT License
├── CHANGELOG.md                    Version history
├── setup.sh                        Setup script for local use
├── requirements.txt                Empty — no dependencies
├── metadata/
│   ├── manifest.json               Machine-readable skill metadata
│   ├── routing-map.md              Reference file routing decision table
│   └── dependency-notes.md         Script and environment dependency notes
├── references/
│   ├── voice_base.md               Profile A: BASE humanize voice (Filipino)
│   ├── voice_a.md                  Profile B: VOICE-A (polished Filipino CpE)
│   ├── voice_b.md                  Profile C: VOICE-B (developing Filipino CpE)
│   ├── voice_c.md                  Profile D: VOICE-C (Pakistani ESL PhD) [NEW v6.5.0]
│   ├── voice_c_style_essence.md      Forensic quick-reference for VOICE-C [NEW v6.5.0]
│   ├── humanization_techniques.md  All rhetorical + structural techniques
│   ├── tier5_mistake_layer.md      Probabilistic human mistake injection rules
│   ├── bu_format_specs.md          Institutional format compliance specs
│   ├── apa_citation_rules.md       APA 7th edition citation rules
│   ├── section_templates_ch1.md    Chapter 1 section templates
│   ├── section_templates_ch2.md    Chapter 2 section templates
│   ├── section_templates_ch3.md    Chapter 3 section templates
│   ├── section_templates_ch4_ch5.md Chapter 4 and 5 section templates
│   ├── conflict_resolution.md      Voice vs. grammar conflict rules
│   └── authenticity_checklist.md   Phase 4 internal anti-AI checklist
├── scripts/
│   ├── verify_citations.py         APA 7th citation format checker
│   ├── tier5_audit.py              Tier 5 mistake injection auditor
│   └── intake_prefill.py           Intake form pre-population utility
├── examples/
│   ├── example.md                  Consolidated templates for all 4 voices [NEW v6.5.0]
│   ├── example-prompts.md          Real usage prompt examples (Filipino)
│   └── example-outputs.md          Annotated output examples (Filipino)
└── docs/
    ├── architecture.md             System design and orchestration flow
    └── progressive-disclosure.md   Architecture rationale and extension guide
```

---

## Setup

### For Claude Projects (Recommended)

1. Upload `SKILL.md` as the project instructions file in Claude.ai Project
   settings. The frontmatter contains only `name` and `description` (749 chars,
   well under the 1024-char Claude skill limit).
2. Upload all files in `references/` as project knowledge files.
3. The scripts in `scripts/` are available as documentation; Claude can read
   them as reference in standard Projects.
4. The example files in `examples/` are optional reference material — load
   on demand.

### For Claude Computer Use / Bash Tool

1. Clone or upload the full repository.
2. Python 3.9+ required for scripts. No packages needed.
3. Run `bash setup.sh` to verify environment.

### For Local Script Use

```bash
# Verify APA citations
python scripts/verify_citations.py --input my_citations.txt

# Audit Tier 5 mistake injection
python scripts/tier5_audit.py --input my_chunk.txt

# Pre-fill intake form
python scripts/intake_prefill.py \
  --title "My Thesis Title" \
  --section "Introduction" \
  --category development \
  --voice VOICE-A \
  --refs references.txt
```

---

## Usage

### Basic Workflow

1. Open a Claude.ai Project with this skill installed.
2. Tell Claude what you need: "Humanize this," "Write my Introduction,"
   or "Generate my RRL."
3. Claude will output the `[SECTION INTAKE]` form.
4. Fill out the form completely and reply in one message. Specify
   Voice Target (BASE / VOICE-A / VOICE-B / VOICE-C).
5. Claude outputs the `[PRE-GENERATION SUMMARY]`. Review and reply:
   `[CONFIRMED: Generate Introduction]`
6. Claude generates the first chunk (max 250 words).
7. After each chunk, write your own bridge sentence and paste it.
8. Repeat until the section is complete.
9. Output ends with `[✓ humanized]`.

### Voice Profiles

| Profile | Family | Description | Best For |
|---|---|---|---|
| BASE | Filipino undergrad | Generic authentic Filipino student voice | Any section, calibrated to student's own sample |
| VOICE-A | Filipino undergrad | Polished Filipino CpE undergraduate voice | Chapter 2 mandatory; Chapter 1, 3, 4, 5 |
| VOICE-B | Filipino undergrad | Developing Filipino CpE undergraduate voice | Chapter 1, 3, 4, 5 |
| VOICE-C | Pakistani ESL PhD | the author forensic voice (0% Turnitin) | Graduate / PhD research; UTAUT, PLS-SEM, agricultural economics, social science |

**Within the Filipino undergraduate family**: do not use the same profile for
 two consecutive chunks. Chapter 2 (RRL, RRS, Synthesis) uses VOICE-A only.

**VOICE-C is its own family**: once locked, all chunks in the chapter use
 VOICE-C. No rotation against Filipino profiles.

### Voice Family Lock

Once a voice family is declared for a chapter, it cannot be switched
mid-chapter. To switch voice:
1. Close the current chapter first.
2. Start a new chapter in a fresh conversation.
3. Declare the new voice family at intake.

Attempting to switch voice mid-chapter triggers `[VOICE LOCK VIOLATION]`.

### VOICE-C Specific Intake Fields

When Voice Target: VOICE-C is declared, the intake form requires three
additional fields:
- Theoretical framework (e.g., UTAUT, TAM, DOI, TPB, TRA)
- Methodological approach (e.g., PLS-SEM, ANN, CB-SEM, cross-sectional survey)
- Construct abbreviations (e.g., FIN, TOE, PEX, ENA, RTA, EEX, SIN)

Without these, the `[FRAMEWORK REQUIRED: X]` error flag is raised.

### Bridge Sentences

After each chunk, Claude will ask for a bridge sentence.

**Acceptable:**
> "The development of automated sorting systems has also been explored in
> related agricultural research."

**Not acceptable:**
> "continue" / "next" / "go" / "ok"

The bridge sentence requirement is what breaks AI continuity patterns.
It is not optional.

---

## Cross-Skill Handoff from /thesis-writer

If you are using /thesis-writer alongside this skill:

1. Use /thesis-writer and request **BULLET EXPORT** format — NOT prose.
2. Open a **fresh conversation** with this skill.
3. Paste only the bullets in the intake form.

Do not paste /thesis-writer prose directly. It compounds AI structure and
produces output that still reads as machine-generated.

---

## Compliance

- **Format**: Institutional Thesis Format ([the University] / Pakistani university graduate
  school format compatible)
- **Citation**: APA 7th Edition
- **Bibliography**: Alphabetical, hanging indent, end-matter
- **Spelling (VOICE-C only)**: British/Commonwealth
  (fertiliser, utilised, behaviour, modelling, operationalisation)

---

## Absorbed Skills

This skill fully replaces and absorbs:
- `/voice-profile-a`
- `/voice-profile-b`
- `/voice-profile-c` (new in v6.5.0)

Those skills do not need to be loaded separately when this skill is installed.

---

## Frontmatter Specification (v6.5.0)

The `SKILL.md` frontmatter contains **only** two fields:

```yaml
---
name: white-lotus-humanizer
description: <749-character description>
---
```

All other metadata (`version`, `compliance`, `citation_style`,
`absorbed_skills`) lives in:
- The markdown body of `SKILL.md` (META section)
- `metadata/manifest.json` (machine-readable)

This ensures compatibility with strict Claude skill validators that enforce
a 1024-character limit on the `description` field and reject unknown
frontmatter fields.

---

## Maintenance

- Voice profiles are stored in `references/` as independent files.
  Update a profile without touching SKILL.md.
- Format compliance rules are in `references/bu_format_specs.md`.
  Update when your institution releases a new format revision.
- APA rules are in `references/apa_citation_rules.md`.
  Update if APA releases a new edition.
- Section templates are split by chapter in `references/`.
  Update individual chapter files without affecting other chapters.
- VOICE-C forensic detail lives in `references/voice_c.md` and
  `references/voice_c_style_essence.md`. Update both files together — they are
  co-loaded and reference each other.

---

## License

MIT License. See LICENSE.
