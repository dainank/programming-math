from vector_drawing import *

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

print(revised_add(ex2_6))

def translate(translation, vectors):
   return [add(translation, v) for v in vectors]

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