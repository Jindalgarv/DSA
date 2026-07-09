class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        # return self.climbStairs(n-1)+self.climbStairs(n-2)
        prev,curr=1,2
        for i in range(2,n):
            prev,curr=curr,prev+curr
        return curr
