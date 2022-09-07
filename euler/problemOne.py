# https://projecteuler.net/problem=1

###############
#   PROBLEM   #
###############
# If we list all the natural numbers below 10
# that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import numpy as np


def multiples(num):
    total = np.arange(0, num)
    conditionList = [total % 3 == 0, total % 5 == 0]
    choiceList = [total, total]
    total = np.select(conditionList, choiceList, 0)
    print(total)
    return total.sum()


def retOne():
    return 1


if __name__ == "__main__":
    print(multiples(1000))
