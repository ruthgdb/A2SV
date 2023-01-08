class Solution:
    def calcSlope(self, x1, y1, x2, y2):
        if x2 == x1:
            return float("inf")
        
        return (y2 - y1) / (x2 - x1)
        
    def maxPoints(self, points: List[List[int]]) -> int:
        slopes = defaultdict(set)
        sameLine = defaultdict(set)
        maxPoints = 1
        
        for i in range(len(points)):
            slopes.clear()
            sameLine.clear()
            
            for j in range(len(points)):
                if i == j:
                    continue
                    
                slope = self.calcSlope(points[i][0], points[i][1], points[j][0], points[j][1])
                if slope == float("inf"):
                    sameLine[points[i][0]].add(tuple(points[i]))
                    sameLine[points[i][0]].add(tuple(points[j]))
                else:
                    slopes[slope].add(tuple(points[i]))
                    slopes[slope].add(tuple(points[j]))
        
            for slope in slopes:
                maxPoints = max(maxPoints, len(slopes[slope]))

            for line in sameLine:
                maxPoints = max(maxPoints, len(sameLine[line]))

        return maxPoints