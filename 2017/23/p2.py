# glancing the input gave me this...
def isPrime(n):
	if n == 2 or n == 3: return True
	if n < 2 or n%2 == 0: return False
	if n < 9: return True
	if n%3 == 0: return False
	r = int(n**0.5)
	f = 5
	while f <= r:
		if n%f == 0: return False
		if n%(f+2) == 0: return False
		f +=6
	return True

b = 67
b *= 100
b += 100000
c = b
c += 17000
h = 0

while True:
	if not isPrime(b):
		h += 1
	if c == b: break
	b += 17

print(h)
