#!python3
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.
"""

import logging, time

logging.basicConfig(level=logging.DEBUG,
                    format="[%(levelname)s] %(message)s")

numbersDict = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}


def convert(n):
    """
    >>> convert(1)[0]
    3
    >>> convert(12)[0]
    6
    >>> convert(20)[0]
    6
    >>> convert(25)[0]
    10
    >>> convert(100)[0]
    10
    >>> convert(101)[0]
    16
    >>> convert(115)[0]
    20
    >>> convert(117)[0]
    22
    >>> convert(123)[0]
    24
    >>> convert(342)[0]
    23
    >>> convert(606)[0]
    16
    >>> convert(987)[0]
    25
    >>> convert(1000)[0]
    11
    """
    if n in numbersDict:
        return len(numbersDict[n]), numbersDict[n]
    # else, n is greater than 20

    # reverse so that n[0] is the ones place an so on
    n = list(map(int, reversed(str(n))))

    word = []

    wordHundred  = "hundred"
    wordAnd      = "and"
    wordThousand = "thousand"

    if (n[1]*10 + n[0]) in numbersDict:
        word.append(numbersDict[(n[1]*10 + n[0])])
    else:
        word.append(numbersDict.get(n[0], ""))
        word.append(numbersDict.get(n[1] * 10, ""))

    if len(n) > 2:
        if n[1] or n[0]: word.append(wordAnd)
        hundreds = numbersDict.get(n[2], "")
        needHundred = wordHundred if hundreds else ""
        word.append(needHundred)
        word.append(hundreds)

    if len(n) > 3:
        thousands = numbersDict.get(n[3], "")
        needThousand = wordThousand if thousands else ""
        word.append(needThousand)
        word.append(thousands)

    return len("".join(word)), " ".join(reversed(word))


def solve(n):
    totalLength = 0
    for i in range(1, n+1):
        length, text = convert(i)
        totalLength += length
    return totalLength



if __name__ == '__main__':
    print()
    s = time.time()
    n = solve(5)
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("The number of letters in sum of the numbers from 1 to 5 is", n)
    print("Found in %d minutes and %f seconds." % (minutes, seconds))

    print()
    s = time.time()
    n = solve(1000)
    e = time.time()
    t = e-s
    minutes = t // 60
    seconds = t % 60
    print("The number of letters in sum of the numbers from 1 to 1000 is", n)
    print("Found in %d minutes and %f seconds." % (minutes, seconds))
