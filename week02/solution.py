"""
COMP 363 -- Week 02 reference solution: From a `while` Loop to Recursion
(Newton's method for square roots).

Structured after https://github.com/lgreco/sicp/blob/main/Chapter%201/1-1-8-sqrt.py --
a class wrapping the same Newton's-method idea, with the repetition
expressed recursively instead of with a loop. The epsilon (0.0001) and
iteration cap (1,000) below match the values used in class and in
newton_raphson.ipynb, so this solution is directly comparable to that
starting point.

Here's what you started with in newton_raphson.ipynb:

    def newton_sqrt(a):
        if a < 0:
            raise ValueError("Cannot compute square root of a negative number.")
        elif a == 0:
            return 0

        x = a / 2.0
        epsilon = 0.0001
        stop_after = 1_000
        iterations_count = 0

        while abs(x * x - a) > epsilon and iterations_count < stop_after:
            x = (x + a / x) / 2.0
            iterations_count += 1
        return x

That `while` loop is doing two jobs at once: deciding *when to stop*
(the loop condition) and deciding *what to do on each pass* (the loop
body). Below, those two jobs become two separate methods --
`_is_good_enough` (when to stop) and `_improve` (what to do on each
pass) -- and the loop itself becomes `_sqrt_iter`, a method that calls
itself instead of looping.
"""

EPSILON = 0.0001       # How close guess*guess has to land to x to accept it.
STOP_AFTER = 1_000     # Safety cap: max number of recursive calls allowed.


class SQRT:
    """Computes square roots with Newton's method, using recursion in
    place of the while loop for the repeated-improvement step."""

    def __init__(self, epsilon: float = EPSILON, stop_after: int = STOP_AFTER) -> None:
        """epsilon controls how close counts as "good enough"; stop_after
        plays exactly the role stop_after/iterations_count played in the
        while-loop version -- a safety net so a call that isn't
        converging still terminates instead of running forever."""
        self._x = 0.0
        self.epsilon = epsilon
        self.stop_after = stop_after

    def _is_good_enough(self, guess: float) -> bool:
        """True once `guess` is close enough to be accepted as
        sqrt(self._x).

        This is the while loop's condition, inverted: the loop kept
        going *while* `abs(x*x - a) > epsilon` was true. A recursive
        base case instead stops *when* the guess is good enough -- so
        here we write the "good enough" check directly, and the
        recursive step below decides what to do with it.
        """
        return abs(guess * guess - self._x) < self.epsilon

    def _average(self, a: float, b: float) -> float:
        """Average of two numbers. The 2.0 in Newton's formula isn't a
        magic number -- it's here because we're averaging exactly two
        values (the guess and x / guess). Once we cover arrays, the same
        idea generalizes: averaging n values means dividing by the
        length of the array holding them."""
        return (a + b) / 2.0

    def _improve(self, guess: float) -> float:
        """One Newton step: exactly the update the while loop's body
        performed every pass (`x = (x + a / x) / 2.0`), just written as
        a function that *returns* the next guess instead of overwriting
        a variable in place."""
        return self._average(guess, self._x / guess)

    def _sqrt_iter(self, guess: float, tries_so_far: int = 0) -> float:
        """The recursive replacement for the while loop.

        Every while loop of the shape

            while not done(state):
                state = update(state)
            return state

        has this recursive twin:

            def step(state):
                if done(state):
                    return state
                return step(update(state))

        Here, `state` is `guess`, `done(state)` is `_is_good_enough`,
        and `update(state)` is `_improve`. `tries_so_far` is the loop
        counter (`iterations_count` in the while-loop version) --
        instead of a variable that lives outside the loop and gets
        mutated each pass, it's a parameter with a default value,
        carried forward fresh on each recursive call. Nothing here is
        ever overwritten in place: each call gets its own `guess` and
        its own `tries_so_far`; the "next" state is just the argument
        passed to the next call.
        """
        if self._is_good_enough(guess) or tries_so_far >= self.stop_after:
            # Base case -- the recursive twin of "while not done(state)"
            # being false: we're done, so return the state as-is.
            return guess
        # Recursive case -- "state = update(state)" followed by looping
        # back around, expressed as calling ourselves with the new state.
        return self._sqrt_iter(self._improve(guess), tries_so_far + 1)

    def sqrt(self, x: float) -> float:
        """Public method: compute the square root of x recursively.

        Two edge cases the while-loop version handled that a purely
        recursive rewrite can't drop:

        1. Negative input has no real square root -- refuse it once,
           here, rather than re-checking it on every recursive call.
        2. x == 0 is its own square root, and also the one input for
           which the very first guess (x / 2.0 == 0) would cause a
           division-by-zero inside `_improve` -- handle it directly
           instead of letting it fall into the recursion.
        """
        if x < 0:
            raise ValueError("Cannot compute square root of a negative number.")
        if x == 0:
            return 0.0

        self._x = x
        # Start the same way the while-loop version did: guess = x / 2.
        return self._sqrt_iter(x / 2.0)


# ---------------------------------------------------------------------
# Demonstration and self-check: compare the recursive result against
# Python's own math.sqrt, and confirm the two edge cases above actually
# work the way they're supposed to.
# ---------------------------------------------------------------------
if __name__ == "__main__":
    import math

    demo = SQRT()

    print("\nTest       Newton's         Actual")
    print("   x       sqrt(x)          sqrt(x)")
    print("-" * 40)
    for num in [4, 2, 10, 1234, 0.01]:
        print(f"{num:>8}   {demo.sqrt(num):12.6f}   {math.sqrt(num):12.6f}")
    print("-" * 40)

    print("\nsqrt(0) =", demo.sqrt(0))

    try:
        demo.sqrt(-9)
    except ValueError as e:
        print("sqrt(-9) correctly raised ValueError:", e)
