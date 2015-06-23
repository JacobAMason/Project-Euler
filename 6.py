#!python3
"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

import logging, time

logging.basicConfig(level=logging.DEBUG,
                    format="[%(levelname)s] %(message)s")

def solve(n):
    
    sumOfSquares = sum([x*x for x in range(1, n+1)])
    squareOfSums = pow(sum(range(1, n+1)), 2)

    return squareOfSums - sumOfSquares


if __name__ == '__main__':
    print()
    s = time.time()
    n = solve(10)
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("difference is", n)
    print("Found in {} minutes and {} seconds.".format(minutes, seconds))

    print()
    s = time.time()
    n = solve(100)
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("difference is", n)
    print("Found in {} minutes and {} seconds.".format(minutes, seconds))
