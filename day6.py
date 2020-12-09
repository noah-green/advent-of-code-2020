puzzle_name = 'Custom Customs'

def solution1(puzzle_input):
    return sum(len(set().union(*group.split())) for group in puzzle_input.split('\n\n'))


def solution2(puzzle_input):
    return sum(len(set('abcdefghijklmnopqrstuvwxyz').intersection(*group.split())) for group in puzzle_input.split('\n\n'))
