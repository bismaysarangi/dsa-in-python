import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)

new_arr = np.insert(arr, 0, [[10, 27, 36]], axis = 1)
print(new_arr)
arr_2 = np.append(arr, [[1, 5, 4]], axis = 0)
print(arr_2)