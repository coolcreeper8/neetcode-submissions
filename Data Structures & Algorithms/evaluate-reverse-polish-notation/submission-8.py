class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        funcs = {"+" : lambda x,y: x+y, "-" : lambda x,y : x-y ,
                 "*" : lambda x,y : x*y, "/" : lambda x,y: x/y }
        
        stack = []

        for tok in tokens:
            if tok not in funcs:
                stack.append(int(tok))
            else:
                b, a = stack.pop(), stack.pop()
                stack.append(int(funcs[tok](a, b)))
            
        
        return int(stack[0])


    [22]