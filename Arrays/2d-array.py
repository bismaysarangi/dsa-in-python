import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)

new_arr = np.insert(arr, 0, [[10, 27, 36]], axis = 1)
print(new_arr)
arr_2 = np.append(arr, [[1, 5, 4]], axis = 0)
print(arr_2)

print(arr[0][2])

a = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 4, 7]])

def access_element(a, r, c):
    # if r >= len(a) or c >= len(a[0]):
    #     return "Wrong input"
    # else:
    #     return a[r][c]
    
    try:
        return a[r][c]
    except IndexError:
        return "Wrong input"

print(access_element(a, 2, 2))


def traverse(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            print(a[i][j], end = " ")

(traverse(a))



def searching(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] == 4:
                print(str(i) + " " + str(j))

(searching(a))

# Deletion 

new_a = np.delete(a, 0, axis = 1)
print(new_a)

# import array
# help(array.array)

