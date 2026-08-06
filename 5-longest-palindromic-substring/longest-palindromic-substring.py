class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_len = 1
        n = len(s)

        def expand(left, right):
            nonlocal start, max_len

            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    start = left
                left -= 1
                right += 1

        for i in range(n):
            expand(i, i)       # Odd-length palindrome
            expand(i, i + 1)   # Even-length palindrome

        return s[start:start + max_len]