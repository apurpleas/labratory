import math


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