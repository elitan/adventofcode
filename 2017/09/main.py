import re
import sys

def part2():

    s = open('input').readline().strip()

    # remove canceled chars
    s = re.sub('!.', '', s)

    # extract all garbage chars
    s = re.findall('<(.*?)>', s)

    # sum the len of all garbage chars
    garbage_chars = sum([len(x) for x in s])

    return garbage_chars


def part1():

    s = open('input').readline().strip()

    # remove canceled chars
    s = re.sub('!.', '', s)

    # remove all garbage chars
    s = re.sub('<.*?>', '', s)

    score = 0
    total_score = 0

    for c in s:

        if c not in '{}':
            continue

        # one depth 'down' in the recursion
        # depth in terms of score
        if c == '{':
            score += 1
            total_score += score
        else: # one depth up
            score -= 1

    return total_score

def main():
    print('part 1: ', part1())
    print('part 2: ', part2())

if __name__ == '__main__':
    main()
