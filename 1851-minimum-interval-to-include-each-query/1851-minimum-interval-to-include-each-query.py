import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        answer = [-1] * len(queries)
        queries = [(query, i) for i, query in enumerate(queries)]
        intervals.sort()
        queries.sort()
        heap = []
        idx = 0 
        
        for query, i in queries:
            # add intervals whos start time is less than query (diff, end time)
            while idx < len(intervals) and intervals[idx][0] <= query:
                heappush(heap, (intervals[idx][1] - intervals[idx][0] + 1, intervals[idx][1]))
                idx += 1
            
            # remove intervals whose end time is less than query
            while heap and heap[0][1] < query:
                heappop(heap)
            
            # update res is there is heap
            if heap:
                answer[i] = heap[0][0]
            
        return answer