# Problem: Second largest in an array
def getSecondLargest(self, arr):
        # Code Here
        if len(set(arr)) <= 1:
            return -1
        
        largest = 0
        for num in arr:
            if num >= largest:
                largest = num
        
        second_largest = 0
        for num in arr:
            if num >= second_largest and num != largest:
                second_largest = num
        
        return second_largest

# Problem: Check if array is sorted and rotated
def checkRotatedAndSorted(self, arr, n):
        # code here
        count = 0
        for i in range(n):
            if arr[i] > arr[(i + 1) % n]:
                count += 1
            if count > 1:
                return False
        return True

# Problem: Rotate array by k times
def rotateArr(self, arr, k):
     for i in range(k):
          arr.insert(0, arr.pop())
     return arr 

# Move Zeroes to end of array
def moveZeroes(self, arr, n):
    for i in range(n):
        if arr[i] == 0:
            arr.append(arr.pop(i))
    return arr

# Problem: Remove Duplicates from sorted array
def removeDuplicates(self, arr, n):
        # code here
        s = set(arr)
        arr.clear()
        for i in s:
            arr.append(i)       

        arr.sort()
        return arr 

