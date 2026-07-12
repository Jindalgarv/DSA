# from math import factorial
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         return factorial(m+n-2)//(factorial(m-1)*factorial(n-1))

from math import comb
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m+n-2,m-1)