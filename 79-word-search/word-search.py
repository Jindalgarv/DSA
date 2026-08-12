class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        m,n=len(board),len(board[0])
        visited=[[0]*n for _ in range(m)]
        def dfs(i,j,idx):
            if idx==len(word)-1:
                return True
            visited[i][j]=1
            for dr,dc in directions:
                nr,nc=i+dr,j+dc
                if 0<=nr<m and 0<=nc<n and word[idx+1]==board[nr][nc] and not visited[nr][nc]:
                    if dfs(nr,nc,idx+1):
                        return True
            visited[i][j]=0
            return False
            
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if dfs(i,j,0):
                        return True
        return False