import sys
from functools import reduce

class CircularList:

    def __init__(self, init_list = []):
        self.list = []

        for value in init_list:
            self.list.append(value)

    def append(self, value):
        self.list.append(value)

    def __len__(self):
        return len(self.list)

    def __getitem__(self, key):

        if type(key) is int:
            return self.list[key]

        elif type(key) is slice:

            start = key.start % len(self.list)
            stop = key.stop % len(self.list)
            step = key.step

            if start < stop:
                return self.list[start:stop]
            elif start == stop:
                return []
            else: # start > stop
                return self.list[start:] + self.list[:stop]

    def __setitem__(self, key, value):
        if type(key) is int:

            self.list[key] = value

        elif type(key) is slice:

            # nothing to add
            if not value:
                return

            start = key.start % len(self.list)
            stop = key.stop % len(self.list)
            step = key.step

            if start < stop:
                self.list[start:stop] = value

            elif start == stop:
                self.list = value[-start:] + value[:-start]

            else: # start > stop

                back_list_start = len(self.list) - start
                back_list = value[:back_list_start]

                front_list = value[back_list_start:]

                self.list = front_list + self.list[stop:start] + back_list

    def __str__(self):
        return str(self.list)

    def __repr__(self):
        return self.__str__()

def knot_hash(circular_list, input_lengths, current_position = 0, skip_size = 0):

    for current_length in input_lengths:

        # where to cut?
        start = current_position
        stop = start + current_length

        # extract and reverse sublist
        sublist = circular_list[start:stop]
        sublist = sublist[::-1]

        # put it back in
        circular_list[start:stop] = sublist

        # increase position and skip size
        current_position += current_length + skip_size
        skip_size += 1

    return circular_list, current_position, skip_size

def part1(input_file_name, list_length):

    circular_list = CircularList([x for x in range(list_length)])

    # read input lengths from file
    input_lengths = [int(x) for x in open(input_file_name).readline().split(',')]

    cl = knot_hash(circular_list, input_lengths, 0, 0)[0]

    return cl[0] * cl[1]

def part2(input_file_name, list_length):

    input_lengths = [ord(x) for x in open(input_file_name).readline().strip()]

    input_lengths += [17, 31, 73, 47, 23]

    sparse_hash = CircularList([x for x in range(list_length)])

    # run hash function 64 times and keep current position and skip size
    current_position = 0
    skip_size = 0
    for x in range(64):

        sparse_hash, current_position, skip_size = knot_hash(sparse_hash, input_lengths, current_position, skip_size)

    dense_hash = []
    for i in range(16):
        pos = i * 16

        xor_n = reduce(lambda x, y: x^y, sparse_hash[pos:pos+16])

        hex_str = hex(xor_n)[2:].zfill(2)

        dense_hash.append(hex_str)

    return ''.join(dense_hash)


def main():

    input_file_name = 'input'
    list_length = 256

    print('part 1: ', part1(input_file_name, list_length))
    print('part 2: ', part2(input_file_name, list_length))

if __name__ == '__main__':
    main()
