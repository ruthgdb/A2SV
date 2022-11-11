class Solution:
    def find_idx(self, left, right, arr, target):        
        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] < target:
                left = mid + 1
            elif arr[mid] > target:
                right = mid - 1
            else:
                return mid

        return right

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float("inf")
        pref_sum = [0]

        for i in range(len(nums)):
            pref_sum.append(pref_sum[-1] + nums[i])
        
        for i in range(len(pref_sum)):
            if pref_sum[i] >= target:
                idx = self.find_idx(0, i, pref_sum, pref_sum[i] - target)
                min_len = min(min_len, i - idx)
            
        return min_len if min_len != float("inf") else 0