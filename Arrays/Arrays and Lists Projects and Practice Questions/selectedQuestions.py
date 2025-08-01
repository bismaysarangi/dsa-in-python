# Problem: Contains Duplicate
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
