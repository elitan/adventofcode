import re
import sys

def replaceNth(s, a, b, n):
	start = -1
	for i in xrange(n):
		start = s.find(a, start+1)
	return s[:start] + b + s[start+len(a):]

def walk(s):
	global map_table
	for find, replace in map_table:
		a = re.findall(ur'(%s)' % )
	pass

start_input = open('input').read()

map_table = dict()
for line in open('mapping'):
	line = line.rstrip()
	find, replace = re.findall(ur'(\w+) => (\w+)', line)[0];
	map_table[replace] = find;



