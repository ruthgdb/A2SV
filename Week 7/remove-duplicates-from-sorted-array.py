class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left =  0
        right = 1
        i = 0
        
        while(right < len(nums)):
            if(nums[left] == nums[right]):
                nums[right] = 101
                right += 1
            else:
                left = right
                right += 1
                i += 1
                
        nums.sort()
        nums = nums[:i+1]
        return i+1
        