import sys

map_count = {}
password_len = 0
with open('input', 'r') as f:
	for line_count, line in enumerate(f):
		line = line.rstrip()

		# initiate map_count
		password_len = len(line)
		if line_count == 0:
			for i in range(password_len):
				map_count[i] = {}

		for i, l in enumerate(line):
			if l in map_count[i]:
				map_count[i][l] += 1
			else:
				map_count[i][l] = 1

password = ''
password_b = ''
for i in range(password_len):
	password += max(map_count[i].items(), key=lambda k: k[1])[0]
	password_b += min(map_count[i].items(), key=lambda k: k[1])[0]
print(password)
print(password_b)
