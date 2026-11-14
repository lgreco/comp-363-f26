# Week 12 (Optional Project) — Specify, Then Build: An Autocomplete with Claude

Optional. This is not a prompt-engineering course, so nothing here is required. A few of you asked how to work with an agent beyond the chat box, and this is the answer in practice.

The project has six stages. Stage 1, the slow but correct baseline, is what we started in class on Friday. Stages 2 to 6 each replace part of it with a better algorithm. We won't meet in class for any of them: you can take the project as far as you like on your own, and I'm happy to work through any stage with you one on one. Email me to set up a time.

Stage 1 is described in [`prompt_engineering.md`](./prompt_engineering.md). Read that first. It was written for a class session, so where it says "today" or "next time", read "stage 1" and "stage 2". This page covers what we did in class this week, what you need to get started, the later stages, and how to turn the work in.

## This week in class

**Monday 11/9: the five-minute prompt.** We asked Claude, in the chat window, to "write Python code for Borůvka's method", as if the deadline were five minutes away. The code ran, and it was obviously not the code of a student in this course: extensive unit tests nobody asked for, no comments, several `return`s per function, a disjoint-set object we never discussed, Pythonic multiple assignment, `continue`. Pasting in the actual assignment specification improved it, but it still ranked the edges, which is Kruskal's algorithm, not Borůvka's.

**Wednesday 11/11: context changes everything.** The same request from Claude Code, run inside the course repository, came back exactly as we wanted, because the agent had read the notes and the earlier solutions first. Then we looked at a real **operational prompt**: the Markdown file I wrote to prepare for the faculty panel on AI. It covered who I am, the audience, the constraints, the sources, the core message, and the hard questions I expected. That took about an hour and a half to write, and it replaced days of work. The value I add is the prompt, not the output, and reviewing the output is not optional.

**Friday 11/13: you drove.** One of you ran Claude Code on the big screen while the rest of us, playing the team, questioned "the boss" (me) about what an autocomplete system is supposed to do. Then we wrote a specification before writing any code. Along the way:

- An autocomplete takes a **prefix** and a number **k**, and returns the k most frequent words that start with that prefix. Each new letter narrows the candidates and the ranking is redone.
- **Binary search, as we know it, answers a different question.** It tells you whether a whole word is in the list. But `pre` may not be a word, and we want every word that *starts* with it. Whether binary search can still help is worth thinking about when you reach the handout's last question.
- **Ask before you build.** Building our own frequency table from Project Gutenberg would have meant scraping, a literary bias, and stemming problems (*child*/*children*). We checked with the boss and used an existing list instead: Peter Norvig's `count_1w.txt`.

## What you need

- **The word list.** Download [Norvig's `count_1w.txt`: the 333,000 most common English words with their counts](https://norvig.com/ngrams/count_1w.txt) (about 5 MB) into your working folder. Each line is a word, a tab, and the number of times it appeared in a very large web corpus, so split on whitespace, not on a single space. Don't commit it to your own repository; link to it.
- **Small first, then large.** Test on a hand-made list of 30 to 50 words, small enough that you can work out every answer by hand, and put at least one tie in it on purpose. For timing, use the first 1,000, 10,000 and 100,000 lines of Norvig's file. The file is sorted by frequency, so each slice is still a realistic word list.
- **An agent.** Claude Code, or the agent you normally use, with an account you can sign in to. Starting it in your working folder lets it see your specification and the word list.

## Where we left the specification on Friday

This is roughly what we wrote together in `specifications.md`. Use it as a starting point, not as the answer. It was written in half an hour, so it has gaps, and the handout's edge cases (empty prefix, no matches, ties, uppercase) were never discussed.

A good specification gives exactly **one** answer for every input. "Edge cases should be handled appropriately" and "the function should be efficient" decide nothing, so the agent decides for you, silently. Make a decision for each case, say why when it isn't obvious, and include a small table of example calls with their expected results. Each row of that table should turn into a test almost word for word.

```markdown
We are a group of students in a senior-level algorithms course. We want a
working and deliberately simple baseline autocomplete system for the terminal.

- Load the word frequency file ([frequency file](./count_1w.txt)).
- Create a small sample file of about 100 words, sorted alphabetically, for testing.
- Write a function `complete(prefix, k)` that returns the k most frequent
  entries that start with prefix.
- Use a straightforward approach. Do not optimize yet.
- Write unit tests for normal cases and edge cases.

# Constraints

- Pure Python. No NumPy, no third-party libraries.
- Keep the code simple enough for our level of understanding.
- Split the code into separate files as needed.

# How to work

- Before writing any code, give us a plan with the functions you want to
  write and their signatures.
- Describe the edge cases you want to test.
- Estimate the running time.
```

## One more experiment

On Friday I asked for this, and we ran out of time. Before you write your specification, give a fresh agent session a one-line prompt: *"Build me an autocomplete system from a dictionary file."* Save what comes back. When you're done, compare it with what your specification produced, and say in a few sentences which one you could defend line by line in my office.

## Stages 2 to 6: going further on your own

Finish stage 1 before you read this section. The handout's last question asks what you would change to make your code faster, and you should answer it yourself first.

Every stage works the same way as stage 1: write a specification (or update the one you have), predict the running time, ask the agent for a plan and review it, build, test, and time. Two rules hold at every stage:

- **The stage 1 version is the reference.** Never delete it. Every faster version must give exactly the same answers, and you check that with a test that compares the two on thousands of random prefixes.
- **Predict, then measure.** Write the running time you expect before you time anything, and explain any mismatch.

| Stage | Goal | Question to answer |
|---|---|---|
| 2 | Sort the words once. Use binary search (Python's `bisect`) to find the first word with the prefix, then walk forward through the matches. | How does $O(n)$ compare with $O(\log n + m)$ as the word list grows? |
| 3 | Design a data structure that stores shared beginnings once and doesn't start from scratch with every letter typed. See below. | Does it beat stage 2 in Python, on speed and on memory? Predict the winner first. |
| 4 | Return only the top 5. Compare sorting all the matches with keeping a heap of size $k$ (`heapq`, or the `MinHeap363` from Week 9). | When does a size-$k$ heap beat sorting all $m$ matches? |
| 5 | "Did you mean...?" When nothing matches, suggest close words using edit distance, computed by dynamic programming. | Why is comparing the input with every word too slow? |
| 6 | Make the suggestions fast: compare only words of similar length, or stop filling a row of the table once every entry is over the limit. *Stretch:* look up BK-trees. | Which pruning rule saves the most work, and why? |

### Stage 3: design it before you name it

Before you open the agent, print the words that match `pre` and look at them. Write down two things you notice about how the words are stored and how each query starts. Then give the agent this prompt, in plan mode:

```text
I'm a student in an algorithms course. We built an autocomplete that keeps
words in a sorted list and uses binary search to find the words starting
with a prefix. We noticed two things:

1. Many words share the same beginning (prefix, prefer, prepare, present),
   so the same letters are stored over and over.
2. When a user types one letter at a time ("p", "pr", "pre"), each query
   starts from scratch, even though the previous query already narrowed
   things down.

I want to design a better data structure myself, with your help. Please
act as a tutor, not as a solution provider:

- Do NOT name any existing data structure and do NOT write code.
- Ask me one question at a time that pushes me toward a design.
- When I propose an idea, ask me to try it on a small example
  (use the words: to, tea, ten, i, in, inn) before telling me whether
  it works.
- If I'm stuck after two attempts, give me a hint, not the answer.

When I've described a design that works, tell me whether it matches a
known data structure, give me its name, and then ask me to predict the
running time of finding all words with a given prefix.
```

Draw the structure on paper as you go. If you can't draw it, you don't understand it yet, however fluent the conversation looks. Once you have it, explain it back to the agent and ask it to find the gaps in your explanation. Only then build it.

## Reading

- [Peter Norvig, natural-language corpus data and word counts](https://norvig.com/ngrams/) — where `count_1w.txt` comes from and how it was built.
- [Anthropic, prompt engineering: an overview of techniques](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview) — being clear and direct, giving context, structuring a long prompt. Most of what we did on Friday, with names.
- [Anthropic, best practices for working with Claude Code](https://code.claude.com/docs/en/best-practices) — how to work with an agent in practice. Start with "Tell Claude what it can't see" (context, as on 11/11) and "Give Claude a check to run" (tests the agent can run itself).
- [Anthropic Academy courses on Skilljar](https://anthropic.skilljar.com/) — free courses, as recommended on 11/11 for the winter break. Roughly one a day, skipping the ones that don't apply to you. *Optional.*
- [Python `unittest`: writing and running tests](https://docs.python.org/3/library/unittest.html) and [Python `time.perf_counter_ns` for timing](https://docs.python.org/3/library/time.html#time.perf_counter_ns) — the two tools the handout asks for.

## Turning it in

Upload to Sakai. For **stage 1**, by Friday, November 20:

1. your specification (`specifications.md`) and your runtime prediction, written **before** you ran anything;
2. your code and tests;
3. the paragraph answering the handout's three questions;
4. the one-line-prompt comparison above.

Include the plan the agent gave you before it wrote code, and anything you changed in it. If you can't explain a line of your code, take it out or find out what it does. I may ask.

For **each later stage** you complete, any time before the last day of classes: the specification, your prediction, the code with its tests, the test that compares it with stage 1, your timings, and a short paragraph answering that stage's question. For stage 3, add the transcript of your conversation with the agent and a photo of your drawing.

Keep the stage 1 version after you turn it in. It is slow on purpose and correct on purpose, and it is how you'll know every faster version is right.
