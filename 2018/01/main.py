import sys

l = [int(x) for x in sys.stdin]

i = 0
frequencies = set()
current_frequency = l[i]

while current_frequency not in frequencies:
    frequencies.add(current_frequency)
    i = (i + 1) % len(l)
    current_frequency += l[i]

print(sum(l))
print(current_frequency)
