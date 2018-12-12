import re
import sys
from collections import defaultdict


def transition(state, i):

	transition_data = {
		'...##': '#',
		'..#..': '#',
		'.#...': '#',
		'.#.#.': '#',
		'.#.##': '#',
		'.##..': '#',
		'.####': '#',
		'#.#.#': '#',
		'#.###': '#',
		'##.#.': '#',
		'##.##': '#',
		'###..': '#',
		'###.#': '#',
		'####.': '#',
		# '#..#.': '.',
		# '##...': '#',
		# '#....': '.',
		# '#...#': '#',
		# '...#.': '.',
		# '.#..#': '#',
		# '#.#.#': '.',
		# '.....': '.',
		# '##.##': '#',
		# '##.#.': '#',
		# '###..': '#',
		# '#.##.': '.',
		# '#.#..': '#',
		# '##..#': '#',
		# '..#.#': '#',
		# '..#..': '.',
		# '.##..': '.',
		# '...##': '#',
		# '....#': '.',
		# '#.###': '#',
		# '#..##': '#',
		# '..###': '#',
		# '####.': '#',
		# '.#.#.': '#',
		# '.####': '.',
		# '###.#': '#',
		# '#####': '#',
		# '.#.##': '.',
		# '.##.#': '.',
		# '.###.': '.',
		# '..##.': '.',
		# '.#...': '#',
	}

	a = ''
	a = state[i-2] + state[i - 1] + state[i] + state[i + 1] + state[i + 2]
	try:
		return transition_data[a]
	except:
		return '.'


def printState(state, left_most, right_most):
	for i in range(left_most, right_most + 1):
		print(state[i], end='')
	print('')

def main():

	input_data = '.#####.##.#.##...#.#.###..#.#..#..#.....#..####.#.##.#######..#...##.#..#.#######...#.#.#..##..#.#.#'
	input_data = '#..#.#..##......###...###'
	state = defaultdict(lambda: '.')

	left_most = float('inf')
	right_most = 0
	for i, c in enumerate(input_data):
		state[i] = c #0 if c == '.' else 1
		if c == '#':
			left_most = min(left_most, i)
			right_most = max(right_most, i)

	print(state)
	print(left_most, right_most)

	printState(state, left_most, right_most)

	p1 = 0
	for i in range(21):
		new_state = defaultdict(lambda: '.')
		for i in range(left_most-10, right_most + 20):
			c = transition(state, i)
			p1 += 1 if c == '#' else 0
			new_state[i] = c

		printState(new_state, left_most-10, right_most + 20)
		print('current answ: ', p1)

		state = new_state


if __name__ == '__main__':
	main()
