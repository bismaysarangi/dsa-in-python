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


# Duplicate Number
# Write a function to remove the duplicate numbers on given integer array/list.

def remove_duplicates(arr):
    # TODO
    return list(set(arr))


# Pairs
# Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.

# Example

# pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
# Output : ['2+5', '4+3', '3+4', '-2+9']


# Note:

# 4+3 comes from second and third elements from the main list.

# 3+4 comes from third and seventh elements from the main list.

def pair_sum(arr, sum):
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == sum:
                result.append(f"{arr[i]}+{arr[j]}")
    return result


# Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example :

# Input: nums = [1,2,3,1]
# Output: true

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False