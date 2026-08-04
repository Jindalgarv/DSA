class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch not in pairs:
                stack.append(ch)
            elif not stack or stack.pop() != pairs[ch]:
                return False

        return not stack