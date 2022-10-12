from vector_drawing import * #2
from random import uniform #2
from math import sin, cos, asin, pi, acos, atan2 #2.3
from vectors import *

vectors_414 = [(x, y) for x in range(0,6) for y in range(0,6)]
Sv = [(x**2, y**2) for x in range(0,6) for y in range(0,6)]

draw(
    Points(*vectors_414),
    grid=(1, 1),
    nice_aspect_ratio=False,
    window_title='Exercise 4.14'
)

draw(
    Points(*Sv),
    grid=(1, 1),
    nice_aspect_ratio=False,
    window_title='Exercise 4.14'
)
