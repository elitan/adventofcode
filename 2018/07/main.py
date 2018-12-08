import sys
import re
import time
from collections import defaultdict

def part1(instructions):

    p1 = ""

    while instructions:

        steps = set()
        steps_found = set()

        for instruction in instructions:
            a, b = instruction
            steps.add(a)
            steps.add(b)
            steps_found.add(b)

        not_found = steps - steps_found

        # get current step to take now
        step_now = list(not_found)
        step_now.sort()
        step_now = step_now[0]

        # append on p1
        p1 += step_now

        # remove instructions associated to step_now
        instructions = list(filter(lambda x: x[0] != step_now, instructions))

    p1 += list(steps)[0]
    print(p1)


def part2(instructions, workers_n):

    total_steps = set()
    waiting_steps = set()
    working_steps = set()
    completed_steps = set()

    for inst in instructions:
        a, b = inst
        total_steps.add(a)
        total_steps.add(b)
        waiting_steps.add(b)

    workers = [None for x in range(workers_n)]
    seconds = -1
    while len(completed_steps) != len(total_steps):
        seconds += 1

        # remove completed steps
        for i, worker in enumerate(workers):
            if worker is None:
                continue
            step, completed_at = worker
            if seconds == completed_at:
                workers[i] = None
                working_steps.remove(step)
                completed_steps.add(step)

        # no free workers
        if None not in workers:
            continue

        # update waiting steps
        waiting_steps = set()
        for inst in instructions:
            a, b = inst
            if a in completed_steps:
                continue
            waiting_steps.add(b)

        # add new steps
        possible_steps = list(total_steps - waiting_steps - working_steps - completed_steps)
        possible_steps.sort()
        for i, worker in enumerate(workers):
            if not possible_steps:
                break
            if worker is None:
                step = possible_steps.pop(0)
                completed_at = seconds + 60 + ord(step) - 64
                workers[i] = [step, completed_at]
                working_steps.add(step)

    print(seconds)

def main():

    regex = r"Step (.+) must be finished before step (.+) can begin."
    instructions = [re.findall(regex, x.rstrip())[0] for x in sys.stdin]

    part1(instructions)

    workers_n = 5
    part2(instructions, workers_n)


if __name__ == '__main__':
    main()
