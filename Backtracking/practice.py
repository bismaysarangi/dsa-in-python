from typing import List

# Problem: Subset
def subsets(self, nums):
    res = []
    curr_subset = []

    def dfs(i):
        if i >= len(nums):
            res.append(curr_subset.copy())
            return
        # Include nums[i]
        curr_subset.append(nums[i])
        dfs(i + 1)
        # Exclude nums[i]
        curr_subset.pop()
        dfs(i + 1)
    
    dfs(0)
    return res

# Problem: Permutations
def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans, sol = [], []

        def backtrack():
            if len(sol) == n:
                ans.append(sol.copy())
                return 
            
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()

        backtrack()
        return ans