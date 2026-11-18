# Proposed Codebook for Coding Lecture Transcripts

*Prepared 2026-11-18 from a full read of lecture transcripts for COMP 363. Codes are grounded in passages that actually occur; every example cites the lecture date.*

The actual prompt I gave Claude was:

>  Read the actual transcipts for comp363 and propose category codes for quantitative research analysis. The idea is to
  tag different parts of the lecture with codes like "humor", "cs history", "back in my day reflection", etc.

---

## 1. Scope at a glance

| Item | Value |
|---|---|
| Lectures scanned | **32** transcripts (2026-08-31 → 2026-11-18); **31 usable** (2026-09-04 is truncated at 364 words) |
| Total words | **141,451** (mean ≈ 4,400 per lecture; shortest full lecture ≈ 3,200) |
| Estimated speaking time | **≈ 16–18 hours** of instructor speech, at 130–150 words/minute (≈ 16.8 h at 140 wpm) |
| Class time | ≈ 26.7 hours (32 × 50-minute MWF meetings). The gap reflects whiteboard writing, student talk (not transcribed), wait time, and roll call |
| Time to complete the analysis | **≈ 4 min 46 s** wall-clock, from the request (17:35:29 UTC) to the delivered codebook (17:40:15 UTC), per the session log |
| Approximate API-equivalent cost | **≈ $3.25** (see §7) |

---

## 2. Things to know before coding

1. **The transcripts are your voice only.** The transcription agent keeps "the voice that has the loudest signal" (said in the 2026-11-02 lecture), so student talk is mostly absent. Any student-related code is inferred from how you respond. Say this in the methods section.
2. **Missing data.** 2026-09-04 stops mid-sentence at "[inaudible]". Exclude it or flag it.
3. **De-identification.** The transcripts contain full roll calls, students named inside examples ("Ben writes a $3,000 check"), and private conversations after class (condolences about a student's dog, grad-school plans, a missing assignment). Remove names before analysis, sharing, or IRB submission.
4. **No timestamps.** Use the **paragraph** as the coding unit and **its word count as a stand-in for time**. Allow more than one code per paragraph. Give plain technical explanation the default code `CONTENT`, so you can report shares of words such as "X % off pure content".
5. **The transcripts look cleaned up.** They read as lightly edited (few false starts or filler words). Don't code disfluency or hesitation.

---

## 3. Codebook

### A. Humor

| Code | Definition | Include / exclude | Example |
|---|---|---|---|
| `HUM-SELF` | Humor aimed at yourself | Excludes self-disclosure that isn't meant to be funny (→ `PERS-*`) | "I cannot count and they have me teaching computer science theory" (09-11); "best Greek professor… worst Greek professor… because I'm the only one" (08-31) |
| `HUM-TEASE` | Teasing named or present students, or colleagues | Double-code `EX-NAMED` when a student is named | "assuming that Kevin possesses a modicum of intelligence" (09-14); "your texting sucks. LOL." (11-13) |
| `HUM-TRANSGRESS` | Mock-illicit, violent or dark jokes | Includes mock disclaimers that follow such a joke | slashing tires, blackmail (09-25); "blow us to kingdom come" (11-04); electric-shock bracelets (11-09) |
| `HUM-RUNBIT` | Callback to a recurring joke | Record the bit ID as an attribute (see §4) | "take it up with Giuseppe" (08-31) |

### B. Personal narrative

| Code | Definition | Example |
|---|---|---|
| `PERS-BACKINMYDAY` | Generational contrast, older technology, "when I was your age" | phone books (08-31); 4-bit/8-bit high-school computers (09-14); Morse code "correlates 100% with… over 50" (10-12); Fortran had no shallow copies (11-06) |
| `PERS-CAREER` | Your academic or professional biography | physics PhD in Ohio, the Superconducting Super Collider and Star Wars program collapsing, the pivot to computer engineering (10-07); expert witness in an IP case (09-21); Amsterdam sabbatical (10-07) |
| `PERS-STRUGGLE` | Admitting difficulty or failure as a learner | took 3.5 years to understand MSTs (10-19); "I skipped classes, I did assignments at the last minute" (11-09); "I hated graphs" (09-28) |
| `PERS-LIFE` | Family, pets, hobbies, food, travel | deep-fried turkeys (09-23); corn-maze drone (10-02); speeding tickets (10-26); flying, dogs, bike rides (11-11); Halloween makeup (10-30) |

### C. History

| Code | Definition | Example |
|---|---|---|
| `HIST-CS` | People behind algorithms and where terms came from | Peano and 0! (08-31); Karatsuba correcting Kolmogorov (09-18); RAND naming "dynamic programming" (09-21); Borůvka 1926 (10-07); Dijkstra's coffee with his fiancée (10-30); Claude Shannon (11-09) |
| `HIST-TECH` | Wider history of science and technology | Babylonian square roots (09-02); linotype "ETAOIN SHRDLU" (10-12); the 1730 Amsterdam distance table passed around the room (10-28); the Paris kilogram/meter prototypes (11-18) |
| `HIST-MIL` | Defense and Cold War context | SDI/"Star Wars" (10-07); Chicago as a nuclear target, MCI Downers Grove (10-19); cutting Moscow–Berlin rail links (11-02) |

### D. Teaching devices

| Code | Definition | Example |
|---|---|---|
| `ANA-EVERYDAY` | Everyday analogy for a technical idea | Mexican restaurant (08-31); driving to O'Hare (09-16); ER triage (10-21); semi truck to 7-Eleven (10-21); socks → pants → shoes (10-30) |
| `ANA-LOCAL` | Chicago or Midwest place-based examples | Art Institute (recurring); interstates (10-02); Kenosha/Beloit (10-09); Springfield (10-26) |
| `DEMO-EMBODIED` | Students act out the structure, or an object is passed around | factorial "bucket brigade" (08-31); desks as graph components (10-07); "who's the oldest?" (10-14) |
| `EX-NAMED` | A real student named inside a hypothetical | "Gabriel drops the class" (09-23); loans to Ezra and Gabriel (11-02) |
| `DEV-MAGIC` | The "assume the solution is handed to us" framing | "divinely provisioned solution" (09-11); "somehow that answer appears before us" (09-21) |
| `APP-REAL` | Real-world applications and industry cases | DNA/BLAST (09-11); 401(k) investing (09-21); Google PageRank (09-30); CSX rolling stock and stranded Southwest pilots (11-04); aviation and surgical checklists (10-30) |

### E. Teaching and metacognition

| Code | Definition | Example |
|---|---|---|
| `PED-STUDY` | Study-habit advice | "a notebook full of blank pages and at least 3 pencils" (09-11); "do 24 cells by hand" (09-25) |
| `PED-HELPSEEK` | Encouraging questions and help-seeking | "more important… that you learn how to ask questions" (10-16); "safest… most forgiving space to ask" (10-12) |
| `PED-ERROR` | Live mistakes, uncertainty, corrections | homework posted for 2027 (09-28); MST sum that doesn't reach 31 (10-07); "I don't know… let me look it up" (11-04); "thank you for making a good mistake" (11-06) |
| `PED-REFLECT` | Reflecting aloud on your own teaching | "don't blame Huffman, blame me" (10-16); "that's why I don't do PowerPoint for these topics" (09-21) |
| `CURR-LINK` | References to other courses or colleagues | COMP 163/170/271/272/264/371; Bill, Karima, Läufer |
| `CURR-CRITIQUE` | Criticism of textbooks or curriculum norms | master theorem "all about marketing" (09-18); Johnsonbaugh's book (09-21); O(V+E) "truth in advertising" (09-30) |

### F. Disciplinary identity and opinion

| Code | Definition | Example |
|---|---|---|
| `DISC-IDENT` | Computer science vs. math vs. physics identity | "never get into a fight with a mathematician" (09-11); "started by a bunch of physicists… little respect for mathematical rigor" (09-16); "the essay is the code" (11-11) |
| `DISC-TERM` | Mocking computer-science vocabulary | "forest… not… arboretum" (10-14); "our ability to name things is really whacked" (10-21); "residual graph… justify that $120,000 salary" (11-06) |
| `OPINION-TECH` | Opinions on languages, style or tools | Python's "we're all adults" vs. Java's `final` (09-28, 10-09); multiple returns (11-09); disjoint sets "a very cold day in hell" (11-09) |
| `MAXIM` | Catchphrases | "every problem can be solved with an array"; "prove me wrong"; "trust me — famous last words" |

### G. Career

| Code | Definition | Example |
|---|---|---|
| `CAREER-INTERVIEW` | Technical interview advice | "what is a graph?" (09-28); fast/slow-pointer loop detection (10-26); "the most essential data structure for DFS" (10-14) |
| `CAREER-PROF` | Workplace readiness, grad school, recommendation letters | "the rest of the team sees you as dead weight" (10-12); "not about what you know but about who you are" (11-06) |

### H. AI

| Code | Definition | Example |
|---|---|---|
| `AI-INSTRUSE` | Your own AI use, disclosed in class | grader agents (10-07, 11-09); weekly syllabus-check emails (11-02); Inquisitor oral-exam agent and panel-prep prompt (11-11) |
| `AI-POLICY` | Rules and guidance on students' AI use | "don't ask Claude… I cannot enforce it" (10-12); "'solve it for me'… that's hiring someone" (11-06) |
| `AI-DEMO` | Live AI demonstrations | Borůvka in the chatbot (11-09); CLI and Codespaces (11-11); a student driving Claude Code (11-13) |
| `AI-LEARN` | Effects of AI on learning and skill | cognitive offloading (10-07); "illusion of understanding" (11-13); "syntax is no longer a pedagogical priority" (11-09) |
| `AI-SOCIETY` | Labor, higher education, democracy | "if you're an accountant, you're done" (10-07); "the middle class disappears… no tax base" (11-02); Nadella's 80% claim (11-11) |
| `AI-ETHICS` | Privacy and data ethics around AI | transcription drops students' voices for FERPA (11-02); only first names sent to Claude (11-11); scraping Wikipedia vs. Gutenberg (11-13) |

### I. Classroom, relationships and institution

| Code | Definition | Example |
|---|---|---|
| `RAPPORT` | Small talk | fall-break plans (10-02); lunch for this weather (09-30) |
| `CARE` | Wellbeing and pastoral care | "come to me first. Don't go on Twitter" (10-26); condolences after class (10-23); workload across courses (11-09) |
| `STUDENT-VOICE` | Asking students to shape the course or institution | choosing the remaining weeks (10-28, 10-30); Thanksgiving-Monday vote (11-06); "what do you want the other professors to hear?" (11-09) |
| `INST-CRITIQUE` | Commentary on higher education or the institution | more than four courses is "borderline fraud" (11-09); "the desk that goes up and down… someone got promoted" (11-06) |
| `CAMPUS` | The physical setting | far-away whiteboard (08-31); dead markers (10-09); Mundelein elevators (recurring); an 82° room (11-18) |
| `REC-META` | Remarks about the recording or the AI listening | "for the record, because these things are recorded, that was a joke" (09-18); "Claude will be wondering on the recording… why is he so quiet" (10-28) |
| `PHIL` | Philosophical or existential asides | AI as the next evolutionary step (08-31); "may you live in interesting times" (10-07); P = NP would make "creativity mechanical" (11-18) |
| `LOGISTICS` | Assignments, schedule, roll call, Sakai | — |
| `CONTENT` | Default: technical exposition with none of the above | — |

---

## 4. Running bits to track with `HUM-RUNBIT`

| Bit ID | Lectures |
|---|---|
| `heist` (Art Institute / Louvre) | 08-31, 09-11, 09-21, 09-23, 09-25, 11-18 |
| `elevators` (Mundelein) | 09-14, 10-19, 10-28, 11-02, 11-04, 11-11, 11-13 |
| `bribery` | 09-16, 09-18, 09-21, 09-28, 10-23 |
| `chicago-nuke` | 09-02, 10-19, 10-28, 11-02, 11-04 |
| `heaven-purgatory-hell` | 09-02, 09-18, 09-30 |
| `peano` | 08-31, 09-11, 09-21 |
| `springfield-rice` | 10-26, 10-28, 10-30 |
| `prove-me-wrong` | 08-31, 09-11, 10-26, 10-30 |
| `array-maxim` | 10-12, 10-14, 10-21, 10-23 |
| `moon-landing-staged` | 09-02, 09-14 |
| `lottery-7eleven` | 08-31, 10-09 |
| `famous-last-words` | 10-26, 11-06 |
| `immortality-killed` (P = NP) | 11-18 (twice) |

---

## 5. Suggested pilot and reliability plan

1. **Pilot.** Have two coders independently code 4 lectures that differ in character: **09-21** (dynamic programming, humor-heavy), **10-07** (long AI/career reflection), **10-28** (artifact and Bellman-Ford), and **11-09** (AI demo and higher-ed critique).
2. **Check agreement.** Compute Cohen's κ per code, and merge or redefine codes below κ ≈ 0.6. Expect confusion between `HIST-CS`/`HIST-TECH`, `PED-ERROR`/`PED-REFLECT`, and `HUM-TRANSGRESS`/`HUM-RUNBIT`.
3. **Code questions as episodes.** Questions to the class are constant; only code extended exchanges.
4. **Measures.** For each lecture: word share per code family; the number of distinct codes; and the time between a code's first appearance and its callbacks (from `HUM-RUNBIT`).

## 6. One finding worth testing

The code mix clearly changes across the term:
- **Weeks 1–6** are dominated by `HUM-*`, `ANA-*` and `HIST-*` alongside content.
- **10-07 onward** brings sustained `AI-*`, `CAREER-*` and `PHIL`.
- **11-09 to 11-13** are almost entirely `AI-DEMO`, `AI-POLICY` and `AI-INSTRUSE`.

A plot of code-family word share over time should show this clearly.

---

## 7. How the time and cost were measured

**Time.** From the Claude Code session log (`~/.claude/projects/…/0ffe35a4-….jsonl`): the request was received at 17:35:29 UTC and the codebook delivered at 17:40:15 UTC, about 4 min 46 s of wall-clock time. Producing this report took a few more minutes.

**Tokens.** These are the usage fields Claude Code logged for each model response (17 responses) up to the start of this report request:

| Category | Tokens | Rate (Claude Opus 5.5, API list price) | Cost |
|---|---|---|---|
| Uncached input | 36 | $4.00 / MTok | ≈ $0.00 |
| Cache writes (1-hour TTL) | 284,686 | $8.00 / MTok (2× input) | $2.28 |
| Cache reads | 2,304,033 | $0.20 / MTok | $0.46 |
| Output (including reasoning) | 24,395 | $20.00 / MTok | $0.49 |
| **Total** | **≈ 2.61 M** | | **≈ $3.23** |

Caveats:
- With a 5-minute cache TTL ($5/MTok for writes) the total would be about **$2.37**.
- Generating this report adds a few cents.
- These are API-equivalent figures. On a Claude subscription the work is covered by the plan, not billed per token.
- The ~190k tokens of transcript text were read once. Almost all the rest is cache reads of the growing conversation, which is why the cost stays low despite 2.3 M tokens read.
