def find_lowest(numbers):
	i = 0
	while True:
		if i not in numbers:
			return i
		i += 1

fp = open('in', 'r')
numbers = set()
for line in fp:
	line = line.rstrip()
	a, z = list(map(int, line.split('-')))
	for i in range(a, (z + 1)):
		numbers.add(i)

print(find_lowest(numbers))
