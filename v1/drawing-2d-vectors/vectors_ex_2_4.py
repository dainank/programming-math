from vector_drawing import *  # 2
from random import uniform  # 2
from math import sin, cos, asin, pi, acos, atan2  # 2.3

dino_vectors = [(6, 4), (3, 1), (1, 2), (-1, 5), (-2, 5), (-3, 4), (-4, 4),
                (-5, 3), (-5, 2), (-2, 2), (-5,
                                            1), (-4, 0), (-2, 1), (-1, 0), (0, -3),
                (-1, -4), (1, -4), (2, -3), (1, -2), (3, -1), (5, 1)
                ]


def length(v):
    return sqrt(v[0]**2 + v[1]**2)


def to_cartesian(polar_vector):  # convert polar to Cartesian coordinates
    length, angle = polar_vector[0], polar_vector[1]
    return (length*cos(angle), length*sin(angle))


def to_polar(vector):   # convert Cartesian to polar coordinates
    x, y = vector[0], vector[1]
    angle = atan2(y, x)
    return (length(vector), angle)


rotation_angle = pi/4
dino_polar = [to_polar(v) for v in dino_vectors]
dino_rotated_polar = [(l, angle + rotation_angle) for l, angle in dino_polar]
dino_rotated = [to_cartesian(p) for p in dino_rotated_polar]
draw(
    Polygon(*dino_vectors, color=gray),
    Polygon(*dino_rotated, color=red)
)


def rotate(angle, vectors):  # 2.42
    polars = [to_polar(v) for v in vectors]
    return [to_cartesian((l, a+angle)) for l, a in polars]


def add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])


def translate(translation, vectors):
    return [add(translation, v) for v in vectors]


new_dino = translate((8, 8), rotate(5 * pi/3, dino_vectors))  # more concise


def regular_polygon(n):  # 2.43
    return [to_cartesian((1, 2*pi*k/n)) for k in range(0, n)]
