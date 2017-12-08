import sys
from collections import defaultdict

def part1(input_file_name):

    nodes = set()
    below_nodes = set()

    for line in open(input_file_name):

        line = line.rstrip().split(' ')

        nodes.add(line[0])

        for n in line[3:]:
            n = n.replace(',', '')
            below_nodes.add(n)

    return list(nodes - below_nodes)[0]

def getWeight(nodes, current_node_name):

    weight, children = nodes[current_node_name]

    total_weight = weight

    child_weights = []
    child_weights_dict = {}

    for child in children:
        w = getWeight(nodes, child)
        total_weight += w
        child_weights.append(w)
        child_weights_dict[child] = w

    # if child_weights and not balanced
    if child_weights and child_weights[0] * len(child_weights) != sum(child_weights):

        # since we found the unbalancing, we will exit the program inside this
        # if statement

        # find the correct and wrong weight
        for child_weight in child_weights:
            if child_weights.count(child_weight) == 1:
                wrong_weight = child_weight
            if child_weights.count(child_weight) > 1:
                correct_weight = child_weight

        # find node that is wrong
        for child_name, weight in child_weights_dict.items():

            if weight == wrong_weight:
                wrong_node_name = child_name
                break

        # find the diff
        diff = correct_weight - wrong_weight

        # now calc the correct value for the 'wrong' node
        ret = nodes[wrong_node_name][0] + diff

        print('answer: ', ret)
        sys.exit()

        return ret

    return total_weight

def part2(input_file_name):

    nodes = {}

    for line in open(input_file_name):

        line = line.rstrip().split(' ')

        name = line[0]
        weight = int(line[1][1:-1]) # remove parenteces

        nodes_children = []
        nodes[name] = (weight, nodes_children)

        for n in line[3:]:

            n = n.replace(',', '')

            nodes_children.append(n)

    start_node_name = part1(input_file_name)

    weight = getWeight(nodes, start_node_name)


def main():

    input_file_name = 'input'

    print('part 1:', part1(input_file_name))
    print('part 2:', part2(input_file_name))

if __name__ == '__main__':
    main()
