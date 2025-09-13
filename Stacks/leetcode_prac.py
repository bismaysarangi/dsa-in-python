# Problem: Valid Parentheses
def isValid(self, s: str) -> bool:
    stack = []
    mapping = {")" : "(", "}" : "{", "]" : "["}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack and mapping[char] != stack.pop():
                return False
    
    return not stack

# Problem: Min Stack
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            current_min = val
        else:
            current_min = min(val, self.stack[-1][1])
        self.stack.append((val, current_min))
        
    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None

# Stack Sorting
def sortStack(stack):
    temp_stack = []

    while stack:
        num = stack.pop()

        while temp_stack and temp_stack[-1] < num:
            stack.append(temp_stack[-1])
            temp_stack.pop()
            
        temp_stack.append(num)

    return temp_stack

# Problem: Evaluate Reverse Polish Notation
def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                second, first = stack.pop(), stack.pop()
                stack.append(first - second)
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                second, first = stack.pop(), stack.pop()
                stack.append(int(first / second))
            else:
                stack.append(int(char))
        
        return stack[0]

# Problem: Remove Outer Parentheses
def removeOuterParentheses(self, s: str) -> str:
    stack = []
    res = ""

    for c in s:
        if c == "(":
            if stack:
                res += c
                stack.append(c)
            else:
                stack.append(c)
        else:
            if len(stack) == 1:
                stack.pop()
            else:
                res += c
                stack.pop()
    
    return res

# Problem: Valid Anagram
from collections import Counter
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    count_s, count_t = Counter(s), Counter(t)
    return count_s == count_t

# Problem: Rotate String
def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if goal in 2 * s:
            return True
        return False

# Problem: Isometric Strings
def isIsomorphic(s: str, t: str) -> bool:
    mapST, mapTS = {}, {}

    for charS, charT in zip(s, t):
        if charS in mapST and mapST[charS] != charT:
            return False
        if charT in mapTS and mapTS[charT] != charS:
            return False

        mapST[charS] = charT
        mapTS[charT] = charS

    return True

# Problem: Longest Common Prefix
def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""
    
    for i in range(len(strs[0])):
        char = strs[0][i]

        for word in strs[1:]:
            if i == len(word) or word[i] != char:
                return strs[0][:i]
    
    return strs[0]

# Problem: Largest Odd Number
def largestOddNumber(self, num: str) -> str:
        i = len(num) - 1
        while i >= 0 and int(num[i]) % 2 == 0:
            i -= 1
        
        return num[: i + 1]