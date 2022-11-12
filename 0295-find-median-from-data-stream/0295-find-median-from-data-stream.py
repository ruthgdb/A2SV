class MedianFinder:

    def __init__(self):
        self.minimums = []
        self.maximums = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minimums, -num)
        popped_element = -heapq.heappop(self.minimums)
        heapq.heappush(self.maximums, popped_element)
        
        if len(self.minimums) < len(self.maximums):
            popped_element = heapq.heappop(self.maximums)
            heapq.heappush(self.minimums, -popped_element)
            
    def findMedian(self) -> float:
        if len(self.minimums) == len(self.maximums):
            median = (-self.minimums[0] + self.maximums[0]) / 2
        else:
            median = -self.minimums[0]
            
        return median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()