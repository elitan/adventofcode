# wrong 0529031614

# p2
# wrong 552860567

import re
import sys


def part1():

	recepies = [3, 7]
	a_index, b_index = 0, 1

	in_data = 440231
	while len(recepies) < in_data + 10:

		s = recepies[a_index] + recepies[b_index]

		for l in str(s):
			recepies.append(int(l))

		recepies_len = len(recepies)
		a_index = (a_index + recepies[a_index] + 1) % recepies_len
		b_index = (b_index + recepies[b_index] + 1) % recepies_len

	return ''.join(map(str, recepies[in_data:in_data+10]))


def part2():
	recepies = [3, 7]
	a_index, b_index = 0, 1

	in_data = list(map(int, list('01245')))
	in_data = list(map(int, list('59414')))
	in_data = list(map(int, list('440231')))
	in_data_len = len(in_data)

	build_index = 0

	while True:

		s = recepies[a_index] + recepies[b_index]

		for l in str(s):
			l = int(l)
			recepies.append(int(l))
			if l == in_data[build_index]:
				build_index += 1
			else:
				build_index = 0

			if build_index >= in_data_len:
				print('FOUND!')
				return(len(recepies) - abs(in_data_len))

		recepies_len = len(recepies)
		a_index = (a_index + recepies[a_index] + 1) % recepies_len
		b_index = (b_index + recepies[b_index] + 1) % recepies_len




def main():
	print(part1())
	print(part2())

if __name__ == '__main__':
	main()
