class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pre_pro=[1]*n
        succ_pro=[1]*n
        res=[1]*n
        for i in range(1,n):
            pre_pro[i]=pre_pro[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            succ_pro[i]=succ_pro[i+1]*nums[i+1]
        for i in range(n):
            res[i]=pre_pro[i]*succ_pro[i]
        print(pre_pro)
        print(succ_pro)
        return res

        
        