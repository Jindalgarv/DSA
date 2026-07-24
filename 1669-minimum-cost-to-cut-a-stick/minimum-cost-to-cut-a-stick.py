class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        c=len(cuts)
        cuts.append(n)
        cuts.append(0)
        cuts.sort()
        @cache
        def solve(i,j):
            if i>j:
                return 0
            mini=float('inf')
            for ind in range(i,j+1):
                cost=cuts[j+1]-cuts[i-1]+ solve(i,ind-1)+solve(ind+1,j)
                mini=min(mini,cost)
            return mini
        return solve(1,c)