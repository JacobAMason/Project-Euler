#!python3
"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

import logging, time

logging.basicConfig(level=logging.DEBUG,
                    format="[%(levelname)s] %(message)s")


def solve(power):
    return sum(map(int, str(pow(2, power))))



if __name__ == '__main__':
    print()
    s = time.time()
    n = solve(15)
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("The sum of the digits in 2^15 is", n)
    print("Found in %d minutes and %f seconds." % (minutes, seconds))

    print()
    s = time.time()
    n = solve(1000)
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("The sum of the digits in 2^1000 is", n)
    print("Found in %d minutes and %f seconds." % (minutes, seconds))
