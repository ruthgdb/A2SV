from sortedcontainers import SortedList

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        graph = defaultdict(SortedList)
        maxSum = float("-inf")
        
        for node1, node2 in edges:
            graph[node1].add(vals[node2])
            graph[node2].add(vals[node1])
         
        for i in range(len(vals)):
            currSum = vals[i]
            count = 0

            for val in reversed(graph[i]):
                if count == k:
                    break
                    
                if val > 0:
                    currSum += val
                count += 1
                
            maxSum = max(maxSum, currSum)
                
        return maxSum if maxSum != float("-inf") else 0