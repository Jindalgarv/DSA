class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for x in asteroids:
            if x>0:
                stack.append(x)
            else:
                while(stack and stack[-1]>0):
                    if(abs(x)>stack[-1]):
                        stack.pop()
                    elif(abs(x)==stack[-1]):
                        stack.pop()
                        break
                    else:
                        break
                else:
                    stack.append(x)
        return stack