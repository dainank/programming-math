from vector_drawing import *

ex2_2 = [
    (2, -2), (0, 0), 
]

draw(
    Points(*ex2_2, color=blue),
    Arrow(*ex2_2, color=black),
    grid=(1, 1),
    nice_aspect_ratio=False,
    title='Exercise 2.2'
)