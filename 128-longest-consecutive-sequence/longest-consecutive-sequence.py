class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        s=set(nums)
        longest=1
        for x in s:
            if x-1 not in s:
                length=1
                while(x+length in s):
                    length+=1
                    longest=max(longest,length)
                    
        return longest