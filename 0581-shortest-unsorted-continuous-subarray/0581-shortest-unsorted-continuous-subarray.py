class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        minStack = []
        maxStack = []
        first = -1
        last = -1
        
        for i, num in enumerate(nums):            
            while minStack and minStack[-1][0] > num:
                temp, idx = minStack.pop()
                first = min(first, idx) if first != -1 else idx
                
            minStack.append((num, i))
            
        if first == -1:
            return 0
                
        for i in range(len(nums) - 1, -1, -1):            
            while maxStack and maxStack[-1][0] < nums[i]:
                temp, idx = maxStack.pop()
                last = max(last, idx)
                
            maxStack.append((nums[i], i))
        
        return last - first + 1