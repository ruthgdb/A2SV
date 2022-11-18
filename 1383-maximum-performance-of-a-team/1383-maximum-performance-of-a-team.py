class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        effSpeed = list(zip(efficiency, speed))
        
        effSpeed.sort(reverse=True)
        minHeap = []
        runSum = 0
        maxPerformance = -inf
        
        for i in range(len(speed)):
            heapq.heappush(minHeap, effSpeed[i][1])
            runSum += effSpeed[i][1]
            
            if len(minHeap) > k:
                temp = heapq.heappop(minHeap)
                runSum -= temp
                
            curPerf = runSum * effSpeed[i][0]
            maxPerformance = max(curPerf, maxPerformance)
            
        return maxPerformance % (10 ** 9 + 7)
            
            
        
        
        