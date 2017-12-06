def getMaxValueAndIndex(memory_banks):

    max_i = 0
    max_v = 0

    for i, x in enumerate(memory_banks):
        if x > max_v:
            max_i = i
            max_v = x

    return max_v, max_i

def main():

    # read in banks from file
    memory_banks = [ int(x.rstrip()) for x in open('in').readline().split('\t') ]

    # visited states
    states = set()
    states_steps = {}

    steps = 0

    while tuple(memory_banks) not in states:

        # states visited
        states.add(tuple(memory_banks))

        # keep track on what step we found this particular memory_bank
        states_steps[tuple(memory_banks)] = steps

        max_v, max_i = getMaxValueAndIndex(memory_banks)

        # how many blocks should we visit?
        l = min(len(memory_banks), max_v)

        # base value to distribute.
        base_v_to_distribute = max_v // len(memory_banks)

        # an extra 1 v for the first `extra_val_range` banks
        extra_val_range = max_v % len(memory_banks)

        # manipulate memory banks
        memory_banks[max_i] = 0

        # fill in the values
        for i in range(l):

            # v = base_v_to_distribute + (i < extra_val_range)
            v = base_v_to_distribute

            if i < extra_val_range:
                v += 1

            # start one index to the right of max_i with i offset
            memory_banks[(max_i + 1 + i) % len(memory_banks)] += v

        # print(memory_banks)

        steps += 1

    # answer to p1
    print(steps)

    # answer to p2
    print(steps - states_steps[tuple(memory_banks)])

if __name__ == '__main__':
    main()
