import re
import sys

re_cpy = re.compile(r'cpy (\d+|\w+) (\w+)')
re_inc = re.compile(r'inc (\w+)')
re_dec = re.compile(r'dec (\w+)')
re_jnz = re.compile(r'jnz (\d+|\w+) (-?\d+)')

with open('input', 'r') as f:
	instructions  = [line.rstrip() for line in f]

register = {
	'a': 0,
	'b': 0,
	'c': 1,
	'd': 0,
}
fp = 0

while fp < len(instructions):

	instruction = instructions[fp]

	if instruction.startswith('cpy'):
		a, reg = re.findall(re_cpy, instruction)[0]
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
		a, rel = re.findall(re_jnz, instruction)[0]
		if a.isdigit():
			c = int(a)
		else:
			c = register[a]

		if c != 0:
			fp += int(rel)
			continue
	fp += 1

print(register)
