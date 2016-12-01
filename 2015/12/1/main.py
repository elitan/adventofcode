import re

with open('input') as f:
	for line in f:
		s = line.rstrip()

a = 0
for d in re.findall(ur'-?[0-9]+', s):
	a += int(d)

print(a)
