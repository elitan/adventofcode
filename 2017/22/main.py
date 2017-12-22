import sys
from collections import defaultdict

def part1(input_file_name):

	grid = defaultdict(int)

	for row, line in enumerate(open(input_file_name)):
		for col, node in enumerate(line.rstrip()):
			if node == '#':
				grid[(row, col)] = 1

	# start position
	n = len(open(input_file_name).readline().rstrip()) // 2
	position = (n, n)
	direction = 0 # start facing up

	# 0 = up
	# 1 = right
	# 2 = down
	# 3 = left

	# +1 = right turn
	# -1 = left turn

	# % 4 - not to be forgotten

	direction_map = [
		(-1, 0),
		(0, 1),
		(1, 0),
		(0, -1)
	]

	caused_infections = 0

	for i in range(10000):

		infected = position in grid

		# if infected
		if infected:

			# new direction 'right'
			direction = (direction + 1) % 4

			# remove infection
			del grid[position]

			# move
			position = tuple([a+b for a,b in zip(position, direction_map[direction])])

		elif not infected:

			caused_infections += 1

			# new direction 'left'
			direction = (direction - 1) % 4

			# add infection
			grid[position] = 1

			# move
			position = tuple([a+b for a,b in zip(position, direction_map[direction])])


	return caused_infections

def part2(input_file_name):

	# -1 / None = clean
	# 0 = weaked
	# 1 = infected
	# 2 = flagged
	# -1 / None = clean

	grid = defaultdict(int)

	for row, line in enumerate(open(input_file_name)):
		for col, node in enumerate(line.rstrip()):
			if node == '#':
				grid[(row, col)] = 1

	# start position and direction
	n = len(open(input_file_name).readline().rstrip()) // 2
	position = (n, n)
	prev_position = position
	direction = 0 # start facing up

	direction_map = [
		(-1, 0),
		(0, 1),
		(1, 0),
		(0, -1)
	]

	caused_infections = 0

	for i in range(10000000):

		state = None
		if position in grid:
			state = grid[position]

		# save 'last position'

		if state == None: # clean -> weakened

			# turn left
			direction = (direction - 1) % 4

			# add weakened
			grid[position] = 0

			# move
			prev_position = position
			position = tuple([a+b for a,b in zip(position, direction_map[direction])])

		elif state == 0: # weakened -> infected

			# add infection
			grid[position] = 1

			caused_infections += 1

			# move
			prev_position = position
			position = tuple([a+b for a,b in zip(position, direction_map[direction])])

		elif state == 1: # infected -> flagged

			# turn right
			direction = (direction + 1) % 4

			# add flagged
			grid[position] = 2

			# move
			prev_position = position
			position = tuple([a+b for a,b in zip(position, direction_map[direction])])

		elif state == 2: # flagged -> 'clean'

			del grid[position]

			# calc new direction
			vector = tuple([a-b for a,b in zip(prev_position, position)])
			direction = direction_map.index(vector)

			# move back to last position
			position, prev_position = prev_position, position

		else:
			print('eerrrr unvalid state')
			sys.exit()

	return caused_infections


def main():

	input_file_name = 'in'
	# input_file_name = 'test'

	print('part 1: ', part1(input_file_name))
	print('part 2: ', part2(input_file_name))


if __name__ == '__main__':
	main()
