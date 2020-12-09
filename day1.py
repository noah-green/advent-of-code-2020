puzzle_name = "Report Repair"


from itertools import combinations


def solution1(puzzle_input):
    hash_table = set()
    for n in [int(line) for line in puzzle_input.split()]:
        hash_table.add(n)
        if 2020 - n in hash_table:
            return n * (2020 - n)


def solution2(puzzle_input):
    numbers = [int(line) for line in puzzle_input.split()]
    hash_table = set(numbers)
    for pair in combinations(numbers, 2):
        complement = 2020 - (pair[0] + pair[1])
        if complement in hash_table:
            return pair[0] * pair[1] * complement
