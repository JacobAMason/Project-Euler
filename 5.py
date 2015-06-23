#!python3
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import logging, time

logging.basicConfig(level=logging.DEBUG,
                    format="[%(levelname)s] %(message)s")

def solve(n):
    factors = [2]
    for f in range(2, n+1):
        logging.debug("Number {}".format(f))
        for p in factors:
            if not f%p:
                f /= p
                logging.debug("  uses factor %d, reduced to %d" % (p, f))

        if f != 1:
            factors.append(f)
            logging.debug("  created factor %d" % (f))

    product = 1
    for f in factors:
        product *= f
    return product


if __name__ == '__main__':
    print()
    s = time.time()
    n = solve(10)
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("smallest number is", n)
    print("Found in {} minutes and {} seconds.".format(minutes, seconds))

    print()
    s = time.time()
    n = solve(20)
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("smallest number is", n)
    print("Found in {} minutes and {} seconds.".format(minutes, seconds))
