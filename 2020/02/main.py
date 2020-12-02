import sys
import re

regex = r"(\d+)-(\d+) (\w): (\w+)"

valid_passwords_p1 = 0
valid_passwords_p2 = 0

for line in sys.stdin:
  line = line.rstrip()
  low, high, letter, password = re.findall(regex, line)[0]
  low = int(low)
  high = int(high)

  occurrences = password.count(letter)

  if (occurrences >= low and occurrences <= high):
    valid_passwords_p1 += 1
  
  found = password[low - 1] == letter     # found = 1 if correct
  found += password[high - 1] == letter   # found = 2 if correct
  if (found == 1):
    valid_passwords_p2 +=1

print(valid_passwords_p1)
print(valid_passwords_p2)