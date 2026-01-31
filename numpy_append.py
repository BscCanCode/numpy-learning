import numpy as np

array = np.array([12,34,23,12,34,67])

new_array = np.append(array, [23,54,23])

print("Og matrix: ", array)
print("Element appended matrix: ", new_array) #values will be appended at last