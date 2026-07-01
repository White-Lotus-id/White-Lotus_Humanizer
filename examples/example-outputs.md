# Example Outputs

Annotated output examples demonstrating correct skill behavior.

---

## Example 1: Pre-Generation Summary Block

```
[PRE-GENERATION SUMMARY]

Section: Introduction / Background of the Study
Category: Development
Voice Target: VOICE-A
RDE Agenda: Industry-Energy-Tech — SDGs 4, 5, 8, 9, 10, 11, 16, 17
Soul Level: Maximum (locked)

GENERATING: INTRODUCTION

REFERENCES (5):
1. Santos, J. R., & Cruz, M. A. (2022). Power quality in Philippine distribution
   networks. Journal of Electrical Engineering Philippines, 14(2), 45-58.
   https://doi.org/10.xxxx/xxxx
   APA: OK
   Verification: [NEEDS SEARCH — will verify before generation]
   Claim Match: Pending verification

2. ALECO. (2023). Annual service reliability report. Albay Electric Cooperative.
   APA: [CITATION FORMAT CORRECTED — no URL/DOI added; organizational author
   format OK]
   Verification: [UNVERIFIABLE — internal report, no public abstract]
   Claim Match: OK — used as institutional data source only

3. Dela Cruz, P. B. (2021). Voltage monitoring systems for rural electrification.
   Philippine Institute of Electrical Engineers Journal, 8(1), 12-24.
   APA: OK
   Verification: [NEEDS SEARCH]
   Claim Match: Pending

4. Reyes, L. C., & Torres, A. M. (2020). Household appliance damage from
   undervoltage events in Bicol Region. Energy Research Philippines, 5(3), 88-102.
   APA: OK
   Verification: [NEEDS SEARCH]
   Claim Match: Pending

5. Garcia, R. F. (2023). Smart home power monitoring solutions. IEEE Access,
   11, 24531-24545. https://doi.org/10.1109/ACCESS.2023.xxxxx
   APA: OK
   Verification: [VERIFIED VIA SEARCH]
   Claim Match: OK

GLOSSARY (4 terms locked):
| Term | Definition |
|---|---|
| Brownout | A prolonged reduction in voltage supply below the acceptable threshold, as experienced in ALECO service territory, causing appliance damage and service interruption |
| Undervoltage | Voltage level that drops below 0.90 per unit of nominal supply voltage, as defined by ERC standards |
| ALECO | Albay Electric Cooperative, the distribution utility serving Polangui and surrounding municipalities |
| PZEM-004T | A power monitoring module used in this study to measure voltage, current, and power factor in real time |

FLAGGED FOR REVIEW:
- References 1, 3, 4 pending web search verification. Proceeding with
  [UNVERIFIABLE] flag if abstracts are not found.
- ALECO internal report: cite as gray literature. Will flag if claim match
  cannot be verified.

Reply: [CONFIRMED: Generate Introduction]
Or send corrections.
```

---

## Example 2: Generated Introduction Chunk (VOICE-A)

```
[SECTION: Introduction — CHUNK 1 OF 3]

Electricity is something that most households in the Philippines consider a
basic part of daily life, which means its absence or sudden instability is
not just an inconvenience but a real economic problem (Santos & Cruz, 2022).
In Albay, this problem is well-known. Families who live inside the ALECO
service territory have become so used to voltage fluctuations that they have
a word for it already: brownout. Because of that, the term does not just
mean a power interruption, it also means the steady hum of appliances
suddenly going quiet, the refrigerator warming up, and the water pump
failing to start in the morning (Reyes & Torres, 2020).

The researchers observe that the cause of these events is not one single
failure but a combination of aging infrastructure, rising household demand,
and the seasonal battering of Bicol's typhoon corridor (ALECO, 2023). At the
moment, the distribution network serving Polangui was not originally
designed to carry the load that modern households put on it, which means
that even without a storm, voltage levels can drop below the threshold that
appliances need in order to function safely (Dela Cruz, 2021). This is
because the cooperative has not been able to expand its infrastructure at
the same pace that residential connections have grown, and that gap is not
abstract (intentional) — a family with a chest freezer full of a week's
worth of fish knows exactly what it costs when the voltage drops too long.

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

---

## Annotation

The example above shows:

1. `(intentional)` marker on first Tier 5 injection (vague pronoun + abstract
   claim). Only one marker in the entire output.
2. VOICE-A voice: "Because of that," "which means," "in order to," "The
   researchers observe that."
3. Embodied specificity: the refrigerator, water pump, chest freezer, and ALECO
   as place name.
4. Problem genealogy in progress: everyday problem (para 1), infrastructure
   cause (para 2).
5. No em dashes anywhere.
6. No semicolons.
7. "the researchers" (lowercase plural) as primary self-reference.
8. Chunk ends with bridge sentence request, not "continue."

---

## Example 3: Correct Bridge Sentence Refusal

Student types: "continue"

```
Please write your own bridge sentence before I continue. A single word or
"continue" will not work here.

Example of an acceptable bridge sentence:
"Existing solutions for voltage monitoring have been developed in other
countries but they often require expensive equipment that most households
in Polangui cannot afford."

Your bridge sentence:
```
