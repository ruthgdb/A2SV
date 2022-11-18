class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        smaller_idx = -1
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                smaller_idx = i
                smaller_num, idx = float("inf"), -1

                for i in range(smaller_idx + 1, len(nums)):
                    if nums[i] > nums[smaller_idx] and nums[i] <= smaller_num:
                        smaller_num = nums[i]
                        idx = i

                nums[idx], nums[smaller_idx] = nums[smaller_idx], nums[idx]

                left, right = smaller_idx + 1, len(nums) - 1

                while left < right:
                    if nums[left] > nums[right]:
                        nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
                break
        
        if smaller_idx == -1:
            nums.sort()