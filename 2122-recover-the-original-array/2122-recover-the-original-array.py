class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        k_candidates = [(nums[i] - nums[0]) // 2 for i in range(1, len(nums)) if (nums[i] - nums[0]) // 2 != 0]
        count = Counter(nums)
        
        for k in k_candidates:
            count_temp = count.copy()
            res = []
            
            for i in range(len(nums)):
                if count_temp[nums[i]] == 0:
                    continue
                    
                if count_temp[nums[i]] > 0 and count_temp[nums[i] + (2*k)] > 0:
                    res.append(nums[i] + k)
                    count_temp[nums[i]] -= 1
                    count_temp[nums[i] + (2*k)] -= 1
                    
            if len(res) == len(nums) // 2:
                return res
            
            