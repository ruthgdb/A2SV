class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        neighbours = defaultdict(set)
        queue = deque()
        visited = set()
        res = []
        
        for first, second in adjacentPairs:
            neighbours[first].add(second)
            neighbours[second].add(first)
            
        for val in neighbours:
            if len(neighbours[val]) == 1:
                queue.append(val)
                break
                
        while queue:
            curr = queue.popleft()
            visited.add(curr)
            res.append(curr)
            
            for nei in neighbours[curr]:
                if nei not in visited:
                    queue.append(nei)
                    
        return res