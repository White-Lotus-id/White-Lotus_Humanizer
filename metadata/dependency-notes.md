# Dependency Notes

---

## Python Scripts

### scripts/verify_citations.py

- **Python version**: 3.9+
- **Dependencies**: None (standard library only — `re`, `argparse`, `sys`)
- **Usage**: `python scripts/verify_citations.py --input FILE`
- **Notes**: Does heuristic APA 7th format checks only. Does not perform web
  search. Web search for abstract verification must be done manually or via
  Claude's web search tool during Phase 0.2.

### scripts/tier5_audit.py

- **Python version**: 3.9+
- **Dependencies**: None (standard library only — `re`, `argparse`, `sys`,
  `collections`)
- **Usage**: `python scripts/tier5_audit.py --input FILE`
- **Notes**: Heuristic pattern scanner. Will produce false positives on some
  authentic student writing. Use as a supplement to the internal Phase 4 pass,
  not as a replacement.

### scripts/intake_prefill.py

- **Python version**: 3.9+
- **Dependencies**: None (standard library only — `argparse`, `sys`, `textwrap`)
- **Usage**: `python scripts/intake_prefill.py --title "TITLE" --section "SECTION"`
- **Notes**: Produces a filled intake block. Student must still review and
  correct all pre-filled fields before confirming.

---

## Claude Project Requirements

This skill requires no external API keys or third-party services.

When used in Claude Projects:
- Upload SKILL.md as the project instruction file.
- Upload all files under references/ as project knowledge files.
- Scripts under scripts/ are available for Claude to invoke via bash in
  computer-use environments. In standard Claude Projects, they serve as
  reference documentation.
- No npm or pip packages required.

---

## Optional Runtime Environment

For full script execution:
- Python 3.9 or higher
- No virtual environment required
- No requirements.txt needed (all standard library)

---

## Co-loading Requirements (v6.5.0)

### voice_c.md + voice_c_style_essence.md

These two files are **co-loaded** whenever VOICE-C is declared. Neither file
should be loaded alone:
- `voice_c.md` is the full forensic profile (identity, register, ESL markers,
  paragraph structure, citation conventions, tone by section, what NOT to do).
- `voice_c_style_essence.md` is the operational quick-reference (Three Rules of
  Mimicry, ESL marker density targets, connector inventory, per-hypothesis
  template, fake abstract example, cheat sheet).

The essence file references the full file and vice versa. Loading only one
produces incomplete guidance.

### voice_c.md + section_templates_ch4_ch5.md (Discussion only)

When VOICE-C Discussion is requested, both files load together. The section
template provides the structural skeleton; `voice_c.md` provides the
5-move per-hypothesis template that overrides the generic Filipino
undergraduate Discussion structure.

---

## File Size Reference

| File | Approximate Size | Load Priority |
|---|---|---|
| SKILL.md | ~14 KB | Always (orchestrator) |
| references/voice_base.md | ~6 KB | Lazy — BASE tasks |
| references/voice_a.md | ~7 KB | Lazy — VOICE-A tasks |
| references/voice_b.md | ~7 KB | Lazy — VOICE-B tasks |
| references/voice_c.md | ~14 KB | Lazy — VOICE-C tasks (co-loaded with voice_c_style_essence.md) |
| references/voice_c_style_essence.md | ~9 KB | Lazy — VOICE-C tasks (co-loaded with voice_c.md) |
| references/humanization_techniques.md | ~28 KB | Lazy — all generation |
| references/tier5_mistake_layer.md | ~6 KB | Lazy — on demand |
| references/bu_format_specs.md | ~3 KB | Lazy — every Filipino undergraduate session |
| references/apa_citation_rules.md | ~2 KB | Lazy — every session |
| references/section_templates_ch1.md | ~15 KB | Lazy — Ch 1 tasks |
| references/section_templates_ch2.md | ~5 KB | Lazy — Ch 2 tasks |
| references/section_templates_ch3.md | ~3 KB | Lazy — Ch 3 tasks |
| references/section_templates_ch4_ch5.md | ~3 KB | Lazy — Ch 4/5 tasks |
| references/conflict_resolution.md | ~3 KB | Lazy — edge cases |
| references/authenticity_checklist.md | ~4 KB | Lazy — Phase 4 internal |
| examples/example.md | ~14 KB | Lazy — reference / teaching |
| examples/example-prompts.md | ~5 KB | Lazy — reference |
| examples/example-outputs.md | ~6 KB | Lazy — reference |

**Estimated context usage (Filipino undergraduate typical session):** 20-30 KB
  (SKILL.md + voice profile + 2-3 lazy references).
**Estimated context usage (VOICE-C typical session):** 40-55 KB
  (SKILL.md + voice_c.md + voice_c_style_essence.md + section template +
  humanization_techniques + apa_citation_rules).
**Savings vs monolithic SKILL.md:** ~60-70% token reduction for typical tasks.
