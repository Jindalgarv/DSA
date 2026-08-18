class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n=len(arr)
        left,right=0,0
        for i in range(n-1):
            if arr[i+1]>=arr[i]:
                continue
            else:
                left=i
                break
        for j in range(n-1,0,-1):
            if arr[j-1]<=arr[j]:
                continue
            else:
                right=j
                break
        if left==n-1 or right==0:
            return 0
        result=min(n-left-1,right)
        i,j=0,right
        while i<=left and j<n:
            if arr[i]<=arr[j]:
                result=min(result,j-i-1)
                i+=1
            else:
                j+=1
        return result
        