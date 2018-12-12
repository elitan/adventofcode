import re
import sys
from collections import defaultdict


def transition(state, i):
	transition_data = {
		'#####': '#',
		'####.': '#',
		'###..': '#',
		'###.#': '#',
		'##...': '#',
		'##..#': '#',
		'##.##': '#',
		'##.#.': '#',
		'#.###': '#',
		'#..##': '#',
		'#...#': '#',
		'#.#..': '#',
		'.#.#.': '#',
		'.#...': '#',
		'.#..#': '#',
		'..#.#': '#',
		'...##': '#',
		'..###': '#',
	}

	a = ''
	a = state[i-2] + state[i - 1] + state[i] + state[i + 1] + state[i + 2]
	try:
		return transition_data[a]
	except:
		return '.'


def printState(state):
	state_keys = list(state.keys())
	for key in range(min(state_keys) - 2, max(state_keys) + 2):
		print(state[key], end='')
	print('')

def main():

	input_data = '.#####.##.#.##...#.#.###..#.#..#..#.....#..####.#.##.#######..#...##.#..#.#######...#.#.#..##..#.#.#'
	state = defaultdict(lambda: '.')

	left_most = float('inf')
	right_most = 0
	for i, c in enumerate(input_data):
		state[i] = c #0 if c == '.' else 1
		if c == '#':
			left_most = min(left_most, i)
			right_most = max(right_most, i)

	prev_p1 = 0
	for i in range(200):
		new_state = defaultdict(lambda: '.')
		p1 = 0
		state_keys = list(state.keys())
		for key in range(min(state_keys) - 2, max(state_keys) + 2):
			c = transition(state, key)
			p1 += key if c == '#' else 0
			new_state[key] = c

		print(i, ' - current answ: ', p1, p1 - prev_p1)

		prev_p1 = p1
		state = new_state

	# 5811 + (50000000000 - 1 - 88) * 62

if __name__ == '__main__':
	main()
