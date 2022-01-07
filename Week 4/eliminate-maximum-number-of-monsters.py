class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = [0] * len(dist)
        for i in range(len(dist)):
            time[i] = ceil(dist[i]/speed[i])
        time.sort()
        for i in range(len(dist)):
            if i >= time[i]:
                return i      
        return len(time)