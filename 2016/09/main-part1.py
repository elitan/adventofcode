import re

with open('input', 'r') as f:
    compressed = f.readline().rstrip()

re_letter_repetitions = re.compile(r'(\d+)x(\d+)')
extracted = ''

while compressed:
    if not '(' in compressed and not ')' in compressed:
        extracted += compressed
        compressed = ''
        continue
    else:
        next_marker_start = compressed.index('(')
        next_marker_end = compressed.index(')')

        if next_marker_end < next_marker_start:
            extracted += compressed
            compressed = ''
            continue

        # extract marker info
        letters, repetitions = list(map(int, re.findall(re_letter_repetitions, compressed[next_marker_start + 1:next_marker_end])[0]))

        # extract compressed data
        tmp_extracted = ''
        for i in range(repetitions):
            tmp_extracted += compressed[next_marker_end + 1:next_marker_end + letters + 1]

        # move str before marker
        extracted += compressed[:next_marker_start]
        compressed = compressed[next_marker_end + letters + 1:]

        # add the compressed data
        extracted += tmp_extracted

print(len(extracted))
