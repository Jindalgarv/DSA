class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        while l<=r:
            m=(l+r)//2
            time=0
            for x in piles:
                if x%m==0:
                    time+=x//m
                else:
                    time+=x//m+1
            if time>h:
                l=m+1
            else:
                r=m-1

        return l

        