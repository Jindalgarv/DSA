from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq=Counter(nums)
        ans=0
        for e,f in freq.items():
            if f>len(nums)//2:
                return e