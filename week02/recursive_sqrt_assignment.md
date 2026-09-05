# Assignment: From a `while` Loop to Recursion — Newton's Method for Square Roots

## What you already have

In class you built `newton_sqrt(a)` in [`newton_raphson.ipynb`](newton_raphson.ipynb).
It works by starting from a guess, and repeatedly improving that guess
inside a `while` loop, until the guess is "good enough" (within some
tolerance $\epsilon$) or you've tried too many times.

That `while` loop is doing two jobs at once:

1. Deciding **when to stop** (the loop condition).
2. Deciding **what to do on each pass** (the loop body — compute a new
   guess from the old one).

## The assignment

Rewrite `newton_sqrt` so that the repetition is expressed **recursively**
instead — no `while`, no `for`, no explicit loop of any kind. The function
should call itself.

You don't need to invent the math. The formula

$$
x_{n+1} = \frac{1}{2}\left(x_n + \frac{a}{x_n}\right)
$$

is the same one from class and the same one already in your notebook.
What changes is the *control structure* around it, not the arithmetic.

## How to think about the conversion

Every `while` loop of the shape

```
while not done(state):
    state = update(state)
return state
```

has a recursive twin of the shape

```
def step(state):
    if done(state):
        return state
    return step(update(state))
```

Your job is to figure out, concretely, what `state`, `done(...)`, and
`update(...)` are in `newton_sqrt`. Some questions to work through on
paper before you write any code:

- In the loop, what is the one piece of information that changes from
  one pass to the next? (There's only one thing being updated — that's
  your recursive parameter.)
- What does the loop's condition check? That's your **base case** —
  except inverted. A `while` loop keeps going *while* a condition holds;
  a recursive base case stops *when* the equivalent condition is met.
  Don't just paste the `while` condition in — think about what it means
  for the guess to be "good enough," and write that check as its own
  small function if it helps you reason about it.
- What does the loop body compute? That becomes the argument to your
  recursive call.

## A structural hint, not a solution

You may find it clearer to break the work into a few small helper
functions rather than one dense function — e.g., something that decides
if a guess is good enough, something that produces an improved guess from
an old one, and a function that does the actual recursing. This isn't
required, but plenty of people find that naming these pieces separately
makes the recursive step read almost like English: "if the guess is good
enough, return it; otherwise, recurse on an improved guess." How you
structure it (free functions, a class, nested functions) is up to you.

## Two things the loop was doing that you can't lose

Your recursive version still needs to handle the same edge cases the
loop did:

1. **Negative input.** `newton_sqrt` refuses negative `a`. Your version
   should too — decide where that check belongs.
2. **A cap on how long you'll keep trying.** The loop had `stop_after` to
   guarantee termination even if convergence were somehow slow. A
   recursive version needs an equivalent safeguard — think about how to
   track "how many times have I recursed so far" without a loop counter
   variable sitting outside the function. (Hint: what could an extra
   parameter with a default value do for you here?)

Also think about *why* this second safeguard matters even more in
recursion than it did in the loop — Python has a limit on how deep a
call stack can go before it gives up. What happens to your function if
that limit is reached before your tolerance is?

## Checking your work

Once you have a recursive version, don't just eyeball it — run both your
original `newton_sqrt` and your new recursive version on the same
handful of inputs (try a perfect square, a non-perfect square, and a
number close to 0) and confirm they agree to within your tolerance. If
they don't, the disagreement is almost always in how the base case is
phrased — check it against the loop condition it replaced, term by term.

## Something to think about, not to hand in

The iterative version carries its "current guess" in a variable that
gets overwritten on every pass. The recursive version never overwrites
anything — each call gets its own guess, and the "next" guess is just the
argument to the next call. Where did the *loop counter* go, in your
recursive version? Is it the same idea in a different container? That
distinction — mutating state in place vs. passing a new value forward —
is most of what recursion is really asking you to practice here; the
square-root math is just the vehicle.

## A word on getting stuck

An imperfect or incomplete solution here is not a failure — it's a
genuinely good outcome. If your recursion won't terminate, your base
case never triggers, or you're staring at a `RecursionError` you can't
explain, that's exactly the kind of thing worth bringing to me *before*
the deadline, and exactly the kind of thing that makes for a productive
group discussion in class *after* it. The goal isn't a perfect submission
on the first try; it's the learning that comes from wrestling with a
problem, including the creative frustration of watching something not
work the way you expected.
