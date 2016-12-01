import re
import sys
from numpy import uint16

variables = dict()

def get_operand(op):
	global variables

	if op.isdigit():
		return uint16(op)
	if op in variables:
		return variables[op]
	return None

def operation(s):
	global variables

	operands = ["AND", "OR", "LSHIFT", "RSHIFT"]
	for op in operands:
		if op in s:
			g = re.compile(ur'([a-z]+|\d+) [A-Z]+ ([a-z]+|\d+) -> ([a-z]+)').match(s)
			a = get_operand(g.group(1))
			b = get_operand(g.group(2))
			out = g.group(3)

			if a == None or b == None:
				return False

			if type(a) != uint16 and type(b) != uint16:
				#print(a,op,b,out)
				pass

			if op == "AND":
				variables[out] = a &  b
			elif op == "OR":
				variables[out] = a |  b
			elif op == "LSHIFT":
				variables[out] = a << b
			elif op == "RSHIFT":
				variables[out] = a >> b
			return True

	if "NOT" in s:
		g = re.compile(ur'NOT ([a-z]+|\d+) -> ([a-z]+)').match(s)
		b = get_operand(g.group(1))
		if b == None:
			return False
		out = g.group(2)
		variables[out] = ~b
		return True

	# normal assign variable
	g = re.compile(ur'([a-z]+|\d+) -> ([a-z]+)').match(s)
	b = get_operand(g.group(1))
	if b == None:
		return False
	out = g.group(2)
	variables[out] = uint16(b)
	return True

def operation_2(s):
	global variables

	operands = ["AND", "OR", "LSHIFT", "RSHIFT"]
	for op in operands:
		if op in s:
			g = re.compile(ur'([a-z]+|\d+) [A-Z]+ ([a-z]+|\d+) -> ([a-z]+)').match(s)
			a = get_operand(g.group(1))
			b = get_operand(g.group(2))
			out = g.group(3)

			if out == 'b':
				return True

			if a == None or b == None:
				return False

			if type(a) != uint16 and type(b) != uint16:
				#print(a,op,b,out)
				pass

			if op == "AND":
				variables[out] = a &  b
			elif op == "OR":
				variables[out] = a |  b
			elif op == "LSHIFT":
				variables[out] = a << b
			elif op == "RSHIFT":
				variables[out] = a >> b
			return True

	if "NOT" in s:
		g = re.compile(ur'NOT ([a-z]+|\d+) -> ([a-z]+)').match(s)
		b = get_operand(g.group(1))
		if b == None:
			return True
		out = g.group(2)
		if out == 'b':
			return False
		variables[out] = ~b
		return True

	# normal assign variable
	g = re.compile(ur'([a-z]+|\d+) -> ([a-z]+)').match(s)
	b = get_operand(g.group(1))
	if b == None:
		return False
	out = g.group(2)
	if out == 'b':
		return True	
	variables[out] = uint16(b)
	return True

c = False
while not c:
	with open('input') as f:
		c = True
		for line in f:
			line = line.rstrip()
			if not operation(line):
				#print(line)
				c = False

print(variables['a'])
a_val = variables['a']
variables = None
variables = dict()

variables['b'] = a_val

c = False
while not c:
	with open('input') as f:
		c = True
		for line in f:
			line = line.rstrip()
			if not operation_2(line):
				c = False
print(variables['a'])