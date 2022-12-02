class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        mergedList = []
        
        start, end = intervals[0]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            else:
                mergedList.append([start, end])
                start, end = intervals[i]
        
        mergedList.append([start, end])
        return mergedList