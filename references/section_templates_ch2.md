# Section Templates — Chapter 2

Templates for all Chapter 2 sections of a Institutional thesis.
Voice for all Chapter 2 content: VOICE-A only.

---

## Chapter 2 Voice Rule

All sections in Chapter 2 use VOICE-A voice only.
No substitutions. See references/voice_a.md.

---

## Review of Related Literature (RRL)

**Target**: 600-1,000 words
**Format**: Thematic, no subtitles, one paragraph per source (3-4 sentences MAX),
2020+ sources preferred

**Opening (exact):**
"This chapter presents the review of related literature and studies relevant to
the proposed system."

### RRL Paragraph Formula (MANDATORY — confirmed from 0% samples)

Every RRL paragraph follows this 4-step sequence exactly. No exceptions.
Maximum 3-4 sentences per source. Never write a 5-sentence RRL paragraph.

```
STEP 1 — Citation opener (sentence 1):
[Author et al. (Year)] + past tense verb + what they did.
Example: "Göhler et al. (2023) detailed the creation of in-ovo sexing methods
to fix the ethical and financial issues caused by culling male chicks."

STEP 2 — Zoom in (sentence 2):
"In this case, [what the study specifically focused on] because [reason],
which means [implication]."
Example: "In this case, the authors prefer non-invasive systems since they
do not harm the embryo, which means the eggs can still hatch after
sex is identified."

STEP 3 — Finding (sentence 3):
"[Also/Since/The Researcher found that] [result], which means [consequence]."
Example: "Also, using optical imaging and machine learning is becoming
more common because these tools are easy to scale up for actual
hatchery use, which means they work well for commercial operations."

STEP 4 — Relevance or gap (sentence 4, optional):
"Because of that, [why this matters to the current study OR what gap remains]."
Example: "Because of that, their work supports looking into computer
vision systems that can classify embryo sex through image features."
```

**Connector distribution inside RRL paragraphs:**
- Sentence 1: Author name as subject (no connector)
- Sentence 2: "In this case,"
- Sentence 3: "Also," OR "Since [clause],"
- Sentence 4: "Because of that,"

Never open two consecutive RRL paragraphs with the same connector.

**Theme Map requirement:**
Request from student before generating any RRL chunk:
```
Theme 1: [theme name] — [Author(s)]
Theme 2: [theme name] — [Author(s)]
```
Do not generate without confirmed Theme Map.

---

## Review of Related Studies (RRS)

**Target**: 400-700 words
**Format**: Past-tense, finding-focused, one paragraph per study (3-4 sentences MAX)

### RRS Paragraph Formula (MANDATORY — confirmed from 0% samples)

```
STEP 1 — Study intro (sentence 1):
[Author et al. (Year)] + past tense verb + method or approach.
Example: "Liu et al. (2020) used high-resolution infrared thermography
to monitor the thermal decay of seeds in order to measure their vigor."

STEP 2 — Finding (sentence 2):
"The researchers [observed/noted/found] that [result], which means [implication]."
Example: "The researchers note that the study showed how thermal patterns
represent internal seed conditions, which means there is a strong link
between temperature decay and the vigor of Oryza sativa."

STEP 3 — Limitation or contrast (sentence 3):
"Also, [limitation], which means [gap that follows from it]."
OR
"In this case, [additional observation] because [reason]."
Example: "Also, that specific study focused on building a regression
model and did not use machine learning classification for automated
sorting, which means the actual sorting process was not addressed."

STEP 4 — Gap connection (sentence 4):
"Because of that, the researchers [see/find/believe] [relevance or
opportunity] in order to [purpose of current study]."
Example: "Because of that, the researchers see an opportunity to expand
on this by integrating classification mechanisms that can handle the
actual sorting process."
```

**Theme Map requirement:**
Same rule as RRL. Do not generate without confirmed Theme Map.

---

## Synthesis of Reviewed Literature and Studies and Gap Bridged by the Study

**Section title (exact):**
"Synthesis of Reviewed Literature and Studies and Gap Bridged by the Study"

**Target**: 200-300 words

**Template (VOICE-A SYNTHESIS):**
```
The researchers recognizes/recognize that [theme] is [important] because
[reason] (Citation).
[Follow-on supporting literature, 1 sentence].
[Because of that, the researchers find that [methodology gap]].
[Transition to solution with "the [field] is shifting toward"].
[Specific technology statement with "in order to" purpose clause].
[Also, [additional component of solution]].
[Closing: "Basically, the researchers want to [goal] in order to [broader purpose]"].
```

**Connector rule for Synthesis:**
Must use at least 4 different connectors from the 5-Connector Rotation
(see humanization_techniques.md 2.0.1) across the synthesis paragraph block.

**Last sentence rule:**
The final sentence must name the gap this study bridges — not "will bridge."
NOT: "This gap will be bridged by this study."
YES: "That gap is what this study addresses."

**Soul note**: Soul peaks in Synthesis. "What the researchers found when they
reviewed the literature was a consistent absence of..."
