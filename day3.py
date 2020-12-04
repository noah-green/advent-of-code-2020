puzzleName = 'Tobaggan Trajectory'

def checkTrees(input, down, over):
    x = 0
    trees = 0
    for line in input.split()[::down]:
        trees += 1 if line[x] == '#' else 0
        x = (x + over) % (len(line))
    return trees


def solvePart1(input):
    return checkTrees(input, 1, 3)


def solvePart2(input):
    return (
        checkTrees(input, 1, 1) *
        checkTrees(input, 1, 3) *
        checkTrees(input, 1, 5) *
        checkTrees(input, 1, 7) *
        checkTrees(input, 2, 1)
    )
