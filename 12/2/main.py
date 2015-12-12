import json
import sys
import re

s = 0

def remove_red(data):
	if "red" in data.values(): 
		return {}
	return data


with open('input', 'r') as f:
	for line in f:
		data = line.rstrip()

# remove red
data = str(json.loads(data, object_hook=remove_red))

#print(data)

a = 0
for d in re.findall(ur'-?[0-9]+', data):
	a += int(d)

print("")
print(a)