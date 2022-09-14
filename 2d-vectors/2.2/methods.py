def add(v1,v2): # adding vectors
   return (v1[0] + v2[0], v1[1] + v2[1])

# example impl.
vectors_gen = [(0, 0), (0, 1)]
dino_vectors2 = [add((-1.5,-2.5), v) for v in vectors_gen]

from math import sqrt
def length(v):
   return sqrt(v[0]**2 + v[1]**2)