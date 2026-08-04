class Solution:
    def trap(self, height: List[int]) -> int:
#NOT SPACED OPTIMISED USING O(2N) SPACE
        # n=len(height)
        # water=0
        # preMax,sufMax=[0]*n,[0]*n
        # preMax[0],sufMax[-1]=height[0],height[-1]
        # for i in range(1,n):
        #     preMax[i]=max(preMax[i-1],height[i])
        # for i in range(n-2,-1,-1):
        #     sufMax[i]=max(sufMax[i+1],height[i])
        # for i in range(n):
        #     water+=min(preMax[i],sufMax[i])-height[i]
        # return water

#SPACE OPTIMISED
        # n=len(height)
        # left_max,right_max=0,0
        # l,r=0,n-1
        # water=0
        # while l<r:
        #     left_max=max(left_max,height[l])
        #     right_max=max(right_max,height[r])
        #     if height[l]<=height[r]:
        #         l+=1
        #         if height[l]<min(left_max,right_max):
        #             water+=min(left_max,right_max)-height[l]
        #     else:
        #         r-=1
        #         if height[r]<min(left_max,right_max):
        #             water+=min(left_max,right_max)-height[r]
        # return water
#GPT VERSION OF SPACE OPTIMISED JUST SMALL IMPROVEMENT IN MY CODE

        l, r = 0, len(height) - 1
        left_max = right_max = 0
        water = 0

        while l < r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])

            if left_max <= right_max:
                water += left_max - height[l]
                l += 1
            else:
                water+= right_max - height[r]
                r -= 1

        return water