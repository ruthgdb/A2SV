class Solution:
    def checkRectangle(self, x1, x2, pos):
        minArea = float("inf")
        
        for y1 in pos[x1]:
            if y1 in pos[x2]:
                for y2 in pos[x2]:
                    if y1 != y2 and y2 in pos[x1]:
                        minArea = min(minArea, abs(x1 - x2) * abs(y2 - y1))
                     
        return minArea
        
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort()
        pos = defaultdict(set)
        area = float("inf")
        visited = set()
        
        for x, y in points:
            pos[x].add(y)
            
        for pt1 in pos:
            for pt2 in pos:
                if pt1 != pt2 and (pt1, pt2) not in visited:
                    visited.add((pt2, pt1))
                    area = min(area, self.checkRectangle(pt1, pt2, pos))
            
        return area if area != float("inf") else 0