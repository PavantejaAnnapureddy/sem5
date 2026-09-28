class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.dummy = Node(0)   # sentinel
        self.size = 0

    def _get_node(self, index):
        if index < 0 or index >= self.size:
            return None
        cur = self.dummy.next
        for _ in range(index):
            cur = cur.next
        return cur

    def get(self, index: int) -> int:
        node = self._get_node(index)
        return node.val if node else -1

    def addAtHead(self, val: int) -> None:
        newNode = Node(val, self.dummy.next)
        self.dummy.next = newNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        cur = self.dummy
        while cur.next:
            cur = cur.next
        cur.next = Node(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        prev = self.dummy
        for _ in range(index):
            prev = prev.next
        newNode = Node(val, prev.next)
        prev.next = newNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        prev = self.dummy
        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)