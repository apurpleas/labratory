import math
import unittest

def area(r: float) -> float:
    """
    Calculates the area of the circle through the radius
    :param r: radius
    :returns area
    """
    return math.pi * r * r


def perimeter(r: float) -> float:
    """
    Calculates the perimeter of the circle through the radius
    :param r: radius
    :returns perimeter
    """
    return 2 * math.pi * r



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
