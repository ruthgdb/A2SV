class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        indices = defaultdict(list)
        count = Counter(nums)
        maxCount = max(count.values())
        minLength = float("inf")
        
        for i, num in enumerate(nums):
            indices[num].append(i)
            
        for num in count:
            if count[num] == maxCount:
                first = indices[num][0]
                last = indices[num][-1]
                minLength = min(minLength, last - first + 1)
                
        return minLength