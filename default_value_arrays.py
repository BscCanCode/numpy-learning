import numpy as np

def show_array(array_zeros, array_ones, array_fill):
    print("Default_values_zeros: ", array_zeros)
    print("Default values_one: ", array_ones)
    print("Default_values_eight: ", array_fill)

array_zeros = np.zeros((3,3))

array_ones = np.ones((3,3))

array_fill = np.full((3,3), 8)

show_array(array_zeros, array_ones, array_fill)
