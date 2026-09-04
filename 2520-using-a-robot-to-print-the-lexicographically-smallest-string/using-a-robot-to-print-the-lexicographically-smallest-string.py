class Solution:
    def robotWithString(self, s: str) -> str:
        minsuf = ["{"]*(len(s)+1)

        for i in range(len(s)-1,-1,-1):
            minsuf[i]= min(minsuf[i+1],s[i])
        
        p,t = [],[]
        for i in range(len(s)):
            t.append(s[i])

            while t and t[-1] <= minsuf[i+1]:
                p.append(t.pop())

        return "".join(p)