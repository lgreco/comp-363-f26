# Assignment: Classic vs. Karatsuba Multiplication — A Timing Study

## The starter code

[`multiplication.py`](multiplication.py) contains two working multiplication
routines and everything they need. Read it before you run anything; the
comments explain each step.

Numbers are **lists of decimal digits, most significant digit first**:

```python
1234  ->  [1, 2, 3, 4]
11    ->  [1, 1]
```

The only arithmetic the code performs is single-digit multiplication,
digit-by-digit addition (with carry), and digit-by-digit subtraction (with
borrow). Python's built-in big integers are never used to compute a product.

```python
from multiplication import *

multiply_classic([1, 1], [1, 1])      # [0, 1, 2, 1]   (11 x 11 = 121, in 2n = 4 digits)
multiply_karatsuba([1, 1], [1, 1])    # [0, 1, 2, 1]
```

Both functions require `x` and `y` to have the **same length, a power of 2**,
and return exactly `2n` digits. The product of two $n$-digit numbers can
actually have either $2n-1$ or $2n$ digits (as the notebook notes), but our
code always 0-pads the result on the left as needed, so that it is exactly
$2n$ digits long. That is why $11 \times 11 = 121$ comes back as
`[0, 1, 2, 1]`. Use `strip_leading_zeros` to remove the padding when you
want to display a result.

For inputs whose lengths are not a power of 2, or not equal, left-pad with
zeros first:

```python
x, y = pad_to_power_of_two(from_int(123456), from_int(789))   # both length 8
strip_leading_zeros(multiply_classic(x, y))                   # [9, 7, 4, 0, 6, 7, 8, 4]
```

### The two recursions

Both algorithms are derived in [`master_theorem.ipynb`](master_theorem.ipynb),
which you should read first: it splits $x$ and $y$ into halves
$A, B$ and $C, D$, writes the classic product as four half-size products,
gives Karatsuba's three-product rearrangement, and analyzes both with the
Master Theorem. The code uses the notebook's names, in upper case, for the
halves and the partial products (`A`, `B`, `C`, `D`, `AC`, `BC`, `AD`,
`BD`), so they can't be mistaken for the lower-case $c$ and $d$ of the
Master Theorem's recurrence $T(n) = r\,T(n/c) + n^d$.

$$
xy = AC\cdot 10^{n} + (BC + AD)\cdot 10^{n/2} + BD \qquad \text{(classic, } r=4\text{)}
$$

$$
xy = AC\cdot 10^{n} + \bigl((A+B)(C+D) - AC - BD\bigr)\cdot 10^{n/2} + BD \qquad \text{(Karatsuba, } r=3\text{)}
$$

The notebook stores numbers as strings; the starter code stores them as
lists of integer digits instead. A string is immutable and holds characters,
whereas a list of ints lets us add and subtract digits directly, which is
exactly what the recurrences need.

One detail in `multiply_karatsuba` deserves your attention: $A+B$ can carry
out of its top digit and become $n/2 + 1$ digits long, which would stop the
subproblem from shrinking. The code sets that carry aside and multiplies
only the $n/2$-digit remainders recursively. Find where this happens and
make sure you can explain why it is needed.

The code also counts single-digit multiplications for you:
`reset_digit_mult_count()` before a call, `get_digit_mult_count()` after.

## Part 1 — Check that the code is right

Before timing anything, convince yourself both functions work.

1. Trace `multiply_classic([1, 2], [3, 4])` by hand, writing out $A,B,C,D$ and
   the four partial products `AC`, `BC`, `AD`, `BD`. Then do the same for `multiply_karatsuba`.
2. Write a short test that, for many random pairs of lengths $1, 2, 4, 8, 16$,
   compares both functions against Python's own `*` (use `to_int` /
   `from_int`). Include the all-9s case, e.g. `[9]*8` times `[9]*8`; it
   exercises every carry.

## Part 2 — Timing with `perf_counter_ns()`

Python's nanosecond timer is `time.perf_counter_ns()` from the `time` module
(some languages call this `nanoTime()`). It returns an integer count of
nanoseconds from an arbitrary starting point, so only *differences* between
two readings mean anything:

```python
import time

start = time.perf_counter_ns()
product = multiply_classic(x, y)
elapsed_ns = time.perf_counter_ns() - start
```

Time **only** the multiplication. Build the input lists before you start the
clock.

A single measurement is noisy: the operating system, other programs, and
Python's memory management all interfere. Repeat each measurement several
times and keep the **minimum** (the run least disturbed by noise) or the
**median**. State which one you used and why.

### Generating inputs of many lengths

Use the standard library's `random` module, with a fixed seed so your results
are reproducible. `random_digits(n, rng)` in the starter code returns $n$
random digits:

```python
import random
rng = random.Random(363)

lengths = [2**p for p in range(1, 10)]     # 2, 4, 8, ..., 512
```

Both algorithms must see the **same** inputs at each length.

### A skeleton for the experiment

```python
import time
import random
from multiplication import *

def time_one(func, x, y, trials):
    """Return the best (smallest) of `trials` timings of func(x, y), in ns."""
    best = None
    for _ in range(trials):
        start = time.perf_counter_ns()
        func(x, y)
        elapsed = time.perf_counter_ns() - start
        if best is None or elapsed < best:
            best = elapsed
    return best

rng = random.Random(363)
rows = []                                   # one row per length
for p in range(1, 10):
    n = 2**p
    x = random_digits(n, rng)
    y = random_digits(n, rng)

    t_classic = time_one(multiply_classic, x, y, trials=5)
    t_karatsuba = time_one(multiply_karatsuba, x, y, trials=5)

    reset_digit_mult_count()
    multiply_classic(x, y)
    m_classic = get_digit_mult_count()
    reset_digit_mult_count()
    multiply_karatsuba(x, y)
    m_karatsuba = get_digit_mult_count()

    rows.append((n, t_classic, t_karatsuba, m_classic, m_karatsuba))
```

**Mind the cost.** The classic algorithm performs $n^2$ single-digit
multiplications. Lengths through 512 finish in a fraction of a second;
each doubling beyond that roughly quadruples the classic time. Add
1024 or 2048 only if you are willing to wait, and start small.

## Part 3 — Getting the numbers out

### Option A: print, then paste into a spreadsheet

Print one comma-separated line per length, with a header:

```python
print("n,classic_ns,karatsuba_ns,classic_mults,karatsuba_mults")
for n, tc, tk, mc, mk in rows:
    print(f"{n},{tc},{tk},{mc},{mk}")
```

Copy the output into a text file ending in `.csv` and open it in Excel or
Google Sheets (or paste it into a sheet and use *Data → Split text to
columns*, with comma as the separator). Then insert a scatter or line chart
with $n$ on the horizontal axis.

### Option B: plot in Python with pandas and matplotlib

Install both once, from a terminal: `pip install pandas matplotlib`.

**pandas** holds tabular data in a `DataFrame` — think of a spreadsheet
you can program. Each column is named:

```python
import pandas as pd

df = pd.DataFrame(rows, columns=["n", "classic_ns", "karatsuba_ns",
                                  "classic_mults", "karatsuba_mults"])
df["classic_ms"] = df["classic_ns"] / 1e6        # new column, computed
print(df)                                        # inspect it
df.to_csv("timings.csv", index=False)            # save for later, or for a spreadsheet
```

**matplotlib** draws the picture:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(df["n"], df["classic_ns"] / 1e6, marker="o", label="classic")
ax.plot(df["n"], df["karatsuba_ns"] / 1e6, marker="s", label="Karatsuba")
ax.set_xlabel("number of digits, n")
ax.set_ylabel("time (ms)")
ax.set_title("Classic vs. Karatsuba multiplication")
ax.legend()
fig.savefig("timing.png", dpi=150)
plt.show()
```

Two refinements to try:

- **Log–log axes.** Add `ax.set_xscale("log", base=2)` and
  `ax.set_yscale("log")`. A running time of $c\,n^k$ becomes a straight line
  whose *slope* is $k$, which makes the two algorithms far easier to compare.
- **Reading the slope numerically.** With log-log data, the ratio between
  successive rows tells you the exponent. `df["classic_ns"].pct_change()`
  gives the relative growth from one length to the next; when $n$ doubles,
  a ratio of 4 suggests $n^2$ and a ratio of 3 suggests $n^{\log_2 3}$.

## Part 4 — Analysis and what to submit

Submit your code, your plots (or spreadsheet charts), your raw timing table,
and a short written report (about one page) answering:

1. **Master Theorem.** For each algorithm, identify $r$, $c$, and $d$ in
   $T(n) = r\,T(n/c) + n^d$, as in the notebook. Point to the lines of code
   (splitting, `add_digits`, `subtract_digits`, `shift`) that make
   $f(n)=n^d$, and justify your value of $d$. Which case of the theorem
   applies, and what running time does it predict?
2. **Multiplication counts.** For each $n$, how do `classic_mults` and
   `karatsuba_mults` compare with $n^2$ and $n^{\log_2 3}$? The notebook
   compares $1024^2 = 1{,}048{,}576$ with $1024^{1.58}\approx 57{,}052$;
   what do your measured counts say for the lengths you tested? Write the
   recurrence for each algorithm's count (only the multiplications, so
   $f(n)=0$ and the base case is one multiplication) and solve it.
3. **Running times.** Which algorithm is faster at each length? Is there a
   crossover length below which classic wins? If you saw none in the range
   you tested, say what you'd expect to find at very small $n$ and why.
4. **Growth rate.** When $n$ doubles, by what factor does each algorithm's
   time grow? Are the ratios consistent with $\Theta(n^2)$ and
   $\Theta(n^{\log_2 3})$?
5. **Counts vs. clock.** Karatsuba does far fewer single-digit
   multiplications, but it also does more additions, subtractions, list
   copies, and slicing. Does the ratio of the two algorithms' *times* match
   the ratio of their *multiplication counts*? Explain any gap.
6. **Reproducibility.** How much did repeated timings of the same input
   vary? What did taking the minimum (or median) do for you?

## Something to think about, not to hand in

Padding to the next power of 2 can nearly double the length of a number:
a 513-digit input becomes 1024 digits. What does this do to the running time
of each algorithm for lengths just above a power of 2, and how might you
avoid it?
