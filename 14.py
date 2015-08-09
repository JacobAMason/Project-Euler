#!python3
"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import logging, time

logging.basicConfig(level=logging.DEBUG,
                    format="[%(levelname)s] %(message)s")


def nextTerm(n):
    if n % 2 == 0:
        return n//2
    else:
        return 3*n + 1


def solve(largestStartingNumber):
    chainLengthsDict = {}
    largestChainStartingNumber = 1
    for startingNumber in range(1, largestStartingNumber):
        n = startingNumber
        thisChainLength = 1
        while n > 1:
            n = nextTerm(n)
            if n in chainLengthsDict:
                thisChainLength += chainLengthsDict[n]
                break
            else:
                thisChainLength += 1
        chainLengthsDict[startingNumber] = thisChainLength
        if chainLengthsDict[largestChainStartingNumber] < chainLengthsDict[startingNumber]:
            largestChainStartingNumber = startingNumber

    return largestChainStartingNumber



if __name__ == '__main__':
    print()
    s = time.time()
    n = solve(10)
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("The longest chain with a starting number under 10 "\
          "starts with", n)
    print("Found in %d minutes and %f seconds." % (minutes, seconds))

    print()
    s = time.time()
    n = solve(1000000)
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("The longest chain with a starting number under 1 million "\
          "starts with", n)
    print("Found in %d minutes and %f seconds." % (minutes, seconds))
