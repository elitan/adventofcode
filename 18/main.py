import copy
import sys

def light_next_state(grid, h, w, i, j):
	print("something")
	s = 0
	light_on = grid[i][j]
	print(grid)
	if i > 0:
		s += grid[i-1][j]
		print("up", grid[i-1][j])
	if i < h-1:
		s += grid[i+1][j]
		print("down", grid[i+1][j])
	if j > 0:
		s += grid[i][j-1]
		print("left", grid[i][j-1])
	if j < w-1:
		s += grid[i][j+1]
		print("right", grid[i][j+1])

	if light_on:
		print("Light is on :: i: %d, j: %d, s: %d. should be: %d" % (i, j, s, (s == 2 or s == 3)))
		return int(s == 2 or s == 3)
	else:
		print("Light is off :: i: %d, j: %d, s: %d. should be: %d" % (i, j, s, (s == 3)))
		return int(s == 3)

grid = list()
w = 0
h = 0
for line in open('input'):
	line = line.rstrip().replace('.', '0').replace('#', '1')
	grid.append(map(int, list(line)))
	h += 1
w = len(grid[0])


for i in range(4):
	#init tmp array
	tmp_grid = list()
	for i, height in enumerate(range(h)):
		tmp_grid.append([light_next_state(grid, h, w, i, j) for j, width in enumerate(range(w))])

	# next state
	print(grid)
	print(tmp_grid)
	sys.exit()
