class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n, maxx = len(nums), 0
        
        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = n + 1
            else:
                maxx = max(maxx, nums[i])
               
        for i in range(n):
            index = abs(nums[i])
            if index < n and nums[index] > 0:
                nums[index] = -1 * nums[index]
       
        for i in range(1, n):
            if nums[i] > 0:
                return i
            
        return maxx + 1