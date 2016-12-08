import re
import sys

HEIGHT = 6
WIDTH = 50

# HEIGHT = 3
# WIDTH = 7

def n_lit(grid):
	s = 0
	for y in range(HEIGHT):
		for x in range(WIDTH):
			s += grid[y][x]
	return s

def print_grid(grid):
	for y in range(HEIGHT):
		g = list(map(lambda x: '#' if x else '.', grid[y]))
		print(g)
	print('')

def generate_grid(x, y):
	grid = []
	for i in range(y):
		tmp_row = []
		for j in range(x):
			tmp_row.append(0)
		grid.append(tmp_row)
	return grid

re_rect = re.compile(r'rect (\d+)+x(\d+)')
re_rotate = re.compile(r'rotate (row|column) (x|y)=(\d+) by (\d+)')
with open('in', 'r') as f:

	grid = generate_grid(WIDTH, HEIGHT)

	for line in f:
		line = line.rstrip()
		if line[0:4] == 'rect':
			x, y = list(map(int, re_rect.findall(line)[0]))
			for i in range(y):
				for j in range(x):
					grid[i][j] = 1
		else: # rotate
			rc, xy, pos, l = re_rotate.findall(line)[0]
			pos, l = int(pos), int(l)

			if rc == 'row':
				tmp_row = [0 for x in range(WIDTH)]
				for i, p in enumerate(grid[pos]):
					tmp_row[(i + l) % WIDTH] = p
					grid[pos] = tmp_row
			else: # column
				tmp_grid = generate_grid(WIDTH, HEIGHT)
				for y in range(HEIGHT):
					tmp_grid[(y + l) % HEIGHT][pos] = grid[y][pos]

				# copy col to new grid
				for y in range(HEIGHT):
					grid[y][pos] = tmp_grid[y][pos]
		print(line)
		print_grid(grid)
print(n_lit(grid))
