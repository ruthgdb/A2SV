class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        maximum = 0
        withoutLast, withoutFirst = [0] * n, [0] * n
        
        for i in range(n - 2, -1, -1):
            house1 = withoutFirst[i + 2] if i + 2 < n else 0
            house2 = withoutFirst[i + 3] if i + 3 < n else 0
            withoutFirst[i] = max(house1, house2) + nums[i]
            maximum = max(maximum, withoutFirst[i])
            
        for i in range(n - 1, 0, -1):
            house1 = withoutLast[i + 2] if i + 2 < n else 0
            house2 = withoutLast[i + 3] if i + 3 < n else 0
            withoutLast[i] = max(house1, house2) + nums[i]
            maximum = max(maximum, withoutLast[i])
        
        return maximum