class Solution:
    def trap(self, heights: List[int]) -> int:
        stack = []
        trappedWater = 0
        
        for i, el in enumerate(heights):
            while stack and stack[-1][0] < el:
                currHeight, idx = stack.pop()
                
                if stack:
                    width = i - stack[-1][1] - 1
                    height = min(stack[-1][0], el) - currHeight
                    
                    trappedWater += width * height
                
            stack.append((el, i))
            
        return trappedWater