import sys
import re
import time
from collections import defaultdict

def walk(data, index, meta_data_sum, depth):

    child_nodes_n = data[index]
    meta_data_entries_n= data[index + 1]

    index += 2

    for i in range(child_nodes_n):
        index, meta_data_sum = walk(data, index, meta_data_sum, depth + 1)

    for i in range(meta_data_entries_n):
        meta_data_sum += data[index + i]

    index += meta_data_entries_n

    return index, meta_data_sum


def part1(data):

    p1 = walk(data, 0, 0, 0)
    print(p1[0])


def walkp2(data, index, depth):

    start_index = index
    child_nodes_n = data[index]
    meta_data_entries_n= data[index + 1]

    index += 2

    child_nodes = []
    for i in range(child_nodes_n):
        value, index = walkp2(data, index, depth + 1)
        child_nodes.append(value);

    # for nodes without child nodes
    if child_nodes_n == 0:
        value = 0
        for i in range(meta_data_entries_n):
            value += data[index + i]
        return value, index + meta_data_entries_n

    # for nodes with child nodes
    value = 0
    for i in range(meta_data_entries_n):
        child_index_ref = data[index + i]
        if child_index_ref > len(child_nodes):
            continue
        value += child_nodes[child_index_ref - 1]
    return value, index + meta_data_entries_n


def part2(data):

    p2 = walkp2(data, 0, 0)
    print(p2[0])

def main():

    # instructions = [re.findall(regex, x.rstrip())[0] for x in sys.stdin
    with open('input') as f:
        data = list(map(int, f.readline().rstrip().split(' ')))

    part1(data)
    part2(data)

if __name__ == '__main__':
    main()
