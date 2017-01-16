def find_next_i(lines, i):
    for line in lines:
        a, z = line
        if a <= i and i < z:
            found = True
            i = z + 1
            return i, False
    return i, True

with open('in', 'r') as fp:
    lines = [list(map(int, line.rstrip().split('-'))) for line in fp]

i = 0
found = False
while not found:
    i, found = find_next_i(lines, i)

print(i)
