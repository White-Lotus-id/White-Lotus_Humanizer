# Progressive Disclosure Architecture

## Why This Architecture Exists

Claude skills loaded as monolithic files consume the entire file's token budget
on every invocation, even when the task only needs a fraction of that content.

A 47 KB SKILL.md costs the same context space whether the student is asking for
a 200-word Objectives section or a full 800-word Introduction. That waste
accumulates over a long session and crowds out space for the actual student
content, references, and generated prose.

Progressive Disclosure solves this by:

1. Keeping the orchestrator (SKILL.md) as small as possible
2. Moving heavy reference content into separate files
3. Instructing Claude to load those files ONLY when the specific task needs them
4. Running scripts ONLY when explicitly required

---

## How Claude Uses This Architecture

### Step 1: Read SKILL.md only

On first invocation, Claude reads SKILL.md. This gives it:
- Behavioral rules and guardrails
- The intake form
- The routing table (which files to load for which tasks)
- The output rules
- The prohibited operations

It does NOT immediately load voice profiles, section templates, or
humanization technique libraries.

### Step 2: Run intake

Claude outputs the Phase 0 intake form and waits for the student's reply.
No reference files are loaded yet.

### Step 3: Load only what is needed

After the student submits the intake form, Claude reads the routing table
in SKILL.md and loads exactly the files needed for that specific task:

- One voice profile reference (the declared one)
- One section template set (for the chapter being worked on)
- Format specs and citation rules (once per session)
- Humanization techniques (for generation tasks)

### Step 4: Generate with loaded context

Claude generates the section using only the loaded references. It does not
need to hold the VOICE-B voice profile in context when it is doing a
VOICE-A task.

### Step 5: Phase 4 internal check

Claude loads the authenticity checklist internally and runs the anti-AI pass.
This reference is loaded at generation time, not at startup.

---

## Best Practices for Extending This Skill

### Adding a new voice profile

1. Create `references/voice_[name].md` following the structure of
   `voice_a.md`
2. Add an entry to `metadata/manifest.json` under `voice_profiles`
3. Add a routing rule to SKILL.md under `# Resource Routing`
4. Add the voice to the voice rotation table in `references/bu_format_specs.md`
5. Document the new profile in README.md

### Adding a new chapter or section

1. Create or update the relevant `references/section_templates_ch[N].md`
2. Add the section to the SECTION DETECTION table in SKILL.md
3. Add a routing rule to SKILL.md under `# Resource Routing`
4. Add an example prompt to `examples/example-prompts.md`

### Adding a new script

1. Create `scripts/[name].py` with full CLI argument handling
2. Add an entry to `metadata/manifest.json` under `scripts`
3. Add a routing rule to SKILL.md under `# Resource Routing`
4. Add the dependency notes to `metadata/dependency-notes.md`

### Updating compliance rules

1. Edit `references/bu_format_specs.md` for BU format changes
2. Edit `references/apa_citation_rules.md` for APA edition changes
3. Update the compliance field in `metadata/manifest.json`
4. Update the META section in SKILL.md
5. Add a CHANGELOG entry

---

## What This Architecture Does NOT Do

- It does not prevent Claude from loading all files if the task genuinely
  requires them. The routing table is a minimum-load guide, not a hard lock.
- It does not guarantee token savings if the student pastes very long drafts.
  Student input size is not controlled by this architecture.
- It does not replace the need for a fresh conversation for each major section.
  Context accumulation across many sections will still consume window space.
