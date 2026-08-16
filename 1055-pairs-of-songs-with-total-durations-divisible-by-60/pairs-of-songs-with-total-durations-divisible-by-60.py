class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d=defaultdict(list)
        for x in time:
            d[x%60].append(x)
        k=len(d[0])
        ans=0
        if k>1:
            ans+=k*(k-1)/2
        i,j=1,59
        while i<j:
            ans+=len(d[i])*len(d[j])
            i+=1
            j-=1
        k=len(d[30])  
        if k>1:
            ans+=k*(k-1)/2
        return int(ans)
