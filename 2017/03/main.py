def getStressTestData(nodes, loc):

    row, col = loc

    data = 0


    # bottom left, bottom, bottom right
    try:
        data += nodes[(row + 1, col - 1)]
    except:
        pass
    try:
        data += nodes[(row + 1, col)]
    except:
        pass
    try:
        data += nodes[(row + 1, col + 1)]
    except:
        pass

    # left, right
    try:
        data += nodes[(row, col + 1)]
    except:
        pass
    try:
        data += nodes[(row, col - 1)]
    except:
        pass

    # top left, top, top right
    try:
        data += nodes[(row - 1, col - 1)]
    except:
        pass
    try:
        data += nodes[(row - 1, col)]
    except:
        pass
    try:
        data += nodes[(row - 1, col + 1)]
    except:
        pass

    return data

def getNextMove(nodes, loc):

    row, col = loc

    # move right
    if (row - 1, col) in nodes and (row, col + 1) not in nodes:
        return (row, col + 1)

    # move up
    if (row, col -1) in nodes and (row - 1, col) not in nodes:
        return (row - 1, col)

    # move left
    if (row + 1, col) in nodes and (row, col - 1) not in nodes:
        return (row, col - 1)

    # move down
    if (row, col + 1) in nodes and (row + 1, col) not in nodes:
        return (row + 1, col)

def part1(in_data):

    # init
    nodes = {}
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

    # init
    nodes = {}
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
