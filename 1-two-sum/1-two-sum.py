class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = defaultdict(int)
        
        for i in range(len(nums)):
            if target - nums[i] in sums:
                return [sums[target - nums[i]], i]
            else:
                sums[nums[i]] = i