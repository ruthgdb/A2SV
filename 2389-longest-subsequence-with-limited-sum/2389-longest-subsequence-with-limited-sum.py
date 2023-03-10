class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefSum = [nums[0]]
        res = []
        
        for i in range(1, len(nums)):
            prefSum.append(prefSum[-1] + nums[i])
            
        for query in queries:
            i = bisect.bisect_right(prefSum, query)
            res.append(i)
            
        return res