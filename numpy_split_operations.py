import numpy as np

arr = np.array([1,2,3,2,1,2])

print("This is the array after split: ", np.split(arr, 2))

arr1 = np.array([[2,1,3],
                 [2,3,2],
                 [4,9,7]])

print("The vsplit is like this: ", np.vsplit(arr1, 3)) #vplit will go down
print("The hsplit is: ", np.hsplit(arr1, 3)) #hsplit will go sideways