import re
import sys

re_cpy = re.compile(r'cpy (\d+|\w+) (\w+)')
re_inc = re.compile(r'inc (\w+)')
re_dec = re.compile(r'dec (\w+)')
re_jnz = re.compile(r'jnz (\d+|\w+) (-?\d+)')
re_out = re.compile(r'out (-?\d+|\w+)')

def isClickSignal(a):

	with open('input', 'r') as f:
		instructions  = [line.rstrip() for line in f]

	signal_checked = 0
	signal_checks = 64

	last_signal = None

	register = {
		'a': a,
		'b': 0,
		'c': 0,
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
		if instruction.startswith('out'):
			v = re.findall(re_out, instruction)[0]

			if v.lstrip('-').isdigit():
				output = int(v)
			else:
				output = register[v]

			if last_signal == output:
				return False

			if output not in [0, 1, None]:
				return False

			last_signal = output
			signal_checked += 1


		if signal_checked == signal_checks:
			return True

		fp += 1


a = 0
while not isClickSignal(a):
	a += 1
print('corrent answer: ', a)
