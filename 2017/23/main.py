from collections import defaultdict

def getValue(v, register):
    if v.replace('-', '').isdigit():
        return int(v)
    return register[v]


def main():

	register = defaultdict(int)
	register['a'] = 1
	pc = 0
	mul = 0

	instructions = []
	for line in open('in'):
		instructions.append(line.strip().split(' '))

	while pc >= 0 and pc < len(instructions):


		instr, a, b = instructions[pc]

		if instr == 'set':
			register[a] = getValue(b, register)
		elif instr == 'sub':
			register[a] -= getValue(b, register)
		elif instr == 'mul':
			register[a] *= getValue(b, register)
			mul += 1
		elif instr == 'jnz':
			if getValue(a, register) != 0:
				pc += getValue(b, register)
				continue

		pc += 1

	print(register)
	print(mul)

if __name__ == '__main__':
	main()
