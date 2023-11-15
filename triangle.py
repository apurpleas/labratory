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