class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        res = []
        curr = [str(nums[0])]
        cont = True
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if curr[0] != str(nums[i - 1]):
                    curr.append(str(nums[i - 1]))
                res.append('->'.join(curr))
                curr = [str(nums[i])]
                if i != len(nums) - 1:
                    cont = False
                else:
                    cont = True
            else:
                cont = True
                
        if cont:
            if curr[0] != str(nums[-1]):
                curr.append(str(nums[-1]))
            res.append('->'.join(curr))
            
        return res