print(sum(len(x.rstrip().split()) == len(set(x.rstrip().split())) for x in open('input')))
print(sum(len([''.join(sorted(y)) for y in x.rstrip().split()]) == len(set([''.join(sorted(y)) for y in x.rstrip().split()])) for x in open('input')))
