import sys
import time

init_state = list(map(int, sys.stdin.readline().rstrip().split(',')))

for i in range(0, 100):
  for j in range(0, 100):

    pc = 0
    state = init_state.copy()

    state[1] = i
    state[2] = j

    while state[pc] != 99:
      if state[pc] == 1:
        state[state[pc + 3]] = state[state[pc + 1]] + state[state[pc + 2]]
      else:
        state[state[pc + 3]] = state[state[pc + 1]] * state[state[pc + 2]]
      pc += 4

    if state[0] == 19690720:
      print(i, j, 100*i+j)
      sys.exit()
