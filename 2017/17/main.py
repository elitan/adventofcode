def part1():

    steps = 366

    current_position = 0
    state = [0]

    for i in range(1, 2018):
        current_position = (current_position + steps) % len(state)
        current_position += 1

        state.insert(current_position, i)

    return state[current_position + 1]

def part2():

    steps = 366

    current_position = 0
    position_one = None

    for list_length in range(1, 50000001):

        current_position = (current_position + steps) % list_length
        current_position += 1

        if current_position == 1:
            position_one = list_length

    return position_one

def main():

    print('part 1: ', part1())
    print('part 2: ', part2())

if __name__ == '__main__':
    main()
