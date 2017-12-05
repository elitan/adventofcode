# part 1
jump_offsets = []
for n in open('input'):
    jump_offsets.append(int(n.rstrip()))

current_i = 0
new_i = 0
steps = 0

while new_i > 0 and new_i < len(jump_offsets):

    # jump tmp
    new_i = current_i + jump_offsets[current_i]

    # change the previous offset value
    jump_offsets[current_i] += 1

    # actual jump, prep for next iteration
    current_i = new_i

    steps += 1

print(steps)


# part 2
jump_offsets = []
for n in open('input'):
    jump_offsets.append(int(n.rstrip()))

current_i = 0
new_i = 0
steps = 0

# take steps as long we are inside the maze
while new_i > 0 and new_i < len(jump_offsets):

    # jump tmp
    new_i = current_i + jump_offsets[current_i]

    # change the previous offset value
    jump_offsets[current_i] += 1 if jump_offsets[current_i] < 3 else -1

    # actual jump, prep for next iteration
    current_i = new_i

    steps += 1

print(steps)
