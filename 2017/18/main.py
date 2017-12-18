from collections import defaultdict

def getValue(v, register):
    if v.replace('-', '').isdigit():
        return int(v)
    return register[v]

def main():

    file_input_name = 'test'
    file_input_name = 'in'

    register = defaultdict(int)

    register['a'] = 2

    instructions = []

    for line in open(file_input_name):
        instructions.append(line.strip().split(' '))

    # program counter
    program_pcs = [0, 0]

    # program registers
    registers = [defaultdict(), defaultdict()]
    registers[0]['p'] = 0
    registers[1]['p'] = 1

    # program_bus[0] = 'help', is program 0 sending value 'help'
    program_bus = [[],[]]
    waiting = [False, False]
    sent_p_one = 0
    program_id = 0
    deadlock = False
    while not deadlock:

        # get current program id
        program_id = program_id % 2

        # current pc of this program
        pc = program_pcs[program_id]
        register = registers[program_id]

        # get current instruction
        instr = instructions[pc]

        if instr[0] == 'snd':
            program_bus[program_id].append(getValue(instr[1], register))

            if program_id == 1:
                    sent_p_one += 1

        elif instr[0] == 'set':
            register[instr[1]] = getValue(instr[2], register)

        elif instr[0] == 'add':
            register[instr[1]] += getValue(instr[2], register)

        elif instr[0] == 'mul':
            register[instr[1]] *= getValue(instr[2], register)

        elif instr[0] == 'mod':
            register[instr[1]] = getValue(instr[1], register) % getValue(instr[2], register)

        elif instr[0] == 'rcv':
            if not program_bus[(program_id + 1) % 2]:
                waiting[program_id] = True

                if waiting[(program_id + 1) % 2]:
                    deadlock = True

                # stay at current pc but move to next program
                program_id += 1
                continue

            register[instr[1]] = program_bus[(program_id + 1) % 2].pop(0)

        elif instr[0] == 'jgz':
            if getValue(instr[1], register) <= 0:
                program_pcs[program_id] += 1
                program_id += 1
                continue

            # make jump
            program_pcs[program_id] += getValue(instr[2], register)
            program_id += 1
            continue

        program_pcs[program_id] += 1
        program_id += 1

    print(sent_p_one)

if __name__ == '__main__':
    main()
