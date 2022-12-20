class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        graph = defaultdict(list)
        visited = set()
        
        for i in range(len(rooms)):
            for room in rooms[i]:
                graph[i].append(room)
        
        while queue:
            currRoom = queue.popleft()
            
            if currRoom in visited:
                continue
                
            visited.add(currRoom)
                
            for nextRoom in graph[currRoom]:
                if nextRoom not in visited:
                    queue.append(nextRoom)
        
        return len(visited) == len(rooms)