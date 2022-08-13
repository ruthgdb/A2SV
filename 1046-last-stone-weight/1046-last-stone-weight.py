class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        weight = [-i for i in stones]
        heapq.heapify(weight)
        
        while len(weight) > 1:
            first = -heapq.heappop(weight)
            second = -heapq.heappop(weight)
            if first != second:
                heapq.heappush(weight, second - first)
                
        return -weight[0] if weight else 0