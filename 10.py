#!python3
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import logging, time

logging.basicConfig(level=logging.INFO,
                    format="[%(levelname)s] %(message)s")


def sieve(n):
    l = list(range(n+1))
    for i in range(2, n+1):
        logging.debug("i {}".format(i))
        if l[i] != 0:
            for e in range(2*i, n+1, i):
                logging.debug("  e {}".format(e))
                l[e] = 0

    logging.debug("! l {}".format(l))
    return sum(l) -1


if __name__ == '__main__':
    print()
    s = time.time()
    n = sieve(10)
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("sum of all the primes below 10 is", n)
    print("Found in %d minutes and %f seconds." % (minutes, seconds))

    print()
    s = time.time()
    n = sieve(2*pow(10,6))
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("sum of all the primes below 2 million is", n)
    print("Found in %d minutes and %f seconds." % (minutes, seconds))
