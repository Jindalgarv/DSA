class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in range(len(asteroids)-1,-1,-1):
            if not stack or stack[-1]>0 or asteroids[i]<0:
                stack.append(asteroids[i])
            else:
                if abs(stack[-1])==abs(asteroids[i]):
                    stack.pop()
                    continue
                if abs(stack[-1])>abs(asteroids[i]):
                    continue
                else:
                    while stack and stack[-1]<0 and abs(stack[-1])<abs(asteroids[i]):
                        stack.pop()
                    if stack and -stack[-1]==asteroids[i]:
                        stack.pop()
                        continue
                    if not stack or stack[-1]>0:
                        stack.append(asteroids[i])                    
        stack.reverse()
        return stack

        # stack=[]
        # for x in asteroids:
        #     if x>0:
        #         stack.append()
        #     else:
        #         if stack[-1]<0:

        