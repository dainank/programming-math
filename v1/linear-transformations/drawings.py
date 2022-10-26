from vector_drawing import * #2
from random import uniform #2
from math import sin, cos, asin, pi, acos, atan2 #2.3
from vectors import *

vectors_414 = [(x, y) for x in range(0,6) for y in range(0,6)]
Sv = [(x**2, y**2) for x in range(0,6) for y in range(0,6)]

vectors_416 = [
    (3, 2), (0, 0), (3, -2), (0, 0)
]

vectors_416b = [
    (3, -2), (0, 0), 
]
draw(
    Points(*vectors_416, color=blue),
    Arrow(*[(3, 2), (0, 0)], color=black),
    Arrow(*[(3, -2), (0, 0)], color=black),
    Segment(*[(3, -2), (3, 2)], color=purple),
    grid=(1, 1),
    nice_aspect_ratio=False,
    window_title='Exercise 4.16'
)

draw(
    Points(*(vectors_416 * 2), color=blue),
    Arrow(*[(6, 4), (0, 0)], color=black),
    Arrow(*[(6, -4), (0, 0)], color=black),
    Segment(*[(6, 4), (6, -4)], color=purple),
    grid=(1, 1),
    nice_aspect_ratio=False,
    window_title='Exercise 4.16'
)

draw(
    Points(*vectors_414),
    grid=(1, 1),
    nice_aspect_ratio=False,
    window_title='Exercise 4.14'
)

draw(
    Points(*vectors_414),
    grid=(1, 1),
    nice_aspect_ratio=False,
    window_title='Exercise 4.14'
)

def linear_combination(scalars, *vectors):
   scaled = [scale(s, v) for s, v in zip(scalars, vectors)]
   return add(*scaled)

def transform_standard_basis(transform):
   return transform((1,0,0)), transform((0,1,0)), transform((0,0,1))