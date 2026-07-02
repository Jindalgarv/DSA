class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n=len(board),len(board[0])
        safe=[[0]*n for _ in range(m)]
        directions=((0,1),(1,0),(-1,0),(0,-1))

        def dfs(i,j):
            safe[i][j]=1
            for dr,dc in directions:
                nr,nc=i+dr,j+dc
                if 0<nr<m and 0<nc<n and board[nr][nc]=='O' and not safe[nr][nc]:
                    dfs(nr,nc)

        for i in range(m):
            for j in range(n):
                if (i==0 or i==m-1 or j==0 or j==n-1) and board[i][j]=='O':
                    dfs(i,j)
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O' and not safe[i][j]:
                    board[i][j]='X'


        