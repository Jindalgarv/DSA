# class Solution:
#     def removeStones(self, stones: List[List[int]]) -> int:
        # m,n=0,0
        # for i,j in stones:
        #     m,n=max(m,i+1),max(n,j+1)
        # stone={(r,c) for r,c in stones}
        # total=len(stone)

        # def dfs(row,col):
        #     stone.remove((row,col))
        #     for i in range(m):
        #         if (i,col) in stone:
        #             dfs(i,col)
        #     for j in range(n):
        #         if (row,j) in stone:
        #             dfs(row,j)
        # ans=0
        # for i in range(m):
        #     for j in range(n):
        #         if (i,j) in stone:
        #             dfs(i,j)
        #             ans+=1
        # return total-ans
class DSU:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[0]*n
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if x==y:
            return False
        if self.rank[x]<self.rank[y]:
            x,y=y,x
        self.parent[y]=x
        if self.rank[x]==self.rank[y]:
            self.rank[x]+=1
class Solution:
    def removeStones(self,stones):
        max_row=max(r for r,c in stones)
        max_col=max(c for r,c in stones)
        dsu=DSU(max_row+max_col+2)
        nodes=set()

        for r,c in stones:
            c+=max_row+1
            dsu.union(r,c)
            nodes.add(r)
            nodes.add(c)
        components=len({dsu.find(x) for x in nodes})
        return len(stones)-components

