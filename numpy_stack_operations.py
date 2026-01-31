import numpy as np

arr = np.array([8,9,7])
arr2 = np.array([8,5,3])

print("vstack: \n", np.vstack((arr, arr2))) #vertically stack, more rows are added
print("hstack: \n", np.hstack((arr, arr2))) #horizontal stack, more col are added
