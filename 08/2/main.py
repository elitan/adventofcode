import sys
import re

s = 0

with open('input') as f:
	for line in f:
		line = line.rstrip()

		print(line, len(line))
		# "code"
		start_len = len(line)

		# trim
		line = line[1:-1]

		# remove hex, \\ and \"
		line = re.sub(r"\\\"","AAAA",line)
		line = re.sub(r"\\","AA",line)
		line = re.sub(r"\\x[0-9a-f]{2}","AAAA",line)

		new_len = len(line)+6
		print(line, new_len)

		s += new_len - start_len


print(s)