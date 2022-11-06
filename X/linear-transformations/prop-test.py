from math import pi
from random import randrange
from vectors import to_polar, to_cartesian
from math import pi
from hypothesis import given, strategies as st

def return_two_vectors():
    return [(randrange(10), randrange(10)), (randrange(10), randrange(10))]

def polygon_map(transformation, polygons):
    return [
        [transformation(vertex) for vertex in triangle]
        for triangle in polygons
    ]

def rotate2d(angle, vector):
    l,a = to_polar(vector)
    return to_cartesian((l, a+angle))

def rotate_x(angle, vector):
    x,y,z = vector
    new_y, new_z = rotate2d(angle, (y,z))
    return x, new_y, new_z

def rotate_x_by(angle):
    def new_function(v):
        return rotate_x(angle,v)
    return new_function

vectors = return_two_vectors()
linear_transformation_multiple = randrange(10)
linear_transformation_rotation = rotate_x_by(pi/2)
nonlinear_transformation_squaring = 2

@given(st.integers(), st.integers(), st.integers(), st.integers(), st.integers())
def test_if_scalar_transformation_is_linear(x1, y1, x2, y2, scalar):
    assert (scalar * x1) + (scalar * x2) == scalar(x1 + x2)
    assert (scalar * y1) + (scalar * y2) == scalar(y1 + y2)

test_if_scalar_transformation_is_linear()





