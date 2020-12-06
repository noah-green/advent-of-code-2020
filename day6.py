puzzleName = 'Custom Customs'

def solvePart1(puzzleInput):
    return sum(len(set().union(*group.split())) for group in puzzleInput.split('\n\n'))


def solvePart2(puzzleInput):
    return sum(len(set('abcdefghijklmnopqrstuvwxyz').intersection(*group.split())) for group in puzzleInput.split('\n\n'))
