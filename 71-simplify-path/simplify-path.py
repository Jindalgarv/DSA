class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        parts = path.split("/") 
        for x in parts:
            if x =="" or x==".":
                continue
            elif x=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(x)
        return '/'+'/'.join(stack)
