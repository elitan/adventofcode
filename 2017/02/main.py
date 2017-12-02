def findDivisibleValues(line):

    # go through all numbers
    for digit_a in line:

        # for each number, try to find a number that is divisible with the
        # number (digit_a) we are checking
        for digit_b in line:

            # skip number if you are looking at the same number that we want
            # to check
            if digit_a == digit_b:
                continue

            # get the max and min value of the two number we sant to check
            # for the modolus and division operation to work properly
            max_v = max(digit_a, digit_b)
            min_v = min(digit_a, digit_b)

            # now, if the numbers are evenly divisible, return
            if max_v % min_v == 0:
                return max_v / min_v

def main():
    with open('input') as fh:

        a1 = 0
        a2 = 0

        for line in fh:

            # make each line a array of ints
            line = map(int, line.rstrip().split('\t'))

            a1 += max(line) - min(line)
            a2 += findDivisibleValues(line)

        print(a1)
        print(a2)

if __name__ == '__main__':
    main()
