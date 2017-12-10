import sys

class CircularList:

    def __init__(self):
        self.list = []

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

def main():

    input_file_name = 'input'
    input_list_length = 256

    circular_list = CircularList()

    # read input lengths from file
    input_lengths = [int(x) for x in open(input_file_name).readline().split(',')]
    for x in range(input_list_length):
        circular_list.append(x)

    current_position = 0
    skip_size = 0

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

    print('answer: ', circular_list[0] * circular_list[1])



if __name__ == '__main__':
    main()
