# This code defines a simple implementation of a singly linked list in Python.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

# class Node: This line defines a new class named Node. In the context of linked lists, a node is an individual element of the list which holds the data and a reference to the next node.

# def __init__(self, value): This is the constructor method for the Node class. Whenever a new Node object is created, this method will be called. It takes two parameters: self which is a reference to the current instance of the class, and value which is the data that the node will hold.

# self.value = value: This line sets the value attribute of the node to the value passed to the constructor. This is the data that this node holds.

# self.next = None: This line sets the next attribute of the node to None. In a linked list, the next attribute usually contains a reference to the next node in the list. Here, it's initialized to None because when a node is first created, it doesn't know what the next node is.

# class LinkedList: This line defines a new class named LinkedList. This class represents the linked list itself and will contain nodes.

# def __init__(self, value): This is the constructor method for the LinkedList class. It takes two parameters: self which is a reference to the current instance of the class, and value which is the value for the first node in the linked list.

# new_node = Node(value): This line creates a new Node object with the given value. This new node will be the first node in the linked list.

# self.head = new_node: This line sets the head attribute of the linked list to the new node. In a linked list, the head is a reference to the first node in the list.

# self.tail = self.head: This line sets the tail attribute of the linked list to be the same as the head. This is because, at the moment of creation, the linked list only contains one node, so the head and tail are the same.

# self.length = 1: This line sets the length attribute of the linked list to 1. The length attribute keeps track of how many nodes are in the list. Since we've just created the list with one node, the length is 1.



# Insertion at the Beginning
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        
    # Implement Here
    def prepend(self, value):
        # TODO
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

# Line 1: def prepend(self, value):

# This line is defining a new method for the LinkedList class, called prepend. This method takes two arguments: self, which is a reference to the instance of the LinkedList class that this method is being called on; and value, which is the data for the new node that will be inserted at the beginning of the list.

# Line 2: new_node = Node(value)

# This line creates a new instance of the Node class with the given value. The new_node variable is a local variable in the prepend method that holds a reference to the new node.

# Line 3: new_node.next = self.head

# This line sets the next attribute of the new_node to point to the current head of the LinkedList. This is done because new_node is about to become the new head of the list, so it needs to reference the node that will come after it in the list.

# Line 4: self.head = new_node

# This line updates the head attribute of the LinkedList to point to new_node, effectively making new_node the first node in the list. Since new_node already points to the old head of the list (from the previous line), the rest of the list remains intact.

# Line 5: self.length += 1

# This line increments the length attribute of the LinkedList by 1. This is done because we've just added a new node to the list, so the total number of nodes in the list has increased by 1.

# In conclusion, the prepend method allows a new value to be inserted at the start of the LinkedList. It does this by creating a new node with the given value, linking it to the existing head of the list, then updating the head of the list to be the new node, and finally updating the list's length.

# Time and Space Complexity

# Line 1: def prepend(self, value):

# This line declares the method prepend. The declaration itself has no time or space complexity since it doesn't perform any operations or allocate any space.

# Line 2: new_node = Node(value)

# This line creates a new node. The time complexity is O(1) because creating a new node is a constant time operation, it does not depend on the size of the linked list. The space complexity is also O(1) because we're allocating space for one new node, which is constant.

# Line 3: new_node.next = self.head

# This line assigns the head of the linked list to the next attribute of the new node. The time complexity is O(1) because it's a simple assignment operation. The space complexity is O(1) because we're not allocating any new space, just assigning a reference to an existing node.

# Line 4: self.head = new_node

# This line updates the head of the linked list to the new node. The time complexity is O(1) because, again, it's a simple assignment operation. The space complexity is O(1) because we're not allocating any new space, just updating a reference.

# Line 5: self.length += 1

# This line increments the length of the linked list by 1. The time complexity is O(1) because incrementing a value is a constant time operation. The space complexity is O(1) because we're not allocating any new space, just updating an existing integer.

# In summary, each line in the prepend method operates in O(1) time and space complexity, which means the overall time and space complexity of the method is also O(1).


# Insertion at the End
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        # TODO
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

# Line 1: def append(self, value):

# This line is defining a new method for the LinkedList class, named append. This method takes two arguments: self, a reference to the instance of the LinkedList class that this method is being called on, and value, the data for the new node that will be appended at the end of the list.

# Line 2: new_node = Node(value)

# This line creates a new instance of the Node class with the given value. The new_node variable is a local variable in the append method that holds a reference to the new node.

# Line 3-6:

# if self.head is None and self.tail is None: 
#     self.head = new_node 
#     self.tail = new_node
# These lines check if the LinkedList is empty, that is, the head and tail are both None. If it is empty, it assigns the head and tail of the LinkedList to the new_node. Essentially, the new node becomes the first and only node in the list.

# Line 7-8:

# else: 
#     self.tail.next = new_node 
#     self.tail = new_node
# These lines execute if the LinkedList is not empty. It sets the next attribute of the current tail node to new_node, meaning it connects the last node of the LinkedList to the new_node. Then, it updates the tail attribute of the LinkedList to new_node, as new_node is now the last node in the list.

# Line 9: self.length += 1

# This line increments the length attribute of the LinkedList by 1. This is because we've just added a new node to the list, increasing the total number of nodes in the list by 1.



# Time and Space Complexity

# Line 1: def append(self, value):

# This line defines the append method. Defining a function does not entail any computation or memory allocation, so there's no time or space complexity associated with this line.

# Line 2: new_node = Node(value)

# This line creates a new node. The time complexity is O(1), because creating a new node is a constant-time operation. The space complexity is also O(1), because we're allocating space for one new node.

# Line 3-6:

# if self.head is None and self.tail is None: 
#     self.head = new_node 
#     self.tail = new_node
# This block checks whether the list is empty and, if so, assigns the head and tail to the new node. The time complexity for checking if head and tail are None and assigning them is O(1). There's no additional space allocation here, so the space complexity is O(1).

# Line 7-8:

# else: 
#     self.tail.next = new_node 
#     self.tail = new_node
# In this block, the next pointer of the current tail node is set to the new node, and the tail of the list is updated to the new node. Both these operations have a time complexity of O(1). Again, there's no new space allocation, so the space complexity is O(1).

# Line 9: self.length += 1

# Incrementing the length attribute by 1 has a time complexity of O(1). Since there's no additional space allocation, the space complexity is O(1).