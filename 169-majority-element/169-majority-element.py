class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sets =set(nums) 
        n = len(nums) // 2
        
        for i in sets:
            if nums.count(i) > n:
                return i
                break