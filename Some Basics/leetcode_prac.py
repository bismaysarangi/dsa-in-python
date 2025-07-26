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

# Problem: Possible String count
def possibleStringCount(self, word: str) -> int:
        n = len(word)
        count = n
        for i in range(1, n):
            if word[i] != word[i - 1]:
                count -= 1
        
        return count

def isValid(self, s: str) -> bool:
        if len(s) < 3:
            return False

        vowels = 0
        consonants = 0
        vowel_set = "aeiouAEIOU"

        for c in s:
            if c.isalpha():
                if c in vowel_set:
                    vowels += 1
                else:
                    consonants += 1
            elif not c.isdigit():
                return False  

        return vowels >= 1 and consonants >= 1

# Problem: Jewels and Stones
def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewels = set(jewels)

        for jewel in stones:
            if jewel in jewels:
                count += 1
        
        return count