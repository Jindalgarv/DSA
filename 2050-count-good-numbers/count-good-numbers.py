class Solution:
    def power(self, x, n, mod):
        ans = 1

        while n > 0:
            if n % 2 == 1:
                ans = (ans * x) % mod

            x = (x * x) % mod
            n //= 2

        return ans

    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7

        even = (n + 1) // 2
        odd = n // 2

        return (self.power(5, even, mod) * self.power(4, odd, mod)) % mod