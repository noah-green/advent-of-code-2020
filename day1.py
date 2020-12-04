puzzleName = "Report Repair"

from itertools import combinations

def solvePart1(input):
    numbers = [int(line) for line in input.split()]
    table = set(numbers)
    for n in numbers:
        complement = 2020 -n
        if 2020 - n in table:
            return n * complement


def solvePart2(input):
    numbers = [int(line) for line in input.split()]
    table = set(numbers)
    for pair in combinations(numbers, 2):
        complement = 2020 - (pair[0] + pair[1])
        if complement in table:
            return pair[0] * pair[1] * complement
