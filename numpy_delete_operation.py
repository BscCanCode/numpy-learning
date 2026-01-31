import numpy as np
# for 1d array
arr = np.array([7,9,7,0])

print("Og array: ", arr)

new_arr = np.delete(arr, 2, axis =None) #none passed means for 1d array
print("Deleted after: \n", new_arr)

# for 2d array

arr2 = np.array([[6,5,4],
                 [8,6,8]])

print("Og 2d matrix: \n", arr2)

new_arr2 = np.delete(arr2, 0, axis = 0) #row-wise deletion
print("Row-wise delete: \n", new_arr2)

new_arr3 = np.delete(arr2, 1, axis = 1) #column wise deletion
print("col-wise deletion: \n", new_arr3)