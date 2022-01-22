class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.stack.append(val)
       
        if not self.minimum or val < self.minimum[-1]:
            self.minimum.append(val)
        else:
            self.minimum.append(self.minimum[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()
        
    def top(self) -> int:
        topElement = self.stack.pop()
        self.stack.append(topElement)
        return topElement
    
    def getMin(self) -> int:
        temp = self.minimum.pop()
        self.minimum.append(temp)
        return temp


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()