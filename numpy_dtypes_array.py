import numpy as np

def show(arr, arr2, arr3):
    print("The data_types of array is: ", arr.dtype)
    print("The data_type of array is: ", arr2.dtype)
    print("The data_types of array is: ", arr3.dtype)

arr = np.array([1,2])
arr2 = np.array([[2,3],[4,6],[6,9.7]])
arr3 = np.array(([7.7, 8.8, 8, 9]))

show(arr, arr2, arr3)