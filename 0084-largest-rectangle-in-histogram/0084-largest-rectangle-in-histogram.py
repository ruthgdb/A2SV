class Solution:
    def buildRanges(self, ranges, heights):
        stack = []
        
        for i, height in enumerate(heights):            
            if stack and stack[-1][0] > height:
                currMax, maxIdx = stack.pop()
                ranges[maxIdx] = 0
                
                while stack and stack[-1][0] > height:
                    temp, idx = stack.pop()
                    ranges[idx] += maxIdx - idx
            stack.append((height, i))
            
        if stack:
            currMax, maxIdx = stack.pop()
            ranges[maxIdx] = 0
            
            while stack:
                temp, idx = stack.pop()
                ranges[idx] += maxIdx - idx
                
        stack = []

        for i in range(len(heights) - 1, -1, -1):            
            if stack and stack[-1][0] > heights[i]:
                currMax, maxIdx = stack.pop()
                
                while stack and stack[-1][0] > heights[i]:
                    temp, idx = stack.pop()
                    ranges[idx] += abs(maxIdx - idx)
            
            stack.append((heights[i], i))
            
        if stack:
            currMax, maxIdx = stack.pop()

            while stack:
                temp, idx = stack.pop()
                ranges[idx] += abs(maxIdx - idx)
        
                
    def largestRectangleArea(self, heights: List[int]) -> int:
        ranges = defaultdict(int)
        largestRectangle = 0
        self.buildRanges(ranges, heights)

        for i in ranges:
            largestRectangle = max(largestRectangle, (ranges[i] + 1) * heights[i])
        
        return largestRectangle