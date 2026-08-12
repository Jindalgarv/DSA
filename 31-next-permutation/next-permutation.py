class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n=len(nums)
        ind=-1
        for i in range(n-1,0,-1):
            if nums[i-1]<nums[i]:
                ind=i-1
                break
        if ind==-1:
            nums.reverse()
            return
        for i in range(n-1,ind,-1):
            if nums[ind]<nums[i]:
                nums[ind],nums[i]=nums[i],nums[ind]
                break
        nums[ind+1:]=reversed(nums[ind+1:])
        

        """
        Do not return anything, modify nums in-place instead.
        """
        