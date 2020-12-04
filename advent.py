import contexttimer
import importlib


days = [
    'day1',  #
    'day2',  #     ___       __                 __
    'day3',  #    /   | ____/ /   _____  ____  / /_
    'day4',  #   / /| |/ __  / | / / _ \/ __ \/ __/
#   'day5',  #  / ___ / /_/ /| |/ /  __/ / / / /_
#   'day6',  # /_/  |_\__,_/ |___/\___/_/ /_/\__/
#   'day7',  #
#   'day8',  #          ____
#   'day9',  #   ____  / __/
#   'day10', #  / __ \/ /_
#   'day11', # / /_/ / __/
#   'day12', # \____/_/
#   'day13', #
#   'day14', #    ______          __
#   'day15', #   / ____/___  ____/ /__
#   'day16', #  / /   / __ \/ __  / _ \
#   'day17', # / /___/ /_/ / /_/ /  __/
#   'day18', # \____/\____/\__,_/\___/
#   'day19', #
#   'day20', #    ___   ____ ___   ____
#   'day21', #   |__ \ / __ \__ \ / __ \
#   'day22', #   __/ // / / /_/ // / / /
#   'day23', #  / __// /_/ / __// /_/ /
#   'day24', # /____/\____/____/\____/
#   'day25', #
]


def advent():
    for day in days:
        mod = importlib.import_module(day)
        with open(f'input/day{days.index(day) + 1}.txt') as f:
            puzzleInput = f.read()
        with contexttimer.Timer() as part1Timer:
            part1Answer = mod.solvePart1(puzzleInput)
        with contexttimer.Timer() as part2Timer:
            part2Answer = mod.solvePart2(puzzleInput)

        print(
        f"""
Day {days.index(day) + 1}: {mod.puzzleName}
-----------------------------------------------------------
Part 1: {part1Answer}, calculated in {part1Timer.elapsed} seconds
Part 2: {part2Answer}, calculated in {part2Timer.elapsed} seconds
        """
        )

if __name__ == '__main__':
    advent()
