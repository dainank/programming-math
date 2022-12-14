# Import a library of functions called 'pygame'
import numpy as np
import pygame
import vectors
from math import pi, sqrt, cos, sin, atan2
from random import randint, uniform
from linear_solver import do_segments_intersect
import sys

# DEFINE OBJECTS OF THE GAME


class PolygonModel():
    def __init__(self, points):
        self.points = points  # vector points
        self.rotation_angle = 0  # rotation of object
        self.x = 0  # x coordinate
        self.y = 0  # y coordinate
        self.vx = 0
        self.vy = 0
        self.angular_velocity = 0

    def transformed(self):  # ex 7.1
        rotated = [vectors.rotate2d(self.rotation_angle, v)
                   for v in self.points]
        return [vectors.add((self.x, self.y), v) for v in rotated]

    def move(self, milliseconds):
        dx, dy = self.vx * milliseconds / 1000.0, self.vy * milliseconds / 1000.0
        self.x, self.y = vectors.add((self.x, self.y), (dx, dy))
        self.rotation_angle += self.angular_velocity * milliseconds / 1000.0

    def segments(self):
        point_count = len(self.points)
        points = self.transformed()
        return [(points[i], points[(i+1) % point_count])
                for i in range(0, point_count)]

    def does_collide(self, other_poly):
        for other_segment in other_poly.segments():
            if self.does_intersect(other_segment):
                return True
        return False

    def does_intersect(self, other_segment):
        for segment in self.segments():
            if do_segments_intersect(other_segment, segment):
                return True
        return False


class Ship(PolygonModel):
    def __init__(self):
        # fixed definition for ship
        super().__init__([(0.5, 0), (-0.25, 0.25), (-0.25, -0.25)])

    def laser_segment(self):
        dist = 20. * sqrt(2) # draw till end of screen
        x, y = self.transformed()[0] # tip of ship
        return (x, y), (x + dist * cos(self.rotation_angle), y + dist*sin(self.rotation_angle)) # endpoint of laser


class Asteroid(PolygonModel):
    def __init__(self):
        sides = randint(5, 9)  # 5-9 vectors
        vs = [vectors.to_cartesian((uniform(0.5, 1.0), 2 * pi * i / sides))  # equally spaced angles and random lengths
              for i in range(0, sides)]
        super().__init__(vs)
        self.vx = 0  # uniform(-1,1)
        self.vy = 0  # uniform(-1,1)
        self.angular_velocity = uniform(-pi/2, pi/2)

# INITIALIZE GAME STATE


ship = Ship()

asteroid_count = 10
asteroids = [Asteroid() for _ in range(0, asteroid_count)] # array of astroids

for ast in asteroids: # set positions of astroids
    ast.x = randint(-9, 9)
    ast.y = randint(-9, 9)                      


# HELPERS / SETTINGS

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
BLUE = (0,   0, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)

width, height = 400, 400

# ex 7.2
def to_pixels(x, y): # translate object from centre of coordinate system to centre of PyGame screen
    return (width/2 + width * x / 20, height/2 - height * y / 20)


def draw_poly(screen, polygon_model, color=GREEN):  # receive transformed points convert them to pixels, then draw
    pixel_points = [to_pixels(x, y) for x, y in polygon_model.transformed()]
    pygame.draw.aalines(screen, color, True, pixel_points, 10)


def draw_segment(screen, v1, v2, color=RED):
    pygame.draw.aaline(screen, color, to_pixels(*v1), to_pixels(*v2), 10)


screenshot_mode = False

# INITIALIZE GAME ENGINE


def main():

    pygame.init()

    screen = pygame.display.set_mode([width, height])

    pygame.display.set_caption("Asteroids!")

    done = False
    clock = pygame.time.Clock()

    # p key prints screenshot (you can ignore this variable)
    p_pressed = False

    while not done:

        clock.tick()

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

        # UPDATE THE GAME STATE

        milliseconds = clock.get_time()
        keys = pygame.key.get_pressed() 

        for ast in asteroids:
            ast.move(milliseconds)

        if keys[pygame.K_LEFT]:
            ship.rotation_angle += milliseconds * (2*pi / 1000)

        if keys[pygame.K_RIGHT]:
            ship.rotation_angle -= milliseconds * (2*pi / 1000)

        laser = ship.laser_segment()

        # p key saves screenshot (you can ignore this)
        if keys[pygame.K_p] and screenshot_mode:
            p_pressed = True
        elif p_pressed:
            pygame.image.save(
                screen, 'figures/asteroid_screenshot_%d.png' % milliseconds)
            p_pressed = False

        # DRAW THE SCENE

        screen.fill(WHITE)

        if keys[pygame.K_SPACE]:
            draw_segment(screen, *laser)

        draw_poly(screen, ship)

        for asteroid in asteroids:
            if keys[pygame.K_SPACE] and asteroid.does_intersect(laser):
                asteroids.remove(asteroid)
            else:
                draw_poly(screen, asteroid, color=GREEN)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    if '--screenshot' in sys.argv:
        screenshot_mode = True
    main()

# 7.3

# 7.4
# v = (0, 0)
# No because v will always equal u.

# 7.5
# v = (-2, 6)
# (2, 2) + t * (-1 , 3)

# 7.9
# (2 * 0) + 7 = 7
# (2 * 3.5) + 0 = 7

# 7.10
# (3, 0) + t ?? (0, 1)

# 7.11
def standard_form(v1, v2):
   x1, y1 = v1
   x2, y2 = v2
   a = y2 - y1
   b = x1 - x2
   c = x1 * y2 - y1 * x2
   return a,b,c

# 7.12
def subtract(v1,v2):
    return tuple(v1-v2 for (v1,v2) in zip(v1,v2))

def length(v):
    return sqrt(sum([coord ** 2 for coord in v]))

def distance(v1,v2):
    return length(subtract(v1,v2))

def intersection(u1,u2,v1,v2):
    a1, b1, c1 = standard_form(u1,u2)
    a2, b2, c2 = standard_form(v1,v2)
    m = np.array(((a1,b1),(a2,b2)))
    c = np.array((c1,c2))
    return np.linalg.solve(m,c)

def segment_checks(s1,s2):
   u1,u2 = s1
   v1,v2 = s2
   l1, l2 = distance(*s1), distance(*s2)
   x,y = intersection(u1,u2,v1,v2)
   return [
       distance(u1, (x,y)) <= l1,
       distance(u2, (x,y)) <= l1,
       distance(v1, (x,y)) <= l2,
       distance(v2, (x,y)) <= l2
   ]

# 7.15
# w = (0, 0)