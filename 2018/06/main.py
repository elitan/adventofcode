import sys
import time
from collections import defaultdict, Counter


def winning_coordinate(coordinate_data):

    # find a winner
    min_coordinate = min(coordinate_data.items(), key=lambda x: x[1])

    # find possible tie
    for k, v in coordinate_data.items():

        # skipp same
        if k == min_coordinate[0]:
            continue

        # return None if tie between two nodes
        if v == min_coordinate[1]:
            return None

    # solo winner
    return min_coordinate[0]


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def part1(coordinates):

    # init edges
    grid_edge_top_left = coordinates[0]
    grid_edge_bottom_right = coordinates[0]

    # find edges
    for coordinate in coordinates:
        x, y = coordinate
        grid_edge_top_left = (min(grid_edge_top_left[0], x), min(grid_edge_top_left[1], y))
        grid_edge_bottom_right = (max(grid_edge_bottom_right[0], x), max(grid_edge_bottom_right[1], y))

    # traverse nodes and grid
    grid_distances = defaultdict(lambda: defaultdict(int))
    for coordinate in coordinates:
        for x in range(grid_edge_top_left[0], grid_edge_bottom_right[0] + 1):
            for y in range(grid_edge_top_left[1], grid_edge_bottom_right[1] + 1):
                # print('({}, {}) - distance: {}'.format(x, y, manhattan_distance([x, y], coordinate)))
                # time.sleep(0.4)
                grid_distances[(x, y)][coordinate] = manhattan_distance([x, y], coordinate)

    edge_winning_coordinates = set()

    # check grid edge to find inf growing coordinates
    # check top and bottom
    for y in [grid_edge_top_left[1], grid_edge_bottom_right[1]]:
        for x in range(grid_edge_top_left[0], grid_edge_bottom_right[0] + 1):
            edge_winning_coordinates.add(winning_coordinate(grid_distances[(x, y)]))


    # check left and right
    for x in [grid_edge_top_left[0], grid_edge_bottom_right[0]]:
        for y in range(grid_edge_top_left[1], grid_edge_bottom_right[1] + 1):
            edge_winning_coordinates.add(winning_coordinate(grid_distances[(x, y)]))

    # remove ties
    edge_winning_coordinates.remove(None)

    # append winners
    coordinate_winners = []
    for coordinate_data in grid_distances.items():

        # find the min data with the min coordinate
        # however, must not be unique
        min_data = min(coordinate_data[1].items(), key=lambda x: x[1])

        # check for ties
        tie_found = False
        for calc_coordinate in coordinate_data[1].items():

            # skipp same
            if calc_coordinate[0] == min_data[0]:
                continue

            if calc_coordinate[1] == min_data[1]:
                tie_found = True
                break

        # tie, skip this coordinate
        if tie_found:
            continue

        min_coordinate, min_distance = min_data
        if min_coordinate not in edge_winning_coordinates:
            coordinate_winners.append(min_coordinate)

    # p1 answer
    print(Counter(coordinate_winners).most_common(1))


def isSafe(current_coordinate, coordinates, safe_limit):
    distance = 0
    for coordinate in coordinates:
        distance += manhattan_distance(current_coordinate, coordinate)

        if distance >= safe_limit:
            return False

    return True


def part2(coordinates, safe_limit):

    # init edges
    grid_edge_top_left = coordinates[0]
    grid_edge_bottom_right = coordinates[0]

    # find edges
    for coordinate in coordinates:
        x, y = coordinate
        grid_edge_top_left = (min(grid_edge_top_left[0], x), min(grid_edge_top_left[1], y))
        grid_edge_bottom_right = (max(grid_edge_bottom_right[0], x), max(grid_edge_bottom_right[1], y))

    safe_region_n = 0
    grid_distances = defaultdict(lambda: defaultdict(int))
    for x in range(grid_edge_top_left[0], grid_edge_bottom_right[0] + 1):
        for y in range(grid_edge_top_left[1], grid_edge_bottom_right[1] + 1):
            safe_region_n += isSafe((x, y), coordinates, safe_limit)

    print(safe_region_n)


def main():
    coordinates = [tuple(map(int, x.rstrip().split(', '))) for x in sys.stdin]

    part1(coordinates)

    safe_limit = 10000
    part2(coordinates, safe_limit)


if __name__ == '__main__':
    main()
