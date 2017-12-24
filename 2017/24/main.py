import copy

def part1(components, used_components, connection):
	possible_components = []

	for component in components:
		if connection in component and component not in used_components:
			possible_components.append(component)

	# base case
	if not possible_components:
		return 0

	max_strength = 0
	for component in possible_components:

		# next connection
		nc = component[0] if component[0] != connection else component[1]

		cuc = copy.deepcopy(used_components)
		cuc.add(component)
		v = sum(component) + part1(components, cuc, nc)

		max_strength = max(max_strength, v)

	return max_strength

def part2(components, used_components, connection, depth):
	possible_components = []

	for component in components:
		if connection in component and component not in used_components:
			possible_components.append(component)

	# base case
	if not possible_components:
		return 0, depth

	max_strength = -1
	max_depth = -1
	max_depth_index = -1

	for i, component in enumerate(possible_components):

		# next connection
		nc = component[0] if component[0] != connection else component[1]

		cuc = copy.deepcopy(used_components)
		cuc.add(component)

		s, d = part2(components, cuc, nc, depth + 1)

		# p2 stuff
		sv = sum(component) + s
		if d > max_depth:
			max_depth = d
			max_depth_index = i
			max_strength = sv
		elif d == max_depth:
			if sv > max_strength:
				max_strength = sv
				max_depth_index = i

	return max_strength, max_depth

def main():

	input_file_name = 'test'
	input_file_name = 'in'

	components = []

	for line in open(input_file_name):
		component = tuple(map(int, line.rstrip().split('/')))
		components.append(component)

	connection = 0
	used_components = set()
	m = part1(components, used_components, connection)
	print(m)

	connection = 0
	used_components = set()
	m = part2(components, used_components, connection, 0)
	print(m)

if __name__ == '__main__':
	main()
