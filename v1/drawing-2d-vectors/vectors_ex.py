from vector_drawing import * #2
from random import uniform #2
from math import sin, cos, asin, pi, acos, atan2 #2.3

# All methods on utilized by drawings are present in the archive directory files
def add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def scale(scalar,v):
   return (scalar * v[0], scalar * v[1])

def translate(translation, vectors):
   return [add(translation, v) for v in vectors]

def length(v):
    return sqrt(v[0]**2 + v[1]**2)

ex2_2 = [
    (2, -2), (0, 0), 
]

ex2_6 = [
    (-2, 0), (1.5, 1.5), (4, 1) 
]

ex2_9 = [
    (1, 1), (2, 2)
]

ex2_9_reversed = [
    (2, 2), (1, 1)
]

ex2_15 = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4), 
   (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3), 
   (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)
]

complete_dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4), 
   (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3), 
   (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)
]

dino_vectors2 = [add((-1.5, -2.5), v) for v in complete_dino_vectors]

draw(
    Points(*ex2_2, color=blue),
    Arrow(*ex2_2, color=black),
    grid=(1, 1),
    nice_aspect_ratio=False,
    window_title='Exercise 2.2'
)

draw(
    Points(*complete_dino_vectors, color=purple),
    Polygon(*complete_dino_vectors, color=black),
    grid=(1, 1),
    nice_aspect_ratio=False,
    window_title='Exercise 2.3 & 2.4'
)

draw(
    Points(*[(x, x**2) for x in range(-10, 11)]),
    grid=(1, 10),
    nice_aspect_ratio=False,
    window_title='Exercise 2.5'
)

draw(
    Points(*ex2_9, color=blue),
    Arrow(*ex2_9, color=black),
    grid=(1, 1),
    nice_aspect_ratio=False,
    window_title='Exercise 2.9'
)

draw(
    Points(*ex2_9_reversed, color=blue),
    Arrow(*ex2_9_reversed, color=black),
    grid=(1, 1),
    nice_aspect_ratio=False,
    window_title='Exercise 2.9 - Reversed'
)

u = (-1,1)
v = (1,1)
def random_r():
   return uniform(-3,3)
def random_s(): 
   return uniform(-1,1)
possibilities = [add(scale(random_r(), u), scale(random_s(), v))
                for i in range(0,500)]
draw(
   Points(*possibilities)
)

draw(
   Points(*complete_dino_vectors, color=blue),
   Polygon(*complete_dino_vectors, color=blue),
   Points(*dino_vectors2, color=red),
   Polygon(*dino_vectors2, color=red)
)

# make sure no overlaps (*12, *10)
translations = [(12*x,10*y) for x in range(-5,5) for y in range(-5,5)]

# create polygon with translation multiplier
dinos = [Polygon(*translate(t, complete_dino_vectors),color=blue) for t in translations]

# draw the end result
draw(*dinos, grid=None, axes=None, origin=None, window_title="Exercise 2.11")

# 2.3 ------------
def to_cartesian(polar_vector): # convert polar to Cartesian coordinates
   length, angle = polar_vector[0], polar_vector[1]
   return (length*cos(angle), length*sin(angle))

def to_polar(vector):   # convert Cartesian to polar coordinates
   x, y = vector[0], vector[1]
   angle = atan2(y,x)
   return (length(vector), angle)

print('Exercise 2.27: ')
print(length((-1.34, 2.68)))

print('Exercise 2.28: ')
print('4 / 10 = 0.4')

print('Exercise 2.29: ')
print(to_cartesian((15, 37)))

print('Exercise 2.30: ')
print(f"({8.5 * cos(2.18166)}, {8.5 * sin(2.18166)})")  # in radians

polar_coords = [(cos(x*pi/100.0), 2*pi*x/1000.0) for x in range(0,1000)]
polar_vectors = [to_cartesian(p) for p in polar_coords]
draw(Polygon(*polar_vectors, color=green))

print('Exercise 2.40: ')
print(f"({to_cartesian((1, 1))}, {to_cartesian((1, -1))})")  # in radians