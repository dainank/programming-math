from re import X

from abc import ABCMeta, abstractmethod


class Vector(metaclass=ABCMeta):
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


class Vec2(Vector):  # 2d vector
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self):         # how to format object called up
        return "Vec2({},{})".format(self.x, self.y)

    def __eq__(self, other):    # what counts as equal
        return self.x == other.x and self.y == other.y

    def add(self, v2):
        return Vec2(self.x + v2.x, self.y + v2.y)

    def scale(self, scalar):
        return Vec2(scalar * self.x, scalar * self.y)


class Vec3(Vector):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

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


# impl
v = Vec2(3, 4)
w = v.add(Vec2(1, 2))
print(w)

# Unit Tests
from random import uniform
from math import isclose

def random_scalar():
   return uniform(-10,10)

def random_vec2():
   return Vec2(random_scalar(),random_scalar())

a = random_scalar()
u, v  = random_vec2(), random_vec2()
assert a * (u + v) == a * v  + a * u


def approx_equal_vec2(v,w):
    return isclose(v.x,w.x) and isclose(v.y,w.y)

for _ in range(0,100):
    a = random_scalar()
    u, v  = random_vec2(), random_vec2()
    assert approx_equal_vec2(a * (u + v), 
                             a * v + a * u)
