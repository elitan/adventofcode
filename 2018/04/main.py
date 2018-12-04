import sys
import re
from collections import defaultdict, Counter

def main():

    regex_parse_lines = r"\[(\d+)-(\d+)-(\d+) (\d+):(\d+)] (.+)"
    regex_guard = r"Guard #(\d+) begins shift"

    lines = [re.findall(regex_parse_lines, x.rstrip())[0] for x in sys.stdin]
    lines.sort(key=lambda x: "".join([x[0], x[1], x[2], x[3], x[4]]))

    guard_sleeping = False
    guard_sleep_start_hour = None
    guard_sleep_start_minute = None
    guard_data = defaultdict(list)
    guard_ids = set()

    for data in lines:
        year, month, day, hour, minute, msg = data
        if msg.startswith('Guard'):
            guard_id = int(re.findall(regex_guard, msg)[0])
            guard_ids.add(guard_id)

        elif msg == 'falls asleep':
            guard_sleeping = True
            guard_sleep_start_hour = int(hour)
            guard_sleep_start_minute = int(minute)

        elif msg == 'wakes up':
            guard_sleeping = False
            for i in range(guard_sleep_start_minute, int(minute)):
                guard_data[guard_id].append(i)


    # p1
    sleepiest_guard_id = None
    sleepiest_minutes = 0
    for guard_id in guard_ids:
        if len(guard_data[guard_id]) > sleepiest_minutes:
            sleepiest_minutes = len(guard_data[guard_id])
            sleepiest_guard_id = guard_id

    m = Counter(guard_data[sleepiest_guard_id]).most_common(1)[0]
    print(sleepiest_guard_id * m[0])

    # p2
    sleepiest_guard_id = None
    sleepiest_minute = 0
    for guard_id in guard_ids:
        if len(guard_data[guard_id]) == 0:
            continue
        m = Counter(guard_data[guard_id]).most_common(1)[0]
        if m[0] > sleepiest_minute:
            sleepiest_minute = m[0]
            sleepiest_guard_id = guard_id

    # incorrect: 106224
    print(sleepiest_guard_id * sleepiest_minute)

if __name__ == '__main__':
    main()
