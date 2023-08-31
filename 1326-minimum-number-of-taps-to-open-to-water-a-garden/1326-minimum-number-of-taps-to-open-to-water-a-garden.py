class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = [0] * (n + 1)

        for i in range(len(ranges)):
            start = max(0, i - ranges[i])
            end = min(n, i + ranges[i])
            intervals[start] = max(intervals[start], end)
        
        taps = curr = nxt = 0

        for i in range(n + 1):
            if i > nxt:
                return -1

            if i > curr:
                taps += 1
                curr = nxt

            nxt = max(nxt, intervals[i])

        return taps