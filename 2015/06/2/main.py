import sys
import re

def get_s_s(s):
	regex = re.findall(r'(\d{1,3},\d{1,3})',s)
	return [map(int, x.split(',')) for x in regex]

def get_type(s):
	if "turn on" in s:
		return 1
	elif "turn off" in s:
		return 2
	elif "toggle" in s:
		return 3

def new_light_value(current_value, t):
	if t == 1:
		return 1
	elif t == 2:
		return 0 if current_value == 0 else -1
	elif t == 3:
		return 2

grid = [[0 for x in range(1000)] for x in xrange(1000)]

with open('input') as f:
	for line in f:
		line = line.rstrip()
		r = get_s_s(line)
		t = get_type(line)

		x_start = r[0][0]
		x_stop = r[1][0]
		x_c = c = 1 if x_stop > x_start else -1
		x_stop += x_c

		y_start = r[0][1]
		y_stop = r[1][1]
		y_c = c = 1 if y_stop > y_start else -1
		y_stop += y_c

		for x in range(x_start,x_stop,x_c):
			for y in range(y_start, y_stop,y_c):
				grid[x][y] += new_light_value(grid[x][y], t)


b = 0
for x in range(1000):
	for y in range(1000):
		b += grid[x][y]
print(b)
