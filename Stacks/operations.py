class Stack:
    # List Creation
    def __init__(self):
        self.list = []
    
    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return "\n".join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        return False
    
    def push(self, value):
        self.list.append(value)
        return list
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.list.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.list[-1]
    
customStack = Stack()
# print(customStack.isEmpty())
customStack.push(1)
customStack.push(3)
customStack.push(27)
customStack.push(13)
customStack.pop()
print(customStack)
print(customStack.peek())