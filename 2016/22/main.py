import re
import sys

# part 2 by hand.
# steps to left of top right corner: 49
# then take 31*5 steps to reach next to top left
# then take another step
# 49+31*5+1

with open('in', 'r') as f:
    lines = [line.rstrip() for line in f]
    lines = lines[2:]

xs = 33
ys = 30

# generate 2d grid
grid = []
for iy in range(ys):
    tmp_row = ['.' for ix in range(xs)]
    grid.append(tmp_row)
nodes = {}

# get all avail
for line in lines:
    x, y, total, used, avail, percent = list(map(int, re.findall(r'\/dev\/grid\/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%', line)[0]))
    nodes[(x, y)] = {
        'total': total,
        'used': used,
        'avail': avail,
        'percent': percent
    }

    if used == 0:
        grid[y][x] = '@'

    if used > 100:
        grid[y][x] = '#'

availables_n = 0
for line in lines:
    x, y, total, used, avail, percent = re.findall(r'\/dev\/grid\/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%', line)[0]


for row in grid:
    print(''.join(row))
sys.exit()

for node_key, node_value in nodes.items():

    for avail_key, avail_value in nodes.items():
        if avail_key == node_key:
            continue

        if node_value['used'] > 0 and node_value['used'] < avail_value['avail']:
            print('nodes: ', avail_key, node_key)
            print(node_value['used'], ' < ', avail_value['avail'])
            print(nodes[avail_key])
            print(nodes[node_key])
            print('')
            availables_n += 1

print(availables_n)

# 2
# to come... BFS
