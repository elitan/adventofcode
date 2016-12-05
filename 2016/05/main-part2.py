import hashlib
m = hashlib.md5()

puzzel_input = 'ojvtpuvg'
password_size = 8
password = [None for x in range(password_size)]
index = -1

while complete_password != password_size:
	index += 1
	h = hashlib.md5("{}{}".format(puzzel_input, index).encode('utf-8')).hexdigest()
	if h.startswith('00000'):
		try:
			password_index = int(h[5])
		except:
			continue
		if 0 <= password_index <= (password_size - 1):
			if password[password_index] != None:
				continue
			password[password_index] = h[6]
			complete_password += 1

print(''.join(password))
