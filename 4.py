#!python3
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import logging, time

logging.basicConfig(level=logging.DEBUG,
                    format="[%(levelname)s] %(message)s")

def solve(n):
    highestNDigitNumber = pow(10, n) -1
    lowestNDigitNumber = pow(10, n-1)
    innerTerm = highestNDigitNumber

    palindromes = []

    quit = False
    for x in range(highestNDigitNumber, lowestNDigitNumber, -1):
        for y in range(x, lowestNDigitNumber, -1):
            p = x*y
            s = str(p)
            if s == s[::-1]:
                palindromes.append(p)
                break
    return max(palindromes)


if __name__ == '__main__':
    print()
    s = time.time()
    n = solve(2)
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("largest palindrome is", n)
    print("Found in {} minutes and {} seconds.".format(minutes, seconds))

    print()
    s = time.time()
    n = solve(3)
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("largest palindrome is", n)
    print("Found in {} minutes and {} seconds.".format(minutes, seconds))
