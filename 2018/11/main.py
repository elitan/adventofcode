import re
import sys


def power_level(x, y, serial_number):
	rack_id = x + 10
	power_level = rack_id
	power_level *= y
	power_level += serial_number
	power_level *= rack_id
	if power_level > 100:
		power_level = str(power_level)
		power_level = int(power_level[-3])
	else:
		power_level = 0
	power_level -= 5
	return power_level


def part1(grid):
	max_fuel_level = 0
	max_fuel_level_coordinate = None
	for y in range(1, 297):
		for x in range(1, 297):
			fuel_level = 0
			for y_i in range(3):
				for x_i in range(3):
					fuel_level += grid[y + y_i][x + x_i]

			if fuel_level > max_fuel_level:
				max_fuel_level = fuel_level
				max_fuel_level_coordinate = (x, y)

	return max_fuel_level_coordinate


def part2(grid):
	max_fuel_level = 0
	max_fuel_level_coordinate = None
	for y in range(1, 301):
		for x in range(1, 301):
			max_square_size = min(301 - x, 301 - y)
			fuel_level = 0
			for square_size in range(1, max_square_size):
				for x_i in range(0, square_size):
					fuel_level += grid[y + square_size - 1][x + x_i]
				# do not count bottom right corner value, this value has
				# already been calculated above, hench square_size - 1 here
				# in the range
				for y_i in range(0, square_size - 1):
					fuel_level += grid[y + y_i][x + square_size - 1]

				if fuel_level > max_fuel_level:
					max_fuel_level = fuel_level
					max_fuel_level_coordinate = (x, y, square_size)
					print('new leader: ', max_fuel_level,  max_fuel_level_coordinate)

	return max_fuel_level_coordinate


def main():

	serial_number = 4151
	grid = []
	for y in range(0, 301):
		grid_row = []
		for x in range(0, 301):
			grid_row.append(power_level(x, y, serial_number))
		grid.append(grid_row)


	print(part1(grid))
	print(part2(grid))


if __name__ == '__main__':
	main()
