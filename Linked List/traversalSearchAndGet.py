class Node:
    def __init__(self, value):
        self.value = value      # Store the data
        self.next = None        # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None        # First node in the list
        self.tail = None        # Last node in the list
        self.length = 0         # Number of nodes in the list

    def append(self, value):
        new_node = Node(value)  # Create a new node
        if self.head is None:   # If the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Link the new node to the end
            self.tail = new_node       # Update the tail reference
        self.length += 1               # Increment the length
    
    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next 

    def search(self, target):
        current = self.head 
        index = 0  
        while current:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return False
    
    def get(self, index):
        if index == -1:
            return self.tail
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value if current else None
            
    
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
# print(new_linked_list.tail.value)  # Output: 600
# print(new_linked_list.length)      # Output: 6 
# print(new_linked_list)
new_linked_list.traverse()  
print(new_linked_list.search(400))    # Output: 100 -> 200 -> 300 -> 400 -> 500 -> 600
print(new_linked_list.get(3))