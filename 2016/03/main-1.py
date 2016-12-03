import fileinput

possible_triangles = 0
for line in fileinput.input():
	a, b, c = list(map(lambda x: int(x), line.rstrip().split()))
	if a + b > c and b + c > a and a + c > b:
		possible_triangles += 1
print(possible_triangles)
