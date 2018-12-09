# Nils Ingelhag double linked list FTW !!

class List:
	def __init__(self):
		self.current_node = Node(0)

	def insert_right(self, value_of_node):
		new_node = Node(value_of_node)
		tmp_node = self.current_node.right
		self.current_node.right = new_node
		new_node.left = self.current_node
		tmp_node.left = new_node
		new_node.right = tmp_node
		self.current_node = new_node

	def remove_current_node(self):
		ret_value = self.current_node.value
		left = self.current_node.left
		right = self.current_node.right
		left.right = right
		right.left = left
		self.current_node = right
		return ret_value

	def get_current_value(self):
		return self.current_node.value

	def walk_right(self):
		self.current_node = self.current_node.right

	def walk_left(self):
		self.current_node = self.current_node.left


class Node:
	def __init__(self, value):
		self.value = value
		self.left = self
		self.right = self


i = 0
players_n = 466
players = [0 for _ in range(players_n)]
last_marbel = 71436*100
circle = List()

while i <= last_marbel:

	i += 1

	if i % 23 == 0:
		for _ in range(7):
			circle.walk_left()
		players[i % players_n] += i + circle.remove_current_node()
	else:
		circle.walk_right()
		circle.insert_right(i)

print(max(players))
