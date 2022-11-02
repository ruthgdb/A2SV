class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        
        visited = set(start)
        min_len = 0
        changes = defaultdict(list)
        queue = deque([start])
        bank.append(start)
        
        for change in bank:
            for i in range(8):
                mutation = change[:i] + '*' + change[i + 1:]
                changes[mutation].append(change)
                
        while queue:
            l = len(queue)
            
            for i in range(l):
                curr_mutation = queue.popleft()
                if curr_mutation == end:
                    return min_len

                for i in range(len(curr_mutation)):
                    mutation = curr_mutation[:i] + '*' + curr_mutation[i + 1:]
                    
                    for change in changes[mutation]:
                        if change not in visited:
                            visited.add(change)
                            queue.append(change)
                        
            min_len += 1
            
        return -1