from vectors import scale, add
from teapot import load_triangles
from draw_model import draw_model

def polygon_map(transformation, polygons):
    return [
        [transformation(vertex) for vertex in triangle]
        for triangle in polygons
    ]

def translate_by(translation):
    def new_function(v):
        return add(translation,v)
    return new_function

# for producing snapshot
import sys
import camera
if '--snapshot' in sys.argv:
    camera.default_camera = camera.Camera('ex_translate_teapot_down_z',[0])

draw_model(polygon_map(translate_by((0,0,-20)), load_triangles()))