class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=0,0
        for x in weights:
            r+=x
            l=max(l,x)
        while l<=r:
            mid=(l+r)//2
            s=0
            day=1
            for x in weights:
                s+=x
                if s>mid:
                    s=x
                    day+=1
            if day>days:
                l=mid+1
            else:
                r=mid-1
        return l
