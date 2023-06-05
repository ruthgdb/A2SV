class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        
        slope = (y2 - y1)/ (x2 - x1) if (x2 - x1) != 0 else float("inf")
        
        for i in range(1, len(coordinates) - 1):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[i + 1]
            currSlope = (y2 - y1)/ (x2 - x1) if (x2 - x1) != 0 else float("inf")
            
            if currSlope != slope:
                return False
            
        return True