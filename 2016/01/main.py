with open('in', 'r') as f:
    instructions = f.readline()

direction_steps = [0, 0, 0, 0]
facing = 0 # 0 = north, 1 = east, 2 = south, 3 = west
direction_values = {
    'R': 1,
    'L': -1
}

for instruction in instructions.split(', '):
    move_direction, steps = instruction[0], int(instruction[1:])
    facing = (facing + direction_values[move_direction]) % 4
    direction_steps[facing] += steps

print(abs(direction_steps[0] - direction_steps[2]) + abs(direction_steps[1] - direction_steps[3]))
