# Problem: Contains Duplicate II
def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    index_map = {}

    for i, num in enumerate(nums):
        if num in index_map and i - index_map[num] <= k:
            return True
        index_map[num] = i
    return False

# Problem: Minimum Absolute Difference
def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
    arr.sort()
    min_diff = float('inf')

    for i in range(1, len(arr)):
        min_diff = min(min_diff, arr[i] - arr[i - 1])
    
    result = []
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] == min_diff:
            result.append([arr[i - 1], arr[i]])

    return result

# Problem: Minimum Size Subarray Sum
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
        
    return min_length if min_length != float('inf') else 0

# Problem: Maximum Average Subarray 1
def findMaxAverage(self, nums: List[int], k: int) -> float:
    current_sum = sum(nums[:k])
    max_sum = current_sum

    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum / k
