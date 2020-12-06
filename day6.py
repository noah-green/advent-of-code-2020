puzzleName = 'Custom Customs'

alpha = 'abcdefghijklmnopqrstuvwxyz'

def solvePart1(puzzleInput):
    return sum(len(set(''.join(group.split()))) for group in puzzleInput.split('\n\n'))


def solvePart2(puzzleInput):
    return sum(len(set(alpha).intersection(*group.split())) for group in puzzleInput.split('\n\n'))
