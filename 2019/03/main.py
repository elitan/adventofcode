import sys
from collections import defaultdict

operations_a = sys.stdin.readline().rstrip().split(',')
operations_b = sys.stdin.readline().rstrip().split(',')

def get_points(operations):
  grid = set()
  x,y = 0,0
  length = 1
  length_info = {}
  for op in operations:
    direction = op[0]
    steps = int(op[1:])

    for i in range(steps):
      if direction == 'R':
        x += 1
      elif direction == 'L':
        x -= 1
      elif direction == 'U':
        y += 1
      elif direction == 'D':
        y -= 1

      grid.add((x,y))
      length_info[(x,y)] = length
      length += 1

  return grid, length_info


a_points, a_length = get_points(operations_a)
b_points, b_length = get_points(operations_b)

intersections = list(a_points & b_points)

print(min([sum(list(map(abs, intersection))) for intersection in intersections]))
print(min([a_length[intersection] + b_length[intersection] for intersection in intersections]))
