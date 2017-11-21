import re
import sys

re_cpy = re.compile(r'cpy (\d+|\w+) (\w+)')
re_inc = re.compile(r'inc (\w+)')
re_dec = re.compile(r'dec (\w+)')
re_jnz = re.compile(r'jnz (\w+) (-?\d+)')
re_tgl = re.compile(r'tgl (\w+)')

with open('input', 'r') as f:
	instructions  = [line.rstrip() for line in f]

register = {
	'a': 7,
	'b': 0,
	'c': 0,
	'd': 0,
}
fp = 0

def toggle_instruction(reg, fp, register, instructions):

	# toggle instruction
	try:
		line_to_toggle = instructions[fp + register[reg]]
	except:
		return

	# self toggle
	if register[reg] == 0:
		print('self toggle')
		line_to_toggle = 'inc {}'.format(reg)
		try:
			instructions[fp + register[reg]] = line_to_toggle
		except:
			pass

		return

	if line_to_toggle.count(' ') == 1:
		print('one argument')
		if line_to_toggle.startswith('inc'):
			line_to_toggle = 'dec {}'.format(line_to_toggle[4:])
		else:
			line_to_toggle = 'inc {}'.format(line_to_toggle[4:])

		try:
			instructions[fp + register[reg]] = line_to_toggle
		except:
			pass

		return

	if line_to_toggle.count(' ') == 2:
		print('two arguments')
		print(line_to_toggle)
		if line_to_toggle.startswith('jnz'):
			line_to_toggle = 'cpy {}'.format(line_to_toggle[4:])
		else:
			line_to_toggle = 'jnz {}'.format(line_to_toggle[4:])

		try:
			instructions[fp + register[reg]] = line_to_toggle
		except:
			pass

		return

while fp < len(instructions):

	instruction = instructions[fp]

	if instruction.startswith('cpy'):
		try:
			a, reg = re.findall(re_cpy, instruction)[0]
		except:
			fp += 1
			continue
		if a.isdigit():
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
			fp += int(rel)
			continue

	if instruction.startswith('tgl'):
		reg = re.findall(re_tgl, instruction)[0]
		toggle_instruction(reg, fp, register, instructions)

	print(instruction)
	print(register)
	print(fp)
	for instruction in instructions:
		print(instruction)
	# input('next tick')
	fp += 1

print(register)
