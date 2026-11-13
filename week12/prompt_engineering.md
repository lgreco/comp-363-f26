# Building an Autocomplete

## The problem

Every search box you've used finishes your words for you. Type "alg" and it offers "algorithm," "algebra," "algae." It sounds trivial, but a real system answers that question millions of times a second, across hundreds of thousands of words, and it has to rank the suggestions sensibly. Over the next few sessions we'll build one ourselves, and each improvement will come from an algorithm we've studied.

Today we build the simplest version that is correct. It won't be fast, and that's intentional. This first version becomes our reference: every faster version we write later must give exactly the same answers, and we'll check that automatically.

## What your program should do

You'll be given a word list where each line has a word and how often it appears in English text. Your program answers one question: given a prefix and a number k, what are the k most common words that start with that prefix, most common first?

For example, with the prefix "th" and k = 3, a reasonable answer is "the," "that," "this."

## How you'll work today

You'll use Claude as your programming partner, but you are responsible for the design and for whether the result is correct. Work in this order.

**Specify before you prompt.** With your partner, write down in plain English exactly what the function should do, including the awkward cases. What should happen with an empty prefix? A prefix that matches nothing? A k larger than the number of matches? Two words with the same frequency? Uppercase input? Your answers become the contract that the code and the tests must follow.

**Predict before you measure.** Before running anything, write down the running time you expect for this approach in terms of n, the number of words, and m, the number of matches.

**Then build with the agent.** Give Claude your specification and constraints: pure Python, standard library only, `unittest` for testing, readable code. Ask for a plan first and review it before letting it write code. When the code arrives, read it. You should be able to explain every line.

**Test and time it.** Run the tests. Then time your function on word lists of increasing size using `time.perf_counter_ns()`, and compare the results to your prediction.

## What to hand in at the end of the session

Hand in your written specification, your code and tests, and a short paragraph answering three questions:

1. Did the timings match your prediction, and if not, why not?
2. What edge case did you (or the agent) miss at first?
3. What would you change to make this faster?

That last answer is where we start next time.
