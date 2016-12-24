floors = [[] for x in range(4)]

# generator: 0
# chip: 1

floors[3] = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
floors[2] = ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'TG']
floors[1] = ['.', '.', '.', '.', 'TG', 'RG', 'RM', 'CG', 'CM', '.']
floors[0] = ['SG', 'SM', 'PG', 'PM', '.', '.', '.', '.', '.', '.']

for x in reversed(range(len(floors))):
    for y in floors[x]:
        print('{}\t'.format(y), end='')
    print('')
