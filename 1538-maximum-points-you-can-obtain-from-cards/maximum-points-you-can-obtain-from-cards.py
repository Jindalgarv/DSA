class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        total=sum(cardPoints)
        curr=sum(cardPoints[:n-k])
        ans=total-curr
        l=0
        for i in range(n-k,n):
            curr=curr+cardPoints[i]-cardPoints[l]
            l+=1
            ans=max(ans,total-curr)
        return ans