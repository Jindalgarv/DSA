class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m=len(image)
        n=len(image[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        old_color=image[sr][sc]
        image[sr][sc]=color
        if old_color==color:
            return image
        q = deque()
        q.append((sr,sc))
        while q:
            row,col=q.popleft()
            for r,c in directions:
                new_row,new_col=row+r,col+c
                if 0<=new_row<m and 0<=new_col<n and image[new_row][new_col]==old_color:
                    q.append((new_row,new_col))
                    image[new_row][new_col]=color
        return image

