class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(arr):
            prev2 = arr[0]
            prev1 = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                curr = max(arr[i] + prev2, prev1)
                prev2 = prev1
                prev1 = curr
            return prev1

        n = len(nums)
        if n == 1:
            return nums[0]
        elif n==2:
            return max(nums[0],nums[1])
        return max(solve(nums[:-1]), solve(nums[1:]))