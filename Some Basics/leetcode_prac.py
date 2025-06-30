# Problem: Valid Palindrome
def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        new = ""
        for i in s:
            if 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57:
                new += i

        if new[::-1] == new:
            return True
        return False

# Find First and Last Position of Element in Sorted Array
def searchRange(self, nums: List[int], target: int) -> List[int]:
        indexes = []
        if target not in nums:
            return [-1, -1]

        for i in range(len(nums)):
            if nums[i] == target:
                indexes.append(i)
        
        return [indexes[0], indexes[-1]]