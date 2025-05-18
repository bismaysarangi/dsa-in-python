class Node:
    def __init__(self, value):
        self.value = value
        self.next = None # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
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
    new_linked_list.prepend(i)
    
print(new_linked_list.head.value)  # Output: 600
print(new_linked_list.length)      # Output: 6
print(new_linked_list)             # Output: 600 -> 500 -> 400 -> 300 -> 200 -> 100