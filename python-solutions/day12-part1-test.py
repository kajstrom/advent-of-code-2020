import unittest
from day12 import Ship

def make_action(type, value):
    return {
        "type": type,
        "value": value
    }

class TestDay12(unittest.TestCase):

    def testTurnRight90Deg(self):
        the_ship = Ship()
        the_ship.perform_action({
            "type": "R",
            "value": 90
        })

        self.assertEqual("S", the_ship.direction)

    def testTurnRight180Deg(self):
        the_ship = Ship()
        the_ship.perform_action(make_action("R", 180))

        self.assertEqual("W", the_ship.direction)

    def testTurnRight270Deg(self):
        the_ship = Ship()
        the_ship.perform_action(make_action("R", 270))

        self.assertEqual("N", the_ship.direction)

    def testTurnLeft90Deg(self):
        the_ship = Ship()
        the_ship.perform_action(make_action("L", 90))

        self.assertEqual("N", the_ship.direction)

    def testTurnLeft180Deg(self):
        the_ship = Ship()
        the_ship.perform_action(make_action("L", 180))

        self.assertEqual("W", the_ship.direction)

    def testTurnLeft270Deg(self):
        the_ship = Ship()
        the_ship.perform_action(make_action("L", 270))

        self.assertEqual("S", the_ship.direction)

if __name__ == '__main__':
    unittest.main()