# Works only for sorted arrays

def binarySearch(array, value):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if array[mid] == value:
            return mid
        elif array[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return -1

