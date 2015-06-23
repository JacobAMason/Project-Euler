#!python3
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import logging, time

logging.basicConfig(level=logging.DEBUG,
                    format="[%(levelname)s] %(message)s")

def solve(n):
    current = 2
    target = n
    maxPrimeFactor = n
    
    while target != 1:
        if target/current == target//current:
            target /= current
            maxPrimeFactor = current
            logging.debug("  ! new prime factor {}".format(current))
        current += 1
    return maxPrimeFactor

if __name__ == '__main__':
    print()
    s = time.time()
    n = solve(10)
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("Greatest Prime factor is", n)
    print("Found in {} minutes and {} seconds.".format(minutes, seconds))

    print()
    s = time.time()
    n = solve(13195)
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("Greatest Prime factor is", n)
    print("Found in {} minutes and {} seconds.".format(minutes, seconds))
    
    print()
    s = time.time()
    n = solve(600851475143)
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("Greatest Prime factor is", n)
    print("Found in {} minutes and {} seconds.".format(minutes, seconds))
