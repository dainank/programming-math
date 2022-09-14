from vector_drawing import *

ex2_2 = [
    (0, 0), (2, -2)
]

draw(
    Points(*[(x, x**2) for x in range(-10, 11)]),
    grid=(1, 10),
    nice_aspect_ratio=False
)