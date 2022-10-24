from math import isclose
from random import uniform

from abc import ABCMeta, abstractmethod, abstractproperty


class Vector(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def zero():
        pass

    def __neg__(self):
        return self.scale(-1)

    @abstractmethod
    def scale(self, scalar):
        pass

    @abstractmethod
    def add(self, other):
        pass

    def subtract(self, other):
        return self.add(-1 * other)

    def __sub__(self, other):
        return self.subtract(other)

    def __mul__(self, scalar):
        return self.scale(scalar)

    def __rmul__(self, scalar):
        return self.scale(scalar)

    def __add__(self, other):
        return self.add(other)

    def __truediv__(self, scalar):
        return self.scale(1.0/scalar)


class Vec0(Vector):
    def __init__(self):
        pass

    def add(self, other):
        return Vec0()

    def scale(self, scalar):
        return Vec0()

    @classmethod
    def zero(cls):
        return Vec0()

    def __eq__(self, other):
        return self.__class__ == other.__class__ == Vec0

    def __repr__(self):
        return "Vec0()"


class Vec2(Vector):  # 2d vector
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self):         # how to format object called up
        return "Vec2({},{})".format(self.x, self.y)

    def __eq__(self, other):    # what counts as equal
        return self.x == other.x and self.y == other.y

    def zero():
        return Vec2(0, 0)

    def add(self, v2):
        return Vec2(self.x + v2.x, self.y + v2.y)

    def scale(self, scalar):
        return Vec2(scalar * self.x, scalar * self.y)


class Vec3(Vector):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def zero():
        return Vec3(0, 0, 0)

    def add(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def scale(self, scalar):
        return Vec3(scalar * self.x, scalar * self.y, scalar * self.z)

    def __eq__(self, other):
        return (self.x == other.x
                and self.y == other.y
                and self.z == other.z)

    def __repr__(self):
        return "Vec3({},{},{})".format(self.x, self.y, self.z)


class Vec1(Vector):
    def __init__(self, x):
        self.x = x

    def add(self, other):
        return Vec1(self.x + other.x)

    def scale(self, scalar):
        return Vec1(scalar * self.x)

    @classmethod
    def zero(cls):
        return Vec1(0)

    def __eq__(self, other):
        return self.x == other.x

    def __repr__(self):
        return "Vec1({})".format(self.x)


class CoordinateVector(Vector):
    @abstractmethod
    def dimension(self):
        pass

    def __init__(self, *coordinates):
        self.coordinates = tuple(x for x in coordinates)

    def __repr__(self):
        return "{}{}".format(self.__class__.__qualname__, self.coordinates)


# impl
v = Vec2(3, 4)
w = v.add(Vec2(1, 2))
print(w)

# Unit Tests


def random_scalar():
    return uniform(-10, 10)


def random_vec2():
    return Vec2(random_scalar(), random_scalar())


def random_vec3():
    return Vec3(random_scalar(), random_scalar(), random_scalar())


a = random_scalar()
u, v = random_vec2(), random_vec2()
assert a * (u + v) == a * v + a * u


def approx_equal_vec2(v, w):
    return isclose(v.x, w.x) and isclose(v.y, w.y)


def approx_equal_vec3(v, w):
    return isclose(v.x, w.x) and isclose(v.y, w.y) and isclose(v.z, w.z)


for _ in range(0, 100):
    a = random_scalar()
    u, v = random_vec2(), random_vec2()
    assert approx_equal_vec2(a * (u + v),
                             a * v + a * u)


def test(zero, eq, a, b, u, v, w):
    ...
    assert eq(zero + v, v)
    assert eq(0 * v, zero)
    assert eq(-v + v, zero)


for i in range(0, 100):
    a, b = random_scalar(), random_scalar()
    u, v, w = random_vec3(), random_vec3(), random_vec3()
    test(approx_equal_vec3, a, b, u, v, w)
