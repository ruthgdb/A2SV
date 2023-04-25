import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.nums = list(range(1,1001))
        heapify(self.nums)
        self.removed = set()

    def popSmallest(self) -> int:
        num = heappop(self.nums)
        self.removed.add(num)
        return num

    def addBack(self, num: int) -> None:
        if num in self.removed:
            heappush(self.nums, num)
            self.removed.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)