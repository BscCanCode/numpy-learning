import numpy as np

array = np.array([[1,2,3],
                 [4,5,6]])

print(array)
print("row wise")
new_array = np.insert(array, 2, [4,4,4], axis=0) #inserting values row-wise

print(new_array)
print("col-wise")
new_array2d = np.insert(array, 2, [9,8], axis=1)
print(new_array2d)   #inserting values column wise 

print("1d array")
array1d = np.array([1,2,3,4,4])
print(array1d)
print()
new_array1d = np.insert(array1d, 1, 100, axis=None) #inserting values in flatten array
print(new_array1d)