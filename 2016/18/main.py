def safe_tiles(row):
    return row.count('.')

def next_tile(l, c, r):
    if l == '^' and c == '^' and r == '.':
        return '^'
    elif l == '.' and c == '^' and r == '^':
        return '^'
    elif l == '^' and c == '.' and r == '.':
        return '^'
    elif l == '.' and c == '.' and r == '^':
        return '^'
    return '.'

def get_next_row(current_row):
    next_row = ''
    current_row_len = len(current_row)
    for i in range(current_row_len):
        if i == 0: # left most
            l, c, r = '.', current_row[i], current_row[i + 1]
        elif i == (current_row_len - 1): # right most
            l, c, r = current_row[i - 1], current_row[i], '.'
        else:
            l, c, r = current_row[i - 1], current_row[i], current_row[i + 1]
        next_row += next_tile(l, c, r)
    return next_row

current_row = '^.^^^..^^...^.^..^^^^^.....^...^^^..^^^^.^^.^^^^^^^^.^^.^^^^...^^...^^^^.^.^..^^..^..^.^^.^.^.......'
l = 400000
s = 0

for _ in range(l):
    s += safe_tiles(current_row)
    current_row = get_next_row(current_row)

print(s)
