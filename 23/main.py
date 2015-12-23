def run(instructions, registers, pc_start):
	pc = pc_start
	while pc >= 0 and pc < len(instructions):
		pc = parse_instruction(instructions, registers, pc)

def parse_instruction(instructions, registers, pc):
	instr_list = instructions[pc].replace(',', '').split(' ')
	instr = instr_list[0]

	if instr == 'hlf':
		registers[instr_list[1]] /= 2
	elif instr == 'tpl':
		registers[instr_list[1]] *= 3
	elif instr == 'inc':
		registers[instr_list[1]] += 1
	elif instr == 'jmp':
		return pc + int(instr_list[1])
	elif instr == 'jie':
		if registers[instr_list[1]] % 2 == 0:
			return pc + int(instr_list[2])
	elif instr == 'jio':
		if registers[instr_list[1]] == 1:
			return pc + int(instr_list[2])
	return (pc + 1)

instructions = [f.rstrip() for f in open('input')]

registers = {'a': 0, 'b': 0}
run(instructions, registers, 0)
print("p1", registers)

registers = {'a': 1, 'b': 0}
run(instructions, registers, 0)
print("p2", registers)
