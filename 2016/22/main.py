import re
import sys

with open('in', 'r') as f:
    lines = [line.rstrip() for line in f]
    lines = lines[2:]

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

for key, value in nodes.items():
    print(key, value)
    print('')

availables_n = 0
for line in lines:
    x, y, total, used, avail, percent = re.findall(r'\/dev\/grid\/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%', line)[0]

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
