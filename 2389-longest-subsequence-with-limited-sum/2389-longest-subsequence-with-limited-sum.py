class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefSum = [nums[0]]
        answer = []
        
        for i in range(1, len(nums)):
            prefSum.append(prefSum[-1] + nums[i])
        
        for i in range(len(queries)):
            idx = bisect.bisect(prefSum, queries[i])
            answer.append(idx)
            
        return answer