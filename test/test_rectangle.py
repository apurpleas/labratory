import unittest

def area(a: float, b: float) -> float:
    """
    Calculates the area of the rectangle
    :param a: first side of the rectangle
    :param b: second side of the rectangle
    :returns area
    """
    return a * b


def perimeter(a: float, b: float) -> float:
    """
    Calculates the perimeter of the rectangle
    :param a: first side of the rectangle
    :param b: second side of the rectangle
    :returns perimeter
    """
    return 2 * (a + b)


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