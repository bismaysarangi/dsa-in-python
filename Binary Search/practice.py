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

# Problem: Search Insert Position
def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

# Problem: First Bad Version
def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        
        return left

# Problem: Valid Perfect Square
def isPerfectSquare(self, num: int) -> bool:
     low = 0
     high = num

     while low <= high:
          mid = (low + high) // 2
          square = mid * mid
          if square == num:
               return True
          elif square < num:
               low = mid + 1
          else:
               high = mid - 1
               
     return False

# Problem: Search in a 2D Matrix
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
     m = len(matrix)
     n = len(matrix[0])
     t = m * n
     l = 0
     r = t - 1

     while l <= r:
          mid = (l + r) // 2
          i = mid // n
          j = mid % n

          if matrix[i][j] == target:
                return True
          elif matrix[i][j] < target:
                l = mid + 1
          else:
                r = mid - 1

     return False

# Problem: Find Minimum in Rotated Sorted Array
def findMin(self, nums: List[int]) -> int:
     left = 0
     right = len(nums) - 1

     while left < right:
          mid = (left + right) // 2
          if nums[mid] > nums[right]:
               left = mid + 1
          else:
               right = mid
               
     return nums[left]