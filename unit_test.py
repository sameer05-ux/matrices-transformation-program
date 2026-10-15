import numpy
import random
import matrix_transformations as matrix

def test_multiplication():
    for i in range(10000):
        rows = random.randint(1,6)
        columns = random.randint(1,6)
        matrix_1 = matrix.Matrix([[random.randint(-10,10) for i in range(columns)] for n in range(rows)])
        
        rows = random.randint(1,6)
        matrix_2 = matrix.Matrix([[random.randint(-10,10) for i in range(rows)] for n in range(columns)])

        m1 = numpy.array(matrix_1.rows)
        m2 = numpy.array(matrix_2.rows)

        assert numpy.all(m1@m2 == numpy.array(matrix_1.multiply(matrix_2).rows))

test_multiplication()
