class Solution:

    def fib(self, n: int) -> int:
        dp=[-1]*(n+1)
        def f(n):
            if dp[n]!=-1:
                return dp[n]
            if n==0 or n==1:
                return n
            dp[n]=self.fib(n-1)+self.fib(n-2)
            return dp[n]
        return f(n)


        