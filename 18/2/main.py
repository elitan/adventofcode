import copy
import sys

def light_next_state(grid, h, w, i, j):
	s = 0
	light_on = grid[i][j]
	if i > 0:
		# up
		s += grid[i-1][j]
		if j > 0:
			#up left
			s += grid[i-1][j-1]
		if j < w - 1:
			#up right
			s += grid[i-1][j+1]
	if i < h-1:
		#down
		s += grid[i+1][j]
		if j > 0:
			#down left
			s += grid[i+1][j-1]
		if j < w - 1:
			#down right
			s += grid[i+1][j+1]
	if j > 0:
		#left
		s += grid[i][j-1]
	if j < w-1:
		#right
		s += grid[i][j+1]

	if light_on:
		return int(s == 2 or s == 3)
	else:
		return int(s == 3)

grid = list()
w = 0
h = 0
for line in open('input'):
	line = line.rstrip().replace('.', '0').replace('#', '1')
	grid.append(map(int, list(line)))
	h += 1
w = len(grid[h-1])


for i in range(100):
	#init tmp array
	tmp_grid = list()
	for i, height in enumerate(range(h)):
		tmp_grid.append([light_next_state(grid, h, w, i, j) for j, width in enumerate(range(w))])

	# p2, turn on corders
	tmp_grid[0][0] = 1
	tmp_grid[0][w-1] = 1
	tmp_grid[h-1][0] = 1
	tmp_grid[h-1][w-1] = 1

	grid = tmp_grid

p1 = 0
for r in tmp_grid:
	p1 += sum(r)
print(p1)