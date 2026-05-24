class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        #finding row
        l,r=0,m-1

        while l<=r:
            row=(l+r)//2

            if matrix[row][-1]<target:
                l=row+1
            elif matrix[row][0]>target:
                r=row-1
            else:
                 break
        #finding column
        l,r=0,n-1
        while l<=r:
            mid=(l+r)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]>target:
                r=mid-1
            else:
                l=mid+1
        return False
            

        