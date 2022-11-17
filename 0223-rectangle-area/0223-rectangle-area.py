class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)
        x_intersection = min(ax2, bx2) - max(ax1, bx1)
        y_intersection = min(ay2, by2) - max(ay1, by1)
        intersection_area = 0
        
        if y_intersection > 0 and x_intersection > 0:
            intersection_area = x_intersection * y_intersection
        
        return area1 + area2 - intersection_area