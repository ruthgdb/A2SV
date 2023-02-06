class Solution:
    def racecar(self, target: int) -> int:
        #count, pos, speed
        queue = deque([(0, 0, 1)]) 
        
        while queue:
            count, pos, speed = queue.popleft()
            
            if pos == target:
                return count
            
            queue.append((count + 1, pos + speed, speed * 2))
            
            # if reverse
            if (pos + speed > target and speed > 0) or (pos + speed < target and speed < 0):
                queue.append((count + 1, pos, -1 if speed > 0 else 1))

        return -1