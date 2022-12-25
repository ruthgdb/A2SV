class Solution:
    def buildRangeFromLeft(self, ranges, heights):
        stack = []
        
        for i, height in enumerate(heights):            
            currMax = None

            while stack and stack[-1][0] > height:
                temp, idx = stack.pop()
                if not currMax:
                    currMax, maxIdx = temp, idx
                    ranges[maxIdx] = 0
                ranges[idx] += maxIdx - idx
                    
            stack.append((height, i))
            
        currMax = None

        while stack:
            temp, idx = stack.pop()
            if not currMax:
                currMax, maxIdx = temp, idx
                ranges[maxIdx] = 0

            ranges[idx] += maxIdx - idx
             
    def buildRangeFromRight(self, ranges, heights):
        stack = []

        for i in range(len(heights) - 1, -1, -1):            
            currMax = None

            while stack and stack[-1][0] > heights[i]:
                temp, idx = stack.pop()
                if not currMax:
                    currMax, maxIdx = temp, idx
                ranges[idx] += abs(maxIdx - idx)

            stack.append((heights[i], i))
            
        currMax = None

        while stack:
            temp, idx = stack.pop()
            if not currMax:
                currMax, maxIdx = temp, idx
            ranges[idx] += abs(maxIdx - idx)
        
                
    def largestRectangleArea(self, heights: List[int]) -> int:
        ranges = defaultdict(int)
        largestRectangle = 0
        self.buildRangeFromLeft(ranges, heights)
        self.buildRangeFromRight(ranges, heights)

        for i in ranges:
            largestRectangle = max(largestRectangle, (ranges[i] + 1) * heights[i])
        
        return largestRectangle