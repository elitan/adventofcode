import re

def valid_k(i, disks):
    for disk in disks:
        if i % disk[1] != disk[0]:
            return False
    return True

disks = []

file_name = 'in-test'
file_name = 'in'
file_name = 'in-2'

lines = [line.rstrip('\n') for line in open(file_name)]
for line in lines:

    n, positions, time, current_position = list(map(int, list(re.findall(r'Disc #(\d+) has (\d+) positions; at time=(\d+), it is at position (\d+).', line)[0])))
    m = ((positions - current_position) - n) % positions
    print('k = {} % {}'.format(m, positions))
    disks.append([m, positions])

found = False
i = 0
while not found:
    i += 1
    if valid_k(i, disks):
        found = True

print('anser: {}'.format(i))
