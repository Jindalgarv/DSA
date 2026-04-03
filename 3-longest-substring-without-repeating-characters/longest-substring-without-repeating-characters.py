class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=set()
        length=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[j] not in longest:
                    longest.add(s[j])
                    length=max(length,len(longest))
                else:
                    longest=set()
                    break
        return length

            
            