class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zeros = 0
        ones = 0
        targets = defaultdict(int)
        targets[0] = -1
        maxLen = 0
        
        for i, num in enumerate(nums):
            zeros += num == 0
            ones += num == 1
            
            if zeros - ones in targets:
                maxLen = max(maxLen, i - targets[zeros - ones])
            else:
                targets[zeros - ones] = i
                
            if zeros == ones:
                maxLen = max(maxLen, i + 1)
                
        return maxLen 