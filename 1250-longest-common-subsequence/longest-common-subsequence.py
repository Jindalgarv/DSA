class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1,n2=len(text1),len(text2)
        dp=[[-1]*n2 for _ in range(n1)]
        def solve(i1,i2):
            if dp[i1][i2]!=-1:
                return dp[i1][i2]

            if i1==0 and i2==0:
                if text1[i1]==text2[i2]:
                    return 1
                return 0
            elif i1==0:
                if text1[i1]==text2[i2]:
                    return 1
                dp[i1][i2]=solve(i1,i2-1)
            elif i2==0:
                if text1[i1]==text2[i2]:
                    return 1
                dp[i1][i2]=solve(i1-1,i2)
            elif text1[i1]==text2[i2]:
                dp[i1][i2]=1+solve(i1-1,i2-1)
            else:
                dp[i1][i2]=max(solve(i1-1,i2),solve(i1,i2-1))
            return dp[i1][i2]
        return solve(n1-1,n2-1)


