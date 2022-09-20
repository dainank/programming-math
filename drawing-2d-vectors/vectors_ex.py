from vector_drawing import *

ex2_2 = [
    (2, -2), (0, 0), 
]

complete_dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4), 
   (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3), 
   (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)
]

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