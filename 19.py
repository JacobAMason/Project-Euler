#!python3
"""
You are given the following information, but you may prefer to do some
research for yourself.

1 Jan 1900 was a Monday.

Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century
unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
"""

import logging, time

logging.basicConfig(level=logging.DEBUG,
                    format="[%(levelname)s] %(message)s")


def get_days_in_month(month, year):
    if month in [4, 6, 9, 11]:
        return 30
    if month == 2:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return 29
                else:
                    return 28
            else:
                return 29
        else:
            return 28
    else:
        return 31


def solve():
    day = 1
    for month in range(1, 13):
        day += get_days_in_month(month, 1900)
        day %= 7
    sundays = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if day == 0:
                sundays += 1
            day += get_days_in_month(month, year)
            day %= 7
    return sundays

if __name__ == '__main__':
    print()
    s = time.time()
    n = solve()
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print(n, "Sundays fell on the first of the month during the twentieth"\
    " century")
    print("Found in %d minutes and %f seconds." % (minutes, seconds))
