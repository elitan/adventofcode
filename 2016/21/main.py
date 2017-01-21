import re
import sys
from itertools import permutations

def swap_position(x, y, password):
    password[x], password[y] = password[y], password[x]
    return password

def swap_letter(x, y, password):
    a, b = password.index(x), password.index(y)
    password[a], password[b] = password[b], password[a]
    return password

def rotate_based(x, password):
    i = password.index(x) + 1
    if i > 4:
        i += 1
    i = i % len(password)
    return rotate_direction('right', i, password)

def rotate_direction(direction, x, password):
    pw_len = len(password)
    if direction == 'left':
        return password[x:] + password[:x]
    else:
        return password[-x:] + password[:-x]

def reverse(x, y, password):
    y += 1
    return password[0:x] + password[x:y][::-1] + password[y:]

def move(x, y, password):
    tmp_char = password[x]
    del password[x]
    password.insert(y, tmp_char)
    return password

def scramble(password, lines):

    password = list(password)

    for line in lines:
        if 'swap position' in line:
            x, y = list(map(int, re.findall(r'swap position (\d+) with position (\d+)', line)[0]))
            password = swap_position(x, y, password)
        elif 'swap letter' in line:
            x, y = re.findall(r'swap letter (\w+) with letter (\w+)', line)[0]
            password = swap_letter(x, y, password)
        elif 'rotate based' in line:
            x = re.findall(r'rotate based on position of letter (\w+)', line)[0]
            password = rotate_based(x, password)
        elif 'rotate' in line:
            direction, x = re.findall(r'rotate (left|right) (\d+) steps?', line)[0]
            x = int(x)
            password = rotate_direction(direction, x, password)
        elif 'reverse' in line:
            x, y = list(map(int, re.findall(r'reverse positions (\d+) through (\d+)', line)[0]))
            password = reverse(x, y, password)
        elif 'move' in line:
            x, y = list(map(int, re.findall(r'move position (\d+) to position (\d+)', line)[0]))
            password = move(x, y, password)
    return ''.join(password)



fh = open('in', 'r')
lines = [line.rstrip() for line in fh]
fh.close()

password = 'abcdefgh'
print(scramble(password, lines))

unscramble = 'fbgdceah'
for perm in permutations(unscramble):
    if scramble(''.join(perm), lines) == unscramble:
        print(''.join(perm))
        sys.exit()
