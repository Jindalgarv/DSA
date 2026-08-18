class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != ']':
                stack.append(ch)
                continue

            string = []
            while stack[-1] != '[':
                string.append(stack.pop())

            stack.pop()  # '['

            k = []
            while stack and stack[-1].isdigit():
                k.append(stack.pop())

            string.reverse()
            k.reverse()

            stack.append(int("".join(k)) * "".join(string))

        return "".join(stack)