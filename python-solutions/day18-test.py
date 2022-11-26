import unittest
from day18 import do_math, parse_values

class TestDay18(unittest.TestCase):
    def testDoMath(self):
        operations = [1, "+", 2, "*", 3, "+", 4, "*", 5, "+", 6]
        self.assertEqual(71, do_math(operations))

    def testParseValuesWithNoParentheses(self):
        line = "1 + 2 * 3 + 4 * 5 + 6"
        self.assertEqual([1, "+", 2, "*", 3, "+", 4, "*", 5, "+", 6], parse_values(line)[0])

    def testParseValueWithSimpleParentheses(self):
        line = "1 + (2 + 3)"
        self.assertEqual([1, "+", [2, "+", 3]], parse_values(line)[0])