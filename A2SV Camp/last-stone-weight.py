class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)
        
        if len(stones) == 1:
            return stones[0]
        
        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            heapq._heapify_max(stones)
            stone2 = heapq.heappop(stones)
            if stone1 != stone2:
                heapq.heappush(stones, abs(stone1 - stone2))
            heapq._heapify_max(stones)
        
        if len(stones) > 0:
            return stones[0]
        else:
            return 0