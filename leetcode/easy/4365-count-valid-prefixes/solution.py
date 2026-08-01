class Solution:
    def countValidPrefixes(self, s: str) -> int:
        c0 = 0
        c1 =0
        valid=0

        for i,char in enumerate(s):
            if char =='0':
                c0 +=1
            else:
                c1 +=1
            length = i +1

            if length %2 ==0:
                if c0 ==c1:
                    valid+=1
            else:
                if abs(c0-c1) <=1:
                    valid+=1
        return valid