class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n=len(matrix),len(matrix[0])
        arr=[]
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    arr.append((i,j))
        for row,col in arr:
            for i in range(m):
                matrix[i][col]=0
            for j in range(n):
                matrix[row][j]=0
        
