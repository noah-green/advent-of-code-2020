puzzleName = 'Binary Boarding'

def calcSeat(boardingPass):
    rowID = boardingPass[:7]
    colID = boardingPass[7:]
    row = range(128)
    col = range(8)
    for i in rowID:
        if i == 'F':
            row = row[:len(row)//2]
        if i == 'B':
            row = row[len(row)//2:]
    row = row[0]
    for i in colID:
        if i == 'L':
            col = col[:len(col)//2]
        if i == 'R':
            col = col[len(col)//2:]
    col = col[0]
    return (row, col)

def calcSeatID(seat):
    return seat[0] * 8 + seat[1]

def getSeatfromID(seatID):
    return (seatID//8, seatID%8)


def solvePart1(puzzleInput):
    passes = puzzleInput.split()
    seats =  [calcSeat(boardingPass) for boardingPass in passes]
    return max(seat[0] * 8 + seat[1] for seat in  seats)


def solvePart2(puzzleInput):
    seatsIDs = [calcSeatID(calcSeat(boardingPass)) for boardingPass in puzzleInput.split()]
    seatsIDs.sort()
    prevSeatID = seatsIDs[0]
    for i in seatsIDs:
        if i > prevSeatID + 1:
            return prevSeatID + 1
        prevSeatID = i
