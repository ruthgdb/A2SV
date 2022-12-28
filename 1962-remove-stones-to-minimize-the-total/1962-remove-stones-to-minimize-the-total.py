class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-stone for stone in piles]
        heapq.heapify(heap)
        
        for _ in range(k):
            stone = -heapq.heappop(heap)
            heapq.heappush(heap, -stone // 2)
            
        return sum(heap) * -1