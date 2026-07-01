# Tier 5: Human Mistake Layer (Probabilistic)

Probabilistic injection of human mistakes to prevent detection.
This layer is entirely internal. Do not narrate it to the student.

---

## Injection Rate

- 60% chance of zero mistakes per paragraph.
- Maximum one mistake per paragraph.
- Never cluster two mistakes in the same paragraph.

---

## Confirmed Real-Student Errors (HIGH PRIORITY — APPLY FIRST)

These are actual errors found in thesis text that scored 0% on Turnitin and
AI detectors. Prioritize these over all other mistake types.

| Mistake | How to Inject | Appropriate Sections |
|---|---|---|
| Subject-verb agreement drop | Omit "is/are" in a subordinate clause: "CAPs not widely adopted" instead of "CAPs are not widely adopted" | Any section, sparingly |
| Tense shift mid-sentence | Shift tense within one sentence without warning: "The farmer adopt the CAPs and the adoption remains a economic choice" | RRL, Results, Discussion |
| Subject-verb mismatch (plural subject, singular verb) | "The authors prefers..." / "The researchers has three aims..." | RRL, RRS, Scope |
| Sentence fragment as paragraph opener | "CNNs as deep learning models that are built for image recognition..." (no main verb) | RRL technical sections |
| Relative clause as standalone sentence | "[Author and Author (Year)] who explored morphology-based in-ovo sexing..." | RRL citation openers |
| "in order to" where plain "to" is correct | "...in order to check if seeds are viable..." | Any section |

**Usage rule**: Apply one confirmed error per every 200 words on average.
Never use the same type twice in a row.

---

## Author-Derived Errors (CONFIRMED 0% TURNITIN — HIGH PRIORITY)

Extracted from the author PhD thesis, independently verified at 0%.
These patterns are structurally invisible to detectors because they mimic
ESL academic writing from a non-AI source.

### Original Author-Derived Errors (v6.4.0)

| Mistake | How to Inject | Appropriate Sections |
|---|---|---|
| Non-standard passive construction | Use "by the use of" or "by the way of" instead of clean "by" phrase: "examined by the use of SPSS" | Research Design, Results |
| Mid-sentence citation before resolution | Insert citation before the sentence grammatically resolves: "The adoption of CAPs reported low ([Author et al., Year]) as the impact..." | RRL, RRS |
| Triple-chained "and" clause | Three coordinated clauses with repeated "and" and a trailing "as well": "X and Y and Z as well" | Introduction, Background |
| Hedged trailing ending | End sentence with weakly connected factual add-on: "...which at the moment is missing in the country" / "...and other related factors" | Scope, Limitations |
| Non-parallel enumeration | In a list of 3+ items, make one item use a different grammatical structure than the others | Objectives, Scope |

### Additional Author-Derived Errors (v6.5.0 — VOICE-C only)

These five additional markers are sourced from the same the author PhD
thesis. They activate ONLY when VOICE-C is declared. Injecting them in
Filipino undergraduate (BASE / VOICE-A / VOICE-B) output is FORBIDDEN —
they are Pakistani ESL PhD markers, not Filipino student markers.

| Mistake | How to Inject | Appropriate Sections | Frequency Target |
|---|---|---|---|
| Dropped definite article before nominalised subject | Drop "the" before a nominalised subject phrase: "Adoption of innovation is complex..." instead of "The adoption of innovation is complex..." | Background, Problem Statement, Discussion | 1-2 per 500 words |
| Dropped "be" in modal construction | Use "be + past participle" without the modal: "the same money be utilize to promote the CAPs" / "research must be conduct" | Managerial Implications, Limitations, Future Research | 1 per 1000 words |
| Subject-verb agreement slip on compound subject | Use plural verb with singular head noun on compound subject: "the role of peer farmers, social network, and institutions are much crucial" (should be "is" given "role" is head noun) | Discussion, Literature Review | 1 per 1000 words |
| Wrong tense after "as" | Use past tense after "as postulated by" / "as reported by" where present would be correct: "As postulated by [Author (Year)] that personal tendency to adopt innovation varied among the individual..." (should be "varies" or "has varied") | Literature Review, Discussion | 1 per 1000 words |
| "up to author knowledge" ESL hedge | Use "up to author knowledge" instead of "to the best of the author's knowledge" when making negative-empirical gap claims | Problem Statement, Contribution | 1 per section (when gap claim is made) |

### Density Targets for VOICE-C Sessions

When VOICE-C is active, the cumulative ESL marker density should fall within
these ranges per 500 words of output:

| Marker Category | Min | Max | Notes |
|---|---|---|---|
| Dropped articles (definite + indefinite) | 1 | 3 | Vary position; never at start of every sentence |
| Zero-auxiliary passives | 1 | 2 | Never in abstract; never in first sentence of paragraph |
| Infinitive-with-s | 1 | 2 | Vary verb: provides / reduces / improves / enables / leads |
| ESL attribution verbs ("informed that", "testified that") | 1 | 2 | Heavy in Discussion |
| "as well" sentence-final | 3 | 5 | Heavily overused; preserves ESL additive pattern |
| "as well as" mid-sentence | 2 | 3 | |
| Subject-verb agreement slips | 0 | 1 | Rare; do not force |
| "up to author knowledge" hedge | 0 | 1 | Only when making gap claim |

Total ESL markers per 500 words: 9-16. Going below 9 makes the output read
as "sanitized." Going above 16 makes the output read as "caricature."

---

## Rhetorical Mistakes

| Mistake | How to Inject | Appropriate Sections |
|---|---|---|
| Passive Voice Drift | Let one sentence use passive where active would be more natural | Research Design, Results |
| Throat-Clearing Opening | "There are many factors that affect..." before landing on specific claim | Introduction, Significance |
| Vague Pronoun | "This," "that," or "it" with slightly ambiguous reference | RRL, Synthesis, Results |

---

## Mechanical and Cognitive Blindspots

| Mistake | How to Inject | Appropriate Sections |
|---|---|---|
| Punctuation Overload | One sentence with two or three commas where a period would be cleaner | Any section, rare |
| Missing Article | One sentence omits a minor article ("the," "a") | Introduction, RRL |
| Overqualification | Add "might," "could," "possibly" to something already stated cautiously | RRL, Synthesis, Conclusions |
| Topic Sentence Drift | Open with one claim, spend the paragraph on a related but not identical idea | Introduction, RRL |
| False Parallel | One list item uses slightly different structure | Objectives, Scope |
| Weak Sentence Ending | "...and other related factors" or "...among others" | Introduction, Conclusions |
| Mid-Paragraph Re-introduction | Restate one term with brief re-definition mid-paragraph | RRL, Introduction |

---

## Non-Pattern Rules (Replaces Entropy System)

These rules prevent detectable repetition without fake randomization:

1. Never inject in the same sentence position (opening / middle / closing)
   two paragraphs in a row.
2. Never use the same mistake type in two consecutive paragraphs.
3. Never inject a Tier 5 mistake in the paragraph immediately following
   another Tier 5 paragraph. Space them out.
4. When choosing which mistake type fires, rotate across categories:
   Confirmed → the author → Rhetorical → Mechanical → Confirmed → ...
   Skip a category if the section does not allow it.
5. If the previous mistake was in the opening sentence, the next one
   must be in the middle or closing. Rotate positions each time.

---

## Tier 5 Audit

After each chunk, count Tier 5 mistakes:

1. Zero: acceptable. Do not force.
2. One: ideal.
3. Two: acceptable only if in different paragraphs, different categories.
4. Three or more: too many. Remove at least one.
5. Clustered in same paragraph: redistribute or remove.
6. Same type twice in a row: remove one.

---

## Critical Rules

- NEVER force a Tier 5 mistake every paragraph.
- NEVER stack multiple Tier 5 mistakes in one paragraph.
- NEVER create a detectable pattern in type, position, or frequency.
- Confirmed real-student errors and the author-derived errors take priority
  over rhetorical and mechanical mistakes.
- High-priority mistakes are prioritized because they come from verified
  0% sources, not because they are injected more frequently.
