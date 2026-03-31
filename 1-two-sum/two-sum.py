class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            key=nums[i]
            if target-key in d:
                return[i,d[target-key]]
            d[key]=i
