class Solution:
    def minElement(self, nums: List[int]) -> int:
        mele=nums[0]
        for x in nums:
            ele=0
            while x:
                ele+=x%10
                x=x//10
            mele=min(mele,ele)
        return mele
                
        