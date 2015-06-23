#!python3
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import logging, time

logging.basicConfig(level=logging.INFO,
                    format="[%(levelname)s] %(message)s")

def solve(n):
    foundSolution = False
    for a in range(1, n):
        for b in range(a, n):
            c = n - a - b
            if (a*a + b*b == c*c):
                foundSolution = True
                return (a * b * c)





if __name__ == '__main__':
    print()
    s = time.time()
    n = solve(12)
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("Pythagorean triplet is", n)
    print("Found in %d minutes and %f seconds." % (minutes, seconds))

    print()
    s = time.time()
    n = solve(1000)
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("Pythagorean triplet is", n)
    print("Found in %d minutes and %f seconds." % (minutes, seconds))
