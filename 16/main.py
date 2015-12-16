import re

mfcsam = [l.rstrip() for l in open('mfcsam')]

p1 = 0;
p1_high = 0;
with open('input') as f:
	for i, line in enumerate(f,1):
		line = line.rstrip() + ','
		score = 0
		for m in mfcsam:
			r = re.findall(m+',', line)
			if r:
				score += 1
		if score > p1_high:
			p1_high = score
			p1 = i
print(p1)

# p2
m_values = dict()
for m in mfcsam:
	name, value = m.split(': ')
	operator = '=='
	if name in ['cats', 'tress']:
		operator = '>'
	elif name in ['pomeranians', 'goldfish']:
		operator = '<'
	m_values[name] = operator+value

p2 = 0
p2_high = 0
with open('input') as f:
	for i, line in enumerate(f,1):
		line = re.sub('Sue \d+: ', '', (line.rstrip()))
		score = 0
		for p in line.split(', '):
			name, value = p.split(': ')
			if eval(value+m_values[name]):
				score += 1
		if score > p2_high:
			p2_high = score
			p2 = i
print(p2)
