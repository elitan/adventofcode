import sys

a,b = list(map(int, sys.stdin.readline().rstrip().split('-')))

def valid_password_p1(password):
  password = str(password)
  two_adjacent_digits = False

  for i in range(len(password) - 1):

    if int(password[i + 1]) < int(password[i]):
      return False

    if not two_adjacent_digits and password[i] == password[i + 1]:
      two_adjacent_digits = True

  if two_adjacent_digits:
    return password
  else:
    return False

p1 = 0
valid_passwords = []
for password in range(a, b):
  valid_password = valid_password_p1(password)
  if valid_password:
    valid_passwords.append(valid_password)


def valid_password_p2(password):
  for i in range(len(password) - 1):

    if password[i] == password[i + 1]:
      # check that left nor right is same
      if i == 0: # if first pair to check
        if password[i] != password[i + 2]:
          return True
      elif i == len(password) - 2: # if last two pairs to check
        if password[i] != password[i - 1]:
          return True
      elif password[i] not in [password[i - 1], password[i + 2]]: # check a pair with digits left and right of the pair
        return True
  return False

p2 = 0
for password in valid_passwords:
  p2 += valid_password_p2(password)

print(len(valid_passwords))
print(p2)
