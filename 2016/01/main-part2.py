import sys

# if east or south, multiply with 1, else -1
def step_direction(n):
    if n in [1, 2]:
        return 1
    else:
        return -1

with open('in', 'r') as f:
    instructions = f.readline()

grid_size = 1000
grid = []
for x in range(grid_size):
    row = []
    for y in range(grid_size):
        row.append(0)
    grid.append(row)

facing = 0 # 0 = north, 1 = east, 2 = south, 3 = west
direction_values = {
    'R': 1,
    'L': -1
}

current_position = [int(grid_size/2), int(grid_size/2)]
grid[current_position[0]][current_position[1]]= 1

for instruction in instructions.split(', '):
    move_direction, steps = instruction[0], int(instruction[1:])
    facing = (facing + direction_values[move_direction]) % 4

    if facing == 0 or facing == 2:
        current_position_index = 1 # move y
    else:
        current_position_index = 0 # move x

    for s in range(steps):
        current_position[current_position_index] += step_direction(facing)
        if grid[current_position[0]][current_position[1]]:
            print('already visited!', current_position)
            print(abs(current_position[0] - 500) + abs(current_position[1] - 500))
            sys.exit()
        grid[current_position[0]][current_position[1]] = 1 # mark as visited
