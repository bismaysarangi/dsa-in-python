class Stack:
    # List Creation
    def __init__(self):
        self.list = []

    # Linked List Creation
    # def __str__(self):
    #     values = self.list.reverse()
    #     values = [str(x) for x in self.list]
    #     return "\n".join(values)
    
    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return "\n".join(values)