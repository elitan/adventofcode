import sys

def is_nice(s):
	# check two pair of char
	two_pair_found = False
	for i in range(1, len(s)):
		pair = "%s%s" % (s[i-1], s[i])
		if len(s.split(pair)) == 3:
			two_pair_found = True
			break
	if not two_pair_found:
		return False

	# check two char of the same between one char
	for i in range(2, len(s)):
		if s[i] == s[i-2]:
			return True

	return False

with open ("input", "r") as myfile:
	s = 0
	for line in myfile:
		line = line.rstrip()
		if is_nice(line):
			s += 1

print(s)
