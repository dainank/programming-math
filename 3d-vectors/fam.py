# This file serves primarily as an area to experiment and gain familiarity with 3D matplotlib tools.

from draw3d import *  # 2

draw3d(
    Points3D((2, 2, 2), (1, -2, -2)),   # render points
    Segment3D((0, 0, 0), (2, 2, 2)),                 # render arrow from origin to vector
    Segment3D((0, 0, 0), (1, -2, -2)),
    Segment3D((2, 2, 2), (1, -2, -2))   # segment line between two points
)