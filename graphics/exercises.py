from math import sqrt, sin, cos, acos, atan2
from cube_teapot import polygon_map
from exercises import translate_by
from teapot import load_triangles
from draw_model import draw_model

def add(*vectors):
    return tuple(map(sum,zip(*vectors)))

### Exercise 4.1
def translate_by(translation):  # function takes in single variable
    def new_function(v):    # new function takes in single variable, it will always have translation + new input
        return add(translation, v)
    return new_function

# for example
translate_by_111 = translate_by((1, 1, 1))
print(translate_by_111((2, 3, 2)))  # works as intended see console

### Exercise 4.2
draw_model(polygon_map(translate_by((0,0,-20)), load_triangles()))  # draw, polygon, with triangles (coordinates) and translate