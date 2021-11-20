from utils import time_fn

def read_input():
    file = open("inputs/day12.txt", "r")
    lines = file.read().splitlines()
    file.close()

    actions = []

    for line in lines:
        type = line[0:1]
        value = int(line[1:])

        actions.append({
            "type": type,
            "value": value
        })

    return actions

class Ship():
    direction = 'E'
    loc_x = 0
    loc_y = 0

    def perform_action(self, action):
        type =  action["type"]
        value = action["value"]

        if type == "R" or type == "L":
            self.turn(type, value)
        elif type in ["N", "E", "S", "W"]:
            self.move(type, value)
        elif type == "F":
            self.forward(value)
        else:
            print("Unknown action type")

    def turn(self, direction, degrees):
        directions = ["N", "E", "S", "W"]
        turns = int(degrees / 90)
        curr_idx = directions.index(self.direction)
        
        if direction == "R":
            new_direction_idx = (curr_idx + turns) % 4
            self.direction = directions[new_direction_idx]
        else:
            new_direction_idx = curr_idx - turns

            if new_direction_idx < 0:
                new_direction_idx = 4 - abs(new_direction_idx)
            
            self.direction = directions[new_direction_idx]

    def move(self, direction, value):
        if direction == "E":
            self.loc_x += value
        elif direction == "W":
            self.loc_x -= value
        elif direction == "N":
            self.loc_y += value
        elif direction == "S":
            self.loc_y -= value

    def forward(self, value):
        self.move(self.direction, value)

class Ship2():
    loc_x = 0
    loc_y = 0
    waypoint_x = 10
    waypoint_y = 1

    def perform_action(self, action):
        type = action["type"]
        value = action["value"]

        if type in ["L", "R"]:
            self.rotate(type, value)
        elif type in ["N", "E", "S", "W"]:
            self.move_waypoint(type, value)
        elif type == "F":
            self.forward(value)

    def forward(self, value):
        self.loc_x += self.waypoint_x * value
        self.loc_y += self.waypoint_y * value

    def rotate(self, direction, degrees):
        times = int(degrees / 90)

        if direction == "R":
            for _ in range(times):
                self.rotate_clockwise()
        else:
            #times = 4 - times
            for _ in range(times):
                self.rotate_counter_clockwise()

    def rotate_counter_clockwise(self):
        wy = self.waypoint_x
        wx = -1 * self.waypoint_y

        self.waypoint_y = wy
        self.waypoint_x = wx

    def rotate_clockwise(self):
        wx = self.waypoint_y
        wy = -1 * self.waypoint_x

        self.waypoint_x = wx
        self.waypoint_y = wy


    def move_waypoint(self, direction, value):
        if direction == "N":
            self.waypoint_y += value
        elif direction == "S":
            self.waypoint_y -= value
        elif direction == "E":
            self.waypoint_x += value
        elif direction == "W":
            self.waypoint_x -= value

actions = read_input()

def part1():
    the_ship = Ship()
    
    for action in actions:
        the_ship.perform_action(action)
        #print(f"Location {the_ship.loc_x}, {the_ship.loc_y}")

    print(f"Final location {the_ship.loc_x}, {the_ship.loc_y}")
    distance = abs(the_ship.loc_x) + abs(the_ship.loc_y)
    print(f"Part1: distance from starting point {distance}")

def part2():
    the_ship = Ship2()

    for action in actions:
        the_ship.perform_action(action)

    print(f"Final location {the_ship.loc_x}, {the_ship.loc_y}")
    distance = abs(the_ship.loc_x) + abs(the_ship.loc_y)
    print(f"Part2: distance from starting point {distance}")
    
if __name__ == '__main__':
    time_fn(part1)
    time_fn(part2)