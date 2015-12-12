class Dealer:
	house_dict = None
	houses_visited = 1

	def __init__(self, start_house):
		self.current_house = start_house
		if not Dealer.house_dict:
			Dealer.house_dict = {"0,0": self.current_house}

	def move(self, direction):
		if direction == '^':
			if not self.current_house.up:
				self.current_house.up = House(self.current_house.x, self.current_house.y+1)
				self.current_house.up.down = self.current_house

				self.connect_house(self.current_house.up)

				self.current_house = self.current_house.up
				Dealer.houses_visited += 1
			else:
				self.current_house = self.current_house.up
		elif direction == '>':
			if not self.current_house.right:
				self.current_house.right = House(self.current_house.x+1, self.current_house.y)
				self.current_house.right.left = self.current_house

				self.connect_house(self.current_house.right)

				self.current_house = self.current_house.right
				Dealer.houses_visited += 1
			else:
				self.current_house = self.current_house.right
		elif direction == 'v':
			if not self.current_house.down:
				self.current_house.down = House(self.current_house.x, self.current_house.y-1)
				self.current_house.down.up = self.current_house

				self.connect_house(self.current_house.down)

				self.current_house = self.current_house.down
				Dealer.houses_visited += 1
			else:
				self.current_house = self.current_house.down
		elif direction == '<':
			if not self.current_house.left:
				self.current_house.left = House(self.current_house.x-1, self.current_house.y)
				self.current_house.left.right = self.current_house

				self.connect_house(self.current_house.left)

				self.current_house = self.current_house.left
				Dealer.houses_visited += 1
			else:
				self.current_house = self.current_house.left

		self.current_house.visit()

	def connect_house(self, house):
		if not house.up:
			house.up = self.find_and_connect_house(house.x,house.y+1)
			if house.up:
				house.up.down = house
		if not house.right:
			house.right = self.find_and_connect_house(house.x+1,house.y)
			if house.right:
				house.right.left = house
		if not house.down:
			house.down = self.find_and_connect_house(house.x,house.y-1)
			if house.down:
				house.down.up = house
		if not house.left:
			house.left = self.find_and_connect_house(house.x-1,house.y)
			if house.left:
				house.left.right = house

		self.add_house(house)

	def find_and_connect_house(self, x, y):
		#print("searching: %d, %d" % (x,y))
		try:
			return Dealer.house_dict["%d,%d" % (x,y)]
		except:
			return None

	def add_house(self, house):
		Dealer.house_dict["%d,%d" % (house.x, house.y)] = house


class House:
	def __init__(self, x, y):
		self.x = x
		self.y = y

		self.up = None
		self.right = None
		self.down = None
		self.left = None
		self.visited = 0

	def visit(self):
		self.visited += 1

	def __str__(self):
		return "%d, %d : v: %d" % (self.x, self.y, self.visited)


# part 1

start_house = House(0,0)

s = Dealer(start_house)
rs = Dealer(start_house)
with open ("input", "r") as myfile:
	data=myfile.read().rstrip()

for i, direction in enumerate(list(data)):
	if i % 2 == 0:
		s.move(direction)
	else:
		rs.move(direction)
print(s.houses_visited)