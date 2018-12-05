import sys

def doMutation(s, start_i):
    for i in range(start_i, len(s) - 1):
        if abs(s[i] - s[i+1]) == 32:
            try:
                s = s[:i] + s[i+2:]
            except:
                s = s[:i] # if index out of range...
            return True, s, max(i-1, 0)
    return False, s, None

def main():

    s = sys.stdin.readline().rstrip()

    s_p1= list(map(lambda x: ord(x), s))
    s_p2 = s_p1.copy()

    mutation_happend = True
    start_i = 0
    while mutation_happend:
        mutation_happend, s_p1, start_i = doMutation(s_p1, start_i)

    # p1
    print('p1: ', len(s_p1))

    low_n = sys.maxsize

    for i in range(ord('A'), ord('Z')):
        if i not in s_p2:
            continue

        current_s_p2 = s_p2.copy()

        current_s_p2 = list(filter(lambda x: x != i and x != i + 32 , current_s_p2))

        mutation_happend = True
        start_i = 0
        while mutation_happend:
            mutation_happend, current_s_p2, start_i = doMutation(current_s_p2, start_i)

        if len(current_s_p2) < low_n:
            low_n = len(current_s_p2)

    # p2
    print('p2: ', low_n)


if __name__ == '__main__':
    main()
