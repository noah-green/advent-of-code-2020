puzzle_name = 'Tobaggan Trajectory'


def check_trees(puzzle_input, down, over):
    x = 0
    trees = 0
    for line in puzzle_input.split()[::down]:
        trees += 1 if line[x] == '#' else 0
        x = (x + over) % (len(line))
    return trees


def solution1(puzzle_input):
    return check_trees(puzzle_input, 1, 3)


def solution2(puzzle_input):
    return (
        check_trees(puzzle_input, 1, 1) *
        check_trees(puzzle_input, 1, 3) *
        check_trees(puzzle_input, 1, 5) *
        check_trees(puzzle_input, 1, 7) *
        check_trees(puzzle_input, 2, 1)
    )
