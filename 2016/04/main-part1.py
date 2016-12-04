import fileinput
import sys

def real_room(enc, checksum):
	letter_count = {}
	for l in enc:
		if l in letter_count:
			letter_count[l] += 1 * 10**4
		else:
			letter_count[l] = 1 * 10**4 + ord('z') + 1 - ord(l) # ensure alphabetically order

	# top 5
	top_five = []
	for i in range(5):
		highest_value = 0
		highest_key = ''
		for key, value in letter_count.items():
			if value > highest_value:
				highest_value = value
				highest_key = key
		if highest_key != checksum[i]:
			return False
		letter_count.pop(highest_key, None)
	return True


sector_sum = 0
for line in fileinput.input():
	enc_sector, checksum = line.rstrip().split('[')
	sector_id = int(enc_sector.split('-')[-1])
	enc = ''.join(enc_sector.split('-')[:-1])
	checksum = checksum[:-1]
	print('enc: {}, sector_id: {}, checksum: {}'.format(enc, sector_id, checksum))
	if real_room(enc, checksum):
		print('real', enc, checksum)
		sector_sum += sector_id
	else:
		print('NOT real', enc, checksum)

print(sector_sum)
