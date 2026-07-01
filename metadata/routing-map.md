# Routing Map

This document maps every possible student request to the correct reference
files and scripts to load. Claude should use this as a decision tree before
generating any output.

---

## Voice Profile Routing

| Voice Target Declared | Load |
|---|---|
| BASE | `cat references/voice_base.md` |
| VOICE-A | `cat references/voice_a.md` |
| VOICE-B | `cat references/voice_b.md` |
| VOICE-C (Pakistani ESL PhD) | `cat references/voice_c.md` AND `cat references/voice_c_style_essence.md` (co-loaded) |
| Not declared | Ask before generating |

**Voice Family Lock**: Once a voice family (Filipino undergraduate or Pakistani ESL PhD)
is declared for a chapter, it cannot be switched mid-chapter. VOICE-C is its own
family; BASE / VOICE-A / VOICE-B form the Filipino undergraduate family. Within
the Filipino family, voice rotation rules still apply between chunks.

---

## Section Template Routing

| Section Requested | Load |
|---|---|
| Introduction / Background | `cat references/section_templates_ch1.md` |
| Problem Statement | `cat references/section_templates_ch1.md` |
| Objectives | `cat references/section_templates_ch1.md` |
| Scope and Delimitation | `cat references/section_templates_ch1.md` |
| Significance | `cat references/section_templates_ch1.md` |
| Conceptual Framework | `cat references/section_templates_ch1.md` |
| Definition of Terms | `cat references/section_templates_ch1.md` |
| RRL / Related Literature | `cat references/section_templates_ch2.md` |
| RRS / Related Studies | `cat references/section_templates_ch2.md` |
| Synthesis / Gap | `cat references/section_templates_ch2.md` |
| Research Design / Methodology | `cat references/section_templates_ch3.md` |
| Data Gathering Procedure | `cat references/section_templates_ch3.md` |
| Instrumentation | `cat references/section_templates_ch3.md` |
| Statistical Tools | `cat references/section_templates_ch3.md` |
| Results and Discussion | `cat references/section_templates_ch4_ch5.md` |
| Summary of Findings | `cat references/section_templates_ch4_ch5.md` |
| Conclusions | `cat references/section_templates_ch4_ch5.md` |
| Recommendations | `cat references/section_templates_ch4_ch5.md` |
| Discussion (VOICE-C per-hypothesis) | `cat references/section_templates_ch4_ch5.md` + `cat references/voice_c.md` + `cat references/voice_c_style_essence.md` |
| Contribution / Theoretical Implications (VOICE-C) | `cat references/voice_c.md` + `cat references/voice_c_style_essence.md` |
| Managerial / Practical Implications (VOICE-C) | `cat references/voice_c.md` + `cat references/voice_c_style_essence.md` |
| Chapter Summary / Chapter Conclusion (VOICE-C) | `cat references/voice_c.md` (chapter sandwich pattern) |

---

## Format and Compliance Routing

| Task | Load |
|---|---|
| Any generation or humanization task | `cat references/bu_format_specs.md` |
| Any citation check or reference processing | `cat references/apa_citation_rules.md` |
| Any prose generation | `cat references/humanization_techniques.md` |
| Phase 4 authenticity pass | `cat references/authenticity_checklist.md` |
| Edge case or conflict in grammar/voice | `cat references/conflict_resolution.md` |
| Tier 5 mistake injection review | `cat references/tier5_mistake_layer.md` |

---

## Script Routing

| Task | Run |
|---|---|
| Citation verification requested | `python scripts/verify_citations.py` |
| Tier 5 injection audit needed | `python scripts/tier5_audit.py` |
| Intake form pre-population | `python scripts/intake_prefill.py` |

---

## Minimum Load Per Task

### Humanize existing text (Filipino undergraduate)
1. Voice reference for declared profile (BASE / VOICE-A / VOICE-B)
2. `references/humanization_techniques.md`
3. `references/bu_format_specs.md`
4. `references/authenticity_checklist.md` (internal)

### Humanize existing text (Pakistani ESL PhD — VOICE-C)
1. `references/voice_c.md`
2. `references/voice_c_style_essence.md`
3. `references/humanization_techniques.md` (especially Section 2.16)
4. `references/apa_citation_rules.md`
5. `references/authenticity_checklist.md` (internal — including VOICE-C checks)

### Generate a new section (Filipino undergraduate)
1. Voice reference for declared profile (BASE / VOICE-A / VOICE-B)
2. Section template for that chapter
3. `references/humanization_techniques.md`
4. `references/bu_format_specs.md`
5. `references/apa_citation_rules.md`
6. `references/authenticity_checklist.md` (internal)

### Generate a new section (Pakistani ESL PhD — VOICE-C)
1. `references/voice_c.md`
2. `references/voice_c_style_essence.md`
3. Section template for that chapter
4. `references/humanization_techniques.md` (especially Section 2.16)
5. `references/apa_citation_rules.md`
6. `references/authenticity_checklist.md` (internal — including VOICE-C checks)

### Intake + pre-generation summary only
1. `references/bu_format_specs.md` (Filipino) OR `references/voice_c_style_essence.md` (VOICE-C)
2. `references/apa_citation_rules.md`

---

## What NOT to Load

- Do not pre-load all voice profiles. Load only the declared one.
- Do not load `voice_c.md` without also loading `voice_c_style_essence.md` (they are co-loaded).
- Do not load `voice_c_style_essence.md` without `voice_c.md` (the essence file is meaningless without the full profile).
- Do not load Chapter 4/5 templates for a Chapter 1 request.
- Do not load Tier 5 reference unless Tier 5 audit is explicitly requested.
- Do not load conflict_resolution.md unless an edge case arises.
- Do not run scripts unless the task explicitly requires them.
- Do not load VOICE-C references for a Filipino undergraduate session, even if the student mentions "PhD" or "graduate" in passing. Only load VOICE-C when the student explicitly declares Voice Target: VOICE-C.
