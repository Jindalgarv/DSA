class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res=start^goal
        count=0
        while(res>1):
            count+=res&1
            res=res//2
        if res==1:
            count+=1
        return count
