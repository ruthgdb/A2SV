class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letters = dict()
        intervals = []
        res = []
        
        for i in range(len(s)):
            if s[i] not in letters.keys():
                letters[s[i]] = [i, i]
            else:
                letters[s[i]][1] = i
                
        for val in letters.values():
            intervals.append(val)
            
        intervals.sort()
        start, end = intervals[0][0], intervals[0][1]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(intervals[i][1], end)
            else:
                res.append(end - start + 1)
                start, end = intervals[i][0], intervals[i][1]
        res.append(end - start + 1)
              
        return res