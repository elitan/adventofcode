import sys

numbers = [int(x.strip()) for x in sys.stdin]

for x in numbers:
  for y in numbers:
    for z in numbers:
      if x + y + z == 2020:
        print(x * y * z)
        sys.exit()