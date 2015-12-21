import math

def divisors(n):
	divisors = set()
	divisors.add(1)
	divisors.add(n)
	for i in range(2, int(math.ceil(n**0.5))):
		if n % i == 0:
			divisors.add(i)
			divisors.add(int(n/i))

	if math.sqrt(n) == math.floor(math.sqrt(n)):
		divisors.add(int(math.sqrt(n)))

	return divisors

target = 36000000 / 10
i = 2
while sum(divisors(i)) < target:
	i += 1

print(i)