# wrong answer 16,52
import re
import sys


def getNextCoordinate(x, y, direction):
	if direction == 0:
		return (x, y - 1)
	elif direction == 1:
		return (x + 1, y)
	elif direction == 2:
		return (x, y + 1)
	elif direction == 3:
		return (x - 1, y)


def getNewIntersectionDirection(current_direction, intersections):
	x = intersections % 3
	if x == 0: # left
		return (current_direction - 1) % 4
	elif x == 1:
		return current_direction
	elif x == 2:
		return (current_direction + 1) % 4


def getNewTurnDirection(current_direction, c):
	if current_direction == 1: # currently >
		if c == '\\':
			return 2
		if c == '/':
			return 0
	elif current_direction == 3: # currently <
		if c == '\\':
			return 0
		elif c == '/':
			return 2
	elif current_direction == 0: # currently ^
		if c == '\\':
			return 3
		elif c == '/':
			return 1
	elif current_direction == 2: # currently v
		if c == '\\':
			return 1
		elif c == '/':
			return 3


def main():

	directions = {}
	directions['^'] = 0
	directions['>'] = 1
	directions['v'] = 2
	directions['<'] = 3

	grid = []
	carts = {} # key: (x, y) - direction, intersections

	with open('in') as f:
		for y, line in enumerate(f):
			grid.append(list(line.rstrip()))
			for x, c in enumerate(line.rstrip()):
				if c in ['^', '>', 'v', '<']:
					# print('found x: ', x, 'y: ', y, 'c: ', c)
					carts[(x, y)] = [directions[c], 0]
					grid[y][x] = '.'

	while True:

		# for y, row in enumerate(grid):
		# 	for x, grid_c in enumerate(row):
		# 		try:
		# 			c = carts[(x, y)][0]
		# 		except:
		# 			c = grid_c
		# 		print(c, end='')
		# 	print('')

		new_carts_dict = {}
		carts_list = list(carts.items())
		carts_list.sort()
		crash_coordinates = set(list(carts.keys()))
		print('crash_coordinates: ', crash_coordinates)

		for coordinate, data in carts_list:
			x, y = coordinate
			crash_coordinates.remove((x, y))
			direction, intersections = data

			next_x, next_y = getNextCoordinate(x, y, direction)
			if (next_x, next_y) in crash_coordinates:
				print('found crash:')
				print((next_x, next_y))
				input()
			else:
				crash_coordinates.add((next_x, next_y))

			if grid[next_y][next_x] in ['/', '\\']:
				direction = getNewTurnDirection(direction, grid[next_y][next_x])
			if grid[next_y][next_x] == '+':
				direction = getNewIntersectionDirection(direction, intersections)
				intersections += 1

			new_carts_dict[(next_x, next_y)] = [direction, intersections]

		carts = new_carts_dict


if __name__ == '__main__':
	main()
