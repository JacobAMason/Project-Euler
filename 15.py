#!python3
"""
Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

import logging, time

logging.basicConfig(level=logging.DEBUG,
                    format="[%(levelname)s] %(message)s")

def build_grid(size):
    return [[1 for i in range(size)] for j in range(size)]


def solve(gridSize):
    grid = build_grid(gridSize)
    sums = [sum(grid[0])]

    for i in range(1, len(grid)):
        for j in range(1, len(grid)):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
        sums.append(sum(grid[i]))

    return sum(sums) + 1



if __name__ == '__main__':
    print()
    s = time.time()
    n = solve(2)
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("There are", n, "paths through a 2x2 grid")
    print("Found in %d minutes and %f seconds." % (minutes, seconds))

    print()
    s = time.time()
    n = solve(3)
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("There are", n, "paths through a 3x3 grid")
    print("Found in %d minutes and %f seconds." % (minutes, seconds))

    print()
    s = time.time()
    n = solve(4)
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("There are", n, "paths through a 4x4 grid")
    print("Found in %d minutes and %f seconds." % (minutes, seconds))

    print()
    s = time.time()
    n = solve(20)
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("There are", n, "paths through a 20x20 grid")
    print("Found in %d minutes and %f seconds." % (minutes, seconds))
