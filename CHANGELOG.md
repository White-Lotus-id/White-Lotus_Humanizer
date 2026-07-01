# CHANGELOG — White-Lotus-Humanizer

All notable changes are documented here.

Format: [VERSION] — YYYY-MM-DD

---

## [6.5.0] — 2026-06-25

### Added

- **New voice profile: VOICE-C (Pakistani ESL PhD voice)**. Forensic
  reconstruction of Dr Naeem Hayat's PhD thesis style on Conservative
  Agriculture Practices (CAPs) adoption. Confirmed 0% Turnitin
  AI-detection. Covers UTAUT / TAM / DOI / TPB / TRA theoretical frames,
  PLS-SEM + ANN methodology, agricultural-economics / social-science
  tradition. Lives in `references/voice_c.md`.

- **New forensic quick-reference: `references/naeem_style_essence.md`**.
  Operational in-generation glance-up file loaded alongside `voice_c.md`
  when VOICE-C is active. Contains the Three Rules of Mimicry, ESL
  diagnostic marker density targets, connector inventory, attribution
  verb rankings, per-hypothesis discussion template, finding-attribution
  formula phrases, chapter sandwich pattern, sentence templates, fake
  abstract example, and quick-reference cheat sheet.

- **New example file: `examples/example.md`**. Consolidated template
  collection covering all four voice profiles (BASE, VOICE-A, VOICE-B,
  VOICE-C), full intake protocol, pre-generation summary block,
  annotated chunk outputs for both Filipino undergraduate (VOICE-A) and
  Pakistani ESL PhD (VOICE-C) voices, bridge sentence gate examples
  (acceptable and refused), voice calibration workflow, and error flag
  examples including the new v6.5.0 flags.

- SKILL.md: New "VOICE-C SPECIFIC RULES" section with 15 numbered
  overrides that activate when VOICE-C is declared. Covers British
  spelling, self-reference rotation, sentence openers, attribution
  verbs, of-chains, infinitive-with-s markers, zero-auxiliary passives,
  mid-sentence citation, triple-chained "and", inline numbered lists,
  single-quote coined terms, inline statistics, chapter sandwich,
  per-hypothesis discussion template, and construct abbreviations.

- SKILL.md: Two new error flags: `[VOICE LOCK VIOLATION]` (refuses
  mid-chapter voice switch) and `[FRAMEWORK REQUIRED: X]` (refuses
  VOICE-C Discussion generation without theoretical framework + construct
  list declared).

- SKILL.md: Intake form extended with three new VOICE-C-only required
  fields: Theoretical framework, Methodological approach, Construct
  abbreviations.

- SKILL.md: Section Detection table extended with four VOICE-C-specific
  entries: Discussion, Contribution, Managerial Implications, Chapter
  Summary.

- SKILL.md: Prohibited Operations table extended with three new
  prohibitions: VOICE-C framework-less generation, mid-chapter voice
  family switch, and synonym substitution for the main research
  construct.

- references/humanization_techniques.md: New Section 2.16 Pakistani ESL
  Forensic Voice Patterns. Six pattern families extracted from the Dr
  Naeem Hayat 0% Turnitin thesis: of-chain nominalisation stacking,
  zero-auxiliary passive construction, infinitive-with-s marker,
  "informed that" / "testified that" attribution verbs, "as well" /
  "as well as" overuse, and British/Commonwealth spelling enforcement.

- references/tier5_mistake_layer.md: Naeem-Derived Errors category
  expanded with five additional markers sourced from the Pakistani ESL
  PhD thesis: dropped definite article before nominalised subject,
  dropped "be" in modal construction, subject-verb agreement slip on
  compound subjects, wrong tense after "as", and "up to author
  knowledge" ESL hedge.

- references/authenticity_checklist.md: New VOICE-C Authenticity Checks
  block with eight checklist items covering nominalisation density,
  ESL marker distribution, connector rotation, per-hypothesis template
  adherence, chapter sandwich presence, construct abbreviation
  consistency, British spelling enforcement, and inline-list format.

- metadata/manifest.json: `voice_profiles` array extended with VOICE-C
  entry pointing to `references/voice_c.md`. `references.lazy_loaded`
  extended with `references/voice_c.md` and `references/naeem_style_essence.md`.
  `tags` extended with `pakistani-esl-phd`, `naeem-forensic-voice`,
  `graduate-research`, `pl-sem`, `utaut`. `absorbed_skills` extended
  with `voice-profile-c`.

### Changed

- SKILL.md frontmatter simplified to **only `name` and `description`**
  fields. Removed `version`, `compliance`, `citation_style`, and
  `absorbed_skills` from frontmatter — these now live exclusively in the
  markdown body and in `metadata/manifest.json`. Description is 749
  characters (well under the 1024-character Claude skill limit). This
  resolves compatibility issues with strict Claude skill validators.

- SKILL.md: VOICE PROFILES section rewritten as a 4-row table with voice
  family, label, and use case columns. VOICE-C is documented as
  non-rotating against the Filipino profiles — once a session is locked
  to VOICE-C, all chunks use VOICE-C.

- SKILL.md: RESOURCE ROUTING section extended with explicit load
  instructions for `voice_c.md` and `naeem_style_essence.md`. VOICE-C
  loads both files together; neither is loaded alone.

- SKILL.md: GENERATION PROTOCOL Phase 1 extended — when VOICE-C is
  declared, the pre-generation summary also loads
  `references/naeem_style_essence.md`.

- SKILL.md: GENERATION PROTOCOL Phase 2 checklist extended — VOICE-C
  sessions require theoretical framework + construct list present.

- README.md: Repository structure extended with new files. Setup
  instructions extended with VOICE-C guidance. Voice Profiles table
  extended with a fourth row. New "Voice Family Lock" subsection
  documents the rule that voice cannot be switched mid-chapter.

- metadata/routing-map.md: Decision table extended with two new
  VOICE-C-specific routes (load `voice_c.md` and load
  `naeem_style_essence.md`).

- metadata/dependency-notes.md: New entry for the
  `voice_c.md` + `naeem_style_essence.md` co-loading requirement.

### Preserved from v6.4.0

- All Filipino undergraduate voice profiles (BASE, VOICE-A, VOICE-B)
  fully preserved.
- All Tier 5 non-pattern rules preserved.
- All humanization techniques (Sections 2.1-2.15) preserved.
- All section templates (Ch 1-5) preserved.
- All format compliance specs preserved.
- All APA 7th citation rules preserved.
- All conflict resolution rules preserved.
- All existing authenticity checklist items preserved.
- All scripts (verify_citations.py, tier5_audit.py, intake_prefill.py)
  preserved.
- All cross-skill protocols preserved.
- All existing error flags preserved.

### Migration Notes

- Existing v6.4.0 users upgrading to v6.5.0 do NOT need to re-run any
  Filipino undergraduate thesis sessions. All BASE / VOICE-A / VOICE-B
  behavior is unchanged.
- VOICE-C is opt-in only. No existing Filipino undergraduate workflow
  will trigger VOICE-C loading.
- The frontmatter change (removing `version`, `compliance`,
  `citation_style`, `absorbed_skills` from YAML) is backward-compatible
  with Claude Project upload — Claude only reads `name` and `description`
  from frontmatter anyway.
- The new `examples/example.md` file does NOT replace the existing
  `examples/example-prompts.md` or `examples/example-outputs.md`. All
  three example files coexist.

---

## [6.4.0] — 2026-06-16

### Added

- references/humanization_techniques.md: Section 2.15 Naeem Turnitin
  Resistance Patterns. Six techniques extracted from Dr. Naeem Hayat PhD
  thesis (0% Turnitin confirmed): lexical repetition tolerance, clunky
  passive construction, mid-sentence citation before resolution, triple-
  chained "and" clause, tense asymmetry, exact noun-phrase repetition at
  paragraph scale.

- references/tier5_mistake_layer.md: Naeem-Derived Errors category. Five
  new mistake types from the 0% source: non-standard passive construction,
  mid-sentence citation before resolution, triple-chained "and" clause,
  hedged trailing ending, non-parallel enumeration.

- references/tier5_mistake_layer.md: Non-Pattern Rules section. Five
  explicit placement rules replacing the removed entropy system.

- references/voice_base.md: Lexical Repetition Tolerance rule under
  Student Writing Style Patterns.

- references/authenticity_checklist.md: Naeem Resistance Checks block
  with four checklist items.

### Changed

- SKILL.md: Removed entropy system (country/time/seed). Replaced with
  Mistake Placement Rules section pointing to tier5_mistake_layer.md.

- references/humanization_techniques.md: Section 2.1 expanded to Master
  Vocabulary Replacement List. Absorbs all Pass 2 targets from 2.14.
  Single canonical source for AI-signal word replacement.

- references/humanization_techniques.md: Section 2.14 Pass 2 now
  references 2.1 master list instead of maintaining a duplicate table.

### Removed

- Entropy system (fake random seed via country/time). Was generating
  pseudorandom numbers that were not actually random. Non-pattern rules
  in tier5_mistake_layer.md replace this function correctly.

- references/tier5_mistake_layer.md: Tense Slip (Mechanical Blindspots)
  removed. Duplicate of "Tense inconsistency within a paragraph" already
  in Confirmed Real-Student Errors table.

- references/tier5_mistake_layer.md: Redundant Transition removed.
  Conflicted with 2.0.1 connector rotation rule.

- First Tier 5 injection `(intentional)` marker removed from tier5 rules.
  SKILL.md output rules already prohibit this marker at rule 4. Conflict
  resolved in favor of silence.

---



### Added

- references/section_templates_ch1.md: Verified 0% Scope and Delimitation
  example (plastic container degradation detection study).
  Annotated with structural moves and ESL signature patterns.
  Inserted immediately before the Significance of the Study section.

- references/section_templates_ch1.md: Verified 0% Introduction example
  (three-paragraph block) from a spectral sensor thesis (NIR-based
  quality detection). Annotated with Problem Genealogy lenses,
  structural moves, and casual register markers. Inserted after the existing
  mango example paragraph in the Introduction Paragraph Formula section.

### Purpose

Both additions serve as anchor references when generating or
humanizing Scope and Delimitation and Introduction sections. They are NOT
templates to copy verbatim — they are structural and tonal benchmarks
demonstrating what 0% detection looks like in practice.
Tier 5 non-pattern rules govern probabilistic generation.

---

## [6.2.0] — 2026-06-16

### Added

- Section 2.14: Triple-Fire Protocol in references/humanization_techniques.md.
- Triple-Fire is a mandatory silent pre-output filter that runs on every sentence
  before it leaves the draft pass. Not a triggered repair mode.
- Three passes: Pass 1 (Voice Check), Pass 2 (Vocab Check), Pass 3 (Structure Check).
  All three must clear before a sentence is output.
- Extended AI-signal word list integrated into Pass 2 (extends section 2.1).
- Secondary use case documented: targeted repair for externally flagged sentences.
- Full worked example from DrThava (2024) showing 69% to 0% reduction using the
  same three-pass logic applied to an OTT/UTAUT-2 sentence.
- Added checklist item to Phase 4 Anti-AI Authenticity Checklist for Triple-Fire.

---

## [6.0.0] — 2026-05-27

### Architecture Change

- Refactored from monolithic SKILL.md to Progressive Disclosure Architecture.
- SKILL.md reduced to lightweight orchestrator (~6 KB vs ~47 KB original).
- All voice profiles, section templates, humanization techniques, format specs,
  and citation rules moved into lazy-loaded files under references/.
- Added metadata/ with manifest.json, routing-map.md, and dependency-notes.md.
- Added scripts/ with verify_citations.py, tier5_audit.py, intake_prefill.py.
- Added examples/ with example-prompts.md and example-outputs.md.
- Added docs/ with architecture.md and progressive-disclosure.md.
- Added Resource Routing section to SKILL.md with explicit load instructions.

### Preserved from v5.0

- All voice profiles (BASE, VOICE-A, VOICE-B) fully preserved.
- All grammar error probability maps preserved.
- All section paragraph templates preserved.
- All Tier 5 mistake injection rules preserved.
- All format compliance specs preserved.
- All APA 7th citation rules preserved.
- All section templates (Ch 1-5) preserved.
- All conflict resolution rules preserved.
- All authenticity checklist items preserved.
- All prohibited operations preserved.
- All cross-skill protocols preserved.
- All behavioral rules (output rules, error flags, meta) preserved.

---

## [5.0.0] — 2026-02-19

### Added

- Absorbed /voice-profile-a (Polished Filipino CpE voice)
- Absorbed /voice-profile-b (Developing Filipino CpE voice)
- Three-profile voice system (BASE, VOICE-A, VOICE-B)
- Voice rotation rules by chapter
- Theme Map requirement for RRL/RRS enforced
- Thesis Anchor requirement for Chapters 3-5 enforced
- Bridge sentence gate enforced (refuse "continue"/"next"/"go")
- DECONSTRUCT protocol for AI prose input
- BULLET EXPORT intake mode for /thesis-writer handoff
- Chunked generation max 250 words
- Cross-paragraph irregularity rules
- Phase 4 internal authenticity checklist

### Fixed (premortem fixes F1-F6)

- F1: Bridge sentence gate — refuses single-word continue commands
- F2: Theme Map enforcement — refuses RRL/RRS without map
- F3: Thesis Anchor enforcement — refuses Ch 3-5 without anchor
- F4: Voice rotation — refuses same profile twice in a row
- F5: DECONSTRUCT protocol — silent rebuild of AI prose input
- F6: Tier 5 clustering fix — max one mistake per paragraph, no clustering

---

## [4.0.0] — 2026-01

### Added

- Tier 5 human mistake layer (probabilistic injection)
- Sharp punch sentence rule (1 per 5 paragraphs)
- Problem genealogy architecture (9-lens structure for Introduction)
- Embodied specificity mandate (min 1 per 250 words in Intro and Results)
- Spontaneous thought patterns (4 patterns)
- Resume mode for "continue" after break

### Changed

- Soul level locked permanently at Maximum — no longer a setting

---

## [3.0.0] — 2025

### Added

- Full Chapter 2 support (RRL, RRS, Synthesis)
- APA 7th citation verification via web search
- Pre-generation summary block (Phase 1 gate)
- RDE Agenda detection
- Glossary extraction and locking
- Institutional format compliance
