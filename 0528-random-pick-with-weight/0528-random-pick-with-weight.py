class Solution:

    def __init__(self, w: List[int]):
        self.prefSum = [0]
        self.w = w
        
        for num in w:
            self.prefSum.append(self.prefSum[-1] + num)
            
        self.prefSum = self.prefSum[1:]

    def pickIndex(self) -> int:
        rand = random.randint(1, self.prefSum[-1])
        idx = bisect.bisect_left(self.prefSum, rand)
        return idx

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()