import sys


def main():

    nodes = set()
    below_nodes = set()

    for line in open('input'):

        line = line.rstrip().split(' ')

        nodes.add(line[0])

        for n in line[3:]:
            n = n.replace(',', '')
            below_nodes.add(n)

    print(nodes - below_nodes)


if __name__ == '__main__':
    main()
