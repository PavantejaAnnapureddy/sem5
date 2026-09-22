from collections import deque

class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.q = deque()

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q.appendleft(value)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q.append(value)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.q.popleft()
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.q.pop()
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.q[0]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.q[-1]

    def isEmpty(self) -> bool:
        return len(self.q) == 0

    def isFull(self) -> bool:
        return len(self.q) == self.k