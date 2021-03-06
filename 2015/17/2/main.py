import itertools
import sys
import time

def gen(containers):
	i = 1
	while i < 2**len(containers):
		yield map(int, list("{0:b}".format(i).zfill(len(containers))))
		i += 1

containers = map(int, [ f.rstrip() for f in open('input')])

p1 = 0
target = 150
sums = dict()
for c in gen(containers):
	s = [a*b for a,b in zip(containers,c)]

	if sum(s) == target:
		p1 += 1
		c_sum = sum(c)
		if c_sum in sums:
			sums[c_sum] += 1
		else:
			sums[c_sum] = 1
print(p1)
print(sums)
