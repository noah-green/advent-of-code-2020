puzzleName = "Report Repair"


from itertools import combinations


def solvePart1(puzzleInput):
    hashTable = set()
    for n in [int(line) for line in puzzleInput.split()]:
        hashTable.add(n)
        if 2020 - n in hashTable:
            return n * (2020 - n)


def solvePart2(puzzleInput):
    numbers = [int(line) for line in puzzleInput.split()]
    hashTable = set(numbers)
    for pair in combinations(numbers, 2):
        complement = 2020 - (pair[0] + pair[1])
        if complement in hashTable:
            return pair[0] * pair[1] * complement
