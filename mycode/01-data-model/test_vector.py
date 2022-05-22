import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x!r},{self.y!r})"

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other):
        x = self.x * other
        y = self.y * other
        return Vector(x, y)

    def __abs__(self):
        """
        >>> v1 = Vector(3, 4)
        >>> abs(v1)
        5.0
        """
        return math.hypot(self.x, self.y)

    def __bool__(self):
        """
        >>> v1 = Vector(0, 0)
        >>> bool(v1)
        False
        >>> v2 = Vector(1, 2)
        >>> bool(v2)
        True
        """
        return bool(abs(self))


def test_vector_plus():
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    v3 = v1 + v2

    assert v3.x == 4
    assert v3.y == 5


def test_vector_mul():
    v1 = Vector(1, 2)
    v2 = v1 * 3

    assert v2.x == 3
    assert v2.y == 6


def test_vector_abs():
    v1 = Vector(3, 4)
    assert abs(v1) == 5.0


def test_bool():
    assert bool(False) is False
    assert bool(0) is False
    assert bool(None) is False
    assert bool("") is False

    assert bool(True)
    assert bool(1)
    assert bool("1")
