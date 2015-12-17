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
for c in gen(containers):
	#print(c)
	#print(containers)
	#print(s)
	#print(s, sum(s))
	s = [a*b for a,b in zip(containers,c)]

	if sum(s) == 150:
		p1 += 1
print(p1)
