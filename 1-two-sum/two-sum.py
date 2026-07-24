class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map={}
        for i,num in enumerate(nums):
            complement=target-num
            if complement in index_map:
                return [i,index_map[complement]]
            index_map[num]=i