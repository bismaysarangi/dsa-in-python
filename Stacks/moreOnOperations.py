class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return "\n".join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        return False
    
    def isFull(self):
        if len(self.list) >= self.maxSize:
            return True
        return False
    
    def push(self, value):
        if self.isFull():
            return "Stack is full"
        self.list.append(value)
        return self.list
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.list.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.list[-1]
    
    def delete(self):
        self.list = []
        return "Stack cleared"

customStack = Stack(5)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(3) 
customStack.push(27)
customStack.push(13)
print(customStack)