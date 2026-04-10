class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={')':'(','}':'{',']':'['}
        for x in s:
            if x in mapping:
                if not stack or stack[-1]!=mapping[x]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(x)
        return not stack