import re
import sys

re_cpy = re.compile(r'cpy (-?\d+|\w+) (\w+)')
re_inc = re.compile(r'inc (\w+)')
re_dec = re.compile(r'dec (\w+)')
re_jnz = re.compile(r'jnz (\d+|\w+) (-?\d+|\w+)')
re_tgl = re.compile(r'tgl (\d+|\w+)')

with open('input', 'r') as f:
	instructions  = [line.rstrip() for line in f]

register = {
	'a': 12,
	'b': 0,
	'c': 0,
	'd': 0,
}

fp = 0

while fp < len(instructions):

	instruction = instructions[fp]

	if instruction.startswith('cpy'):

		try:
			a, reg = re.findall(re_cpy, instruction)[0]
		except:
			fp += 1
			continue

		if a.lstrip('-').isdigit():
			register[reg] = int(a)
		else:
			register[reg] = register[a]

	if instruction.startswith('inc'):
		reg = re.findall(re_inc, instruction)[0]
		register[reg] += 1

	if instruction.startswith('dec'):
		reg = re.findall(re_dec, instruction)[0]
		register[reg] -= 1

	if instruction.startswith('jnz'):
		try:
			a, rel = re.findall(re_jnz, instruction)[0]
		except:
			fp += 1
			continue

		if a.isdigit():
			c = int(a)
		else:
			c = register[a]

		if c != 0:

			# how much should we jump?
			if rel.lstrip('-').isdigit():
				rel = int(rel)
			else:
				rel = register[rel]

			fp += int(rel)
			continue

	if instruction.startswith('tgl'):
		reg = re.findall(re_tgl, instruction)[0]

		try:
			instr_to_change = instructions[fp + register[reg]]
		except:
			# trying to modify instruction outside instruction scope
			fp += 1
			continue

		# for one-argurment instructions
		if instr_to_change.count(' ') == 1:

			if instr_to_change.startswith('inc'):
				instr_to_change = 'dec {}'.format(instr_to_change[4:])
			else:
				instr_to_change = 'inc {}'.format(instr_to_change[4:])

		elif instr_to_change.count(' ') == 2:

			if instr_to_change.startswith('jnz'):
				instr_to_change = 'cpy {}'.format(instr_to_change[4:])
			else:
				instr_to_change = 'jnz {}'.format(instr_to_change[4:])

		instructions[fp + register[reg]] = instr_to_change

	fp += 1

print(register)
