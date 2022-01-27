from collections import deque
class MyCircularDeque:

    def __init__(self, k: int):
        self.queue =  deque()
        self.k = k

    def insertFront(self, value: int) -> bool:
        if len(self.queue) < self.k:
            self.queue.appendleft(value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if len(self.queue) < self.k:
            self.queue.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if self.queue:
            self.queue.popleft()
            return True
        return False

    def deleteLast(self) -> bool:
        if not self.queue:
            return False
        else:
            self.queue.pop()
        return True

    def getFront(self) -> int:
        if not self.queue:
            return -1
        return self.queue[0]

    def getRear(self) -> int:
        if not self.queue:
            return -1
        return self.queue[-1]

    def isEmpty(self) -> bool:
        if not self.queue:
            return True
        return False

    def isFull(self) -> bool:
        if len(self.queue) >= self.k:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()