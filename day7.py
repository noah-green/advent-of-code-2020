puzzle_name = 'Handy Haversacks'


from collections import defaultdict
from functools import lru_cache


def solution1(puzzle_input):
    outer_colors = defaultdict(set)
    for line in puzzle_input.splitlines():
        outer_color, line = list(map(str.strip, line.split('bags contain')))
        if line == 'no other bags.':
            continue
        inner_colors = [' '.join(clause.split()[1:3]) for clause in line.split(',')]
        for inner_color in inner_colors:
            outer_colors[inner_color].add(outer_color)
    def outermost_colors(color, result = set()):
        for outer_color in outer_colors[color].difference(result):
            result = result.union(outermost_colors(outer_color, result))
            result.add(outer_color)
        return result
    return len(outermost_colors('shiny gold'))


def solution2(puzzle_input):
    contained_bags = {}
    for line in puzzle_input.splitlines():
        bag, line = list(map(str.strip, line.split('bags contain')))
        if line == 'no other bags.':
            contained_bags[bag] = []
            continue
        contained_bags[bag] = [(' '.join(clause[1:3]), int(clause[0])) for clause in map(str.split, line.split(','))]
    @lru_cache
    def total_contained_bags(bag):
        return sum(total_contained_bags(contained_bag) * num + num for contained_bag, num in contained_bags[bag])
    return total_contained_bags('shiny gold')
