import unittest

def area(a: float) -> float:
    """
    Calculates the area of the square
    :param a: side of the square
    :returns area
    """
    return a * a


def perimeter(a: float) -> float:
    """
    Calculates the perimeter of the square
    :param a: side of the square
    :returns perimeter
    """
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 40)
