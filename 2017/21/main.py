import numpy as np
import sys

def oneLineToGrid(line):
	return np.array([ list(x) for x in line.split('/') ])

def gridToOneLine(grid):
	return '/'.join([ ''.join(x) for x in grid])

def transform(sub_grid, trans_map):

	# look and rotate
	for _ in range(4):
		ol = gridToOneLine(sub_grid)
		if ol in trans_map:
			return trans_map[ol]
		sub_grid = np.rot90(sub_grid)

	# flip
	sub_grid = np.flipud(sub_grid)

	# look and rotate
	for _ in range(4):
		ol = gridToOneLine(sub_grid)
		if ol in trans_map:
			return trans_map[ol]
		sub_grid = np.rot90(sub_grid)

	print('no trans found... exit')
	sys.exit()

def run(input_file_name, iterations):

	input_file_name = 'test'
	input_file_name = 'in'

	# start grid
	grid = np.array([list('.#.'), list('..#'), list('###')])

	trans_map = {}
	for line in open(input_file_name):

		line = line.rstrip()

		a, b = line.split(' => ')

		trans_map[a] = oneLineToGrid(b)

	for x in range(iterations):

		# first special case
		if len(grid) == 3:
			grid = transform(grid, trans_map)
			continue

		# n = size of the sub_grids
		if len(grid) % 2 == 0:
			n = 2
		else:
			n = 3

		tmp_grid_y = None
		tmp_grid_y_set = None
		for i in range(len(grid) // n):

			tmp_grid_x = None
			tmp_grid_x_set = False
			for j in range(len(grid) // n):

				# get the tranformed sub grid
				sub_grid = transform(grid[i*n:i * n + n, j * n:j * n + n], trans_map)

				# append current sub_grid to our tmp_grid
				if not tmp_grid_x_set:
					tmp_grid_x = sub_grid
					tmp_grid_x_set = True
				else:
					tmp_grid_x = np.append(tmp_grid_x, sub_grid, axis=1)

			# add a new x row to the tmp_grid_y
			if not tmp_grid_y_set:
				tmp_grid_y = tmp_grid_x
				tmp_grid_y_set = True
			else:
				tmp_grid_y = np.append(tmp_grid_y, tmp_grid_x, axis=0)

		# our grid is complete in tmp_grid_y. Assign to grid an continue to next
		# iteration
		grid = tmp_grid_y


	s = 0
	for row in grid:
		for item in row:
			s += item == '#'
	return s

def main():

	input_file_name = 'in'

	print('part 1: ', run(input_file_name, 5))
	print('part 2: ', run(input_file_name, 18))


if __name__ == '__main__':
	main()
