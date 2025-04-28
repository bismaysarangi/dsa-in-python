# Problem: Contains Duplicate
def containsDuplicate(self, nums: List[int]) -> bool:
        # Time Complexity: O(n) 
        # Space Complexity: O(n)
        seen = set(nums)
        if len(seen) == len(nums):
            return False
        return True

# Problem: Missing Number in Array
def missingNumber(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        n = len(nums)
        tot_sum = (n * (n + 1)) // 2
        s = sum(nums)
        return tot_sum - s

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
        # Time Complexity: O(n^2)
        # Space Complexity: O(n)
        sorted_nums = sorted(nums)
        smaller_arr = []
        for i in nums:
            smaller_arr.append(sorted_nums.index(i))
        return smaller_arr

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
