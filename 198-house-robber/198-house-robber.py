class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0] 
        
        curr = nums[0]
        money = max(curr, nums[1])
        
        for i in range(2, len(nums)):
            curr, money = money, max(money, curr + nums[i])
        
        return money