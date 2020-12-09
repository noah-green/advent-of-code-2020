import contexttimer
import importlib


advent = [
    'day1',  #
    'day2',  #     ___       __                 __
    'day3',  #    /   | ____/ /   _____  ____  / /_
    'day4',  #   / /| |/ __  / | / / _ \/ __ \/ __/
    'day5',  #  / ___ / /_/ /| |/ /  __/ / / / /_
    'day6',  # /_/  |_\__,_/ |___/\___/_/ /_/\__/
    'day7',  #
    'day8',  #          ____
    'day9',  #   ____  / __/
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

template = """
Day {day}: {puzzle_name}
-----------------------------------------------------------
Part 1: {solution1}, calculated in {time1} seconds
Part 2: {solution2}, calculated in {time2} seconds
"""

if __name__ == '__main__':
    for day in range(1, len(advent) + 1):
        puzzle = importlib.import_module(advent[day - 1])
        with open(f'input/day{day}.txt') as infile, contexttimer.Timer() as timer1, contexttimer.Timer() as timer2:
            puzzle_input = infile.read()
            print(template.format(
                day = day,
                puzzle_name= puzzle.puzzle_name,
                solution1 = puzzle.solution1(puzzle_input),
                time1= timer1.elapsed,
                solution2 = puzzle.solution2(puzzle_input),
                time2 = timer2.elapsed
            ))
