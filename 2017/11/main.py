from collections import defaultdict
import sys

def cancle_out(directions, direction_steps):

    a, b = directions

    # cancle out a and b
    a_tmp = max(0, direction_steps[a] - direction_steps[b])
    b_tmp = max(0, direction_steps[b] - direction_steps[a])

    direction_steps[a] = a_tmp
    direction_steps[b] = b_tmp

def substitute(s, direction_steps):

    a, b, c = s

    # substitute difference between a and b for c
    c_additions = max(direction_steps[a], direction_steps[b]) - abs(direction_steps[a] - direction_steps[b])
    a_tmp = max(0, direction_steps[a] - direction_steps[b])
    b_tmp = max(0, direction_steps[b] - direction_steps[a])

    direction_steps[a] = a_tmp
    direction_steps[b] = b_tmp
    direction_steps[c] += c_additions


def part1(input_file_name):

    input_str = open(input_file_name).readline().strip().split(',')

    direction_steps = defaultdict(int)

    for direction in list(set(input_str)):
        direction_steps[direction] = input_str.count(direction)

    # calcle outs
    cancle_outs = [
        ['n', 's'],
        ['nw', 'se'],
        ['ne', 'sw']
    ]

    substitutes = [
        ['se', 'sw', 's'],
        ['ne', 'nw', 'n'],
        ['ne', 's', 'se'],
        ['nw', 's', 'sw'],
        ['se', 'n', 'ne'],
        ['sw', 'n', 'nw'],
    ]

    for directions in cancle_outs:
        cancle_out(directions, direction_steps)

    for s in substitutes:
        substitute(s, direction_steps)

    steps = 0
    for key, value in direction_steps.items():
        steps += value

    return steps

def part2(input_file_name):
    pass


def main():

    input_file_name = 'in'
    print('part1: ', part1(input_file_name))
    print('part2: ', part2(input_file_name))
if __name__ == '__main__':
    main()
