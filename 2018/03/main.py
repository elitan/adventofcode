import sys
import re
from collections import defaultdict

def no_overlap(grid, x, y, a, b):
    for i in range(a):
        for j in range(b):
            pos = (x+i, y+j)
            if grid[pos] != 1:
                return False
    return True

def main():

    regex = r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)"
    data = [list(map(int, re.findall(regex, x.rstrip())[0])) for x in sys.stdin]

    grid = defaultdict(int)
    for line in data:
        n, x, y, a, b = line

        for i in range(a):
            for j in range(b):
                pos = (x+i, y+j)
                grid[pos] += 1

    p1 = 0
    for key, value in grid.items():
        p1 += value > 1;
    print(p1)

    for line in data:
        n, x, y, a, b = line
        if no_overlap(grid, x, y, a, b):
            print(n) # p2
            sys.exit()

if __name__ == '__main__':
    main()
