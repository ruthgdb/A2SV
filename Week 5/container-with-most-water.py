class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxRight = right
        maxLeft = left
        area = 0
        
        while (left < right):
            temp = abs((left - right) * min(height[left] , height[right]))
            area = max(temp ,area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1           
            
        return area