def quick_sort(nums):
    def partition(low, high):
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1
    
    def quick_sort_helper(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_helper(low, pi - 1)
            quick_sort_helper(pi + 1, high)
    
    quick_sort_helper(0, len(nums) - 1)
    return nums

print(quick_sort([38, 27, 43, 3, 9, 82, 10]))