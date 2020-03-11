#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # base cases
    if n == 0:
        return [[]]
    if n == 1:
        return [['rock'], ['paper'], ['scissors']]
    # helper function to append additional results

    def add_round(list):
        # clone list in [a, a, a, b, b, b, c, c, c] format rather than [a, b, c] * 3
        list = [item for item in list for r in range(3)]
        # loop with index and element
        for i, e in enumerate(list):
            # index 0, 3, 6 etc get rock, 1, 4, 7 etc get paper, 2, 5, 8 etc get scissors
            if i % 3 == 0:
                list[i] = e + ['rock']
            if i % 3 == 1:
                list[i] = e + ['paper']
            if i % 3 == 2:
                list[i] = e + ['scissors']
        return list
    # recursively create the listing
    if n > 1:
        return add_round(rock_paper_scissors(n-1))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
