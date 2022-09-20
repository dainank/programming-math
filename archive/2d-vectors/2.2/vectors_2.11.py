from vector_drawing import *

def add(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def translate(translation, vectors):
   return [add(translation, v) for v in vectors]

dino_vectors = [(6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4), 
   (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3), 
   (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)
]

# make sure no overlaps (*12, *10)
translations = [(12*x,10*y) for x in range(-5,5) for y in range(-5,5)]

# create polygon with translation multiplier
dinos = [Polygon(*translate(t, dino_vectors),color=blue) for t in translations]

# draw the end result
draw(*dinos, grid=None, axes=None, origin=None, title="Exercise 2.11")