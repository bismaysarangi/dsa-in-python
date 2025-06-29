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