class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = 0
        k = k % len(nums)
        
        for i in range(k):
            temp = nums.pop()
            nums.insert(0,temp)
            
        