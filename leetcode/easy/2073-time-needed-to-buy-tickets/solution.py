"""class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        for i, t in enumerate(tickets):
            if i <= k:
                time += min(t, tickets[k])
            else:
                time += min(t, tickets[k] - 1)
        return time"""
from collections import deque
from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        for i, t in enumerate(tickets):
            queue.append([i, t])
        
        time = 0
        
        while queue:
            person = queue.popleft()
            person[1] -= 1
            time += 1
            if person[0] == k and person[1] == 0:
                return time
            if person[1] > 0:
                queue.append(person)
        
        return time