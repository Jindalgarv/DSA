class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        maxlen=0
        seen=set()
        l,r=0,0
        while l<n and r<n:
            if s[r] not in seen:
                seen.add(s[r])
                r+=1
                maxlen=max(maxlen,len(seen))
            else:
                seen.remove(s[l])
                l+=1
        return maxlen

                


                    

        