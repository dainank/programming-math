# This file serves primarily as an area to experiment and gain familiarity with 3D matplotlib tools.

from draw3d import *  # 2
from math import sqrt

draw3d(
    Points3D((2, 2, 2), (1, -2, -2)),   # render points
    # render arrow from origin to vector
    Segment3D((0, 0, 0), (2, 2, 2)),
    Segment3D((0, 0, 0), (1, -2, -2)),
    # segment line between two points
    Segment3D((2, 2, 2), (1, -2, -2), color="red"),
    Box3D(2, 2, 2),
    Box3D(1, -2, -2)
)


def add(*vectors):  # sum of 3d vectors
    by_coordinate = zip(*vectors)   # sorting x/y/z coordinates
    coordinate_sums = [sum(coords)
                       for coords in by_coordinate]  # sums of x/y/z
    return tuple(coordinate_sums)   # the single summed vector

# subtraction/multiplication/division function the same

# finding length


def length(v):
    return sqrt(sum([coord ** 2 for coord in v]))
