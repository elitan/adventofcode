import sys
import time

def next_code(code):
	return (code * 252533) % 33554393

def find_code(find_i, find_j, start_code):
	i, j = 1, 1
	code = start_code
	while True:
		if i == find_i and j == find_j:
			break
		i -= 1
		j += 1
		code = next_code(code)
		if i == 0:
			i, j = j, 1
	return code

start_code = 20151125
c = find_code(2978, 3083, start_code)
print(c)
