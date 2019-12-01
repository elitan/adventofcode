import sys

def getFuel(mass):
  if mass <= 0:
    return 0
  fuel = max(0, int(mass / 3) - 2)
  return fuel + getFuel(fuel)

masses = [int(x.rstrip()) for x in sys.stdin]

print(sum([getFuel(mass) for mass in masses]))
