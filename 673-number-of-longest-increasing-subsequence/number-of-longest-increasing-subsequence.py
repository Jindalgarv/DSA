class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        forward = [1] * n
        count=[1]*n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and forward[i]<forward[j]+1:
                    forward[i] = max(forward[i], forward[j] + 1)
                    count[i]=count[j]
                elif (nums[i] > nums[j]) and (forward[i]==forward[j] + 1):
                    count[i]+=count[j]
        
        maxi=max(forward)
        
        if maxi==1:
            return n
        ans = 0
        for i in range(n):
            if forward[i] == maxi:
                ans += count[i]
        return ans
