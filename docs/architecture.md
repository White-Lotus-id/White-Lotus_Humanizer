# Architecture

## Overview

The humanize skill uses a **Progressive Disclosure Architecture** — a modular,
lazy-loading design that keeps the primary SKILL.md lightweight while storing
heavy reference material in separate files loaded only when needed.

---

## Components

```
humanize/
├── SKILL.md                    <- Orchestrator (always loaded)
├── references/                 <- Heavy knowledge (lazy-loaded)
├── scripts/                    <- Executable utilities (run on demand)
├── metadata/                   <- Manifest, routing, dependency info
├── examples/                   <- Annotated usage examples
└── docs/                       <- Developer documentation
```

---

## Orchestration Flow

```
Student Request
      |
      v
SKILL.md (orchestrator)
  |-- Run intake form (Phase 0)
  |-- Load bu_format_specs.md
  |-- Load apa_citation_rules.md
  |-- Output PRE-GENERATION SUMMARY (Phase 1)
  |-- Wait for confirmation
  |
  v
On [CONFIRMED]:
  |-- Load voice profile reference (one only)
  |-- Load section template reference (one chapter set)
  |-- Load humanization_techniques.md
  |-- Generate chunk (max 250 words)
  |-- Request bridge sentence
  |
  v
After chunk:
  |-- Load authenticity_checklist.md (internal Phase 4)
  |-- Run Tier 5 audit (internal)
  |-- Output [CHUNK COMPLETE] with bridge sentence request
  |
  v
Repeat per chunk until section complete.
Output [✓ humanized]
```

---

## Token Optimization Strategy

The original monolithic SKILL.md was approximately 47 KB. Loading it in full
for every task consumed significant context window space even when the student
only needed one section from one chapter.

This architecture reduces that by:

1. **Always-loaded layer** — SKILL.md contains only orchestration logic,
   behavioral rules, guardrails, intake form, and resource routing instructions.
   Approximately 6 KB.

2. **Lazy-loaded references** — heavy voice profiles, section templates,
   humanization technique libraries, and format specs are only loaded when
   the specific task requires them.

3. **Per-session minimum** — a typical single-section generation session
   loads SKILL.md plus 4-6 reference files, totaling approximately 14-20 KB
   vs the original ~47 KB monolithic load.

4. **Script-gated utilities** — citation verification and Tier 5 audits only
   run when explicitly needed, not on every invocation.

---

## Reference Loading Rules

Claude follows the routing map in `metadata/routing-map.md` to determine
which files to load. The routing table maps:

- Declared voice target → voice profile file
- Section requested → section template file (by chapter)
- Task type → utility references (format specs, citation rules)
- Edge case encountered → conflict resolution file

Files not relevant to the current task are never loaded.

---

## Script Design

Scripts are standalone Python utilities with no external dependencies (standard
library only). They are designed to be:

- Called from command line
- Called via Claude's bash tool in computer-use environments
- Read as reference documentation in standard Claude Projects

Each script outputs structured plain text reports, not JSON, to make them
readable in both terminal and chat contexts.

---

## Cross-Skill Boundary

This skill absorbs two previously separate skills:
- `/rice-thermography-author-mimic`
- `/voice-b-author-mimic`

Both voice profiles are stored as separate lazy-loaded references rather than
being embedded in the orchestrator. This allows them to be loaded independently
and prevents unnecessary context consumption when only one voice profile is
needed.

The cross-skill handoff from `/thesis-writer` is handled by the DECONSTRUCT
protocol defined in SKILL.md. No additional file loading is required for this.
