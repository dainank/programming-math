from vectors import scale, add
from teapot import load_triangles
from draw_model import draw_model

def polygon_map(transformation, polygons):
    return [
        [transformation(vertex) for vertex in triangle]
        for triangle in polygons
    ]

def scale2(v):  # multiply input vector by 2
    return scale(2.0, v)

def translate1left(v):
    return add((-1,0,0), v)

def compose(f1,f2): # chaining mulitple functions
    def new_function(input):
        return f1(f2(input))
    return new_function

# for producing snapshot
import sys
import camera
if '--snapshot' in sys.argv:
    camera.default_camera = camera.Camera('ex_translate_scale',[0])

draw_model(polygon_map(compose(scale2, translate1left), load_triangles()))