# Problem: Contains Duplicate
from typing import List


def containsDuplicate(self, nums: List[int]) -> bool:
        # Time Complexity: O(n) 
        # Space Complexity: O(n)
        return True if len(nums) != len(set(nums)) else False

# Problem: Missing Number in Array
def missingNumber(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        n = len(nums)
        tot_sum = (n * (n + 1)) // 2
        s = sum(nums)
        return tot_sum - s

# Problem: Find closest number to zero
def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]

        for num in nums:
            if abs(num) < abs(closest):
                closest = num
            elif abs(num) == abs(closest):
                closest = max(num, closest)

        return closest 

# Problem: Merge Strings Alternately
def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        word = []

        for i in range(max(n1, n2)):
            if i < n1:
                word.append(word1[i])
            if i < n2:
                word.append(word2[i])
        
        return "".join(word)

# Problem: Find all missing numbers
def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        n = len(nums)
        full_set = set(range(1, n+1))
        nums_set = set(nums)
        return list(full_set - nums_set)

# Problem: Two Sum, Approach: Brute Force
def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Problem: Two Sum, Approach: Hash Map
def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        hash_map = {}
        for i, val in enumerate(nums):
            if target - val in hash_map:
                return i, hash_map[target - val]
            else:
                hash_map[val] = i

# Problem: How many numbers are smaller than the current number, Approach: My Own
def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Time Complexity: O(n log n)
        # Space Complexity: O(n)
        sorted_nums = sorted(nums)
        arr = []

        for i in nums:
            arr.append(sorted_nums.index(i))
        
        return arr

# Problem: How many numbers are smaller than the current number, Approach: Hash Map
def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Time Complexity: O(n log n)
        # Space Complexity: O(n)
        temp = sorted(nums)
        hash_map = {}
        for i, num in enumerate(temp):
            if num not in hash_map:
                hash_map[num] = i
        
        final_arr = []
        for i in nums:
            final_arr.append(hash_map[i])
        return final_arr

# Problem: Minimum time Visiting all points
def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        res = 0
        for i in range(1, len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]

            res += max(abs(x1 - x2), abs(y1 - y2))

        return res

# Problem: Find Numbers with Even Number of Digits
def findNumbers(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        count = 0
        for i in nums:
            str_i = str(i)
            if len(str_i) % 2 == 0:
                count += 1
                
        return count

# Problem: Spiral Matrix
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                  for row in matrix:
                        res.append(row.pop())
            if matrix:
                  res += matrix.pop()[::-1]
            if matrix and matrix[0]:
                  for row in matrix[::-1]:
                        res.append(row.pop(0))
        return res

#Problem: Square of a Sorted Array
def sortedSquares(self, nums: List[int]) -> List[int]:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        return sorted([i ** 2 for i in nums])
# Problem: Three Sum
def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    temp = nums[i] + nums[j] + nums[k]
                    if temp == 0:
                        res.add((nums[i],nums[j],nums[k]))
        return list(res)
# Problem: Best Time to Buy and Sell Stock
def maxProfit(self, prices: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit

# Problem: Find Peak Element
def findPeakElement(self, nums: List[int]) -> int:
        max_element = float('-inf')
        for i in range(len(nums)):
            if nums[i] > max_element:
                max_element = nums[i]
                max_index = i
        
        return max_index

def findPeakElement(self, nums: List[int]) -> int:
        return nums.index(max(nums))

# Problem: Median of two sorted arrays
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        n = len(nums)

        if n % 2 != 0:
            return float(nums[n // 2]) 
        else:
            return (nums[n // 2 - 1] + nums[n // 2]) / 2
        
# Problem: Longest Mountain in an Array
def longestMountain(self, arr: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        res = 0
        n = len(arr)

        for i in range(1, n - 1):
            if arr[i - 1] < arr[i] > arr[i + 1]:
                l = i - 1
                r = i + 1

                while l > 0 and arr[l] > arr[l - 1]:
                    l -= 1

                while r < n - 1 and arr[r] > arr[r + 1]:
                    r += 1
                    i = r

                res = max(res, r - l + 1)

        return res

# Problem: Rotate Image
def rotate(self, matrix: List[List[int]]) -> None:
     matrix.reverse()
     n = len(matrix)

     for i in range(n):
          for j in range(i, n):
               matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Problem: Merge two sorted arrays
def merge(self, nums1: List[int], nums2: List[int]) -> None:
     nums = nums1 + nums2
     nums.sort()
     return nums

# Problem: Finding 2nd largest element in an array without sorting
def findSecondLargest(self, arr: List[int]) -> int:
    nums = list(set(arr))
    if len(nums) <= 1:
        return -1
            
    max_element = max(nums)
        
    max_index = nums.index(max_element)
    nums.pop(max_index)
        
    new_max = max(nums)

    return new_max

# Problem: Check if the array is sorted or not even if it is rotated
def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
            if count > 1:
                return False
        
        return True

# Problem: Remove duplicates from sorted array
def removeDuplicates(self, nums: List[int]) -> int:
        s = set(nums)
        nums.clear()

        for i in s:
            nums.append(i)
        
        nums.sort()
        return nums

# Problem: Left Rotate Array by one
def rotateArrayByOne(self, nums):
        nums[:] = nums[1:] + nums[:1]

# Problem: Rotate Array by k elements
def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            nums.insert(0, nums.pop())


# Problem: Move Zeroes
def moveZeroes(self, nums: List[int]) -> None:
     for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(i)

# Problem: Union of two arrays
def unionArray(self, nums1, nums2):
        union = set(nums1) | set(nums2)
        return list(union)

# Problem: Find Maximum consecutive 1's
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_one, count = 0, 0

        for num in nums:
            if num == 1:
                count += 1
                max_one = max(max_one, count)
            else:
                count = 0
        
        return max_one

# Problem: Subarray Sum Equals K
from collections import defaultdict
def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        freq = defaultdict(int)
        freq[0] = 1

        for num in nums:
            prefix_sum += num
            if (prefix_sum - k) in freq:
                count += freq[prefix_sum - k]
            freq[prefix_sum] += 1
        
        return count

# Problem: Majority Element
def majorityElement(self, nums: List[int]) -> int:
     count = 0
     candidate = None

     for num in nums:
          if count == 0:
               candidate = num
     if num == candidate:
            count += 1
     else:
            count -= 1
     
     return candidate

# Problem: Maximum Subarray
def maxSubArray(self, nums: List[int]) -> int:
     maximum = nums[0]
     current_sum = 0

     for num in nums:
          current_sum += num
          maximum = max(current_sum, maximum)

          if current_sum < 0:
                current_sum = 0
    
     return maximum

# Problem: Rearrange Array Alternately
def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        alternate = []

        for num in nums:
            if num >= 0:
                positive.append(num)
            else:
                negative.append(num)

        for pos, neg in zip(positive, negative):
            alternate.append(pos)
            alternate.append(neg)
        
        return alternate
    
# Problem: Leaders in an Array
def leaders(self, nums: List[int]) -> List[int]:
    n = len(nums)
    leaders = []
    max_right = nums[-1]
    leaders.append(max_right)

    for i in range(n - 2, -1, -1):
        if nums[i] >= max_right:
            max_right = nums[i]
            leaders.append(max_right)

    return leaders[::-1]

# Problem: Rotate by 90 degree
def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(len(matrix)):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for row in matrix:
            row.reverse()
