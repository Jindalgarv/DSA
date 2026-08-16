from bisect import bisect_left,bisect_right
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n=len(nums)
        mid=n//2
        left=nums[:mid]
        right=nums[mid:]
        left_sum,right_sum=[],[]

        def solve(i,curr_sum,arr,ans):
            if i==len(arr):
                ans.append(curr_sum)
                return
            solve(i+1,curr_sum+arr[i],arr,ans)
            solve(i+1,curr_sum,arr,ans)


        solve(0,0,left,left_sum)
        solve(0,0,right,right_sum)
        right_sum.sort()
        ans=float('inf')
        for x in left_sum:
            target=goal-x
            idx=bisect_left(right_sum,target)
            if idx<len(right_sum):
                ans=min(ans,abs(right_sum[idx]-target))
            if idx>0:
                ans=min(ans,abs(right_sum[idx-1]-target))
        return ans

