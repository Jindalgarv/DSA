class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if tokens[i]=='+':
                res=stack[-1]+stack[-2]
                stack.pop()
                stack.pop()
                stack.append(res)
            
            elif tokens[i]=='*':
                res=stack[-1]*stack[-2]
                stack.pop()
                stack.pop()
                stack.append(res)
           
            elif tokens[i]=='-':
                res=stack[-2]-stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
           
            elif tokens[i]=='/':
                # if stack[-2]<0 and stack[-1]>0 or stack[-2]>0 and stack[-1]<0 :
                #     res=-abs(stack[-2])//abs(stack[-1])
                # else:
                #     res=stack[-2]//stack[-1]
                res = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(res)
            else:
                stack.append(int(tokens[i]))
        return stack[-1]

    