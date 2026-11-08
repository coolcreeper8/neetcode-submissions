class MinStack:

    def __init__(self):
        self.deque = []
    def push(self, val: int) -> None:
        if len(self.deque) == 0:
            self.deque.append([val, val])
        else:
            self.deque.append([val, min(val,self.deque[-1][1])])
        
    def pop(self) -> None:
        out =  self.deque.pop()
        return out

    def top(self) -> int:
        return self.deque[-1][0]

    def getMin(self) -> int:
        return self.deque[-1][1]
