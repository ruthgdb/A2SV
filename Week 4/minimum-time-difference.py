class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        inMin = []
        for i in timePoints:
            hour, minute = i.split(":")
            inMin.append((int(hour)*60)+int(minute))
        inMin.sort()
        mini = 1440 + inMin[0] - inMin[len(inMin)-1]
        for i in range(1, len(inMin)):
            mini = min(mini,(inMin[i] - inMin[i-1]))
        return mini