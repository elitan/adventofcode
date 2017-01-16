import sys

with open('in', 'r') as fp:
    lines = [list(map(int, line.rstrip().split('-'))) for line in fp]

lines.sort(key=lambda x: x[0])

first_found = False
i = 0
r = 0
a, z = 0, 0
heighst = 2**32 - 1
for line_i, line in enumerate(lines):
    if z > line[1]:
        continue
    a, z = line
    if a <= i < z:
        i = z + 1
    else:
        if not first_found:
            first_found = True
            print('#1: ', i)
        r += line[0] - i
        i = line[1] + 1

r += heighst - z
print('#2: ', r)
