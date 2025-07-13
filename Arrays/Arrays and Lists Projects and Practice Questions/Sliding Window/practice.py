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

    for i in rannge(1, len(arr)):
        min_diff = min(min_diff, arr[i] - arr[i - 1])
    
    result = []
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] == min_diff:
            result.append([arr[i - 1], arr[i]])
    return result