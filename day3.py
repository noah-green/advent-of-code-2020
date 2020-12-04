puzzleName = 'Tobaggan Trajectory'


def checkTrees(puzzleInput, down, over):
    x = 0
    trees = 0
    for line in puzzleInput.split()[::down]:
        trees += 1 if line[x] == '#' else 0
        x = (x + over) % (len(line))
    return trees


def solvePart1(puzzleInput):
    return checkTrees(puzzleInput, 1, 3)


def solvePart2(puzzleInput):
    return (
        checkTrees(puzzleInput, 1, 1) *
        checkTrees(puzzleInput, 1, 3) *
        checkTrees(puzzleInput, 1, 5) *
        checkTrees(puzzleInput, 1, 7) *
        checkTrees(puzzleInput, 2, 1)
    )
