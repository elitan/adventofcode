import itertools
from functools import reduce

sizes = map(int, [f.rstrip() for f in open('input')])

def lowest_group(sizes, groups):
	target_weight = sum(sizes) / groups 
	for x in range(1, len(sizes)-1):
		for comb in itertools.combinations(sizes, x):
			if sum(comb) == target_weight: #first one to find got lowest numbers from itertools.combinations
				return reduce(lambda x,y: x*y, comb, 1)

print(lowest_group(sizes, 3))
print(lowest_group(sizes, 4))
