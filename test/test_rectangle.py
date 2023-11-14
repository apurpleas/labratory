import unittest

from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_wrong_arguments(self):
        self.assertRaises(ValueError, perimeter, "abc", "bca")

    def test_negative_numbers(self):
        self.assertRaises(ValueError, perimeter, -1, 16)

    def test_none_argument(self):
        self.assertRaises(ValueError, perimeter, None, None)

    def test_wrong_arguments_area(self):
        self.assertRaises(ValueError, area, "abc", "")

    def test_negative_numbers_area(self):
        self.assertRaises(ValueError, area, -1, 15)

    def test_none_argument_area(self):
        self.assertRaises(ValueError, area, None, 18)