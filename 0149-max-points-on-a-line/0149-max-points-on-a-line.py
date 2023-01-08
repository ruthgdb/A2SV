class Solution:
    def calcSlope(self, x1, y1, x2, y2):
        if x2 == x1:
            return float("inf")
        
        return (y2 - y1) / (x2 - x1)
        
    def maxPoints(self, points: List[List[int]]) -> int:
        slopes = defaultdict(set)
        sameLine = 1
        maxPoints = 1
        
        for i in range(len(points)):
            slopes.clear()
            sameLine = 1
            
            for j in range(len(points)):
                if i == j:
                    continue
                    
                slope = self.calcSlope(points[i][0], points[i][1], points[j][0], points[j][1])
                
                if slope == float("inf"):
                    sameLine += 1
                else:
                    slopes[slope].add(tuple(points[i]))
                    slopes[slope].add(tuple(points[j]))
        
                maxPoints = max(maxPoints, len(slopes[slope]), sameLine)

        return maxPoints