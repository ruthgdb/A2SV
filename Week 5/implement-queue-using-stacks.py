class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        while(len(self.stack1) > 0):
            self.stack2.append(self.stack1.pop())
        firstElement = self.stack2.pop()
        while(len(self.stack2) > 0):
            self.stack1.append(self.stack2.pop())
        return firstElement
    def peek(self) -> int:
        while(len(self.stack1) > 0):
            self.stack2.append(self.stack1.pop())
        firstElement = self.stack2.pop()
        self.stack1.append(firstElement)
        while(len(self.stack2) > 0):
            self.stack1.append(self.stack2.pop())
        return firstElement
    def empty(self) -> bool:
        if(len(self.stack1) == 0):
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()