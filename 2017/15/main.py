def part1(a, b):

    points = 0

    for i in range(40*10**6):

        a = a * 16807 %  2147483647
        b = b * 48271 %  2147483647

        # 65535 is 1111 1111 1111 1111 in base 2 (binary)
        points += a & 65535 == b & 65535

    return points

def part2(a, b):

    points = 0

    for i in range(5*10**6):

        a = a * 16807 %  2147483647
        while a % 4 != 0:
            a = a * 16807 %  2147483647

        b = b * 48271 %  2147483647
        while b % 8 != 0:
            b = b * 48271 %  2147483647

        points += a & 65535 == b & 65535

    return points

def main():

    a = 783
    b = 325

    print('part 1: ', part1(a, b))
    print('part 2: ', part2(a, b))

if __name__ == '__main__':
    main()
