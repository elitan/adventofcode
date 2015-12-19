import re
import sys

def replaceNth(s, a, b, n):
	start = -1
	for i in xrange(n):
		start = s.find(a, start+1)
	return s[:start] + b + s[start+len(a):]

start_input = open('input').read()

map_table = dict()
for line in open('mapping'):
	line = line.rstrip()
	find, replace = re.findall(ur'(\w+) => (\w+)', line)[0];
	map_table[replace] = find;

comb_set = set()
for replace, find in map_table.iteritems():
	for i in xrange(start_input.count(find)):
		comb_set.add(replaceNth(start_input, find, replace, i+1))

#print(comb_set)
print(len(comb_set))
