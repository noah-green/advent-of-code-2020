puzzleName = 'Passport Processing'

eyeColors = {
    'amb',
    'blu',
    'brn',
    'gry',
    'grn',
    'hzl',
    'oth'
}

def isValidHeight(input):
    if input[-2:] == 'cm' and input[:-2].isdigit():
        return int(input[:-2]) in range(150, 194)
    elif input[-2:] == 'in' and input[:-2].isdigit():
        return int(input[:-2]) in range(59, 77)
    else:
        return False

def solvePart1(input):
    passports = [{j.split(':')[0] : j.split(':')[1] for j in i.split()} for i in input.split('\n\n')]
    def valid(passport):
        return (
            'byr' in passport and
            'iyr' in passport and
            'eyr' in passport and
            'hgt' in passport and
            'hcl' in passport and
            'ecl' in passport and
            'pid' in passport
        )
    return sum(1 for passport in passports if valid(passport))


def solvePart2(input):
    passports = [{j.split(':')[0] : j.split(':')[1] for j in i.split()} for i in input.split('\n\n')]
    def valid(passport):
        return (
            'byr' in passport and int(passport['byr']) in range(1920, 2003) and
            'iyr' in passport and int(passport['iyr']) in range(2010, 2021) and
            'eyr' in passport and int(passport['eyr']) in range(2020, 2031) and
            'hgt' in passport and isValidHeight(passport['hgt']) and
            'hcl' in passport and passport['hcl'][0] == '#' and all(i in 'abcdef1234567890' for i in passport['hcl'][1:]) and
            'ecl' in passport and passport['ecl'] in eyeColors and
            'pid' in passport and len(passport['pid']) == 9 and passport['pid'].isnumeric()
        )
    return sum(1 for passport in passports if valid(passport))
