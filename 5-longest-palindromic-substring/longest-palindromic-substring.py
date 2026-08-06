# class Solution:
#     def longestPalindrome(self, s: str) -> str:
        # n=len(s)
        # ans=0
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         if s[i:j]==s[j:i:-1]:
        #             ans=max(ans,j-i+1)

        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         if s[i:j]==s[j:i:-1] and ans==j-i+1:
        #             return s[i:j+1]
        # return s[0]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start,max_len=0,1
        n=len(s)
        def f(i,j):
            nonlocal start,max_len
            left,right=i,j
            while left>=0 and right<n:
                if s[left]==s[right]:
                    if right-left+1>max_len:
                        max_len=right-left+1
                        start=left
                    left-=1
                    right+=1
                else:
                    return
            return
            
        for i in range(len(s)):
            f(i,i)
            f(i,i+1)
        return s[start:start+max_len]