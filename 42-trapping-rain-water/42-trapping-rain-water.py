class Solution:
    def trap(self, height: List[int]) -> int:
        n, amount = len(height), 0
        left, right = [0] * n, [0] * n
        
        for i in range(1, n):
            left[i] = max(height[i - 1], left[i - 1])
            
        for i in range(n - 2, -1, -1):
            right[i] = max(height[i + 1], right[i + 1])
            
        for i in range(n):
            val = min(left[i], right[i]) - height[i]
            amount += val if val > 0 else 0
            
        return amount