import re
import itertools
import sys

def calc_value(pl, vs, hh):
	h = 0
	for i in range(len(pl)-1):
		h += vs[pl[i]][pl[i+1]]
		h += vs[pl[i+1]][pl[i]]

	# last and first person:
	h += vs[pl[0]][pl[-1]]
	h += vs[pl[-1]][pl[0]]
	return h

m = re.compile(ur'(\S+) would (gain|lose) (\d+) happiness units by sitting next to (\S+).')

persons = set()
vs = dict()
with open('input') as f:
	for line in f:
		line = line.rstrip()

		g = m.match(line)

		a = g.group(1)
		pn = g.group(2)
		value = int(g.group(3))
		b = g.group(4)

		if a not in vs:
			vs[a] = {}

		vs[a][b] = value if pn == 'gain' else (value * -1)
		persons.add(a)

# ad my self
my_name = 'Me'
vs[my_name] = {}
for p in list(persons):
	vs[my_name][p] = 0
	vs[p][my_name] = 0

persons.add(my_name)

hh = 0
for perm in itertools.permutations(list(persons)):
	tmp_h = calc_value(perm, vs, hh)
	if tmp_h > hh:
		hh = tmp_h

print(hh)