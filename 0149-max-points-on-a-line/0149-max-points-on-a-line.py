class Solution:
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
                    
                if points[j][0] == points[i][0]:
                    sameLine += 1
                    maxPoints = max(maxPoints, sameLine)
                else:
                    slope = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                    slopes[slope].add(tuple(points[i]))
                    slopes[slope].add(tuple(points[j]))
                    maxPoints = max(maxPoints, len(slopes[slope]))

        return maxPoints