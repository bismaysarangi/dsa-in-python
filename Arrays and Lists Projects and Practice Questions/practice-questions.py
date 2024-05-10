# Missing Number
# Write a function to find the missing number in a given integer array of 1 to 100. The function takes to parameter the array and the number of elements that needs to be in array.  For example if we want to find missing number from 1 to 6 the second parameter will be 6.

# Example

# missing_number([1, 2, 3, 4, 6], 6) # 5

def missing_number(arr, n):
    # TODO
    arr.sort()
    
    for i in range(1, n+1):
        if i not in arr:
            return i
    return None


# Max Product of Two Integers
# Find the maximum product of two integers in an array where all elements are positive.

# Example

# arr = [1, 7, 3, 4, 9, 5] 
# max_product(arr) # Output: 63 (9*7)

def max_product(arr):
    # TODO
    arr.sort()
    return arr[-1] * arr[-2]

# Middle Function
# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

# myList = [1, 2, 3, 4]
# middle(myList)  # [2,3]

def middle(arr):
    # TODO
    return arr[1:-1]

# 2D Lists
# Given 2D list calculate the sum of diagonal elements.

# Example

# myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
 
# diagonal_sum(myList2D) # 15

def diagonal_sum(matrix):
    # TODO
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                sum += matrix[i][j] 
    return sum

# Best Score
# Given a list, write a function to get first, second best scores from the list.

# List may contain duplicates.

# Example

# myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
# first_second(myList) # 90 87

def first_second(my_list):
    # TODO
    my_list.sort()
    return my_list[-1], my_list[-2]
