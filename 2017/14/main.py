from functools import reduce
import sys
from collections import deque

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

def true_knot_hash(sparse_hash, input_lengths):


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

    return dense_hash


def dense_hash_to_bin(dense_hash):
    bin_return = ''
    for x in dense_hash:
        bin_return += bin(int(x, 16))[2:].zfill(8)
    return bin_return

def main():

    list_length = 256

    bits_1 = 0

    ones = []

    for row in range(128):
        sparse_hash = CircularList([x for x in range(list_length)])

        input_lengths = [ord(x) for x in 'ffayrhll-{}'.format(row)]
        input_lengths += [17, 31, 73, 47, 23]

        dense_hash = true_knot_hash(sparse_hash, input_lengths)

        bin_hash = dense_hash_to_bin(dense_hash)

        # get coordinates for p2
        for col, bit in enumerate(bin_hash):
            if bit == '1':
                ones.append((row, col))

        # p1 count '1'
        bits_1 += bin_hash.count('1')

    print('part 1: ', bits_1)


    current_group = []
    i = 0

    while ones:

        # get a starting point for a group
        current_group.append(ones.pop())

        # add new coordinates to this group and remove searched
        # search as long as there are coordintes to search
        while current_group:

            row, col= current_group.pop()

            # look right, left, up, down
            if (row, col + 1) in ones:
                current_group.append((row, col + 1))
                ones.remove((row, col + 1))
            if (row, col - 1) in ones:
                current_group.append((row, col - 1))
                ones.remove((row, col - 1))
            if (row + 1, col) in ones:
                current_group.append((row + 1, col))
                ones.remove((row + 1, col))
            if (row - 1, col) in ones:
                current_group.append((row - 1, col))
                ones.remove((row - 1, col))
        i += 1

    print('groups: ', i)

if __name__ == '__main__':
    main()
