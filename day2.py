puzzle_name = 'Password Philosophy'


def solution1(puzzle_input):
    valid = 0
    for line in puzzle_input.splitlines():
        policy, password = line.split(':')
        allowed, letter =  policy.split()
        allowed = allowed.split('-')
        allowed = range(int(allowed[0]), int(allowed[1]) + 1)
        valid += 1 if sum(1 for l in password if l == letter) in allowed else 0
    return valid


def solution2(puzzle_input):
    valid = 0
    for line in puzzle_input.splitlines():
        policy, password = line.split(':')
        password = password.strip()
        positions, letter =  policy.split()
        positions = positions.split('-')
        positions = (int(positions[0]), int(positions[1]))
        valid += 1 if (password[positions[0] - 1 ] == letter) ^ (password[positions[1] -1] == letter) else 0
    return valid
