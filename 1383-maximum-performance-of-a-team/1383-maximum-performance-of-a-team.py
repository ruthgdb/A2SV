class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        perf = [(efficiency[x], speed[x]) for x in range(len(speed))]
        perf.sort(reverse = True)
        heap = []
        total = 0
        res = 0
        mod = 10 ** 9 + 7
        
        for eff, spd in perf:
            heapq.heappush(heap, spd)
            total += spd
            
            if len(heap) > k:
                temp = heapq.heappop(heap)
                total -= temp
            
            res = max(res, total * eff)
            
        return res % mod