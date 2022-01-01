<<<<<<< HEAD
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        newlist = []
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(intervals[i][1], end)
            else:
                newlist.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]
        newlist.append([start, end])
=======
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        newlist = list()
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(intervals[i][1], end)
            else:
                newlist.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]
        newlist.append([start, end])
>>>>>>> eb99cca94aa3d6f79b9499f04a185a0ffd2328cb
        return newlist