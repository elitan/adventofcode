import sys
import re

s = 0

with open('input') as f:
	for line in f:
		line = line.rstrip()
		
		# "code"
		s += len(line)

		# trim
		line = line[1:-1]

		# remove hex, \\ and \"
		line = re.sub(r"\\\"","A",line)
		line = re.sub(r"\\\\","A",line)
		line = re.sub(r"\\x[0-9a-f]{2}","A",line)

		# "memory"
		s -= len(line)

print(s)