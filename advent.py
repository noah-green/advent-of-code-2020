import contexttimer
import importlib

days = [
    'day1',
    'day2',
    'day3',
    'day4',
    #'day5',
    #'day6',
    #'day7',
    #'day8',
    #'day9',
    #'day10',
    #'day11',
    #'day12',
    #'day13',
    #'day14',
    #'day15',
    #'day16',
    #'day17',
    #'day18',
    #'day19',
    #'day20',
    #'day21',
    #'day22',
    #'day23',
    #'day24',
    #'day25'
]

def advent():
    for day in days:
        mod = importlib.import_module(day)
        with open(f'input/day{days.index(day) + 1}.txt') as f:
            input = f.read()
        with contexttimer.Timer() as part1Timer:
            part1Answer = mod.solvePart1(input)
        with contexttimer.Timer() as part2Timer:
            part2Answer = mod.solvePart2(input)
        print('---------------------------------------------------------------------------------')
        print(f'Day {days.index(day) + 1}: {mod.puzzleName}')
        print('---------------------------------------------------------------------------------')
        print(f'Part 1: {part1Answer}, calculated in {part1Timer.elapsed} seconds')
        print(f'Part 2: {part2Answer}, calculated in {part2Timer.elapsed} seconds')
        print('---------------------------------------------------------------------------------')
        print('|')

if __name__ == '__main__':
    advent()
