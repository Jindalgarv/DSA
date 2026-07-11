class Solution:
    def rob(self, nums: List[int]) -> int:
        #for arr1(0 to n-2)
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        prev2=nums[0]
        prev1=max(nums[0],nums[1])
        for i in range(2,n-1):
            prev1,prev2=max((nums[i]+prev2),prev1),prev1
        arr1=prev1
        
        #for arr2(1 to n-1)
        arr2prev2=nums[1]
        arr2prev1=max(nums[1],nums[2])
        for i in range(3,n):
            arr2prev1,arr2prev2=max((nums[i]+arr2prev2),arr2prev1),arr2prev1
        arr2=arr2prev1
        return(max(arr1,arr2))