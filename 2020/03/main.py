import sys

x_d = 3
y_d = 1


def trees_encountered(grid, slope):
  x = 0
  y = 0
  x_d, y_d = slope
  trees = 0
  while y < len(grid):
    row = grid[y]
    p = row[x % len(row)]
    trees += p == '#'
    x += x_d
    y += y_d
  return trees

grid = [row.strip() for row in sys.stdin]

p1 = trees_encountered(grid, [3,1])
print(p1)
print('---')

slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
p2 = 1
for slope in slopes:
  p2 *= trees_encountered(grid, slope)

print(p2)