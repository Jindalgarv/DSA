class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={}
        for i,num in enumerate(nums):
            if (target-num) in freq:
                return [i,freq[target-num]]
            freq[num]=i