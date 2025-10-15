import random
import sys
import os
import numpy as np


old = dict()

def det(a: list[list[int]], start_row: int = None, ignore_cols: set[int] = None):
    if start_row is None:
        start_row = 0
    if ignore_cols is None:
        ignore_cols = set()

    if len(a) - start_row == 1:
        return a[-1][-1]

    elif len(a) - start_row == 2:
        rem = []
        for i in range(start_row, len(a)):
            for j in range(0, len(a[0])):
                if j in ignore_cols:
                    continue
                rem.append(a[i][j])
        return rem[0] * rem[3] - rem[1] * rem[2]

    else:
        key = str(start_row) + ";" + "-".join(map(str, sorted(ignore_cols)))
        try:
            return old[key]
        except KeyError:
            pass

        sign = 1
        d = 0
        for i in range(len(a)):  # `i` is a column index
            if i in ignore_cols:
                continue

            ignore_cols.add(i)
            d += sign * a[start_row][i] * det(a, start_row + 1, ignore_cols)

            ignore_cols.remove(i)
            sign = -sign

        old[key] = d
        return d


def main(size: int):
    a = [[random.randint(-10, 10) for _ in range(size)] for _ in range(size)]
    a_np = np.array(a)
    print(a_np)
    print(a_np.shape)
    print("Det:", det(a))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the array size", file=os.stdout)
        sys.exit(1)

    main(int(sys.argv[1]))
