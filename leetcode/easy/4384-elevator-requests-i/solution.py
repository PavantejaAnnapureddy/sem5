class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
       total = 0
       current = 0
       for i in range(len(requests)):
            if i == 0:
                total += requests[i] - current
            else:
                total += abs(requests[i] - requests[i-1])
       return total