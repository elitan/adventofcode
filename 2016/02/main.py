import fileinput

part = 2

def new_pos(current_pos, instruction):
	x, y = current_pos
	if instruction == 'U':
		y += 1
	elif instruction == 'R':
		x += 1
	elif instruction == 'D':
		y -= 1
	elif instruction == 'L':
		x -= 1
	if (x, y) in pos_map[part]:
		return (x, y)
	else:
		return current_pos

pos_map = {
	1: {
		(0, 0): '7',
		(1, 0): '8',
		(2, 0): '9',
		(0, 1): '4',
		(1, 1): '5',
		(2, 1): '6',
		(0, 2): '1',
		(1, 2): '2',
		(2, 2): '3',
	},
	2: {
		(2, 0): 'D',
		(1, 1): 'A',
		(2, 1): 'B',
		(3, 1): 'C',
		(0, 2): '5',
		(1, 2): '6',
		(2, 2): '7',
		(3, 2): '8',
		(4, 2): '9',
		(1, 3): '2',
		(2, 3): '3',
		(3, 3): '4',
		(2, 4): '1',
	}
}

if part == 1:
	current_pos = (1, 1)
elif part == 2:
	current_pos = (0, 2)
code = ''

for line in fileinput.input():
	for instruction in list(line.rstrip()):
		current_pos = new_pos(current_pos, instruction)
	code += pos_map[part][current_pos]
print(code)
