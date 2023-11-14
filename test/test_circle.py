import math
import unittest

from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = area(10)
        self.assertEqual(res, 100 * math.pi)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 20 * math.pi)

    def test_wrong_arguments(self):
        self.assertRaises(ValueError, perimeter, "abc")

    def test_negative_numbers(self):
        self.assertRaises(ValueError, perimeter, -1)

    def test_none_argument(self):
        self.assertRaises(ValueError, perimeter, None)

    def test_wrong_arguments_area(self):
        self.assertRaises(ValueError, area, "abc")

    def test_negative_numbers_area(self):
        self.assertRaises(ValueError, area, -1)

    def test_none_argument_area(self):
        self.assertRaises(ValueError, area, None)