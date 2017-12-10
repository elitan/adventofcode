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

            else:
                return self.list[start:] + self.list[:stop]

    def __setitem__(self, key, value):
        if type(key) is int:

            self.list[key] = value

        elif type(key) is slice:

            start = key.start % len(self.list)
            stop = key.stop % len(self.list)
            step = key.step

            print('set')
            print('start: ', start, ' , stop: ', stop)

            if start < stop:
                self.list[start:stop] = value

            elif start == stop:

                print('front: ', value[-start:])
                print('back: ', value[:-start])

                self.list = value[-start:] + value[:-start]

            else:
                # you can only substitute len(value) elements in self.list
                # with this calss plz
                #
                back_list_start = len(self.list) - start
                back_list = value[:back_list_start]
                print('back list: ', back_list)

                front_list = value[back_list_start:]
                print('front list: ', front_list)

                print('middle list: ', self.list[stop:start], len(self.list[stop:start]))

                self.list = front_list + self.list[stop:start] + back_list

    def __str__(self):
        return str(self.list)

    def __repr__(self):
        return self.__str__()

def main():

    input_file_name = 'input2'
    input_list_length = 256
    input_file_name = 'test'
    input_list_length = 5

    circular_list = CircularList()

    # read input lengths from file
    input_lengths = [int(x) for x in open(input_file_name).readline().split(',')]
    for x in range(input_list_length):
        circular_list.append(x)


    current_position = 0
    skip_size = 0

    for current_length in input_lengths:
        print('')
        print('circular_list: ', circular_list)
        if len(circular_list) != input_list_length:
            print('wrong')
            sys.exit()
        if (len(circular_list)) != len(set(circular_list)):
            print('wrong 2')
            sys.exit()

        start = current_position
        stop = start + current_length

        sublist = circular_list[start:stop]
        print('sublist: ', sublist)
        sublist = sublist[::-1]
        print('sublist reversed: ', sublist)

        circular_list[start:stop] = sublist

        current_position += current_length + skip_size
        current_position = current_position % input_list_length
        skip_size += 1
        print('skip size: ', skip_size)
        input()

    print('final circular_list: ', circular_list)

    print('answer: ', circular_list[0] * circular_list[1])



if __name__ == '__main__':
    main()
