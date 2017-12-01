def main():

    with open('in') as f:
        number = f.readline().rstrip()

    s = 0
    for d_index, d in enumerate(number):
        if d == number[(d_index + 1) % len(number)]:
            s += int(d)
    print('1: ', s)

    s = 0
    for d_index, d in enumerate(number):
        if d == number[(d_index + len(number) / 2) % len(number)]:
            s += int(d)
    print('2: ', s)


if __name__ == '__main__':
    main()
