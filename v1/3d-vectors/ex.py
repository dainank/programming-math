# all chapter 3 exercises here

from draw3d import *
from fam import *
from math import sin, cos, pi

# 3.1
draw3d(
    Points3D((-1, -2, 2)),
    Segment3D((0, 0, 0), (-1, -2, 2)),
    Box3D(-1, -2, 2)
)

# 3.2
range = [1, -1] # possible values for cube
ex3_2_vertices = [
    (x, y, z) for x in range for y in range for z in range  # the combinations
]

ex3_2_edges = [((-1,y,z),(1,y,z)) for y in range for z in range] +\
            [((x,-1,z),(x,1,z)) for x in range for z in range] +\
            [((x,y,-1),(x,y,1)) for x in range for y in range]

draw3d(
    Points3D(*ex3_2_vertices,color=blue),
    *[Segment3D(*edge) for edge in ex3_2_edges]
)

# 3.3
draw3d(
    Points3D((4, 0, 3),  (-1, 0, 1)),
    Segment3D((0, 0, 0), (4, 0, 3)),
    Segment3D((0, 0, 0), (-1, 0, 1)),
)
print(add((4, 0, 3),  (-1, 0, 1)))
# 3.4
# 3.5
vs = [(sin(pi*t/6), cos(pi*t/6), 1.0/3) for t in range(0,24)]

base = (0, 0, 0)
allPoints = []

for v in vs:
    current = add(base, v)
    allPoints.append(Segment3D((base), (current, next)))
    next = current

draw3d(*allPoints)
# 3.6
# 3.7