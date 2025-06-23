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