import re
import sys

with open('input', 'r') as f:
    compressed = f.readline().rstrip()

re_marker = re.compile(r'^(\((\d+)x(\d+)\))')
re_l = re.compile(r'^(\w+)\(?')

def decompress_len(compressed):
    l = 0
    while compressed:
        letters_match = re.findall(re_l, compressed)
        if letters_match:
            letters = letters_match[0]
            l += len(letters)
            compressed = compressed[len(letters):]
            continue

        marker_match = re.findall(re_marker, compressed)
        if marker_match:
            marker, letters, repetitions = re.findall(re_marker, compressed)[0]
            letters, repetitions = int(letters), int(repetitions)

            to_decompress = compressed[len(marker):len(marker) + letters]
            add_to_l = repetitions * decompress_len(to_decompress)
            l += add_to_l
            compressed = compressed[len(marker) + letters:]
            continue

    return l

print(decompress_len(compressed))
