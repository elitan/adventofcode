import hashlib

class Node:
    def __init__(self, passcode, current_coordinate, path, visited_nodes):
        self.passcode = passcode
        self.current_coordinate = current_coordinate
        self.path = path
        self.visited_nodes = visited_nodes

    def available_doors(in_data, path, coords):
        global GRID_SIZE
        h = self.md5('{}{}'.format(in_data, path))
        chars_open = list('bcdef')
        doors = []
        doors.append(coords[1] != 0 and h[0] in chars_open)             # up
        doors.append(coords[1] < GRID_SIZE[1] and h[1] in chars_open)   # down
        doors.append(coords[0] != 0 and h[2] in chars_open)             # left
        doors.append(coords[0] < GRID_SIZE[0] and h[3] in chars_open)   # right
        return doors

    def md5(s):
        return hashlib.md5(s.encode()).hexdigest()

class NodeHandler:
    def __init__(self, grid_size, passcode):
        self.grid_size = grid_size
        self.passcode = passcode
        self.node_queue = [Node(self.passcode, [0, 0], '', set()))]

    def run(self):
        for node in self.node_queue:
            print('handle node... in for loop')


passcode = 'pvhmgsws'
passcode = 'hijkl'

node_handler = NodeHandler([4, 4], passcode)
node_handler.run()
