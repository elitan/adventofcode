from collections import defaultdict

def main():

	# test
	blueprint = {}
	blueprint['A'] = {
		0: (1, 1, 'B'),
		1: (0, -1, 'B')
	}
	blueprint['B'] = {
		0: (1, -1, 'A'),
		1: (1, 1, 'A')
	}
	steps = 6

	# real
	blueprint = {}
	blueprint['A'] = {
		0: (1, 1, 'B'),
		1: (1, -1, 'E')
	}
	blueprint['B'] = {
		0: (1, 1, 'C'),
		1: (1, 1, 'F')
	}
	blueprint['C'] = {
		0: (1, -1, 'D'),
		1: (0, 1, 'B')
	}
	blueprint['D'] = {
		0: (1, 1, 'E'),
		1: (0, -1, 'C')
	}
	blueprint['E'] = {
		0: (1, -1, 'A'),
		1: (0, 1, 'D')
	}
	blueprint['F'] = {
		0: (1, 1, 'A'),
		1: (1, 1, 'C')
	}
	steps = 12523873

	pos = 0
	state = 'A'
	tape = defaultdict(int)

	for i in range(steps):

		value = tape[pos]
		rule = blueprint[state][value]

		tape[pos] = rule[0]
		pos += rule[1]
		state = rule[2]

	print(sum(tape.values()))


if __name__ == '__main__':
	main()
