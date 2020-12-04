import sys
import re

re_hgt = r"^(\d+)(cm|in)$"
re_hcl = r"^#[a-z0-9]{6}$"
re_pid = r"^\d{9}$"


def get_passports():
    passports = []
    passport = {}

    for row in sys.stdin:
        row = row.strip()
        if not row:
            passports.append(passport)
            passport = {}
            continue

        for item in row.split(' '):
            key, value = item.split(':')
            passport[key] = value
    passports.append(passport)  # add last passport
    return passports


def valid_passport_p1(passport, required_keys):
    return len(required_keys - set(passport.keys())) == 0


def valid_passport_p2(passport, required_keys, valid_ecl_values):
    if len(required_keys - set(passport.keys())) != 0:
        return False

    if not 1920 <= int(passport['byr']) <= 2002:
        return False

    if not 2010 <= int(passport['iyr']) <= 2020:
        return False

    if not 2020 <= int(passport['eyr']) <= 2030:
        return False

    match = re.findall(re_hgt, passport['hgt'])
    if not match:
        return False

    value, unit = match[0]
    value = int(value)
    if unit == 'cm' and not 150 <= value <= 193:
        return False
    if unit == 'in' and not 59 <= value <= 76:
        return False

    re_search_res = re.findall(re_hcl, passport['hcl'])
    if not re_search_res:
        return False

    if not passport['ecl'] in valid_ecl_values:
        return False

    re_search_res = re.findall(re_pid, passport['pid'])
    if not re_search_res:
        return False

    return True


required_keys = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
valid_ecl_values = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
passports = get_passports()
valid_passports_p1 = 0

for passport in passports:
    valid_passports_p1 += valid_passport_p1(passport,
                                            required_keys)
print(valid_passports_p1)

valid_passports_p2 = 0
for passport in passports:
    valid_passports_p2 += valid_passport_p2(passport,
                                            required_keys, valid_ecl_values)
print(valid_passports_p2)
