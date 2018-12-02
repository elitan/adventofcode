import sys

def part1(ids):
    twice_n = 0
    three_times_n = 0
    for id in ids:
        twice_added = False
        three_times_added = False
        for letter in id:
            c = id.count(letter)
            if not twice_added and c == 2:
                twice_added = True
                twice_n += 1
            if not three_times_added and c == 3:
                three_times_added = True
                three_times_n += 1
    return twice_n * three_times_n

def part2(ids):
    for id in ids:
        for id_check in ids:
            # skipp if same
            if id == id_check:
                continue
            # XOR per letter => True of not same chars. Sum Trues(1).
            diff_result = [(ord(a) ^ ord(b)) != 0 for a,b in zip(id, id_check)]
            if sum(diff_result) == 1: # found it
                # build result id
                res_id = ""
                for i, letter in enumerate(id):
                    if not diff_result[i]:
                        res_id += letter
                return res_id

def main():
    ids = [x.rstrip() for x in sys.stdin]
    print(part1(ids))
    print(part2(ids))

if __name__ == '__main__':
    main()
