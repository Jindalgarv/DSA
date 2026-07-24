class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        i,j=0,n-1
        vol=0
        while i<j:
            vol=max(vol,(j-i)*min(height[j],height[i]))
            if height[j]>height[i]:
                i+=1
            else:
                j-=1
        return vol
            
