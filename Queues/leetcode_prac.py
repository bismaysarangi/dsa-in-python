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