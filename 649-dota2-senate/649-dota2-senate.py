class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(senate)
        count = Counter(queue)
                
        while count['R'] != 0 or count['D'] != 0:
            temp = queue.popleft()
            if temp == 'D' and 'R' in queue:
                queue.remove('R')
                count['R'] -= 1
            elif temp == 'D' and 'R' not in queue:
                return "Dire"
            elif temp == 'R' and 'D' in queue:
                queue.remove('D')
                count['D'] -= 1
            else:
                return "Radiant"
            queue.append(temp)
            