from vectors import *

def compose(*args): # chaining multiple functions
    def new_function(input):
        result = input
        for f in reversed(args):
            result = f(result)
        return result
    return new_function

def curry2(f):
    def g(x):
        def new_function(y):
            return f(x,y)
        return new_function
    return g

def polygon_map(transformation, polygons):
    return [
        [transformation(vertex) for vertex in triangle]
        for triangle in polygons
    ]

def scale_by(scalar):
    def new_function(v):
        return scale(scalar, v)
    return new_function

def translate_by(translation):
    def new_function(v):
        return add(translation,v)
    return new_function

def rotate_z(angle, vector):
    x,y,z = vector
    new_x, new_y = rotate2d(angle, (x,y))
    return new_x, new_y, z

def rotate_z_by(angle):
    def new_function(v):
        return rotate_z(angle,v)
    return new_function

def rotate_x(angle, vector):
    x,y,z = vector
    new_y, new_z = rotate2d(angle, (y,z))
    return x, new_y, new_z

def rotate_x_by(angle):
    def new_function(v):
        return rotate_x(angle,v)
    return new_function

def rotate_y(angle,vector):
    x,y,z = vector
    new_x, new_z = rotate2d(angle, (x,z))
    return new_x, y, new_z

def rotate_y_by(angle):
    def new_function(v):
        return rotate_y(angle,v)
    return new_function

B = (
    (0,2,1),
    (0,1,0),
    (1,0,-1)
)

v = (1,-2,-2)

def transform_standard_basis(transform):
    return transform((1,0,0)), transform((0,1,0)), transform((0,0,1))
