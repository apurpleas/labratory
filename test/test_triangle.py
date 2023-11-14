import unittest

from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 1)
        self.assertEqual(res, 0)

    def test_area(self):
        res = area(10, 2)
        self.assertEqual(res, 10)

    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_nonexistent_triangle(self):
        self.assertRaises(ValueError, perimeter, 3, 5, 1)

    def test_perimeter(self):
        res = perimeter(1, 2, 3)
        self.assertEqual(res, 6)

    def test_wrong_arguments(self):
        self.assertRaises(ValueError, perimeter, "abc", 0, 0)

    def test_negative_numbers(self):
        self.assertRaises(ValueError, perimeter, -1, 15, -4)

    def test_none_argument(self):
        self.assertRaises(ValueError, perimeter, None, None, None)

    def test_wrong_arguments_area(self):
        self.assertRaises(ValueError, area, "abc", "q")

    def test_negative_numbers_area(self):
        self.assertRaises(ValueError, area, -1, 5)

    def test_none_argument_area(self):
        self.assertRaises(ValueError, area, None, None)