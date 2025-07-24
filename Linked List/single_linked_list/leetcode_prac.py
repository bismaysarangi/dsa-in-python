class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPlaindroome(self, head: optional[Node]) -> bool:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None

    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True 
# list1 = [1, 2, 3] list2 = [1, 3, 5]
#Merge two sorted lists
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    cur = dummy = ListNode()

    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1, cur = list1.next, list1
        else:
            cur.next = list2
            list2, cur = list2.next, list2
        
    if list1 or list2:
        cur.next = list1 if list1 else list2
    
    return dummy.next

# Check if a linked list has a cycle
def hasCycle(self, head: Optional[ListNode]) -> bool:
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False
# Problem: Middle of Linked List
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow

# Problem: Reverse Linked List
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None

        while head:
            temp = head.next
            head.next = node
            node = head
            head = temp
        
        return node

# Problem: Convert Binary Number in a Linked List to Integer
def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans, curr = 0, head
        while curr:
            ans = (ans << 1) + curr.val
            curr = curr.next
        
        return ans

# Problem: Remove Linked List Elements
def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
     while head and head.val == val:
          head = head.next
     temp = head

     while temp and temp.next:
          if temp.next.val == val:
               temp.next = temp.next.next
          else:
               temp = temp.next
     return head

