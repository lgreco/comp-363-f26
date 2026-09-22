from string_alignment import *

# Everything below runs only when this file is executed directly (e.g.
# `python test_alignment.py`), not when it's imported. Without this guard,
# the loop would also run on import and fail with a NameError, since
# test_cases wouldn't exist yet outside the `if` block.
if __name__ == "__main__":
    test_cases = [
        ["ASTRONOMY", "ASTRONOMY"],
        ["ASTRONOMY", "ASTRONOMICAL"],
        ["ASTRONOMY", "GASTRONOMY"],
        ["CYCLE", "BICYCLE"],
        ["STRANGER", "STRONGER"],
        ["TOMATO", "POTATO"],
        ["ALIGNMENT", "ASSIGNMENT"],
        ["GATTACA", "GATACCA"],
        ["HELLO", "WORLD"],
        ["PYTHON", "JAVA"],
    ]

    for test_case in test_cases:
        X, Y = test_case
        penalty_matrix = compute_penalty(X, Y, a, a_gap)
        print(f"Penalty matrix for aligning '{X}' and '{Y}':")
        for row in penalty_matrix:
            print(row)
        print()
