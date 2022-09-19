from vector_drawing import *
from random import uniform

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

def add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def revised_add(vectors):
    sum_x = 0 # of x coordinates
    sum_y = 0 # of y coordinates
    for vector in vectors:
        sum_x += vector[0]
        sum_y += vector[1]
    return (sum_x, sum_y)

def scale(scalar,v):
   return (scalar * v[0], scalar * v[1])

print(revised_add(ex2_6))

def translate(translation, vectors):
   return [add(translation, v) for v in vectors]

def subtract(v1,v2):
   return (v1[0] - v2[0], v1[1] - v2[1])

def distance(v1,v2):
   return length(subtract(v1,v2))

def perimeter(vectors):
   distances = [distance(vectors[i], vectors[(i+1)%len(vectors)])
                for i in range(0,len(vectors))]
   return sum(distances)

for n in range(-12,15):
   for m in range(-14, 13):
       if distance((n,m), (1,-1)) == 13 and n > m > 0:
           print((n,m))

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

print(translate((1, 1), [
    (0, 0), (0, 1), (-3, -3) 
]))

draw(
    Points(*ex2_9, color=blue),
    Arrow(*ex2_9, color=black),
    grid=(1, 1),
    nice_aspect_ratio=False,
    title='Exercise 2.9'
)

draw(
    Points(*ex2_9_reversed, color=blue),
    Arrow(*ex2_9_reversed, color=black),
    grid=(1, 1),
    nice_aspect_ratio=False,
    title='Exercise 2.9 - Reversed'
)