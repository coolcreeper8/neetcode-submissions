class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        funcs = {"+" : lambda x,y: x+y, "-" : lambda x,y : x-y ,
                 "*" : lambda x,y : x*y, "/" : lambda x,y: x/y }
        
        stack = []

        for tok in tokens:
            if tok not in funcs:
                stack.append(int(tok))
            else:
                args = []
                for i in range(0,2):
                    args.insert(0,stack.pop())
                stack.append(int(funcs[tok](args[0], args[1])))
            
        
        return int(stack[0])


    [22]