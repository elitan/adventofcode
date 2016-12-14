import sys

def pos_open(x, y, fn):
	if y < 0 or x < 0:
		return False
	return '{0:b}'.format(x * x + 3 * x + 2 * x * y + y + y * y + fn).count('1') % 2 == 0

def addable_node(x, y, fn, nodes_to_visit, visited_nodes):
	if (x, y) in nodes_to_visit:
		return False
	elif (x, y) in visited_nodes:
		return False
	return pos_open(x, y, fn)

fn = 1352
next_nodes = [(1, 1, -1)]
nodes_to_visit = set()
visited_nodes = set()
node_info = {}

while next_nodes:
	next_node = next_nodes.pop(0)
	x, y, length = next_node
	current_length = length + 1

	if (x, y) == (31, 39):
		print(current_length)

	visited_nodes.add((x, y))
	node_info[(x, y)] = current_length

	if addable_node(x, y + 1, fn, nodes_to_visit, visited_nodes): # top
		next_nodes.append((x, y + 1, current_length))
		visited_nodes.add((x, y + 1))

	if addable_node(x, y - 1, fn, nodes_to_visit, visited_nodes): # bot
		next_nodes.append((x, y - 1, current_length))
		visited_nodes.add((x, y - 1))

	if addable_node(x + 1, y, fn, nodes_to_visit, visited_nodes): # right
		next_nodes.append((x + 1, y, current_length))
		visited_nodes.add((x + 1, y))

	if addable_node(x - 1, y, fn, nodes_to_visit, visited_nodes): # left
		next_nodes.append((x - 1, y, current_length))
		visited_nodes.add((x - 1, y))

s = 0
for k in node_info:
	if node_info[k] <= 50:
		s += 1
print(s)
