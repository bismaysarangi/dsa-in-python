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