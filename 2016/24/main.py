import sys
import itertools

def getSearchableNodes(grid, nodes_visited, nodes_to_visit_next, current_location):
    row, col = current_location

    # check up, down, left right for a node that is not a wall and
    # has not already been visited or should be visit soon

    searchable_nodes = []

    if grid[row + 1][col][0] != '#' and (row + 1, col) not in nodes_visited and [row + 1, col] not in nodes_to_visit_next:
        searchable_nodes.append([row + 1, col])
    if grid[row - 1][col][0] != '#' and (row - 1, col) not in nodes_visited and [row - 1, col] not in nodes_to_visit_next:
        searchable_nodes.append([row - 1, col])
    if grid[row][col + 1][0] != '#' and (row, col + 1) not in nodes_visited and [row, col + 1] not in nodes_to_visit_next:
        searchable_nodes.append([row, col + 1])
    if grid[row][col - 1][0] != '#' and (row, col - 1) not in nodes_visited and [row, col - 1] not in nodes_to_visit_next:
        searchable_nodes.append([row, col - 1])

    return searchable_nodes;


def getDistance(start_n, end_n, grid, number_locations):

    start_location = number_locations[start_n]
    end_location = number_locations[end_n]

    # set start location to distance 0
    distance = 0
    grid[start_location[0]][start_location[1]][1] = distance


    # using set and tuple for quicker lookup
    nodes_visited = set()
    nodes_visited.add(tuple(start_location))

    nodes_to_visit = getSearchableNodes(grid, nodes_visited, [], start_location)

    while len(nodes_to_visit):

        distance += 1

        nodes_to_visit_next = []
        for i, node_location in enumerate(nodes_to_visit):

            if node_location == end_location:
                return distance

            # add node to visited nod
            nodes_visited.add(tuple(node_location))

            grid[node_location[0]][node_location[1]][1] = distance

            nodes_to_visit_next += getSearchableNodes(grid, nodes_visited, nodes_to_visit_next, node_location)

        nodes_to_visit = nodes_to_visit_next

    return 'error, no route found'

def main():

    grid = [];
    number_locations = {}

    with open('input') as fh:
        for row, line in enumerate(fh):

            # set distance to inf
            line = [ [x, -1] for x in list(line.rstrip())]

            # build the grid
            grid.append(line)

            # get number locations
            for col, node in enumerate(line):
                element, distance = node
                if element.isdigit():
                    number_locations[int(element)] = [row, col]


    # find shortest path cost between all combinations of all number locations
    distances = {}
    for a in itertools.combinations([ x for x in number_locations], 2):

        # reset distance
        for row in grid:
            for element in row:
                element[1] = -1

        # get distance between start_n and end_n
        start_n, end_n = a
        distances[(start_n, end_n)] = getDistance(start_n, end_n, grid, number_locations)

    # remove start location from possible routes
    route_locations = []
    for x in number_locations:
        if x > 0:
            route_locations.append(x)


    # test all possible routes and see what distance is best

    minimal_distance_a1 = 10**10
    minimal_distance_a2 = 10**10

    for a in itertools.permutations(route_locations):

        if '0' in a:
            continue

        # get starting distance between start location and first node
        total_distance = distances[(0, a[0])]

        for x in range(0, len(a) - 1):

            # get min and max v to get the key right at the distances var
            max_v = max(a[x], a[x + 1])
            min_v = min(a[x], a[x + 1])

            # add total distance
            total_distance += distances[(min_v, max_v)]

        minimal_distance_a1 = min(minimal_distance_a1, total_distance)

        # add distance back to 0
        minimal_distance_a2 = min(minimal_distance_a2, (total_distance + distances[(0, a[-1])]))

    print('minimal_distance_a1: ', minimal_distance_a1)
    print('minimal_distance_a2: ', minimal_distance_a2)


if __name__ == '__main__':
    main()
