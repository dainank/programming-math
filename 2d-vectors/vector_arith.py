from vector_drawing import *
from vectors import dino_vectors

def add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

dino_vectors2 = [add((-1.5, -2.5), v) for v in dino_vectors]

draw(
   Points(*dino_vectors, color=blue),
   Polygon(*dino_vectors, color=blue),
   Points(*dino_vectors2, color=red),
   Polygon(*dino_vectors2, color=red)
)

from math import sqrt
def length(v):  # theorem a**2  + b**2 = c**2
   return sqrt(v[0]**2 + v[1]**2)