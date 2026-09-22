from __future__ import annotations

# Price list from class: match 0, mismatch 2, gap 1. compute_penalty() takes
# a and a_gap as callables (rather than hardcoding these values into the
# recurrence) so the same function works with any price list a caller wants.
GAP_PENALTY = 1  # Penalty for introducing a gap
MISMATCH_PENALTY = 2  # Penalty for a mismatch
MATCH_PENALTY = 0  # No penalty for a match


def a(x: str, y: str) -> int:
    """
    Computes the penalty for aligning two characters.

    Parameters:
    x (str): The first character.
    y (str): The second character.

    Returns:
    int: The penalty for aligning the two characters.
    """
    penalty = MISMATCH_PENALTY
    if x == y:
        penalty = MATCH_PENALTY
    return penalty


def a_gap() -> int:
    """
    Returns the penalty for introducing a gap. For now, this is a trivial
    function that returns a constant value, but it can be modified to compute
    the penalty based on the context of the alignment.

    Returns:
    int: The penalty for introducing a gap.
    """
    return GAP_PENALTY


def compute_penalty(X: str, Y: str, a: callable, a_gap: callable) -> list[list[int]]:
    """
    Computes the penalty for aligning two sequences with gaps.

    Parameters:
    X (str): The first sequence.
    Y (str): The second sequence.
    a (function): A function that computes the penalty for a mismatch.
    a_gap (function): A function that computes the penalty for introducing a gap.

    Returns:
    list[list[int]]: The penalty matrix for aligning the two sequences.
    """
    # Initialize the penalty matrix
    m: int = len(X)
    n: int = len(Y)
    P: list[list[int]] = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    # Initialize the first row and column of the penalty matrix. Ok, I am a bit
    # dramatic with setting i,j to int here, but I want to make sure that the type
    # hints are clear and explicit.
    i: int
    j: int
    for i in range(1, m + 1):
        P[i][0] = i * a_gap()
    for j in range(1, n + 1):
        P[0][j] = j * a_gap()
    # Fill the rest of the penalty matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            P[i][j] = min(
                P[i - 1][j] + a_gap(),
                P[i][j - 1] + a_gap(),
                P[i - 1][j - 1] + a(X[i - 1], Y[j - 1]),
            )
    return P