import re
import sys
import itertools
import copy
import os

global_state_counter = 0

def generateStateIndex():
    global global_state_counter
    global_state_counter += 1
    return global_state_counter

def getState(n):

    floors = [[] for x in range(4)]
    if n == 0:
        floors[3] = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
        floors[2] = ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'TM']
        floors[1] = ['.', '.', '.', '.', 'TG', 'RG', 'RM', 'CG', 'CM', '.']
        floors[0] = ['SG', 'SM', 'PG', 'PM', '.', '.', '.', '.', '.', '.']
        return floors, 0


def getStateTestData(n):

    floors = [[] for x in range(4)]

    if n == 0:
        floors[3] = ['.', '.', '.', '.']
        floors[2] = ['.', '.', 'LG', '.']
        floors[1] = ['HG', '.', '.', '.']
        floors[0] = ['.', 'HM', '.', 'LM']
        return floors, 0

    if n == 1:
        floors[3] = ['.', '.', '.', '.']
        floors[2] = ['.', '.', 'LG', '.']
        floors[1] = ['HG', 'HM', '.', '.']
        floors[0] = ['.', '.', '.', 'LM']
        return floors, 1

    if n == 2:
        floors[3] = ['.', '.', '.', '.']
        floors[2] = ['HG', 'HM', 'LG', '.']
        floors[1] = ['.', '.', '.', '.']
        floors[0] = ['.', '.', '.', 'LM']
        return floors, 2

    if n == 3:
        floors[3] = ['.', '.', '.', '.']
        floors[2] = ['HG', '.', 'LG', '.']
        floors[1] = ['.', 'HM', '.', '.']
        floors[0] = ['.', '.', '.', 'LM']
        return floors, 1

    if n == 4:
        floors[3] = ['.', '.', '.', '.']
        floors[2] = ['HG', '.', 'LG', '.']
        floors[1] = ['.', '.', '.', '.']
        floors[0] = ['.', 'HM', '.', 'LM']
        return floors, 0

    if n == 5:
        floors[3] = ['.', '.', '.', '.']
        floors[2] = ['HG', '.', 'LG', '.']
        floors[1] = ['.', 'HM', '.', 'LM']
        floors[0] = ['.', '.', '.', '.']
        return floors, 1

    if n == 6:
        floors[3] = ['.', '.', '.', '.']
        floors[2] = ['HG', 'HM', 'LG', 'LM']
        floors[1] = ['.', '.', '.', '.']
        floors[0] = ['.', '.', '.', '.']
        return floors, 2

    if n == 7:
        floors[3] = ['.', 'HM', '.', 'LM']
        floors[2] = ['HG', '.', 'LG', '.']
        floors[1] = ['.', '.', '.', '.']
        floors[0] = ['.', '.', '.', '.']
        return floors, 3

    if n == 8:
        floors[3] = ['.', '.', '.', 'LM']
        floors[2] = ['HG', 'HM', 'LG', '.']
        floors[1] = ['.', '.', '.', '.']
        floors[0] = ['.', '.', '.', '.']
        return floors, 2

    if n == 9:
        floors[3] = ['HG.', '.', 'LG', 'LM']
        floors[2] = ['.', 'HM', '.', '.']
        floors[1] = ['.', '.', '.', '.']
        floors[0] = ['.', '.', '.', '.']
        return floors, 3

    if n == 10:
        floors[3] = ['HG.', '.', 'LG', '.']
        floors[2] = ['.', 'HM', '.', 'LM']
        floors[1] = ['.', '.', '.', '.']
        floors[0] = ['.', '.', '.', '.']
        return floors, 2

    if n == 11:
        floors[3] = ['HG.', 'HM', 'LG', 'LM']
        floors[2] = ['.', '.', '.', '.']
        floors[1] = ['.', '.', '.', '.']
        floors[0] = ['.', '.', '.', '.']
        return floors, 2

def checkValidStates(states, steps):

    state_string_must_contain = stateToString(getState(steps + 1))

    for state in states:
        state_string = stateToString(state)

        if state_string == state_string_must_contain:
            printState(state)
            print('BINGO!')
            input()
            return

    print('NO SHOW!!!')
    print('steps: ', steps)
    input()


def getStartState():

    # static tmp
    floors = [[] for x in range(4)]
    floors[3] = ['.', '.', '.', '.']
    floors[2] = ['.', '.', 'LG', '.']
    floors[1] = ['HG', '.', '.', '.']
    floors[0] = ['.', 'HM', '.', 'LM']
    return floors,  0

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

def printStates(states):
    for state in states:
        printState(state)

def printState(state):

    floors, elivator_floor, state_index = state
    print('--- state id: {} ---'.format(state_index))

    floors_n = len(floors) - 1 # starting from 0
    for i, x in enumerate(reversed(range(len(floors)))):

        current_floor = floors_n - i

        if elivator_floor == current_floor:
            print('E\t', end='')
        else:
            print('.\t', end='')

        # loop all rows on this floor
        for y in floors[x]:
            print('{}\t'.format(y), end='')
        print('')
    print('---')
    print('')

def splitFloorsAndElivator(floors):
    new_floors = []
    elevator_floor = 0
    for i, floor in enumerate(floors):
        new_floors.append(floor[1:])
        if floor[0] == 'E':
            elevator_floor = i

    return elevator_floor, new_floors



def removeAlreadyVisitedStates(states, states_visited):

    states_not_visited = []

    for state in states:

        floors, elivator_floor, state_index = state

        # generate state string
        state_string = stateToString(state)

        # state is not visited
        if state_string not in states_visited:
            states_not_visited.append(state)

    return states_not_visited

def stateIsLegal(state):
    floors, elevator_floor, state_index = state

    generators = set()
    microchips = set()
    # search for generator and chips
    for p in floors[elevator_floor]:
        if p != '.':
            name, unit = list(p)
            if unit == 'G':
                generators.add(name)
            if unit == 'M':
                microchips.add(name)

    generators_keep = set()
    microchips_keep = set()

    # keep microships that are not connected
    for microchip_name in microchips:
        if microchip_name not in generators:
            microchips_keep.add(microchip_name)

    if len(generators) > 0 and len(microchips_keep) > 0:
        return False

    return True

def removeIlligalStates(states):

    legal_states = []

    for state in states:
        if stateIsLegal(state):
            legal_states.append(state)


    return legal_states

def stateToString(state):

    floors, elevator_floor, state_index = state

    # set elevator floor n at the beginning
    state_string = '{}'.format(elevator_floor)
    state_string += '#'

    for floor in floors:
        state_string += ''.join(floor)
        state_string += '#'

    return state_string

def updateStatesVisited(states, states_visited):

    for state in states:

        # generate state string
        state_string = stateToString(state)

        # add the string to the set of states visited
        states_visited.add(state_string)

    return states_visited

def generatePossibleStates(state, states_visited):

    floors, elevator_floor, state_index = state

    max_floor = len(floors) - 1
    objects = []
    objects_position = {}

    for i, obj in enumerate(floors[elevator_floor]):
        if obj == '.':
            continue

        objects_position[obj] = i
        objects.append(obj)

    # if no objects on this floor. Return empty possible steps
    if len(objects) == 0:
        return []

    possible_states = []

    # 1 element handle
    for obj in objects:

        # move up
        # safe to move up?
        if elevator_floor != max_floor:
            new_floors = copy.deepcopy(floors)

            # generate new floors by move up
            new_floors[elevator_floor][objects_position[obj]] = '.'
            new_floors[elevator_floor + 1][objects_position[obj]] = obj
            possible_states.append([new_floors, elevator_floor + 1, generateStateIndex()])

        # move down
        # safe to move down?
        if elevator_floor != 0:
            new_floors = copy.deepcopy(floors)

            # generate new floors by move down
            new_floors[elevator_floor][objects_position[obj]] = '.'
            new_floors[elevator_floor - 1][objects_position[obj]] = obj
            possible_states.append([new_floors, elevator_floor - 1, generateStateIndex()])

    # if you should try to carry 2 objects, only if there are two
    # objects at the current floor
    if len(objects) >= 2:
        for obj_collection in itertools.combinations(objects, 2):

            # safe to move up?
            if elevator_floor != max_floor:
                new_floors = copy.deepcopy(floors)

                # generate new floors by move up
                for obj in obj_collection:
                    new_floors[elevator_floor][objects_position[obj]] = '.'
                    new_floors[elevator_floor + 1][objects_position[obj]] = obj

                # add the new state to possible states
                possible_states.append([new_floors, elevator_floor + 1, generateStateIndex()])

            # safe to move down?
            if elevator_floor != 0:
                new_floors = copy.deepcopy(floors)

                # generate new floors by move down
                for obj in obj_collection:
                    new_floors[elevator_floor][objects_position[obj]] = '.'
                    new_floors[elevator_floor - 1][objects_position[obj]] = obj

                # add the new state to possible states
                possible_states.append([new_floors, elevator_floor - 1, generateStateIndex()])


    # remove states already visited
    possible_states = removeAlreadyVisitedStates(possible_states, states_visited)

    possible_states = removeIlligalStates(possible_states)

    return possible_states

def finishedState(state):
    floors, elevator_floor, state_index = state
    for pos in floors[-1]:
        if pos == '.':
            return False
    return True


def anyFinishedStates(states):
    for state in states:
        floors, elevator_floor, state_index = state

        if finishedState(state):
            return True

    # if no states
    return False


def main():

    steps = 0
    new_states = [getState(steps) + (generateStateIndex(), )]
    states_visited = set()
    states_visited = updateStatesVisited(new_states, states_visited)

    finished = False

    while not finished and len(new_states) != 0:

        states = new_states
        new_states = []

        print('')
        print('')
        print('currently on step: ', steps)
        print('')
        print('')

        # generate next step new states
        for state in states:

            # any finsihed states in the current new_states?
            if anyFinishedStates(states):
                finished = True
                print('finished state found')
                print('steps: ', steps)
                sys.exit()
                continue

            # generate new states for current floor we are looking at
            new_states_tmp = generatePossibleStates(state, states_visited)

            # also update state visited
            states_visited = updateStatesVisited(new_states_tmp, states_visited)
            # print('states visited:', len(states_visited))
            # for sv in states_visited:
            #     print(sv)

            # for each state in new states tmp, add to new states
            for state_tmp in new_states_tmp:
                new_states.append(state_tmp)
                floors, elevator_floor, state_index = state

        # print('new states for next step:', len(new_states))
        # print('press enter to show states')
        # input()
        # printStates(new_states)
        # print('press enter to go to next step')
        # input()

        # checkValidStates(new_states, steps)
        # we have now taken yet another step for next iteration
        steps += 1

    print('all states examined')



if __name__ == "__main__":
    main()
