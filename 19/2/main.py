import re
import sys
import time
import random

def replaceNth(s, a, b, n):
	start = -1
	for i in xrange(n):
		start = s.find(a, start+1)
	return s[:start] + b + s[start+len(a):]

# but slow, works 100%
def good(s, depth):
	global map_table
	global correct_depths

	# base
	if s == 'e':
		print("DEPTH: ", depth)
		correct_depths.add(depth)
		return

	if 'e' in s:
		return

	# recursion
	for find in map_table:
		for i in xrange(s.count(find)):
			s_new = replaceNth(s, find, map_table[find], i+1)
			walk(s_new, depth + 1)

# but fast, works probably <100%
def bad(s):
	global find_table
	s_origin = s
	while s != 'e':
		s = s_origin
		c = 0
		s_old = ''
		random.shuffle(find_table)
		while s_old != s:
			s_old = s
			for find in find_table:
				while find in s:
					c += s.count(find)
					s = s.replace(find, map_table[find])
	return c


start_input = open('input').read()

map_table = dict()
for line in open('mapping'):
	line = line.rstrip()
	find, replace = re.findall(ur'(\w+) => (\w+)', line)[0];
	map_table[replace] = find;

correct_depths = set()
#walk(start_input, 0)
#print(correct_depths)
#print("lowest depth: ", min(correct_depths))

find_table = [k for k in map_table]

print(bad(start_input))
