class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort()
        pointsSet = set([(x, y) for x, y in points])
        area = float("inf")
        
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                if x1 != x2 and y1 != y2 and (x1, y2) in pointsSet and (x2, y1) in pointsSet:
                    area = min(area, abs(x1 - x2) * abs(y1 - y2))
        
        return area if area != float("inf") else 0