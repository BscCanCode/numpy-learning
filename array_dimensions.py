import numpy as np

def show_array(one_dimension, two_dimension, matrix):
    print(f"One_dimension_array: {one_dimension}")
    print(f"Two_dimension_array: {two_dimension}")
    print(f"A matrix: {matrix}")

one_dimension = np.array([1,2,3])

two_dimension = np.array([[3,4,5],
                         [6,7,8],
                         [9,10,11]])

matrix = np.array([[1,2,4],
                  [4,5,6],
                  [7,8,9]])

show_array(one_dimension, two_dimension, matrix)
