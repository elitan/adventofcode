import hashlib
import sys

class Node:
    def __init__(self, current_coordinate, path, node_handler):
        self.current_coordinate = current_coordinate
        self.path = path
        self.node_handler = node_handler

    def available_doors(self):
        h = self.md5('{}{}'.format(self.node_handler.passcode, self.path))
        chars_open = list('bcdef')
        doors = []

        # check if doors are opened and within the grid
        doors.append(self.current_coordinate[1] != 0 and h[0] in chars_open)                        # up
        doors.append(self.current_coordinate[1] < (self.node_handler.grid_size[1] - 1) and h[1] in chars_open)   # down
        doors.append(self.current_coordinate[0] != 0 and h[2] in chars_open)                        # left
        doors.append(self.current_coordinate[0] < (self.node_handler.grid_size[0] - 1) and h[3] in chars_open)   # right

        return doors

    def md5(self, s):
        return hashlib.md5(s.encode()).hexdigest()

    def add_node(self, path, new_coordinate):
        node = Node(new_coordinate, path, self.node_handler)
        self.node_handler.add_node(node)

    def run(self):
        if self.current_coordinate == (3, 3):
            if not self.node_handler.found_first:
                print('#1: ', self.path)
                self.node_handler.found_first = True
            self.node_handler.path_lengths.append(len(self.path))
            return

        doors = self.available_doors()

        if doors[0]: # up
            path = '{}{}'.format(self.path, 'U')
            new_coordinate = (self.current_coordinate[0], self.current_coordinate[1] - 1)
            self.add_node(path, new_coordinate)
        if doors[1]: # down
            path = '{}{}'.format(self.path, 'D')
            new_coordinate = (self.current_coordinate[0], self.current_coordinate[1] + 1)
            self.add_node(path, new_coordinate)
        if doors[2]: # left
            path = '{}{}'.format(self.path, 'L')
            new_coordinate = (self.current_coordinate[0] - 1, self.current_coordinate[1])
            self.add_node(path, new_coordinate)
        if doors[3]: # right
            path = '{}{}'.format(self.path, 'R')
            new_coordinate = (self.current_coordinate[0] + 1, self.current_coordinate[1])
            self.add_node(path, new_coordinate)


class NodeHandler:
    def __init__(self, grid_size, passcode):
        self.grid_size = grid_size
        self.passcode = passcode
        self.node_queue = [Node((0, 0), '', self)]
        self.path_lengths = []
        self.found_first = False

    def add_node(self, node):
        self.node_queue.append(node)

    def run(self):
        while len(self.node_queue) > 0:
            node = self.node_queue[0]
            del self.node_queue[0]
            node.run()
        # answer for p2
        print('#2: ', max(self.path_lengths))


passcode = 'pvhmgsws'

node_handler = NodeHandler([4, 4], passcode)
node_handler.run()
