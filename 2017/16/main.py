length = 16
instructions_a = [x for x in open('in').readline().strip().split(',')]

instructions_b = []
for inst in instructions_a:

    inst_name = inst[0]

    if inst_name == 's':
        instructions_b.append((inst_name, -1 * int(inst[1:])))
    elif inst_name == 'x':
        instructions_b.append((inst_name, list(map(int, inst[1:].split('/')))))
    elif inst_name == 'p':
        instructions_b.append((inst_name, [x for x in inst[1:].split('/')]))


programs_mapper = {}
programs = [chr(x + 97) for x in range(16)]
current_programs_str = ''.join(programs)

seen = set()

for dance_count in range(10**9):

    if current_programs_str in programs_mapper:
        current_programs_str = programs_mapper[current_programs_str]
        continue

    for full_inst in instructions_b:

        inst, param = full_inst

        if inst == 's':
            programs = programs[param:] + programs[:param]

        elif inst == 'x':

            a, b = param

            tmp = programs[a]

            programs[a] = programs[b]
            programs[b] = tmp

        elif inst == 'p':

            a, b = param

            a_i, b_i = programs.index(a), programs.index(b)

            tmp = programs[a_i]
            programs[a_i] = programs[b_i]
            programs[b_i] = tmp

    str_program = ''.join(programs)

    programs_mapper[current_programs_str] = str_program

    current_programs_str = str_program

print(current_programs_str)
