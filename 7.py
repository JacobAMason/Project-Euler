#!python3
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import logging, time

logging.basicConfig(level=logging.INFO,
                    format="[%(levelname)s] %(message)s")

def solve(n):
    primes = []
    c = 2
    while len(primes) < n:
        foundPrime = True
        for p in primes:
            if p > c//2:
                # c must be prime because all the prime which could render c
                # not a prime (all primes < half of c) have been checked
                logging.debug("break p {}  c {}  c//2  {}".format(p,c,c//2))
                break
            if not c%p:
                foundPrime = False
                break
        if foundPrime:
            primes.append(c)
        c += 1

    logging.debug("Set of primes {}".format(primes))

    return primes[-1]


if __name__ == '__main__':
    print()
    s = time.time()
    n = solve(6)
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("prime number is", n)
    print("Found in %d minutes and %f seconds." % (minutes, seconds))

    print()
    s = time.time()
    n = solve(10001)
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("prime number is", n)
    print("Found in %d minutes and %f seconds." % (minutes, seconds))
