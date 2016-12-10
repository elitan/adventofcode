import re
import sys

test = True
test = False

re_hand_out = re.compile(r'value (\d+) goes to bot (\d+)')
re_instruction = re.compile(r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)')

def add_value_to_bot(bot_n, value, bot_container):
    value = int(value)
    if bot_n in bot_container:
        bot_container[bot_n].append(value)
    else:
        bot_container[bot_n] = [value]
    bot_container[bot_n].sort()

def init_bot_container(bot_n, bot_container):
    if bot_n not in bot_container:
        bot_container[bot_n] = []

def print_bot_container(bot_container, bots):
    chip_n = []
    for n in bots:
        if len(bot_container[n]) > 0:
            print(n, bot_container[n])
            for x in bot_container[n]:
                if x in chip_n:
                    sys.exit()
                else:
                    chip_n.append(x)

bots = []
bot_instruction = {}
bot_container = {}


input_file = 'input'
if test:
    input_file = 'test'

with open(input_file, 'r') as f:
    for line in f:
        line = line.rstrip()

        hand_out_match = re.findall(re_hand_out, line)
        if hand_out_match:
            value, bot_n = hand_out_match[0]
            add_value_to_bot(bot_n, value, bot_container)
            if bot_n not in bots:
                bots.append(bot_n)
            continue

        instruction_match = re.findall(re_instruction, line)
        if instruction_match:
            giver_bot_n, lower_taker_type, lower_taker_n, higher_taker_type, higher_taker_n = instruction_match[0]
            print('instruction match', giver_bot_n, lower_taker_type, lower_taker_n, higher_taker_type, higher_taker_n)
            bot_instruction[giver_bot_n] = {
                'lower_taker_type': lower_taker_type,
                'lower_taker_n': lower_taker_n,
                'higher_taker_type': higher_taker_type,
                'higher_taker_n': higher_taker_n,
            }
            if giver_bot_n not in bots:
                bots.append(giver_bot_n)
            continue

print(bot_container)
print(bot_instruction)
print(bots)
print('')
print('')
print('')

for bot_n in bots:
    init_bot_container(bot_n, bot_container)

match_container = [17, 61]
if test:
    match_container = [2, 3]

while True:
    for bot_n in bots:
        if len(bot_container[bot_n]) != 2:
            continue

        print('do instructions for bot n: ', bot_n)
        bot_container[bot_n].sort()
        if bot_container[bot_n] == match_container:
            print(bot_container[bot_n], match_container)
            print('FOUND!', bot_n)
            sys.exit()

        # do instruction
        lower_taker_type = bot_instruction[bot_n]['lower_taker_type']
        lower_taker_n = bot_instruction[bot_n]['lower_taker_n']
        higher_taker_type = bot_instruction[bot_n]['higher_taker_type']
        higher_taker_n = bot_instruction[bot_n]['higher_taker_n']
        print(lower_taker_type, lower_taker_n, higher_taker_type, higher_taker_n)

        # handle lowest value
        if lower_taker_type == 'bot':
            add_value_to_bot(lower_taker_n, bot_container[bot_n][0], bot_container)

        # handle highest value
        if higher_taker_type == 'bot':
            add_value_to_bot(higher_taker_n, bot_container[bot_n][-1], bot_container)

        # reset bots container
        bot_container[bot_n] = []

        print_bot_container(bot_container, bots)
        input('')
