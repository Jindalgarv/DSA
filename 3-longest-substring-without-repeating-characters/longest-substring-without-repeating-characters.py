class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r,n=0,0,len(s)
        longest=0
        sub=set()
        while(r<n):
            if s[r] not in sub:
                sub.add(s[r])
                r+=1
                longest=max(longest,len(sub))
            else:
                while(s[r] in sub):
                    sub.remove(s[l])
                    l+=1
                sub.add(s[r])
                r+=1
                longest=max(longest,len(sub))
        return longest
            
            