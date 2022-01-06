class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l =  0
        r = 1
        i = 0
        while(r < len(nums)):
            if(nums[l] == nums[r]):
                nums[r] = 101
                r += 1
            else:
                l = r
                r += 1
                i += 1
        nums.sort()
        nums = nums[:i+1]
        return i+1
        