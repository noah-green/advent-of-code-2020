puzzle_name = 'Binary Boarding'

def seat_ID(boarding_pass):
    rowID = boarding_pass[:7]
    colID = boarding_pass[7:]
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
    return row*8 + col


def solution1(puzzle_input):
    return max(seat_ID(boarding_pass) for boarding_pass in puzzle_input.splitlines())


def solution2(puzzle_input):
    seat_IDs = [seat_ID(boarding_pass) for boarding_pass in puzzle_input.splitlines()]
    seat_IDs.sort()
    prev = seat_IDs[0]
    for curr in seat_IDs:
        if curr > prev + 1:
            return prev + 1
        prev = curr
