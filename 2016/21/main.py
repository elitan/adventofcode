import re

def swap_position(x, y, password):
    print('swap position:' , x, y)
    password[x], password[y] = password[y], password[x]
    return password

def swap_letter(x, y, password):
    a, b = password.index(x), password.index(y)
    password[a], password[b] = password[b], password[a]
    return password

def rotate_based(x, password):
    print('rotate based ', password)
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


fh = open('in-test', 'r')
fh = open('in', 'r')

password = 'abcde'
password = 'abcdefgh'
password = list(password)
print('start pw: ', password)
for line in fh:
    line = line.rstrip()
    if 'swap position' in line:
        x, y = list(map(int, re.findall(r'swap position (\d+) with position (\d+)', line)[0]))
        password = swap_position(x, y, password)
        print('current pw: ', password)
    elif 'swap letter' in line:
        x, y = re.findall(r'swap letter (\w+) with letter (\w+)', line)[0]
        password = swap_letter(x, y, password)
        print('current pw: ', password)
    elif 'rotate based' in line:
        x = re.findall(r'rotate based on position of letter (\w+)', line)[0]
        password = rotate_based(x, password)
        print('current pw: ', password)
    elif 'rotate' in line:
        direction, x = re.findall(r'rotate (left|right) (\d+) steps?', line)[0]
        x = int(x)
        password = rotate_direction(direction, x, password)
        print('current pw: ', password)
    elif 'reverse' in line:
        x, y = list(map(int, re.findall(r'reverse positions (\d+) through (\d+)', line)[0]))
        password = reverse(x, y, password)
        print('current pw: ', password)
    elif 'move' in line:
        x, y = list(map(int, re.findall(r'move position (\d+) to position (\d+)', line)[0]))
        password = move(x, y, password)
        print('current pw: ', password)

print('password finished: ', ''.join(password))
