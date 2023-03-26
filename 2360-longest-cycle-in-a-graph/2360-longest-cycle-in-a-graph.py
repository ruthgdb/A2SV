class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        seen = {}
        path_length, res = 0, -1

        for i in range(len(edges)):
            node, start = i, path_length
            while node not in seen and node != -1:
                seen[node] = path_length
                path_length += 1
                node = edges[node]
            if node != -1 and seen[node] >= start:
                res = max(res, path_length - seen[node])
                
        return res