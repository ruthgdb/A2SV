class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        curr = []
        curr.append(points[0][1])
        
        for i in range(1, len(points)):
            if points[i][0] > curr[-1]:
                curr.append(points[i][1])
        
        return len(curr)