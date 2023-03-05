class Solution:
    def minJumps(self, arr: List[int]) -> int:
        indices = defaultdict(list)
        visited = set()
        queue = deque([(0, 0)]) 
        
        for i, num in enumerate(arr):
            indices[num].append(i)
        
        while queue:
            i, count = queue.popleft()
            
            if i == len(arr) - 1:
                return count
            
            if i - 1 not in visited and i - 1 >= 0:
                visited.add(i - 1)
                queue.append((i - 1, count + 1))
            if i + 1 not in visited and i + 1 < len(arr):
                visited.add(i + 1)
                queue.append((i + 1, count + 1))
            
            for nei in indices[arr[i]]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, count + 1))
            
            indices[arr[i]].clear()
            
        return len(arr) - 1