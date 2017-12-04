def validPassphraseP1(passphrase):

    passphrase = passphrase.split(' ')

    return len(passphrase) == len(set(passphrase))

def validPassphraseP2(passphrase):

    passphrase = passphrase.split(' ')

    words = set()

    for word in passphrase:
        words_size = len(words)

        # sort the chars in each word
        words.add(''.join(sorted(list(word))))

        # test if invalid passphrase
        if words_size == len(words):
            return False

    return True

def solve():

    a1 = 0
    a2 = 0
    fh = open('input')
    valid_passphrases = 0

    for line in fh:

        # get passphrase
        passphrase = line.rstrip()

        if validPassphraseP1(passphrase):
            a1 += 1

        if validPassphraseP2(passphrase):
            a2 += 1

    fh.close()

    return a1, a2


def main():

    a1, a2 = solve()

    print('part 1: ', a1)
    print('part 2: ', a2)


if __name__ == '__main__':
    main()
