class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n= len(s)
        count =0
        for i in range(n):
            rotation =s[i:]+s[:i]
            score=0
            for j in range(n-1):
                if rotation[j ]== rotation[j + 1]:
                    score+=1
            if score == k:
               count+=1
        return count