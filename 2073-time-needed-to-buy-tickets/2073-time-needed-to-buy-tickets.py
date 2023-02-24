class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(range(len(tickets)))
        t = 0
        
        while queue:    
            t += 1 
            i = queue.popleft()
            tickets[i] -= 1
            
            if tickets[i] > 0:
                queue.append(i)         
            elif tickets[i] == 0:
                if i == k:
                    break
            
        return t