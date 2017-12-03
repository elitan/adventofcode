# thx thomasjevskij
from collections import defaultdict

def getStressTestData(nodes, loc):

    row, col = loc

    data = 0

    # bottom left, bottom, bottom right
    data += nodes[(row + 1, col - 1)]
    data += nodes[(row + 1, col)]
    data += nodes[(row + 1, col + 1)]

    # left, right
    data += nodes[(row, col + 1)]
    data += nodes[(row, col - 1)]

    # top left, top, top right
    data += nodes[(row - 1, col - 1)]
    data += nodes[(row - 1, col)]
    data += nodes[(row - 1, col + 1)]

    return data

def getNextMove(nodes, loc):

    row, col = loc

    # move right
    if nodes[(row - 1, col)] != 0 and nodes[(row, col + 1)] == 0:
        return (row, col + 1)

    # move up
    if nodes[(row, col - 1)] != 0 and nodes[(row - 1, col)] == 0:
        return (row - 1, col)

    # move left
    if nodes[(row + 1, col)] != 0 and nodes[(row, col - 1)] == 0:
        return (row, col - 1)

    # move down
    if nodes[(row, col + 1)] != 0 and nodes[(row + 1, col)] == 0:
        return (row + 1, col)

def part1(in_data):

    # init first and second element
    nodes = defaultdict(int)
    n = 1
    loc = (0, 0)
    nodes[loc] = n

    n += 1
    loc = (0, 1)
    nodes[loc] = n

    # generate number spiral
    while True:

        n += 1
        loc = getNextMove(nodes, loc)

        nodes[loc] = n

        if n == in_data:
            row, col = loc
            return abs(row) + abs(col)

def part2(in_data):

    # init first and second element
    nodes = defaultdict(int)
    loc = (0, 0)
    nodes[loc] = 1

    loc = (0, 1)
    nodes[loc] = 1

    # generate number spiral
    while True:

        loc = getNextMove(nodes, loc)

        nodes[loc] = getStressTestData(nodes, loc)

        if nodes[loc] > in_data:
            return nodes[loc]


def main():

    in_data = 325489

    print('part 1:')
    print(part1(in_data))

    print('part 2:')
    print(part2(in_data))

if __name__ == '__main__':
    main()
