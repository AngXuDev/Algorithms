#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # set lowest initial price to first element
    lowest = prices[0]
    # set lowest possible profit to zero minus first element
    profit = -prices[0]
    # loop through elements
    for num in prices:
        # if element minus lowest price is larger than current profit, set profit
        if num - lowest > profit and prices.index(num) != 0:
            profit = num - lowest
        # if element is less than lowest price, set lowest price
        if num < lowest:
            lowest = num

    return profit


print(find_max_profit([100, 90, 80, 50, 20, 10]))


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
