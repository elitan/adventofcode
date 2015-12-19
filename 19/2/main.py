import re
import sys
import time

def replaceNth(s, a, b, n):
	start = -1
	for i in xrange(n):
		start = s.find(a, start+1)
	return s[:start] + b + s[start+len(a):]

def walk(s, depth):
	global map_table
	global correct_depth

	#print("%d, inside walk with :: %s" % (depth, s))
	#time.sleep(0.1)

	# base
	if s == 'e':
		print("DEPTH: ", depth)
		correct_depth.add(depth)
		sys.exit()
		return

	if 'e' in s:
		return

	# recursion
	for find in map_table:
		for i in xrange(s.count(find)):
			s_new = replaceNth(s, find, map_table[find], i+1)
			walk(s_new, depth + 1)

start_input = open('input').read()

map_table = dict()
for line in open('mapping'):
	line = line.rstrip()
	find, replace = re.findall(ur'(\w+) => (\w+)', line)[0];
	map_table[replace] = find;


correct_depth = set()
walk(start_input, 0)

print(correct_depth)
print("lowest depth: ", min(correct_depth))
