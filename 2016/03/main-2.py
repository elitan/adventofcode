import fileinput

def possible_triangle(a, b, c):
	return a + b > c and b + c > a and a + c > b

possible_triangles = 0
in_list = []

# read in list
for line in fileinput.input():
	in_list.append(list(map(lambda x: int(x), line.rstrip().split())))

# handle list
for i in range(int(len(in_list) / 3)):
	for x in range(3):
		a, b, c = in_list[i * 3][x], in_list[i * 3 + 1][x], in_list[i * 3 + 2][x]
		if possible_triangle(a, b, c):
			possible_triangles += 1

print(possible_triangles)
