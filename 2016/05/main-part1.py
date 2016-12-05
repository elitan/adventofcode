import hashlib
m = hashlib.md5()

puzzel_input = 'ojvtpuvg'
password = ''
index = 0

while len(password) != 8:
	h = hashlib.md5("{}{}".format(puzzel_input, index).encode('utf-8')).hexdigest()
	if h.startswith('00000'):
		password += h[5]
	index += 1

print(password)
