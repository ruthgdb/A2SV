class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for _ in range(len(nums2))] for _ in range(len(nums1))]
        max_len = 0
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    prev = dp[i - 1][j - 1] if i > 0 and j > 0 else 0
                    dp[i][j] = prev + 1
                    max_len = max(max_len, dp[i][j])
                    
        return max_len