class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        indices = defaultdict(list)
        
        for i, num in enumerate(nums2):
            indices[num].append(i)
          
        @cache
        def dp(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0
            
            best = dp(i + 1, j)
            
            for k in indices[nums1[i]]:
                if k >= j:
                    best = max(best, 1 + dp(i + 1, k + 1))
                    break

            return best
        
        return dp(0, 0)