puzzle_name = 'Passport Processing'

eye_colors = {
    'amb',
    'blu',
    'brn',
    'gry',
    'grn',
    'hzl',
    'oth'
}

def is_valid_height(puzzle_input):
    if puzzle_input[-2:] == 'cm' and puzzle_input[:-2].isdigit():
        return int(puzzle_input[:-2]) in range(150, 194)
    elif puzzle_input[-2:] == 'in' and puzzle_input[:-2].isdigit():
        return int(puzzle_input[:-2]) in range(59, 77)
    else:
        return False

def solution1(puzzle_input):
    passports = [{j.split(':')[0] : j.split(':')[1] for j in i.split()} for i in puzzle_input.split('\n\n')]
    def is_valid(passport):
        return (
            'byr' in passport and
            'iyr' in passport and
            'eyr' in passport and
            'hgt' in passport and
            'hcl' in passport and
            'ecl' in passport and
            'pid' in passport
        )
    return sum(1 for passport in passports if is_valid(passport))


def solution2(puzzle_input):
    passports = [{j.split(':')[0] : j.split(':')[1] for j in i.split()} for i in puzzle_input.split('\n\n')]
    def is_valid(passport):
        return (
            'byr' in passport and int(passport['byr']) in range(1920, 2003) and
            'iyr' in passport and int(passport['iyr']) in range(2010, 2021) and
            'eyr' in passport and int(passport['eyr']) in range(2020, 2031) and
            'hgt' in passport and is_valid_height(passport['hgt']) and
            'hcl' in passport and passport['hcl'][0] == '#' and all(i in 'abcdef1234567890' for i in passport['hcl'][1:]) and
            'ecl' in passport and passport['ecl'] in eye_colors and
            'pid' in passport and len(passport['pid']) == 9 and passport['pid'].isnumeric()
        )
    return sum(1 for passport in passports if is_valid(passport))
