import subprocess

def part2():
    input_file_name = 'input'
    program_name = 'part2.py'

    variables = set()
    for line in open(input_file_name):

        variable = line.split(' ')[0]

        print('max_value = 0', file=open(program_name, 'a'))

        if variable not in variables:
            print('{} = 0'.format(variable), file=open(program_name, 'a'))

        variables.add(variable)

    for line in open(input_file_name):

        variable = line.split(' ')[0]

        print('{} else 0'.format(line.rstrip().replace('inc', '+=').replace('dec', '-=')), file=open(program_name, 'a'))

        print('max_value = max(max_value, {})'.format(variable), file=open(program_name, 'a'))


    print('print(max_value)', file=open(program_name, 'a'))

    result = subprocess.run(['python', program_name], stdout=subprocess.PIPE)
    result = result.stdout.decode('utf-8')

    subprocess.run(['rm', program_name], stdout=subprocess.PIPE)

    return result

def part1():
    input_file_name = 'input'
    program_name = 'part1.py'

    variables = set()
    for line in open(input_file_name):

        variable = line.split(' ')[0]

        if variable not in variables:
            print('{} = 0'.format(variable), file=open(program_name, 'a'))

        variables.add(variable)

    for line in open(input_file_name):

        print('{} else 0'.format(line.rstrip().replace('inc', '+=').replace('dec', '-=')), file=open(program_name, 'a'))


    print('print(max(', end='', file=open(program_name, 'a'))
    for v in variables:
        print('{}, '.format(v), end='', file=open(program_name, 'a'))
    print('))', file=open(program_name, 'a'))

    result = subprocess.run(['python', program_name], stdout=subprocess.PIPE)
    result = result.stdout.decode('utf-8')

    subprocess.run(['rm', program_name], stdout=subprocess.PIPE)

    return result

def main():
    print('part1: ', part1())
    print('part2: ', part2())

if __name__ == '__main__':
    main()
