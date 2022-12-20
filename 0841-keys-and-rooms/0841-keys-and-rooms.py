class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = set()
        
        while queue:
            currRoom = queue.popleft()
            
            if currRoom in visited:
                continue
                
            visited.add(currRoom)
                
            for nextRoom in rooms[currRoom]:
                if nextRoom not in visited:
                    queue.append(nextRoom)
        
        return len(visited) == len(rooms)