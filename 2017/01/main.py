
def FrontToBack(number):

    print(number[0])
    print(number[-1])

    if number[0] != number[-1]:
        return number

    last_digit = number[-1]
    # how many digits to move?
    for i, digit in enumerate(number):
        print(digit, i)

    return number

def main():

    with open('in') as f:
        number = f.readline().rstrip()

    number = FrontToBack(number)

    print(number)

    # move number from back to front if same


if __name__ == '__main__':
    main()
