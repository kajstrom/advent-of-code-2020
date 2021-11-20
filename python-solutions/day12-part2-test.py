import unittest
from day12 import Ship2

def make_action(type, value):
    return {
        "type": type,
        "value": value
    }

class TestDay12(unittest.TestCase):

    def testTurnRight90Deg(self):
        the_ship = Ship2()
        the_ship.perform_action({
            "type": "R",
            "value": 90
        })

        self.assertEqual(-10, the_ship.waypoint_y)
        self.assertEqual(1, the_ship.waypoint_x)

    def testTurnRight180Deg(self):
        the_ship = Ship2()
        the_ship.perform_action({
            "type": "R",
            "value": 180
        })

        self.assertEqual(-1, the_ship.waypoint_y)
        self.assertEqual(-10, the_ship.waypoint_x)

    def testTurnRight270Deg(self):
        the_ship = Ship2()
        the_ship.perform_action({
            "type": "R",
            "value": 270
        })

        self.assertEqual(10, the_ship.waypoint_y)
        self.assertEqual(-1, the_ship.waypoint_x)

    def testTurnRight360Deg(self):
        the_ship = Ship2()
        the_ship.perform_action({
            "type": "R",
            "value": 360
        })

        self.assertEqual(1, the_ship.waypoint_y)
        self.assertEqual(10, the_ship.waypoint_x)

    def testTurnLeft90Deg(self):
        the_ship = Ship2()
        the_ship.perform_action({
            "type": "L",
            "value": 90
        })

        self.assertEqual(10, the_ship.waypoint_y)
        self.assertEqual(-1, the_ship.waypoint_x)

    def testTurnLeft180Deg(self):
        the_ship = Ship2()
        the_ship.perform_action({
            "type": "L",
            "value": 180
        })

        self.assertEqual(-1, the_ship.waypoint_y)
        self.assertEqual(-10, the_ship.waypoint_x)

    def testTurnLeft270Deg(self):
        the_ship = Ship2()
        the_ship.perform_action({
            "type": "L",
            "value": 270
        })

        self.assertEqual(-10, the_ship.waypoint_y)
        self.assertEqual(1, the_ship.waypoint_x)

    def testMoveNorth(self):
        the_ship = Ship2()
        the_ship.perform_action({
            "type": "N",
            "value": 3
        })

        self.assertEqual(4, the_ship.waypoint_y)
        self.assertEqual(10, the_ship.waypoint_x)

    def testMoveSouth(self):
        the_ship = Ship2()
        the_ship.perform_action({
            "type": "S",
            "value": 3
        })

        self.assertEqual(-2, the_ship.waypoint_y)
        self.assertEqual(10, the_ship.waypoint_x)

    def testMoveWest(self):
        the_ship = Ship2()
        the_ship.perform_action({
            "type": "W",
            "value": 3
        })

        self.assertEqual(1, the_ship.waypoint_y)
        self.assertEqual(7, the_ship.waypoint_x)

    def testMoveEast(self):
        the_ship = Ship2()
        the_ship.perform_action({
            "type": "E",
            "value": 3
        })

        self.assertEqual(1, the_ship.waypoint_y)
        self.assertEqual(13, the_ship.waypoint_x)

    def testForward(self):
        the_ship = Ship2()
        the_ship.perform_action({
            "type": "F",
            "value": 10
        })

        self.assertEqual(100, the_ship.loc_x)
        self.assertEqual(10, the_ship.loc_y)

    def testRotateAndForward(self):
        the_ship = Ship2()
        the_ship.perform_action({
            "type": "L",
            "value": 180
        })
        the_ship.perform_action({
            "type": "F",
            "value": 10
        })

        self.assertEqual(-100, the_ship.loc_x)
        self.assertEqual(-10, the_ship.loc_y)

if __name__ == '__main__':
    unittest.main()