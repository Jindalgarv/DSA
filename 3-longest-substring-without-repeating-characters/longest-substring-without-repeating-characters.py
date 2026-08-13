class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        l,r=0,0
        ans=0
        contains=set()

        while r<n:

            if s[r] not in contains:
                contains.add(s[r])
                r+=1
                ans=max(ans,r-l)
            else:
                contains.remove(s[l])
                l+=1
        return ans