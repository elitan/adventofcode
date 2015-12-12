import sys
import copy

def second_min(l):
	ltmp = copy.deepcopy(l)
	del ltmp[ltmp.index(min(ltmp))]
	return min(ltmp)

#part 1
s = 0
with open('input') as f:
	for line in f:
		line = line.rstrip()
		a,b,c = map(int, line.split('x'))
		s += 2*a*b+2*b*c+2*c*a + min([a*b,b*c,c*a])
print(s)

# part 2
s = 0
with open('input') as f:
	for line in f:
		line = line.rstrip()
		a,b,c = map(int, line.split('x'))
		s += 2*min(a,b,c) + 2*second_min([a,b,c]) + a*b*c
print(s)