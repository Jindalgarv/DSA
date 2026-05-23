class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        return self.bSearch(nums,l,r,target)
    def bSearch(self,nums,l,r,target) -> int:
        if l>r:
            return -1
        mid=(l+r)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            return self.bSearch(nums,l,mid-1,target)
        else: return self.bSearch(nums,mid+1,r,target)
        return -1
    

        