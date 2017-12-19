def getNewPosition(current_position, direction):
    row, col = current_position
    if direction == 'down':
        return (row + 1, col)
    elif direction == 'up':
        return (row - 1, col)
    elif direction == 'left':
        return (row, col - 1)
    elif direction == 'right':
        return (row, col + 1)

def getNewDirection(current_position, current_direction, grid):
    row, col = current_position
    if current_direction in ['down', 'up']:
        if (row, col - 1) in grid and grid[(row, col - 1)] != '|':
            return 'left'
        else:
            return 'right'
    else: # direction is left or right
        if (row - 1, col) in grid and grid[(row - 1, col)] != '-':
            return 'up'
        else:
            return 'down'

def main():

    input_file_name = 'in'
    start_position_found = False
    grid = {}

    for row, line in enumerate(open(input_file_name)):
        for col, c in enumerate(line[:-1]):

            if c == ' ':
                continue

            if not start_position_found:
                start_position = (row, col)
                start_position_found = True

            grid[(row, col)] = c

    letters = []
    steps = 0
    position = start_position
    direction = 'down'

    try:
        while True:

            if grid[position].isalpha():
                letters.append(grid[position])
            steps += 1

            # get next positoin
            position = getNewPosition(position, direction)

            if grid[position] in ['|', '-']:
                continue # to next position
            elif grid[position] == '+':
                direction = getNewDirection(position, direction, grid)
    except: #YOLO
        print(''.join(letters))
        print(steps)


if __name__ == '__main__':
    main()
