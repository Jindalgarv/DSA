class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x

        if target < 0:
            return -1
        elif target==0:
            return n

        l = 0
        curr_sum = 0
        ans = 0

        for r in range(n):
            curr_sum += nums[r]

            while curr_sum > target:
                curr_sum -= nums[l]
                l += 1

            if curr_sum == target:
                ans = max(ans, r - l + 1)

        return -1 if ans == 0 else n - ans