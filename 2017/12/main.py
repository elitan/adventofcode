def getStartPid(connections, groups):
    if not groups:
        return '0'

    found_pids = set()
    for group in groups:
        found_pids = found_pids.union(group)

    for pid in connections.keys():

        # found a pid that was not yet found in a group
        if pid not in found_pids:
            return pid

    return False

def addProgramToGroup(pid, connections, group):

    group.add(pid)

    for connected_pid in connections[pid]:

        if connected_pid not in group:
            group.add(connected_pid)
            addProgramToGroup(connected_pid, connections, group)

def part1(connections):

    group_0 = set()

    addProgramToGroup('0', connections, group_0)

    return len(group_0)

def part2(connections):
    groups = []

    # run for as long not all pids is in a group
    while sum([len(x) for x in groups]) < len(connections):

        # find new start pid that is not in a group
        start_pid = getStartPid(connections, groups)

        # add an empty set for this new group
        groups.append(set())

        addProgramToGroup(start_pid, connections, groups[-1])

    return len(groups)

def main():
    input_file_name = 'in'

    connections = {}
    # connection['0'] = ['2', '3']

    for line in open(input_file_name):

        pid, connected_pids = line.strip().split(' <-> ')

        connected_pids = connected_pids.split(', ')

        connections[pid] = connected_pids

    print('part 1: ', part1(connections))
    print('part 2: ', part2(connections))

if __name__ == '__main__':
    main()
