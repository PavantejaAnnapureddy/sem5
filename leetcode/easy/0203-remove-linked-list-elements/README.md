# Remove Linked List Elements

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given the `head` of a linked list and an integer `val`, remove all the nodes of the linked list that has `Node.val == val`, and return  *the new head*.

 

 **Example 1:** 

```
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

```

 **Example 2:** 

```
Input: head = [], val = 1
Output: []

```

 **Example 3:** 

```
Input: head = [7,7,7,7], val = 7
Output: []

```

 

 **Constraints:** 

- The number of nodes in the list is in the range [0, 104].
- 1 <= Node.val <= 50
- 0 <= val <= 50

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 22.8 MB (beats 6.96%)  
**Submitted:** 2026-09-29T09:35:58.781Z  

```py
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
```

---

[View on LeetCode](https://leetcode.com/problems/remove-linked-list-elements/)