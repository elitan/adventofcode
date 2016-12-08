import re

def is_abba(s):
	return len(s) == 4 and s[0] == s[3] and s[1] == s[2] and s[0] != s[1]

def contain_abba(address):
	for i in range(len(address) - 3):
		if is_abba(address[i:i+4]):
			return True
	return False

def support_tls(address, bracket_matches):
	for bm in bracket_matches:
		if contain_abba(bm):
			return False
	return contain_abba(address)

s = 0
re_brackets = re.compile(r'\[\w+\]')
with open('in', 'r') as f:
	for line in f:
		bracket_matches = list(map(lambda x: x.replace('[', '',).replace(']', ''), re_brackets.findall(line)))
		address = re.sub(re_brackets, '----', line.rstrip())
		s += support_tls(address, bracket_matches)
print(s)
