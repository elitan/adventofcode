import re
import sys
import itertools
import copy


def getFloors():

    # static tmp
    floors = [[] for x in range(4)]
    floors[3] = ['.', '.', '.', '.', '.']
    floors[2] = ['.', '.', '.', '.', '.']
    floors[1] = ['E', 'HG', 'HM', 'LG', '.']
    floors[0] = ['.', '.', '.', 'LM', '.']
    return floors

    # TODO
    re_floor = r'The (\w+) floor contains a '
    floors = []
    with open('test') as fh:
        for line in fh:
            line = line.strip();

            # remove first '... floor contains a '
            line = re.sub(re_floor, '', line)

            units = line.split(', ')
            print(line)
            for i, unit in enumerate(units):
                units[i] = unit.replace('a ', '').replace('and a ', '').replace('.', '')

            print(units)
            input()

    sys.exit()

def printFloors(floors):
    for x in reversed(range(len(floors))):

        # loop all rows on this floor
        for y in floors[x]:
            print('{}\t'.format(y), end='')
        print('')

def splitFloorsAndElivator(floors):
    new_floors = []
    elivator_floor = 0
    for i, floor in enumerate(floors):
        new_floors.append(floor[1:])
        if floor[0] == 'E':
            elivator_floor = i

    return elivator_floor, new_floors


def generatePossibleSteps(floors):

    elivator_floor, floors = splitFloorsAndElivator(floors);

    max_floor = len(floors) - 1
    objects = []
    objects_position = {}

    for i, obj in enumerate(floors[elivator_floor]):
        if obj == '.':
            continue

        objects_position[obj] = i
        objects.append(obj)
    print(objects)
    print(objects_position)

    # if no objects on this floor. Return empty possible steps
    if len(objects) == 0:
        return []

    possible_steps = []

    # 1 element handle
    for obj in objects:

        # move up
        # safe to move up?
        if elivator_floor != max_floor:
            print('move up OK')
            new_floors = copy.deepcopy(floors)

            # move up
            new_floors[elivator_floor][objects_position[obj]] = '.'
            new_floors[elivator_floor + 1][objects_position[obj]] = obj
            possible_steps.append(new_floors)
            print(new_floors)
            printFloors(new_floors)
            sys.exit()

        # move down
        if elivator_floor != 0:
            print('move down OK')
            new_floors = copy.deepcopy(floors)

            # move up
            new_floors[elivator_floor][objects_position[obj]] = '.'
            new_floors[elivator_floor - 1][objects_position[obj]] = obj
            possible_steps.append(new_floors)

    print(possible_steps)
    sys.exit()
    for step in possible_steps:
        print(step)
        printFloors(step)
        sys.exit()


    # 2 or more elements handle
    # first loop for permutations var 'r'
    for r in range(2, len(objects)):
        for obj_collection in itertools.permutations(objects, r):

            print(type(obj_collection))
            print(obj_collection)
        sys.exit()



    # start with
    print(floors[elivator_floor])
    pass


def main():
    # generator: 0
    # chip: 1

    floors = getFloors()
    elivator_floor = 1
    steps_taken = set()

    printFloors(floors)

    generatePossibleSteps(floors)


if __name__ == "__main__":
    main()
