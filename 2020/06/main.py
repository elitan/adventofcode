import sys


def get_all_answers():
    all_answers = []
    group_answers = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            all_answers.append(group_answers)
            group_answers = []
            continue
        group_answers.append(list(line))
    all_answers.append(group_answers)
    return all_answers


all_answers = get_all_answers()
p1 = 0
for group_answers in all_answers:
    tmp = []
    for a in group_answers:
        tmp.extend(a)
    p1 += len(set(tmp))
print(p1)

p2 = 0
for group_answers in all_answers:
    p2 += len(set(group_answers[0]).intersection(*map(set, group_answers)))
print(p2)
