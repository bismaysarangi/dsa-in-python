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