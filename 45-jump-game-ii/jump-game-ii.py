class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest,curr_end,jumps=0,0,0
        for i in range(len(nums)-1):
            farthest=max(farthest,i+nums[i])
            if curr_end==i:
                jumps+=1
                curr_end=farthest
        return jumps
            
