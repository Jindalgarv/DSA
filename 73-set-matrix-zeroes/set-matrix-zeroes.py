# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
        # """
        # Do not return anything, modify matrix in-place instead.
        # """
#BRUTE FORCE just keep a track of all 0 and then place all other 0's
        # m,n=len(matrix),len(matrix[0])
        # arr=[]
        # for i in range(m):
        #     for j in range(n):
        #         if not matrix[i][j]:
        #             arr.append((i,j))
        # for row,col in arr:
        #     for i in range(m):
        #         matrix[i][col]=0
        #     for j in range(n):
        #         matrix[row][j]=0

#Better with space O(m+n)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n=len(matrix),len(matrix[0])
        row=[0]*m
        column=[0]*n
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    row[i]=1
                    column[j]=1

        for i in range(m):
            for j in range(n):
                if row[i] or column[j]:
                    matrix[i][j]=0

#OPTIMAL WITH CONSTANT SPACE
#1,2,3
#2,0,0
#0,3,0

# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         m,n=len(matrix),len(matrix[0])
#         for i in range(m):
#             for j in range(n):
#                 if not matrix[i][j]:
#                     matrix[i][0]=0
#                     matrix[0][j]=0

        # for i in range(m):
        #     for j in range(n):
        #         if row[i] or column[j]:
        #             matrix[i][j]=0

        


               
