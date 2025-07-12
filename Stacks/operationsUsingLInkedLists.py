class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def __str__(self):
        values = [str(node.value) for node in self.LinkedList]
        return "\n".join(reversed(values))
    
    def isEmpty(self):
        return self.LinkedList.head == None
    
    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.LinkedList.head
        self.LinkedList.head = self.LinkedList.head.next
        return popped_node.value
    

customStack = Stack()
customStack.push(1)
customStack.push(3)
customStack.push(27)
customStack.push(13)
customStack.pop()
print(customStack.isEmpty())
print(customStack.LinkedList.head.value)
print(customStack)