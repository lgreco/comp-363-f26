# Assignment: Building the Alignment Cost Matrix

## What you already have

In class, and in [`string_alignment.ipynb`](string_alignment.ipynb), we worked out how to compute the
cost of optimally aligning two strings $X_m$ and $Y_n$ — without ever
enumerating the alignments themselves. We got there by assuming the optimal
alignment was simply handed to us, looking at its last column, and noticing
it can only take one of three forms:

$$
\left | x_{m-1}\atop y_{n-1} \right |,\qquad
\left | x_{m-1}\atop \texttt{-} \right |,\qquad
\left | \texttt{-}\atop y_{n-1} \right |
$$

That observation gave us a recurrence for $P(i,j)$, the cost of optimally
aligning the length-$i$ prefix of $X$ with the length-$j$ prefix of $Y$:

$$
P(i,j) = \min \left \{ P(i-1,j-1) + a_{x_{i-1}\,y_{j-1}},\quad
P(i-1,j)+a_{\text{gap}},\quad P(i,j-1)+a_{\text{gap}} \right \}
$$

with base cases $P(0,0) = 0$ and $P(i,j) = (i+j)\times a_{\text{gap}}$ when
$0 \leq (i+j) \leq 1$ (i.e., whenever one of the two strings involved is
empty). Our price list for this assignment is the one we used in class:

- match ($x = y$): **0**
- mismatch ($x \neq y$): **2**
- gap: **1**

You already did one cell of this by hand in class: $P(1,1)$ for `bicycle`
and `cycle` is the minimum of $0+2$, $1+1$, and $1+1$, which is $2$.

## The assignment

Write code that builds the **entire cost matrix** $P$ for two input
strings and reports the optimal alignment cost, $P(m,n)$.

This means:

1. A function that, given two strings, allocates a table of size
   $(m+1)\times(n+1)$ and fills in the base-case row and column.
2. A double loop — over $i$ from $1$ to $m$ and $j$ from $1$ to $n$ — that
   fills in the rest of the table using the recurrence above.
3. A way to retrieve both the full table and the final answer, $P(m,n)$,
   from your function.

**What's explicitly out of scope this time:** figuring out *what the
optimal alignment looks like* — which characters line up, where the gaps
go. That requires backtracking through the matrix you just built, and
we're doing that together in class once you've had a chance to work with
your own solutions. This assignment stops at the cost matrix and the
number in its bottom-right corner.

## Questions to work through before you write code

- The recurrence for $P(i,j)$ refers to $P(i-1,j-1)$, $P(i-1,j)$, and
  $P(i,j-1)$. In what order do you have to fill in the table so that all
  three of those are already known by the time you need them?
- The base cases handle the first row and first column. Why can't you
  just start the double loop at $i=0, j=0$ and let the recurrence handle
  everything, the way it's written above?
- Where does the price list live in your code? Is it a fixed part of the
  function, or something a caller can change? Think back to why we said
  "you might come up with any price list you like" — should your function
  agree with only *this* price list, or with any reasonable one?

## Checking your work

Once your function runs, verify it against a few pairs by hand-tracing
at least one small one yourself (the way we did for `bicycle`/`cycle` in
class), then check the final costs your code reports against these:

| $X$ | $Y$ | $P(m,n)$ |
|---|---|---|
| `CAT` | `CATS` | 1 |
| `CATS` | `DOGS` | 6 |
| `BICYCLE` | `CYCLE` | 2 |
| `CRANE` | `RAIN` | 3 |
| `ASTRONOMY` | `GASTRONOMY` | 1 |
| `DELICIOUS` | `RELIGIOUS` | 4 |
| `INTENTION` | `EXECUTION` | 8 |

If your numbers don't match, the mismatch is almost always in the base
case row/column or in an off-by-one in the loop bounds — check those
before suspecting the recurrence itself.

## Something to think about, not to hand in

Every cell of your matrix was computed from at most three neighbors. That
means every cell also silently "remembers" which of those three neighbors
it came from — even though your code, as specified above, never records
that. When we do backtracking together, we'll be recovering exactly that
lost information by replaying the arithmetic in reverse. As you fill in
your table, notice whether there's anything cheap you could stash at each
cell right now that would make that replay trivial later — you don't need
to implement it, just notice the opportunity.

## A word on getting stuck

If your matrix disagrees with the table above on one pair but not others,
that's useful information, not a failure — it usually means one specific
case (a tie in the minimum, an empty-string edge case, a string-length
mismatch) is exposing a real gap in your understanding of the recurrence,
which is exactly the kind of thing worth bringing to class before we move
on to backtracking.
