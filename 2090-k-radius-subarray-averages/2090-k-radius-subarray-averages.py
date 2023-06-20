class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < (k * 2 + 1):
            return [-1] * len(nums)
        
        res = []
        right = 0
        total = 0
        
        for i in range(k * 2 + 1):
            total += nums[i]
            right += 1
        
        for left in range(len(nums) - (k * 2)):
            res.append(total // (k * 2 + 1))
            if right == len(nums):
                break
                
            total += nums[right]
            total -= nums[left]
            right += 1
            
        return [-1 for _ in range(k)] + res + [-1 for _ in range(k)]