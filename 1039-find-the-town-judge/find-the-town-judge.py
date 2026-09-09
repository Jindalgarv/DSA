class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        s=set()
        for a,b in trust:
            s.add(a)
        if len(s)!=n-1:
            return -1
        for i in range(1,n+1):
            if i not in s:
                t=i
                break

        for i in range(1,n):
            if i !=t and [i,t] not in trust:
                return -1
        return t

            