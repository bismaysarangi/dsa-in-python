class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

newNode = Node(10)
print(newNode.value)


# Creation of a single linked list

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

new_linked_list = LinkedList(10)
print(new_linked_list.length)

