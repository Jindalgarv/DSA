class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        water=0
        preMax,sufMax=[0]*n,[0]*n
        preMax[0],sufMax[-1]=height[0],height[-1]
        for i in range(1,n):
            preMax[i]=max(preMax[i-1],height[i])
        for i in range(n-2,-1,-1):
            sufMax[i]=max(sufMax[i+1],height[i])
        for i in range(n):
            water+=min(preMax[i],sufMax[i])-height[i]
        return water
