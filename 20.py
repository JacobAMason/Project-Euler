#!python3
"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

import logging, time

logging.basicConfig(level=logging.DEBUG,
                    format="[%(levelname)s] %(message)s")

from functools import reduce

def solve(n):
    return sum(map(int, str(reduce(lambda a,b: a*b, range(1, n+1)))))


if __name__ == '__main__':
    print()
    s = time.time()
    n = solve(10)
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("The sum of the digits in the number 10! is", n)
    print("Found in %d minutes and %f seconds." % (minutes, seconds))

    print()
    s = time.time()
    n = solve(100)
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("The sum of the digits in the number 100!", n)
    print("Found in %d minutes and %f seconds." % (minutes, seconds))
