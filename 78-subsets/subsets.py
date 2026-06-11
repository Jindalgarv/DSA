class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        subsets=1<<n
        res=[]
        for num in range(subsets):
            arr=[]
            for i in range(n):
                if (num&(1<<i)):
                    arr.append(nums[i])
            res.append(arr)
        return res