import itertools
import sys
import copy

def printState(state):
    floors = state[1]
    print('e#', state[0])
    for floor in floors[::-1]:
        print(floor)
    # print('')

def stateIsLegal(state):
    elevator = state[0]
    floors = state[1]
    floor_to_check = floors[elevator]

    generators = set()
    microchips = set()

    for obj in floor_to_check:
        name, unit = list(obj)
        if unit == 'G':
            generators.add(name)
        if unit == 'M':
            microchips.add(name)

    if len(microchips) > len(generators):
        return False

    generators_keep = set()
    microchips_keep = set()

    # keep generators that are not connected
    for generator_name in generators:
        if generator_name not in microchips:
            generators_keep.add(generator_name)

    # keep microships that are not connected
    for microchip_name in microchips:
        if microchip_name not in generators:
            microchips_keep.add(microchip_name)

    if len(generators_keep) > 0 and len(microchips_keep) > 0:
        return False

    return True

def stateFinished(state):

    floors = state[1]

    # check all floors except the top floor
    # if all floors are empty, except the top. State is finished
    for floor in floors[:-1]:
        if len(floor) != 0:
            return False
    return True

def anyFinishedStates(states):
    for state in states:
        if stateFinished(state):
            printState(state)
            return True
    return False

def generatePossibleStates(state, states_visited):
    elevator = state[0]
    floors = state[1]
    max_floor = len(floors) - 1 # starting at index 0

    possible_states = []

    # if no objects on this floor. Return empty possible steps
    if len(floors[elevator]) == 0:
        return possible_states

    base_floors = [list(floor) for floor in floors]

    # handle 1 object
    for obj in base_floors[elevator]:

        # move up
        if elevator != max_floor:
            tmp_floors = copy.deepcopy(base_floors)
            tmp_floors[elevator + 1].append(obj)
            tmp_floors[elevator].remove(obj)
            possible_states.append((elevator + 1, tuple([tuple(sorted(floor)) for floor in tmp_floors])))

        # move down
        if elevator != 0:
            tmp_floors = copy.deepcopy(base_floors)
            tmp_floors[elevator - 1].append(obj)
            tmp_floors[elevator].remove(obj)
            possible_states.append((elevator - 1, tuple([tuple(sorted(floor)) for floor in tmp_floors])))

    # handle 2 objects, early exit
    if len(floors[elevator]) < 2:
        return possible_states

    for combination in itertools.combinations(base_floors[elevator], 2):

        # move up
        if elevator != max_floor:
            tmp_floors = copy.deepcopy(base_floors)
            tmp_floors[elevator + 1] = tmp_floors[elevator + 1] + list(combination)
            tmp_floors[elevator] = set(tmp_floors[elevator]) - set(combination)
            possible_states.append((elevator + 1, tuple([tuple(floor) for floor in tmp_floors])))

        # move down
        if elevator != 0:
            tmp_floors = copy.deepcopy(base_floors)
            tmp_floors[elevator - 1] = tmp_floors[elevator - 1] + list(combination)
            tmp_floors[elevator] = set(tmp_floors[elevator]) - set(combination)
            possible_states.append((elevator - 1, tuple([tuple(floor) for floor in tmp_floors])))


    true_possible_states = []
    # clear from floors already visited
    for possible_state in possible_states:
        # check if not already visited nor illigal
        if possible_state not in states_visited and stateIsLegal(possible_state):
            true_possible_states.append(possible_state)
            states_visited.add(possible_state)

    #
    return true_possible_states


def main():

    states_visited = set()
    states_to_visit = []
    finished = False

    steps = 0
    elevator = 0
    floors = (('HM', 'LM'), ('HG',), ('LG',), ())
    floors = (('SG', 'SM', 'PG', 'PM'), ('TG', 'RG', 'RM', 'CG', 'CM'), ('TM', ), ())
    first_state = (elevator, (floors))

    states_visited.add(first_state)
    states_to_visit.append(first_state)

    while not finished and len(states_to_visit) != 0:


        # new states for this 'step'
        new_states = []

        print('')
        print('all new states at step: {}!'.format(steps))
        print('states visited: {}'.format(len(states_visited)))
        print('')
        for state in states_to_visit:

            # printState(state)

            generated_new_states = generatePossibleStates(state, states_visited)

            if anyFinishedStates(generated_new_states):
                finished = True
                print('finished in {} steps'.format(steps + 1))
                sys.exit()
                print('new states: ', new_states)

            new_states += generated_new_states


        states_to_visit = new_states
        # all states visited for this step, go to next
        steps += 1



if __name__ == "__main__":
    main()
