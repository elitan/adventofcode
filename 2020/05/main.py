import sys
import math


def get_row(boarding_pass):
    row_min = 0
    row_max = 127
    for direction in boarding_pass[:7]:
        half = math.ceil((row_max - row_min) / 2)
        if direction == 'F':
            row_max -= half
        else:
            row_min += half
    return row_min


def get_seat(boarding_pass):
    row_min = 0
    row_max = 7
    for direction in boarding_pass[-3:]:
        half = math.ceil((row_max - row_min) / 2)
        if direction == 'L':
            row_max -= half
        else:
            row_min += half
    return row_min


def get_seat_id(row, seat):
    return row * 8 + seat


seat_ids = set()
boarding_passes = [line.strip() for line in sys.stdin]
for boarding_pass in boarding_passes:
    row = get_row(boarding_pass)
    seat = get_seat(boarding_pass)
    seat_id = get_seat_id(row, seat)
    seat_ids.add(seat_id)


print(max(seat_ids))
potential_seat_ids = set([x for x in range(0, max(seat_ids) + 1)])
print(potential_seat_ids - seat_ids)
