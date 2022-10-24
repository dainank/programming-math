import matplotlib.pyplot as plt
from math import sqrt
from abc import ABCMeta, abstractmethod, abstractproperty
from datetime import datetime
from math import sqrt, sin, cos, acos, atan2, isclose
from datetime import datetime, timedelta
from random import uniform, random, randint


def add(*vectors):
    return tuple(map(sum, zip(*vectors)))


def subtract(v1, v2):
    return tuple(v1-v2 for (v1, v2) in zip(v1, v2))


def length(v):
    return sqrt(sum([coord ** 2 for coord in v]))


def dot(u, v):
    return sum([coord1 * coord2 for coord1, coord2 in zip(u, v)])


def distance(v1, v2):
    return length(subtract(v1, v2))


def perimeter(vectors):
    distances = [distance(vectors[i], vectors[(i+1) % len(vectors)])
                 for i in range(0, len(vectors))]
    return sum(distances)


def scale(scalar, v):
    return tuple(scalar * coord for coord in v)


def to_cartesian(polar_vector):
    length, angle = polar_vector[0], polar_vector[1]
    return (length*cos(angle), length*sin(angle))


def rotate2d(angle, vector):
    l, a = to_polar(vector)
    return to_cartesian((l, a+angle))


def translate(translation, vectors):
    return [add(translation, v) for v in vectors]


def to_polar(vector):
    x, y = vector[0], vector[1]
    angle = atan2(y, x)
    return (length(vector), angle)


def angle_between(v1, v2):
    return acos(
        dot(v1, v2) /
        (length(v1) * length(v2))
    )


def cross(u, v):
    ux, uy, uz = u
    vx, vy, vz = v
    return (uy*vz - uz*vy, uz*vx - ux*vz, ux*vy - uy*vx)


def component(v, direction):
    return (dot(v, direction) / length(direction))


def unit(v):
    return scale(1./length(v), v)


def linear_combination(scalars, *vectors):
    scaled = [scale(s, v) for s, v in zip(scalars, vectors)]
    return add(*scaled)

# exercises


def test(eq, a, b, u, v, w):
    assert eq(u + v, v + u)
    assert eq(u + (v + w), (u + v) + w)
    assert eq(a * (b * v), (a * b) * v)
    assert eq(1 * v, v)
    assert eq((a + b) * v, a * v + b * v)
    assert eq(a * v + a * w, a * (v + w))


def test(zero, eq, a, b, u, v, w):
    assert eq(zero + v, v)
    assert eq(0 * v, zero)
    assert eq(-v + v, zero)


def random_scalar():
    return uniform(-10, 10)


# 6.8
for i in range(0, 100):
    a, b = random_scalar(), random_scalar()
    u, v, w = random_scalar(), random_scalar(), random_scalar()
    # check if two floating numbers close (0 is 0 vector)
    test(0, isclose, a, b, u, v, w)

# 6.9


class Vector(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def zero():
        pass

    def __neg__(self):
        return self.scale(-1)

    @abstractmethod
    def scale(self, scalar):
        pass

    @abstractmethod
    def add(self, other):
        pass

    def subtract(self, other):
        return self.add(-1 * other)

    def __sub__(self, other):
        return self.subtract(other)

    def __mul__(self, scalar):
        return self.scale(scalar)

    def __rmul__(self, scalar):
        return self.scale(scalar)

    def __add__(self, other):
        return self.add(other)

    def __truediv__(self, scalar):
        return self.scale(1.0/scalar)


class CarForSale(Vector):
    retrieved_date = datetime(2018, 11, 30, 12)

    def __init__(self, model_year, mileage, price, posted_datetime,
                 model="(virtual)",
                 source="(virtual)",
                 location="(virtual)", description="(virtual)"):
        self.model_year = model_year
        self.mileage = mileage
        self.price = price
        self.posted_datetime = posted_datetime
        self.model = model
        self.source = source
        self.location = location
        self.description = description

    def add(self, other):
        def add_dates(d1, d2):
            age1 = CarForSale.retrieved_date - d1
            age2 = CarForSale.retrieved_date - d2
            sum_age = age1 + age2
            return CarForSale.retrieved_date - sum_age
        return CarForSale(
            self.model_year + other.model_year,
            self.mileage + other.mileage,
            self.price + other.price,
            add_dates(self.posted_datetime, other.posted_datetime)
        )

    def scale(self, scalar):
        def scale_date(d):
            age = CarForSale.retrieved_date - d
            return CarForSale.retrieved_date - (scalar * age)
        return CarForSale(
            scalar * self.model_year,
            scalar * self.mileage,
            scalar * self.price,
            scale_date(self.posted_datetime)
        )

    @classmethod
    def zero(cls):
        return CarForSale(0, 0, 0, CarForSale.retrieved_date)


def random_time():
    return CarForSale.retrieved_date - timedelta(days=uniform(0, 10))


def approx_equal_time(t1, t2):
    test = datetime.now()
    return isclose((test-t1).total_seconds(), (test-t2).total_seconds())


def random_car():
    return CarForSale(randint(1990, 2019), randint(0, 250000),
                      27000. * random(), random_time())


# They pass
def approx_equal_car(c1, c2):
    return (isclose(c1.model_year, c2.model_year)
            and isclose(c1.mileage, c2.mileage)
            and isclose(c1.price, c2.price)
            and approx_equal_time(c1.posted_datetime, c2.posted_datetime))


# They pass
for i in range(0, 100):
    a, b = random_scalar(), random_scalar()
    u, v, w = random_car(), random_car(), random_car()
    test(CarForSale.zero(), approx_equal_car, a, b, u, v, w)


# 6.10
class Function(Vector):
    def __init__(self, f):
        self.function = f

    def add(self, other):
        return Function(lambda x: self.function(x) + other.function(x))

    def scale(self, scalar):
        return Function(lambda x: scalar * self.function(x))

    @classmethod
    def zero(cls):
        return Function(lambda x: 0)

    def __call__(self, arg):
        return self.function(arg)


f = Function(lambda x: 0.5 * x + 3)
g = Function(sin)

plt.plot([f, g, f+g, 3*g], -10, 10)


# 6.11
def approx_equal_function(f1, f2):
    results = []
    for _ in range(0, 10):
        x = uniform(-10, 10)
        results.append(isclose(f(x), f2(x)))
    return all(results)

# only works for functions that spit out the same results

# 6.12


def random_function():
    degree = randint(0, 5)
    p = Vector(*[uniform(-10, 10) for _ in range(0, degree)])
    return Function(lambda x: p(x))


for i in range(0, 100):
    a, b = random_scalar(), random_scalar()
    u, v, w = random_function(), random_function(), random_function()
    test(Function.zero(), approx_equal_function, a, b, u, v, w)

# 6.13


class Function(Vector):
    def __init__(self, f):
        self.function = f

    def add(self, other):
        return Function(lambda x, y: self.function(x, y) + other.function(x, y))

    def scale(self, scalar):
        return Function(lambda x, y: scalar * self.function(x, y))

    @classmethod
    def zero(cls):
        return Function(lambda x, y: 0)

    def __call__(self, *args):
        return self.function(*args)

# 6.14
    # 4 is correct, 9x9 = 81.

# 6.15


class Matrix(Vector):
    @abstractproperty
    def rows(self):
        pass

    @abstractproperty
    def columns(self):
        pass

    def __init__(self, entries):
        self.entries = entries

    def add(self, other):
        return self.__class__(
            tuple(
                tuple(self.entries[i][j] + other.entries[i][j]
                      for j in range(0, self.columns()))
                for i in range(0, self.rows())))

    def scale(self, scalar):
        return self.__class__(
            tuple(
                tuple(scalar * e for e in row)
                for row in self.entries))

    def __repr__(self):
        return "%s%r" % (self.__class__.__qualname__, self.entries)

    def zero(self):
        return self.__class__(
            tuple(
                tuple(0 for i in range(0, self.columns()))
                for j in range(0, self.rows())))


class Matrix3x2(Matrix):
    def rows(self):
        return 3

    def columns(self):
        return 3

# 6.16


def random_matrix(rows, columns):
    return tuple(
        tuple(uniform(-10, 10) for j in range(0, columns))
        for i in range(0, rows)
    )


def random_3_by_2():
    return Matrix3x2(random_matrix(3, 2))


def approx_equal_matrix_3_by_2(m1, m2):
    return all([
        isclose(m1.matrix[i][j], m2.matrix[i][j])
        for j in range(0, 2)
        for i in range(0, 3)
    ])


for i in range(0, 100):
    a, b = random_scalar(), random_scalar()
    u, v, w = random_3_by_2(), random_3_by_2(), random_3_by_2()
    test(Matrix3x2.zero(), approx_equal_matrix_3_by_2, a, b, u, v, w)

# 6.17


class LinearMap3d_to_5d(Vector):
    def __call__(self, arg):
        return self.function(arg)

def random_image():
   return ImageVector([(randint(0,255), randint(0,255), randint(0,255))
                           for i in range(0,300 * 300)])