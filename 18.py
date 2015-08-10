#!python3
"""
By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by
trying every route. However, Problem 67, is the same challenge with a triangle
containing one-hundred rows; it cannot be solved by brute force, and requires
a clever method! ;o)
"""

import logging, time

logging.basicConfig(level=logging.DEBUG,
                    format="[%(levelname)s] %(message)s")


def build_triangle():
    l = list(map(str.split, [
"75",
"95 64",
"17 47 82",
"18 35 87 10",
"20 04 82 47 65",
"19 01 23 75 03 34",
"88 02 77 73 07 63 67",
"99 65 04 28 06 16 70 92",
"41 41 26 56 83 40 80 70 33",
"41 48 72 33 47 32 37 16 94 29",
"53 71 44 65 25 43 91 52 97 51 14",
"70 11 33 28 77 73 17 78 39 68 17 57",
"91 71 52 38 17 14 91 43 58 50 27 29 48",
"63 66 04 68 89 53 67 30 73 16 69 87 40 31",
"04 62 98 27 23 09 70 98 73 93 38 53 60 04 23",
]))
    triangle = []
    for row in l:
        triangle.append(list(map(int, row)))
    return triangle


def compute_sum_from_children(row, item, triangle):
    triangle[row][item] += max(triangle[row-1][item], triangle[row-1][item+1])
    return triangle


def solve():
    triangle = list(reversed(build_triangle()))
    for row in range(1, len(triangle)):
        for item in range(len(triangle[row])):
            triangle = compute_sum_from_children(row, item, triangle)

    return triangle[-1][0]



if __name__ == '__main__':
    print(build_triangle())

    print()
    s = time.time()
    n = solve()
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("The maximum total from top to bottom of the triangle is", n)
    print("Found in %d minutes and %f seconds." % (minutes, seconds))
