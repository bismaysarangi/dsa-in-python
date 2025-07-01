# Problem: Implement Queue using Stacks

from collections import deque
class MyQueue:
    def __init__(self):
        self.queue = deque()
    def push(self, x: int) -> None:
        self.queue.append(x)
    def pop(self) -> int:
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        return self.queue.popleft()
    def top(self) -> int:
        return self.queue[-1]
    def empty(self) -> bool:
        return len(self.queue) == 0
    
# Problem: Time needed to buy tickets
def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        result = 0
        for i in range(len(tickets)):
            if i <= k:
                result += min(tickets[i], tickets[k])
            else:
                result += min(tickets[i], tickets[k] - 1)
            
        return result