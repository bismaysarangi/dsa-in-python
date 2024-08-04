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
    
    
customStack = Stack()
print(customStack.isEmpty())