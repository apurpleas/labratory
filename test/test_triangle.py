import unittest

def area(a: float, h: float) -> float:
    """
    Calculates the area of the triangle
    :param a: the reference side of the triangle
    :param h: the height of the triangle
    :returns area
    """
    return a * h / 2


def perimeter(a: float, b: float, c: float) -> float:
    """
    Calculates the perimeter of the triangle
    :param a: first side of the triangle
    :param b: second side of the triangle
    :param c: third side of the triangle
    :returns perimeter
    """
    return a + b + c


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

    def test_perimeter(self):
        res = perimeter(1, 2, 3)
        self.assertEqual(res, 6)
