class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        dummy = ListNode(0, head)   # dummy points to head
        prev = dummy
        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next   # skip the node
            else:
                prev = prev.next             # move forward
        return dummy.next