import sys

def severityHit(pc_offset, firewall, firewall_depth):

    range_index = 0
    for pc in range(pc_offset, firewall_depth + pc_offset + 1):

        if range_index not in firewall:
            range_index += 1
            continue

        fw_layers, fw_mod = firewall[range_index]

        # fw at top position?
        if pc % fw_mod == 0:
            return True

        range_index += 1

    return False

def getSeverity(pc_offset, firewall, firewall_depth):

    # calc severity
    severity_hits = 0
    severity = 0
    range_index = 0

    for pc in range(pc_offset, firewall_depth + pc_offset + 1):

        if range_index not in firewall:
            range_index += 1
            continue

        fw_layers, fw_mod = firewall[range_index]

        # fw at top position?
        if pc % fw_mod == 0:
            severity += range_index * fw_layers

        range_index += 1

    return severity


def part1(firewall, firewall_depth):

    severity = getSeverity(0, firewall, firewall_depth);

    return severity

def part2(firewall, firewall_depth):

    pc_offset = 0

    while severityHit(pc_offset, firewall, firewall_depth):
        pc_offset += 1

    return pc_offset

def main():

    input_file_name = 'in'

    firewall = {}
    firewall_depth = 0

    for line in open(input_file_name):
        depth, layers = map(int, line.strip().split(': '))

        firewall_depth = max(firewall_depth, depth)

        # fw will be at top position every mod tick
        mod = 2 + (layers - 2) * 2

        firewall[depth] = (layers, mod)

    print('part 1: ', part1(firewall, firewall_depth))
    print('part 2: ', part2(firewall, firewall_depth))

if __name__ == '__main__':
    main()
