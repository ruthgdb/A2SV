class Node:
    def __init__(self, val = ''):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.newList = Node(homepage)

    def visit(self, url: str) -> None:
        temp = self.newList
        self.newList.next = Node(url)
        self.newList = self.newList.next
        self.newList.prev = temp

    def back(self, steps: int) -> str:
        while self.newList:
            if steps == 0:
                break
                
            if self.newList.prev:
                self.newList = self.newList.prev
                steps -= 1
            else:
                break
                
        return self.newList.val

    def forward(self, steps: int) -> str:
        while self.newList:
            if steps == 0:
                break
             
            if self.newList.next:
                steps -= 1
                self.newList = self.newList.next
            else:
                break
                
        return self.newList.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)