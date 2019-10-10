#!/usr/bin/python

import sys


def making_change(amount, denominations, cache=[]):
    cache = [1]+[0]*amount
    for coin in denominations:
        for i in range(coin, amount+1):
            cache[i] += cache[i-coin]
    return cache[amount]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
