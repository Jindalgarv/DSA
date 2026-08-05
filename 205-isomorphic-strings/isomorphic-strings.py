class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        d2={}
        for a,b in zip(s,t):
            if a in d and d[a]==b:
                continue
            elif a not in d:
                d[a]=b
            else:
                return False
        for b,a in zip(s,t):
            if a in d2 and d2[a]==b:
                continue
            elif a not in d2:
                d2[a]=b
            else:
                return False
        return True
        