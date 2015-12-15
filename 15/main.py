# a bit inspired by https://github.com/ThomasSievert/advent_of_code/blob/master/aoc15/aoc15.py
import re
import itertools

def prod(i):
	p = 1
	for n in i:
		p *= n
	return p

def perm_iterator(l, n):
	for combo in itertools.combinations_with_replacement(l, n):
		if sum(combo) == 100:
			for perm in itertools.permutations(combo):
				yield perm

cookies = list()
with open('input') as f:
	for line in f:
		cookies.append(map(int, re.findall(ur'-?\d+', line.rstrip())))

p1 = 0
p2 = 0
for perm in perm_iterator(range(101), len(cookies)):

	x = list()
	for i, cookie in enumerate(cookies):
		x.append([ ingredient * perm[i] for j, ingredient, in enumerate(cookie)])
	zipped = map(lambda x: max(sum(x), 0), zip(*x))

	p1_test = prod(zipped[:-1])

	p1 = max(p1, p1_test)
	p2 = max(p2, (zipped[-1] == 500) * p1_test)


print(p1)
print(p2)
