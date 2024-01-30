class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        op='+-*/'
        for ele in tokens:
            if ele not in op:
                stack.append(int(ele)) 
            else:
                if ele=="+":
                    stack.append( stack.pop()+stack.pop())
                elif ele=="-":
                    a=stack.pop()
                    b=stack.pop()
                    c=b-a
                    stack.append( c)
                elif ele=="*":
                    stack.append( stack.pop()*stack.pop())
                else:
                    a=stack.pop()
                    b=stack.pop()
                    c=int(b/a)
                    
                    stack.append(c)
