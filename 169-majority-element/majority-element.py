class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        nums.sort()
        if n%2==0:
            return nums[n//2]
        else:
            k=n//2
            return nums[k]
        