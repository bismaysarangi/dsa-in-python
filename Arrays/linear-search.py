import numpy as np

# arr = np.array([1, 2, 3, 4, 5], dtype=int)

arr = np.array([1, 2, 3])

def linear_search(arr):
    for i in arr:
        if i == 3:
            print(i)

linear_search(arr)