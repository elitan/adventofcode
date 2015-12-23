# wow, room for so much improvements in this code, time to go back to bed...
import re

def run(instr_index):
	global a, b, instr
	while instr_index < len(instr):
		instr_index = parse_instruction(instr_index)
	
	print("program ended")
	print(a, b)

def parse_instruction(instr_index):
	global a, b, instr

	# jio
	jio = re.findall(ur'jio (a|b), ([+|-]\d+)', instr[instr_index])
	if jio:
		register, offset = jio[0]
		if register == 'a' and a == 1:
			return instr_index + int(offset)
		elif register == 'b' and b == 1:
			return instr_index + int(offset)
		else:
			return instr_index + 1

	# jie
	jie = re.findall(ur'jie (a|b), ([+|-]\d+)', instr[instr_index])
	if jie:
		register, offset = jie[0]
		if register == 'a' and a % 2 == 0:
			return instr_index + int(offset)
		elif register == 'b' and b % 2 == 0:
			return instr_index + int(offset)
		else:
			return instr_index + 1

	# inc
	inc = re.findall(ur'inc ([a|b])', instr[instr_index])
	if inc:
		register = inc[0]
		if register == 'a':
			a += 1
		elif register == 'b':
			b += 1
		return instr_index + 1

	# tpl
	tpl = re.findall(ur'tpl ([a|b])', instr[instr_index])
	if tpl:
		register = tpl[0]
		if register == 'a':
			a *= 3
		elif register == 'b':
			b *= 3
		return instr_index + 1

	# hlf
	hlf = re.findall(ur'hlf ([a|b])', instr[instr_index])
	if hlf:
		register = hlf[0]
		if register == 'a':
			a /= 2
		elif register == 'b':
			b /= 2
		return instr_index + 1

	# jmp
	jmp = re.findall(ur'jmp ([+|-]\d+)', instr[instr_index])
	if jmp:
		offset = jmp[0]
		return instr_index + int(offset)


instr = [f.rstrip() for f in open('input')]
a,b = 0,0 
run(0)
a,b = 1,0 
run(0)
