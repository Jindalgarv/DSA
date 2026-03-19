# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         n=len(s)
#         if self.isPalindrome(s):
#             return True

#         for i in range(n):
#             t=s[:i]+s[i+1:]
#             if self.isPalindrome(t):
#                 return True
#         return False

#     def isPalindrome(self, s: str) -> bool:
#         l,r=0,len(s)-1
#         while(l<r):
#             if not(s[l].isalnum()):
#                 l+=1
#                 continue
#             if not(s[r].isalnum()):
#                 r-=1
#                 continue
#             if l<r and s[l].lower()!=s[r].lower():
#                 return False
#             l+=1
#             r-=1
#         return True
        

class Solution:
    def validPalindrome(self, s: str) -> bool:
        n=len(s)
        l,r=0,n-1
        while(l<r and s[l]==s[r]):
                l+=1
                r-=1
        if self.isPalindrome(s,l+1,r) or self.isPalindrome(s,l,r-1) :
            return True
        return False


    def isPalindrome(self, s: str,l,r) -> bool:
        while(l<r):
            if l<r and s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
        