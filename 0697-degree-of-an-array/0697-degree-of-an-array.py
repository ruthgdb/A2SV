class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        indices = defaultdict(lambda: [float("inf"), float("-inf")])
        count = Counter(nums)
        maxCount = max(count.values())
        minLength = float("inf")
        
        for i, num in enumerate(nums):
            indices[num][0] = min(indices[num][0], i)
            indices[num][1] = max(indices[num][1], i)
                        
        for num in count:
            if count[num] == maxCount:
                first = indices[num][0]
                last = indices[num][1]
                minLength = min(minLength, last - first + 1)
                
        return minLength