class Solution:
    def canJump(self, nums: List[int]) -> bool:
        currJump = float("-inf")
        
        for i in range(len(nums) - 1):
            currJump = max(currJump - 1, nums[i])
            if currJump == 0:
                return False
            
        return True