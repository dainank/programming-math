from vectors import scale, add
from teapot import load_triangles
from draw_model import draw_model

def scale2(v):
    return scale(2.0, v)

def translate1left(v):
    return add((-1,0,0), v)

original_triangles = load_triangles()   # load our triangles to make the 3d shape

scaled_translated_triangles = [
    [translate1left(scale2(vertex)) for vertex in triangle] # double all the vertices
    for triangle in original_triangles
]

# for producing snapshot
import sys
import camera
if '--snapshot' in sys.argv:
    camera.default_camera = camera.Camera('fig4.6_scale_translate',[0])

draw_model(scaled_translated_triangles)