import fileinput
import sys

def decrypt(enc, sector_id):
	plain_text = ''
	for l in enc:
		if l == '-':
			plain_text += ' '
		else:
			plain_text += chr(((ord(l) + sector_id - ord('a')) % (ord('z') - ord('a') + 1)) + ord('a'))
	return plain_text


sector_sum = 0
for line in fileinput.input():
	enc_sector, checksum = line.rstrip().split('[')
	sector_id = int(enc_sector.split('-')[-1])
	enc = '-'.join(enc_sector.split('-')[:-1])
	checksum = checksum[:-1]
	# print('enc: {}, sector_id: {}, checksum: {}'.format(enc, sector_id, checksum))
	dec = decrypt(enc, sector_id)
	if 'pole' in dec:
		print(decrypt(enc, sector_id), sector_id)
