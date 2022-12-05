class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        maxBombs = 1
        
        def bfs(idx):
            visited = set()
            queue = deque([idx])
            
            while queue:
                currIdx = queue.popleft()
                
                if currIdx in visited:
                    continue

                visited.add(currIdx)

                for nextIdx in graph[currIdx]:
                    if nextIdx not in visited:
                        queue.append(nextIdx)
                        
            return len(visited)
        
        for i, bomb1 in enumerate(bombs):
            for j, bomb2 in enumerate(bombs):
                if i != j:
                    x1, y1, r1 = bomb1
                    x2, y2, r2 = bomb2
                    dist = sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
                    if dist <= r1:
                        graph[i].append(j)
                        
        for i, bomb in enumerate(bombs):
            if i in graph:
                currMax = bfs(i)
                maxBombs = max(maxBombs, currMax)
       
        return maxBombs