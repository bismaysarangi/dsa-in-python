class Node:
    def __init__(self, value = None):
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

# Class Node
# class Node: - This line defines a new class named Node. A Node is a fundamental building block of a linked list, typically holding a value and a reference to the next node in the list.

# def __init__(self, value = None): - This is the constructor method for the Node class. It initializes a new instance of the Node class. The parameter value is optional and defaults to None if not provided.

# self.value = value - This line sets the value attribute of the Node instance. The value stored in the node can be of any type.

# self.next = None - Here, the next attribute of the Node instance is initialized to None. This attribute is used to point to the next node in the linked list. When a node is first created, it doesn't point to any other node, hence None.

# Class LinkedList
# class LinkedList: - This line defines a new class named LinkedList. The LinkedList class is used to create and manage a linked list of Node instances.

# def __init__(self): - This is the constructor method for the LinkedList class. It initializes a new instance of the LinkedList class.

# self.head = None - This line initializes the head attribute of the LinkedList instance to None. The head attribute represents the first node in the linked list. Initially, the list is empty, so head is None.

# def __iter__(self): - This line defines the __iter__ method for the LinkedList class. The __iter__ method is a special method in Python that returns an iterator for an object. It allows the linked list to be iterated over using a for loop.

# curNode = self.head - The method starts by setting a local variable curNode to the head of the list, which is the starting point for the iteration.

# while curNode: - This line starts a while loop that continues as long as curNode is not None. The loop iterates through each node in the list.

# yield curNode - The yield statement is used to return the current curNode from the iterator. It allows the code iterating over the list to receive the current node and pauses the execution of the __iter__ method until the next item is requested.

# curNode = curNode.next - This line moves curNode to the next node in