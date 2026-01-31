import numpy as np

def show(array1, array2, array3):
    print("The dimension of array is: ", array1.ndim)
    print("The dimension of array is: ", array2.ndim)
    print("The dimension of array is: ", array3.ndim)

array1 = np.array([1,2])
array2 = np.array([[3,4,6], [7,8,9]])
array3 = np.array([[[7,8],[9,8],[6,5],[3,6], [9,8]]])

show(array1, array2, array3)
