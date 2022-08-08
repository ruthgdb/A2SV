class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def bkt(nums, path):
            if len(path) == n:
                res.append(path)
                return
                
            for i in range(len(nums)):
                bkt(nums[:i] + nums[i + 1:], path + [nums[i]])
            
        bkt(nums, [])
        return res