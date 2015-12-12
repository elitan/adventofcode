import sys
import re
import hashlib
import itertools

def get_duration(a,b,durations):
	try:
		return durations[a+b]
	except:
		return durations[b+a]

extract = re.compile(r'(\S+) to (\S+) = (\d+)')
citys = set()
durations = dict()
with open('input') as f:
	for line in f:
		line = line.rstrip()
		g = extract.match(line)

		a = g.group(1)
		b = g.group(2)
		duration = g.group(3)
		citys.add(a)
		citys.add(b)
		durations[a+b] = int(duration)

# convert back to list to permute
citys = list(citys)

best_duration = sys.maxint
for perm in itertools.permutations(citys):
	current_duration = 0
	for i in range(1, len(perm)):
		current_duration += get_duration(perm[i-1],perm[i],durations)
		if current_duration > best_duration:
			break
	if current_duration < best_duration:
		best_duration = current_duration
print(best_duration)


worst_duration = 0
for perm in itertools.permutations(citys):
	current_duration = 0
	for i in range(1, len(perm)):
		current_duration += get_duration(perm[i-1],perm[i],durations)
	if current_duration > worst_duration:
		worst_duration = current_duration
print(worst_duration)