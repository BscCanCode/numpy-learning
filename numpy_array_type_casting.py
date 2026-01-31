import numpy as np

array = np.array([[1.9, 2.9, 3.4],
                 [1.3, 5, 6.8]])

int_array = array.astype(int)

print("The original array: ", array)
print("The original array data type: ", array.dtype)
print("The converted array: ", int_array)
print("The converted array data type: ", int_array.dtype)
