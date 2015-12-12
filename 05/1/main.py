import sys

def is_nice(s):
	# check if 3 vowels
	vowels = 0
	vowels_list = ['a', 'e', 'i', 'o', 'u']
	for c in s:
		if c in vowels_list:
			vowels += 1

	if vowels < 3:
		return False

	# check double chars in row
	double_char_found = False
	for i in range(1, len(s)):
		if s[i-1] == s[i]:
			double_char_found = True
			break

	if not double_char_found:
		return False

	good = True
	not_allowed_strings = ['ab', 'cd', 'pq', 'xy']
	for nas in not_allowed_strings:
		if nas in s:
			good = False
			break

	return good

with open ("input", "r") as myfile:
	s = 0
	for line in myfile:
		line = line.rstrip()
		if is_nice(line):
			s += 1

print(s)