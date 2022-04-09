class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0] 
        
        temp = nums[0]
        money = max(temp, nums[1])
        
        for i in range(2, len(nums)):
            temp, money = money, max(money, temp + nums[i])
        
        return money