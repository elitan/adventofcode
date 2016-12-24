import hashlib
import re
import sys
import time

re_three_same = re.compile(r'(.)\1\1')

pi = 'yjdafjpo'
i = 0
p = 2

counting_map = {}
found_indexes = []
max_found_indexes = 80

def get_hash(plain_text, p):
	if p == 1:
		return hashlib.md5(plain_text.encode('utf-8')).hexdigest()
	elif p == 2:
		h = plain_text
		for x in range(2017):
			h = hashlib.md5(h.encode('utf-8')).hexdigest()
		return h

while len(found_indexes) < max_found_indexes:
	plain_text = '{}{}'.format(pi, i)
	h = get_hash(plain_text, p)

	# check still valid
	remove_keys = []
	for k in counting_map:
		if len(found_indexes) < max_found_indexes:
			chars = ''.join([ counting_map[k]['char'] for x in range(5)])
			if chars in h:
				counting_map[k]['inner_count'] += 1
				if counting_map[k]['inner_count'] == 1: # thought they would edit this count for part 2
					# ok key
					found_indexes.append(counting_map[k]['start_i'])
					remove_keys.append(k)
					print(i, found_indexes)
		if i - counting_map[k]['start_i'] == 1000:
			remove_keys.append(k)

	for key in remove_keys:
		del counting_map[key]


	# addin new ones
	m = re_three_same.match(h)
	m = re.findall(re_three_same, h)
	if m:
		counting_map[i] = {
			'start_i': i,
			'inner_count': 0,
			'char': m[0],
		}

	i += 1

print(sorted(found_indexes)[63])
