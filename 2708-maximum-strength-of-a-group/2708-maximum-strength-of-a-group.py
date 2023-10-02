class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        min_num = float("-inf")
        neg_count = 0
        neg_prod = 0
        prod = 0
        
        for num in nums:
            if num < 0:
                if neg_prod == 0:
                    neg_prod += 1
                    
                neg_count += 1
                neg_prod *= num
                min_num = max(min_num, num)
                
            if num > 0:
                prod = max(1, prod)
                prod *= num
        
        if neg_count == 1:
            neg_prod = 0
            
        if neg_count % 2 != 0:
            neg_prod //= min_num
            
        if prod > 0 and neg_prod > 0:
            return prod * neg_prod
        
        return max(prod, neg_prod)