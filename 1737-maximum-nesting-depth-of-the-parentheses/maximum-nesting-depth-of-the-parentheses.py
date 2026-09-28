class Solution:
    def maxDepth(self, s: str) -> int:
        depth=0
        maxdepth=0
        for ch in s:
            if ch=='(':
                depth+=1
                maxdepth=max(depth,maxdepth)
                print(maxdepth)
            elif ch==')':
                depth=max(0,depth-1)
        return maxdepth