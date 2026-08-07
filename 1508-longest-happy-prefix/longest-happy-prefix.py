class Solution:
    def longestPrefix(self, s: str) -> str:
        ans=""
        n=len(s)
        for k in range(1,len(s)):
            if s[0:k]==s[n-k:n]:
                ans=s[0:k]
        return ans



        