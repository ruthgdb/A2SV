import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = [(capital[i], profits[i]) for i in range(len(profits))]
        projects.sort()
        i = 0
        heap = []
        
        while i < len(projects) and projects[i][0] <= w:
            heappush(heap, -projects[i][1])
            i += 1
            
        while heap and k > 0:
            curr_profit = heappop(heap)
            w -= curr_profit
            k -= 1
            
            while i < len(projects) and projects[i][0] <= w:
                heappush(heap, -projects[i][1])
                i += 1
                
        return w