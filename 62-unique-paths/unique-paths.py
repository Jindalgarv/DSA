from math import comb

class Solution:

    # =====================================================
    # 1. RECURSION
    # Time  : O(2^(m+n))
    # Space : O(m+n)
    # =====================================================
    def uniquePaths(self, m: int, n: int) -> int:

        def solve(i, j):
            if i == m - 1 and j == n - 1:
                return 1

            if i >= m or j >= n:
                return 0

            return solve(i + 1, j) + solve(i, j + 1)

        return solve(0, 0)


    # =====================================================
    # 2. MEMOIZATION
    # Time  : O(m*n)
    # Space : O(m*n) + O(m+n)
    # =====================================================
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[-1] * n for _ in range(m)]

        def solve(i, j):
            if i == m - 1 and j == n - 1:
                return 1

            if i >= m or j >= n:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            dp[i][j] = solve(i + 1, j) + solve(i, j + 1)

            return dp[i][j]

        return solve(0, 0)


    # =====================================================
    # 3. TABULATION
    # Time  : O(m*n)
    # Space : O(m*n)
    # =====================================================
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            dp[i][0] = 1

        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


    # =====================================================
    # 4. SPACE OPTIMIZED
    # Time  : O(m*n)
    # Space : O(n)
    # =====================================================
    def uniquePaths(self, m: int, n: int) -> int:

        prev = [1] * n

        for _ in range(1, m):
            curr = [1] * n

            for j in range(1, n):
                curr[j] = curr[j - 1] + prev[j]

            prev = curr

        return prev[-1]


    # =====================================================
    # 5. MATHEMATICAL
    # Time  : Approximately O(min(m, n))
    # Space : O(1)
    # =====================================================
    def uniquePaths(self, m: int, n: int) -> int:

        return comb(m + n - 2, m - 1)