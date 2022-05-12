class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        mini = 60*24
        times = [(int(x[:2]) * 60) + int(x[3:]) for x in timePoints]
        times.sort()
        
        for i in range(len(timePoints) - 1):
            mini = min(mini, times[i + 1] - times[i])
            
        mini = min(mini, (1440 - times[-1]) + times[0])
        
        return mini
            