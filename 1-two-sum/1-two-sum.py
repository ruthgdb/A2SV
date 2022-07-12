class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = defaultdict(int)
        results = []
        
        for i in range(len(nums)):
            if target - nums[i] in sums:
                results.append(sums[target - nums[i]])
                results.append(i)
            else:
                sums[nums[i]] = i
                
        return results