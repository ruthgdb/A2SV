class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.p = set()

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        self.p.add(tuple(point))

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        count = 0

        for x2, y2 in self.p:  
            if x1 == x2 and y1 == y2:
                continue
                
            if x1 == x2:
                dist = abs(y1 - y2)
                count += self.points[(x2, y2)] * self.points[(x2 + dist, y1)] * self.points[(x2 + dist, y2)]
                count += self.points[(x2, y2)] * self.points[(x2 - dist, y1)] * self.points[(x2 - dist, y2)]
            elif y1 == y2:
                dist = abs(x1 - x2)
                count += self.points[(x2, y2)] * self.points[(x2, dist + y2)] * self.points[(x1, dist + y2)]
                count += self.points[(x2, y2)] * self.points[(x2, y2 - dist)] * self.points[(x1, y2 - dist)]  

        return count // 2


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)