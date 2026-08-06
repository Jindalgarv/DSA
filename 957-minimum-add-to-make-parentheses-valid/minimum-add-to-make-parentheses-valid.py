class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        cbo=0
        o,c=0,0
        for ch in s:
            if ch=='(':
                o+=1
            else:
                if o-c==0:
                    cbo+=1
                else:
                    c+=1
        return abs(o-c)+cbo
        