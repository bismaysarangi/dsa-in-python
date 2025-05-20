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
        new_node = Node(value)  # Create a new node
        if self.head is None:   # If the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Link the new node to the end
            self.tail = new_node       # Update the tail reference
        self.length += 1 
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1              
    def insert(self, value, index):
        if index < 0 or index > self.length:
            raise IndexError("Index out of bounds")
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head  
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            self.length += 1
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

new_linked_list = LinkedList()
for i in range(100, 700, 100):
    new_linked_list.append(i)
# for i in range(100, 900, 100):
#     new_linked_list.prepend(i)
new_linked_list.insert(1000, 3)
print(new_linked_list.head.value)  
print(new_linked_list.tail.value)  
print(new_linked_list.length)      
print(new_linked_list)             