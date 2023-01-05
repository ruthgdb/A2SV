class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        minArrows = 1
        currArrow = points[0][1]
        
        for i in range(1, len(points)):
            if currArrow < points[i][0]:
                minArrows += 1
                currArrow = points[i][1]
        
        return minArrows