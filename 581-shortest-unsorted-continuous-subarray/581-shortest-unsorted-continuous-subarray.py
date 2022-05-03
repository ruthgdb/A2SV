class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start, end = len(nums), 0
        stack = []
        
        for i in reversed(range(len(nums))):
            while stack and nums[stack[-1]] < nums[i]:
                end = max(end, stack.pop())
            stack.append(i)
            
        stack = []
        
        for i in range(0, len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                start = min(start, stack.pop())
            stack.append(i)
            
        res = end - start + 1
        
        if res > 0:
            return res
        return 0