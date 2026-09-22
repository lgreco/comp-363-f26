from string_alignment import *

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
