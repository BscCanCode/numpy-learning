import numpy as np

array1 = np.array([1,2,3]).reshape(3,1)
array2 = np.array([3,3,6]).reshape(3,1)

# now we will concantenate both the arrays means will merge the two arrays

#concatenate vertically means here we give axis = 0

new_array1 = np.concatenate((array1, array2), axis = 0)

print("Concatenated_array: ", new_array1)

#concantenate horizonatlly means here we give axis = 1
print("Concanted horizontal")

new_array2 = np.concatenate((array1, array2), axis = 1)

print(new_array2)