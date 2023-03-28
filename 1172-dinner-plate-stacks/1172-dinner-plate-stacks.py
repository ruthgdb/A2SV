class DinnerPlates:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.stack = []
        self.indices = []

    def push(self, val: int) -> None:
        i = self.indices[-1] if self.indices and self.indices[-1] < len(self.stack) else -1
        
        if not self.indices or len(self.stack[i]) > self.cap:
            self.stack.append([val])
            self.indices.append(len(self.stack) - 1)
        else:
            self.stack[i].append(val)
            
        if len(self.stack[i]) == self.cap:
            self.indices.pop()
        
    def pop(self) -> int:
        if not self.stack:
            return -1
        
        while self.stack and not self.stack[-1]:
            self.stack.pop()
            
        if not self.stack:
            return -1
        
        popped = self.stack[-1].pop()
        
        if not self.stack[-1]:
            self.stack.pop()
        else:
            self.indices.append(len(self.stack) - 1)
        
        return popped

    def popAtStack(self, index: int) -> int:
        if index < len(self.stack) and self.stack[index]:
            popped = self.stack[index].pop()
            
            if index == len(self.stack) - 1 and not self.stack[-1]:
                if self.indices and self.indices[-1] == index:
                    self.indices.pop()
                self.stack.pop()
            else:
                self.indices.append(index)
            
            return popped
        
        return -1
    
    
# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)