class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        
        def bkt(nums, path):
            if len(path) == n:
                res.append(path)
                return
                
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                bkt(nums[:i] + nums[i + 1:], path + [nums[i]])
            
        bkt(nums, [])
        return res