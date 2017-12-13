import sys

def getSeverity(pc_offset, firewall, firewall_depth):

    # calc severity
    severity_hits = 0
    severity = 0
    range_index = 0
    for pc in range(pc_offset, firewall_depth + pc_offset + 1):

        # check if there is a firewall here. pc is also what range we are at
        if range_index not in firewall:
            range_index += 1
            continue

        fw_layers, fw_mod = firewall[range_index]

        if pc % fw_mod == 0:
            severity += range_index * fw_layers
            severity_hits += 1

        range_index += 1

    return severity, severity_hits


def part1(firewall, firewall_depth):

    severity, severity_hits = getSeverity(0, firewall, firewall_depth);

    return severity

def part2(firewall, firewall_depth):

    pc_delay = 0
    while True:

        # not the best, getSeverity could just return once severity_hits is > 0
        # but it was okey anywayz
        severity, severity_hits = getSeverity(pc_delay, firewall, firewall_depth);

        if severity_hits == 0:
            return pc_delay

        pc_delay += 1

def main():

    input_file_name = 'in'

    firewall = {}
    firewall_depth = 0

    for line in open(input_file_name):
        depth, layers = map(int, line.strip().split(': '))

        firewall_depth = max(firewall_depth, depth)

        mod = 2 + (layers - 2) * 2

        firewall[depth] = (layers, mod)

    print('part 1: ', part1(firewall, firewall_depth))
    print('part 2: ', part2(firewall, firewall_depth))

if __name__ == '__main__':
    main()
