import re


class Grid:
	def __init__(self):
		self.nodes = []
		self.node_coordinates = set()

	def printGrid(self):

		self.node_coordinates = set()
		for node in self.nodes:
			self.node_coordinates.add((node.x, node.y))

		for y in range(0, 200):
			for x in range(0, 300):
				if (x, y) in self.node_coordinates:
					print('#', end='')
				else:
					print('.', end='')
			print('')

	def addNode(self, x, y, vel_x, vel_y):
		self.nodes.append(Node(x, y, vel_x, vel_y))

	def tick(self):
		for node in self.nodes:
			node.move()

	def randomDistance(self):
		a_x = self.nodes[0].x
		a_y = self.nodes[0].y
		b_x = self.nodes[1].x
		b_y = self.nodes[1].y

		return abs(a_x - b_x) + abs(a_y - b_y)


class Node:
	def __init__(self, x, y, vel_x, vel_y):
		self.x = x
		self.y = y
		self.vel_x = vel_x
		self.vel_y = vel_y


	def __str__(self):
		return 'node: {}, {}. {}. {}'.format(self.x, self.y, self.vel_x, self.vel_y)

	def move(self):
		self.x += self.vel_x
		self.y += self.vel_y


def main():

	file_name = 'in'
	regex = r"position=<(.+)> velocity=<(.+)>"

	grid = Grid()

	with open(file_name) as f:
		for line in f:
			parsed_info = re.findall(regex, line.rstrip())[0]
			x, y, = list(map(int, parsed_info[0].split(',')))
			vel_x, vel_y, = list(map(int, parsed_info[1].split(',')))
			grid.addNode(x, y, vel_x, vel_y)

	seconds = 1
	while True:
		grid.tick()
		print(grid.randomDistance())
		if grid.randomDistance() < 50:

			grid.printGrid()
			print('seconds: ', seconds)
			input()
		seconds += 1


if __name__ == '__main__':
	main()
