class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        
        for _ in range(k + 1):
            temp = prices[:]
            
            for frm, to, cost in flights:
                if prices[frm] != float("inf"):
                    temp[to] = min(prices[frm] + cost, temp[to])

            prices = temp
            
        return prices[dst] if prices[dst] != float("inf") else -1