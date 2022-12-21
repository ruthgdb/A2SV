class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True
        
        graph = defaultdict(list)
        indegrees = [0] * (n + 1)
        blues = set()
        reds = set()
        
        for person1, person2 in dislikes:
            graph[person1].append(person2)
            indegrees[person2] += 1
            
        for i in range(1, n + 1):
            if indegrees[i] == 0:
                queue = deque([(i, False)])
        
        while queue:
            person, color = queue.popleft()
            
            if color:
                if person in reds:
                    return False
                blues.add(person)
            else:
                if person in blues:
                    return False
                reds.add(person)
                      
            for neighbour in graph[person]:
                queue.append((neighbour, not color))       
            
        return True