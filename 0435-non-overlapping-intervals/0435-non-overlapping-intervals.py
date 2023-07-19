class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # [[1,3],[2,4],[3,5],[4,6],[5,7]]
        # [[1,2],[1,3],[2,3],[3,4]]
        
        intervals.sort()
        start =  intervals[0][0]
        end = intervals[0][1]
        removed = 0
        
        
        '''
            start = 1
            end = 2
        '''
        
        for i in range(1,len(intervals)):
            if intervals[i][0] < end:
                if end >= intervals[i][1]:
                    end = intervals[i][1]
                removed += 1
            else:
                end = intervals[i][1]
                
        return removed
                
            
        
        