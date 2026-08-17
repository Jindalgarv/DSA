class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        ans=zeros=0
        for x in s:
            if x=='0':
                zeros+=1
            else:
                if zeros>0:
                    ans=max(ans+1,zeros)
        return ans