"""
determinant.py

A simple educational implementation of matrix determinant calculation
using recursive (Laplace) expansion. This version is not optimized
for performance and is intended for learning purposes only.
"""

import random
import sys
import numpy as np

# Global memoization dictionary
_cache = {}

def det(matrix: list[list[int]], start_row: int = 0, ignore_cols: frozenset[int] = frozenset()) -> int:
    """
    Recursively compute the determinant of a square matrix.

    Args:
        matrix: A list of lists (square matrix).
        start_row: The current row being expanded (used internally in recursion).
        ignore_cols: A frozenset of column indices already ignored.

    Returns:
        The determinant value as an integer.

    Note:
        This is a naive recursive implementation (O(n!)) and
        is suitable only for small matrices (e.g., n < 10).
    """

    n = len(matrix)

    # Base case: 1×1 matrix
    remaining_cols = [j for j in range(n) if j not in ignore_cols]
    if n - start_row == 1:
        # Return the single remaining element in the last row
        last_row = matrix[-1]
        last_col = remaining_cols[0]
        return last_row[last_col]

    # Base case: 2×2 matrix
    if n - start_row == 2:
        vals = []
        for i in range(start_row, n):
            for j in range(n):
                if j in ignore_cols:
                    continue
                vals.append(matrix[i][j])
        return vals[0] * vals[3] - vals[1] * vals[2]

    # Check memoized results
    key = (start_row, ignore_cols)
    if key in _cache:
        return _cache[key]

    # Recursive expansion along the current row
    total = 0
    sign = 1
    for j in range(n):
        if j in ignore_cols:
            continue
        new_ignore = ignore_cols | {j}
        cofactor = sign * matrix[start_row][j] * det(matrix, start_row + 1, new_ignore)
        total += cofactor
        sign = -sign  # alternate sign

    _cache[key] = total
    return total


def main(size: int):
    """Generate a random square matrix and compute its determinant."""
    matrix = [[random.randint(-10, 10) for _ in range(size)] for _ in range(size)]
    np_matrix = np.array(matrix)

    print("Matrix:\n", np_matrix)
    print("Shape:", np_matrix.shape)
    print("Determinant (recursive):", det(matrix))
    print("Determinant (NumPy):", round(np.linalg.det(np_matrix)))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python determinant.py <matrix_size>")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
        main(size)
    except ValueError:
        print("Error: matrix_size must be an integer.")
        sys.exit(1)
