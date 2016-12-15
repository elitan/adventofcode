import hashlib
import re
import sys

re_three_same = re.compile(r'(.)\1\1')

pi = 'abc'
i = 0

counting_map = {}

while True:
	plain_text = '{}{}'.format(pi, i)
	h = hashlib.md5(plain_text.encode('utf-8')).hexdigest()
	print(plain_text, h)

	# check still valid
	remove_keys = []
	for k in counting_map:
		chars = ''.join([ counting_map[k]['char'] for x in range(5)])
		print('look for: ', chars)
		if chars in h:
			counting_map[k]['inner_count'] += 1
			if counting_map[k]['inner_count'] == 5:
				# ok key
				print(k)
				print(counting_map[k])
				sys.exit()
				pass
		elif i - counting_map[k]['i'] > 1000:
			remove_keys.append(k)
			print('terminate')


	for key in remove_keys:
		del counting_map[key]

	# addin new ones
	m = re_three_same.match(h)
	m = re.findall(re_three_same, h)
	if m:
		counting_map[i] = {
			'i': i,
			'inner_count': 0,
			'char': m[0]
		}

	i += 1
	input()
