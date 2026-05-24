class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m=len(matrix),len(matrix[0])
        l,r=0,m*n-1
        while l<=r:
            mid= l+(r-l)//2
            row=mid//m
            col=mid%m
            if target>matrix[row][col]:
                l=mid+1
            elif target<matrix[row][col]:
                r=mid-1
            else:
                return True
        return False
