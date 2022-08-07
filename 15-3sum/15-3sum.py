class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, n, dic = set(), len(nums), dict()
        
        for i in range(len(nums)):
            dic.clear()
            target = 0 - nums[i]
            
            for j in range(i + 1, n):
                if nums[j] not in dic:
                    dic[target - nums[j]] = nums[j]
                else:
                    val = sorted([nums[i], nums[j], dic[nums[j]]])
                    if (val[0], val[1], val[2]) not in res:
                        res.add((val[0], val[1], val[2]))   
            
        return res