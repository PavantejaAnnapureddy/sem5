# Remove Nth Node From End of List

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given the `head` of a linked list, remove the `nth` node from the end of the list and return its head.

 

 **Example 1:** 

```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

```

 **Example 2:** 

```
Input: head = [1], n = 1
Output: []

```

 **Example 3:** 

```
Input: head = [1,2], n = 1
Output: [1]

```

 

 **Constraints:** 

- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

 

 **Follow up:**  Could you do this in one pass?

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.2 MB (beats 64.14%)  
**Submitted:** 2026-08-07T17:16:53.704Z  

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        
        for i in range(n + 1):
            fast = fast.next
        
        while fast is not None:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        
        return dummy.next
        
```

---

[View on LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)