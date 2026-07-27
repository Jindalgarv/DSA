class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        longest=0
        for x in s:
            if x-1 not in s:
                k=0
                while x+k in s:
                    k+=1
                longest=max(longest,k)
        return longest