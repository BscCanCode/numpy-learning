"""
goal is to
1. identify nan values
2. fill nan values
3. identify inf values 
4. fill inf values
"""

import numpy as np

arr = np.array([1,2,np.nan, 4, np.nan, 6])

print(np.isnan(arr))

#fill the nan values

arr1 = np.nan_to_num(arr, nan = 3)
print("Filled values: ", arr1)

#identify infinity values

arr3 = np.array([1,2,3,4,np.inf, 5, 6, -np.inf])
print("Identified: ", np.isinf(arr3))

print("Replaced infinity values with normal values")
arr4 = np.nan_to_num(arr3, posinf=200, neginf=-19) #filling the values with finite values
print(arr4)