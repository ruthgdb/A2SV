class SummaryRanges:

    def __init__(self):
        self.nums = set()
        
    def addNum(self, value: int) -> None:
        self.nums.add(value)
        
    def getIntervals(self) -> List[List[int]]:
        intervals = []
        start = None
        end = None
        for val in sorted(self.nums):
            if start is None:
                start = val
                end = val
            elif val - end == 1:
                end = val
            else:
                intervals.append([start, end])
                start = end = val
        if start is not None:
            intervals.append([start, end])
        return intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()