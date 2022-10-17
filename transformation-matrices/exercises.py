from transforms import compose
from random import randint


def infer_matrix(dimension, transformation):
    def standard_basis_vector(i):
        return tuple(True if i == j else False for j in range(1, dimension + 1))
    standard_basis = [standard_basis_vector(
        i) for i in range(1, dimension + 1)]
    cols = [transformation(v) for v in standard_basis]
    return tuple(zip(*cols))


def random_matrix(rows, cols, min=-2, max=2):
    return tuple(
        tuple(
            randint(min, max) for j in range(0, cols))
        for i in range(0, rows)
    )


def multiply_matrix_vector(matrix, vector):
    return tuple(
        sum(vector_entry * matrix_entry
            for vector_entry, matrix_entry in zip(row, vector))
        for row in matrix
    )


def multiply_matrix_vector(matrix, vector):
    return tuple(
        dot(row, vector)
        for row in matrix
    )


a = ((1, 1, 0), (1, 0, 1), (1, -1, 1))
b = ((0, 2, 1), (0, 1, 0), (1, 0, -1))


def transform_a(v):
    return multiply_matrix_vector(a, v)


def transform_b(v):
    return multiply_matrix_vector(b, v)


compose_a_b = compose(transform_a, transform_b)


def matrix_power(power, matrix):
    result = matrix
    for _ in range(1, power):
        result = matrix_multiply(result, matrix)
    return result
