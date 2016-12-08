import re

def support_ssl(address, bracket_matches):
	bab_set = set()
	for i in range(len(address) - 2):
		a, b, c = address[i: i+3]
		if a == c and a != b:
			bab_set.add('{}{}{}'.format(b, a, b))

	for bm in bracket_matches:
		for i in range(len(bm) - 2):
			if bm[i:i + 3] in bab_set:
				return True
	return False

s = 0
re_brackets = re.compile(r'\[\w+\]')
with open('in', 'r') as f:
	for line in f:
		bracket_matches = list(map(lambda x: x.replace('[', '',).replace(']', ''), re_brackets.findall(line)))
		address = re.sub(re_brackets, '----', line.rstrip())
		s += support_ssl(address, bracket_matches)
print(s)
