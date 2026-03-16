class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n//2-1,-1,-1):
            self.Heapify(nums,n,i)
        for i in range(n-1,0,-1):
            nums[i],nums[0]=nums[0],nums[i]
            self.Heapify(nums,i,0)
        return nums
    def Heapify(self,nums,heapSize,i):
        n=heapSize
        max=i
        l=2*i+1
        r=2*i+2

        if l<n and nums[max]<nums[l]:
            max= l
        if r<n and nums[max]<nums[r]:
            max=r
        if max!=i:
            nums[i],nums[max]=nums[max],nums[i]
            self.Heapify(nums,n,max)
        